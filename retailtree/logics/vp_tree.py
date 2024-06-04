import math
import statistics as stats
from typing import Callable

from retailtree.structs.annotation_struct import Annotation


class VPTree:
    def __init__(self, points, dist_fn):
        # type:(list[Annotation], Callable[[tuple[float, float], tuple[float, float]], float]) -> None
        self.left = None
        self.right = None
        self.left_min = math.inf
        self.left_max = 0
        self.right_min = math.inf
        self.right_max = 0
        self.dist_fn = dist_fn

        if not len(points):
            raise ValueError('Points can not be empty.')

        # Vantage point is point furthest from parent vp.
        self.vp = points[0]
        points = points[1:]

        if len(points) == 0:
            return

        # Choose division boundary at median of distances.
        distances = [self.dist_fn(
            (self.vp.x_mid, self.vp.y_mid), (p.x_mid, p.y_mid)) for p in points]
        median = stats.median(distances)

        left_points = []
        right_points = []
        for point, distance in zip(points, distances):
            if distance >= median:
                self.right_min = min(distance, self.right_min)
                if distance > self.right_max:
                    self.right_max = distance
                    right_points.insert(0, point)  # put furthest first
                else:
                    right_points.append(point)
            else:
                self.left_min = min(distance, self.left_min)
                if distance > self.left_max:
                    self.left_max = distance
                    left_points.insert(0, point)  # put furthest first
                else:
                    left_points.append(point)

        if len(left_points) > 0:
            self.left = VPTree(points=left_points, dist_fn=self.dist_fn)

        if len(right_points) > 0:
            self.right = VPTree(points=right_points, dist_fn=self.dist_fn)

    def _is_leaf(self):
        return (self.left is None) and (self.right is None)

    def get_all_in_range(self, query, max_distance):
        # type: (tuple[float, float], float) -> list[tuple[float, Annotation]]
        neighbors = list() # type: list[tuple[float, Annotation]]
        nodes_to_visit = [(self, 0)]

        while len(nodes_to_visit) > 0:

            node, d0 = nodes_to_visit.pop(0)
            if node is None or d0 > max_distance:
                continue

            d = self.dist_fn(query, (node.vp.x_mid, node.vp.y_mid))
            if d < max_distance:
                neighbors.append((d, node.vp))

            if node._is_leaf():
                continue

            if node.left_min <= d <= node.left_max:
                nodes_to_visit.insert(0, (node.left, 0))
            elif node.left_min - max_distance <= d <= node.left_max + max_distance:
                nodes_to_visit.append((node.left,
                                       node.left_min - d if d < node.left_min
                                       else d - node.left_max))

            if node.right_min <= d <= node.right_max:
                nodes_to_visit.insert(0, (node.right, 0))
            elif node.right_min - max_distance <= d <= node.right_max + max_distance:
                nodes_to_visit.append((node.right,
                                       node.right_min - d if d < node.right_min
                                       else d - node.right_max))

        return neighbors
