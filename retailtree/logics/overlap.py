from retailtree.structs.annotation_struct import Annotation


def calculate_overlap(anno_1, anno_2, axis):
    # type:(Annotation, Annotation, str) -> float
    """
    Calculate overlap of two annotations in given axis.
    Parameters
    ----------
    - anno_1:
        Annotation. The first annotation.
    - anno_2:
        Annotation. The second annotation.
    - axis:
        Str. The axis on which overlap is to be calculated.
        - "x" results in overlap being calculated on x-axis.
        - "y" results in overlap being claculated on y-axis.
    """
    if axis == 'x':
        overlap = max(0, min(anno_1.x_max, anno_2.x_max) -
                      max(anno_1.x_min, anno_2.x_min))
    elif axis == 'y':
        overlap = max(0, min(anno_1.y_max, anno_2.y_max) -
                      max(anno_1.y_min, anno_2.y_min))
    else:
        raise ValueError('Axis can only be either "x" or "y"')
    return overlap
