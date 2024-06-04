
from typing import Any


class Annotation:
    """
    Data objects for annotations.

    Parameters
    ----------
    - id:
        Int. Id of the Annotation.
    - x_min:
        Float. Left-most coordinate of rectangular annotation.
    - x_max:
        Float. Right-most coordinate of rectangular annotation.
    - y_min:
        Float. Top-most coordinate of rectangular annotation.
    - y_max:
        Float. Bottom-most coordinate of rectangular annotation.
    - label:
        Any. Optional label associated with the annotation.
    - metadata:
        Dict. Optional metadata associated with the annotation.   

    """

    def __init__(self, id, x_min, y_min, x_max, y_max, label=None, metadata=None):
        # type:(int, float, float, float, float, Any , dict[Any, Any]) -> None
        self.__id = int(id)
        self.__x_min = float(x_min)
        self.__x_max = float(x_max)
        self.__y_min = float(y_min)
        self.__y_max = float(y_max)
        self.__label = label
        self.__metadata = metadata

        self.__x_mid = None
        self.__y_mid = None
        self.__length = None
        self.__width = None

        # TODO Check compatibility for older versions of python
        self.right = None  # type: Annotation
        self.left = None  # type: Annotation
        self.top = None  # type: Annotation
        self.bottom = None  # type: Annotation

        self.overlap_right = 0
        self.overlap_top = 0
        self.overlap_bottom = 0
        self.overlap_left = 0

    # TODO Change x_min to x_min
    @property
    def id(self):
        return self.__id

    @property
    def x_min(self):
        return self.__x_min

    @property
    def y_min(self):
        return self.__y_min

    @property
    def x_max(self):
        return self.__x_max

    @property
    def y_max(self):
        return self.__y_max

    @property
    def label(self):
        return self.__label

    @property
    def metadata(self):
        return self.__metadata

    # TODO
    @property
    def x_mid(self):
        if self.__x_mid is None:
            self.__x_mid = (abs(self.__x_min)+abs(self.__x_max))/2
        return self.__x_mid

    @property
    def y_mid(self):
        if self.__y_mid is None:
            self.__y_mid = (abs(self.__y_min)+abs(self.__y_max))/2
        return self.__y_mid

    @property
    def length(self):
        if self.__length is None:
            self.__length = abs(self.__x_max - self.__x_min)
        return self.__length

    @property
    def width(self):
        if self.__width is None:
            self.__width = abs(self.__y_max - self.__y_min)
        return self.__width

    def get_coords(self):
        """ 
        Retrieve coordinates of the bounding box.

        Returns:
        dict: A dictionary containing the coordinates of the bounding box.
            - "x_min": The minimum x-coordinate of the bounding box.
            - "y_min": The minimum y-coordinate of the bounding box.
            - "x_max": The maximum x-coordinate of the bounding box.
            - "y_max": The maximum y-coordinate of the bounding box.
            - "x_mid": The x-coordinate of the midpoint of the bounding box.
            - "y_mid": The y-coordinate of the midpoint of the bounding box.
        """
        # TODO
        data = {"x_min": self.__x_min,
                "y_min": self.__y_min,
                "x_max": self.__x_max,
                "y_max": self.__y_max,
                "x_mid": self.x_mid,
                "y_mid": self.y_mid}
        return data

    def __repr__(self) -> str:
        return str(self.id)
