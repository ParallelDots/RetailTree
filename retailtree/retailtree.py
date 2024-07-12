import math
from random import sample
import numpy as np
from typing import Callable

from retailtree.structs.annotation_struct import Annotation
from retailtree.logics.vp_tree import VPTree
from retailtree.logics.right_left import right_left_connections, left_right_connections
from retailtree.logics.top_bottom import top_bottom_connections, bottom_top_connections
from retailtree.utils.dist_func import euclidean


class RetailTree:
    def __init__(self) -> None:
        self.annotations = {}  # type:dict[int, Annotation]
        self.tree = None
        self.__neighbors_radius = None

    def add_annotation(self, annotation):
        """
        Add an annotation object to the annotations dictionary.

        Parameters:
        - annotation: Annotation object
            The annotation object to be added. This should be an instance of the Annotation class.

        """
        self.annotations[annotation.id] = annotation

    def get(self, id):
        # type:(int) -> Annotation
        """
        Retrieve an annotation by its ID.

        Args:
            id (int): The ID of the annotation to retrieve.

        Returns:
            The annotation corresponding to the provided ID.
        """
        return self.annotations[id]

    def build_tree(self, dist_func=euclidean):
        # type:(Callable[[tuple[float, float], tuple[float, float]], float]) -> None
        """
        Builds a Vantage Point Tree (VPTree) using the given distance function.

        This method constructs a VPTree using the provided distance function or the default Euclidean distance if none is provided.

        Args:
        -   dist_func (callable, optional): A function that calculates the distance between two points.
            If not provided, the Euclidean distance function will be used. The function should accept two points as input
            and return a numerical value representing the distance between them.
            A point is a tuple with coordinates (x, y).
        """
        annotations = list(self.annotations.values())

        obj = VPTree(annotations, dist_func)
        self.tree = obj

    def __get_neighbors_radius(self):
        # type:() -> float
        """
        Method to get the radius within which neighbors will be searched for.
        Radius is the max of the diagonals of the annotations considered.
        """
        radius = self.__neighbors_radius
        if not radius:
            annotation_bucket = list(self.annotations.values())

            random_annotations = annotation_bucket
            distance = [math.sqrt(pow(annotation.width, 2) + pow(
                annotation.length, 2)) for annotation in random_annotations]
            radius = max(distance)
            self.__neighbors_radius = radius
        return radius

    def __fetch_neighbors(self, id, radius=1):
        # type:(int, int) -> list[tuple[float, Annotation]]
        radius = radius*self.__get_neighbors_radius()
        neighbors = self.tree.get_all_in_range(
            (self.annotations[id].x_mid, self.annotations[id].y_mid), radius)
        return neighbors

    def __finding_angle(self, origin, neighbor):
        # type:(Annotation, tuple[float, Annotation]) -> int
        translated_point2 = np.array(
            [neighbor[1].x_mid, neighbor[1].y_mid]) - np.array([origin.x_mid, origin.y_mid])
        # print(translated_point2)

        # Calculate the angle between the translated vector and the x-axis
        angle = np.arctan2(translated_point2[1], translated_point2[0])

        # Convert angle from radians to degrees
        angle_degrees = int(np.degrees(angle))
        if angle_degrees < 0:  # Check for negative angle
            angle_degrees += 360
        return angle_degrees

    def __fetching_ann_in_range(self, result_dict, min_angle, max_angle, result_lst):
        if min_angle is None and max_angle is None:
            result_lst.append(result_dict)
        elif min_angle is None and max_angle > result_dict['angle']:
            result_lst.append(result_dict)
        elif max_angle is None and min_angle < result_dict['angle']:
            result_lst.append(result_dict)
        elif min_angle is not None and max_angle is not None:
            if min_angle <= max_angle:
                if min_angle <= result_dict['angle'] <= max_angle:
                    result_lst.append(result_dict)
            else:
                if min_angle <= result_dict['angle'] or max_angle >= result_dict['angle']:
                    result_lst.append(result_dict)

        # if min_angle is None:
        return result_lst

    def neighbors_wa(self, id, radius=1, amin=None, amax=None):
        # type:(int, int, float, float) -> list[dict]
        """
        Retrieves neighboring elements within a specified angle range around a given element.

        Args:
            id (int): The identifier of the central element.
            radius (float, optional): The radius within which to search for neighbors. Defaults to 1.
            amin (min_angle) (float, optional): The minimum angle in degree. Defaults to None.
            amax (max_angle) (float, optional): The maximum angle in degree. Defaults to None.

        Returns:
            list: A list of dictionaries containing information about neighboring elements,
                  including their ID, distance from the central element, and angle relative to it.
        """
        neighbors = self.__fetch_neighbors(id, radius)
        result_lst = []
        origin_annotation = self.get(id)
        for neighbor in neighbors:
            # Finding angle
            if neighbor[1].id == id:
                continue
            angle = self.__finding_angle(origin_annotation, neighbor)
            result_dict = {
                "id": neighbor[1].id,
                "distance": neighbor[0],
                "angle": angle
            }

            self.__fetching_ann_in_range(
                result_dict, amin, amax, result_lst)

        return result_lst

    def neighbors(self, id, radius=1):
        # type:(int, int) -> list[dict]
        """
        Finds neighboring annotations within a specified radius of a given annotation.(Radius specified is taken as a square rather than a circle)

        Uses a Vantage Point Tree (VPTree) to efficiently find annotations within the specified radius.

        Args:
            id (int): The ID of the annotation.
            radius (float, optional): The relative radius within which to search. Defaults to 1.
                If a value less than 1 is provided, it's multiplied by an internal factor.

        Returns:
            list: A list of dicts of IDs and Distance of neighboring annotations found within the specified radius.


        Examples:
            Example usages of find_neighbors:
            # Finds neighbors within the default relative radius of 1
            >>> obj_ann_bucket.find_neighbors(1)
            # Finds neighbors within a custom relative radius of 2.5
            >>> obj_ann_bucket.find_neighbors(2, radius=2.5)
        """
        neighbors = self.__fetch_neighbors(id, radius)
        result_lst = []
        for neighbor in neighbors:
            # Finding angle
            if neighbor[1].id == id:
                continue

            result_dict = {
                "id": neighbor[1].id,
                "distance": neighbor[0]
            }

            result_lst.append(result_dict)

        return result_lst

    def TBLR(self, id, radius=1, overlap=0.5):
        # type:(int, int, float) -> (dict[str, int | bool] | str)
        """
        Computes top, bottom, left, and right connections for a given annotation within a specified radius.

        Finds neighboring annotations within the radius, calculates connections based on overlap percentage, and returns the connections as a dictionary.

        Args:
        -   id (int): The ID of the annotation.
        -   radius (float, optional): The radius within which to search for neighboring annotations. Defaults to 1.
        -   overlap (float, optional): The overlap percentage used to compute connections. Defaults to 0.5.

        Returns:
        -   dict OR str: A dictionary containing top, bottom, left, and right connections of the given annotation.
                Each connection is represented by the ID of the connected annotation, or False if no connection exists.
                If the SKU is not present in the bucket, a string with value 'SKU is absent in annotation bucket' is returned.

        Examples:
            Example usages of TBLR:
            # Computes connections for annotation with ID 1 within the default radius and overlap
            >>> obj_ann_bucket.TBLR(1)
            # Computes connections with custom radius and overlap
            >>> obj_ann_bucket.TBLR(2, radius=2.5, overlap=0.7)
        """

        neighbors = self.__fetch_neighbors(id, radius)

        for _, i in neighbors:
            for _, j in neighbors:
                top_bottom_connections(i, j, overlap)
                right_left_connections(i, j, overlap)
        for _, i in neighbors:
            for _, j in neighbors:
                bottom_top_connections(i, j, overlap)
                left_right_connections(i, j, overlap)

        target_element = self.annotations[id]
        if target_element:
            if target_element.top:
                top = target_element.top.id
            else:
                top = False
            if target_element.bottom:
                bottom = target_element.bottom.id
            else:
                bottom = False
            if target_element.left:
                left = target_element.left.id
            else:
                left = False
            if target_element.right:
                right = target_element.right.id
            else:
                right = False

            result_dict = {"top": top,
                           "bottom": bottom,
                           "left": left,
                           "right": right
                           }
            return result_dict
        else:
            return "SKU is absent in annotation bucket"
