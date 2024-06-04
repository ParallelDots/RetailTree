from retailtree.structs.annotation_struct import Annotation
from retailtree.logics.overlap import calculate_overlap
# Establishing tob-bottom connections


def top_bottom_connections(i, j, given_overlap_percentage):
    # type:(Annotation, Annotation, float) -> None
    if (i.y_max > j.y_max and i.y_min - i.width < j.y_max):
        # Finding overlap percentage
        overlap_percentage = calculate_overlap(i, j, axis='x')/j.length

        # Checking if the annotation overlaps more than 50 percent
        if overlap_percentage >= given_overlap_percentage:
            if i.top == None and j.bottom == None:
                i.overlap_top, i.top,  j.bottom = overlap_percentage, j, i

            # Consider the closest annotation
            elif j.bottom is not None and abs(i.y_min-j.y_max) < abs(j.bottom.y_min - j.y_max):
                j.bottom.top = None
                i.overlap_top, i.top,  j.bottom = overlap_percentage, j, i
            # Consider the closest annotation
            elif i.top is not None and ((j.y_max > i.top.y_max) or (j.y_max == i.top.y_max and overlap_percentage > i.overlap_top)):
                i.top.bottom = None
                i.overlap_top, i.top,  j.bottom = overlap_percentage, j, i


# Establishing tob-bottom connections
def bottom_top_connections(i, j, given_overlap_percentage):
    # type:(Annotation, Annotation, float) -> None
    if j.top == None:
        if (i.y_max <= j.y_min and i.y_max + i.width > j.y_min):
            # Finding overlap percentage
            overlap_percentage = calculate_overlap(i, j, axis='x')/j.length

            # Checking if the annotation overlaps more than 50 percent
            if overlap_percentage >= given_overlap_percentage:
                if i.bottom == None:
                    i.overlap_bottom, i.bottom, j.top = overlap_percentage, j, i
                elif (abs(i.y_max - j.y_min) < abs(i.bottom.y_min - i.y_max)) or (j.y_min == i.bottom.y_min and overlap_percentage > i.overlap_bottom):
                    i.bottom.top = None
                    i.overlap_bottom, i.bottom, j.top = overlap_percentage, j, i
