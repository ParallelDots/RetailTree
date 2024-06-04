from retailtree.structs.annotation_struct import Annotation
from retailtree.logics.overlap import calculate_overlap


# Establishing right-left connections
def right_left_connections(i, j, given_overlap_percentage):
    # type:(Annotation, Annotation, float) -> None
    # Checking the candidate annotations is in the range of base annotations corresponds to x axis
    if (i.x_min < j.x_min and i.x_max + i.length > j.x_min):
        # Finding overlap percentage
        overlap_percentage = calculate_overlap(i, j, axis='y')/j.length

        # Checking if the annotation overlaps more than 50 percent
        if overlap_percentage >= given_overlap_percentage:
            if i.right == None and j.left == None:
                i.overlap_right, i.right, j.left = overlap_percentage, j, i
            elif j.left is not None and abs(i.x_max - j.x_min) < (j.left.x_max - j.x_min):
                j.left.right = None
                i.overlap_right, i.right, j.left = overlap_percentage, j, i
            elif i.right is not None and (j.x_min < i.right.x_min or (j.x_min == i.right.x_min and overlap_percentage > i.overlap_right)):
                i.right.left = None
                i.overlap_right, i.right, j.left = overlap_percentage, j, i


# Establishing left-right connection
def left_right_connections(i, j, given_overlap_percentage):
    # type:(Annotation, Annotation, float) -> None
    if j.right == None:
        # Checking the candidate annotations is in the range of base annotations corresponds to x axis
        if (i.x_min >= j.x_max and i.x_min - i.length < j.x_max):
            # Finding overlap percentage
            overlap_percentage = calculate_overlap(i, j, axis='x')/j.length
            # Checking if the annotation overlaps more than 50 percent
            if overlap_percentage >= given_overlap_percentage:
                if i.left == None:
                    i.overlap_left, i.left, j.right = overlap_percentage, j, i
                elif (abs(i.x_min - j.x_max) < abs(i.left.x_max - i.x_min)) or (j.x_max == i.left.x_max and overlap_percentage > i.overlap_left):
                    i.left.right = None
                    i.overlap_left, i.left, j.right = overlap_percentage, j, i
