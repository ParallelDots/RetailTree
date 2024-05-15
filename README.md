# RetailTree
RetailTree is a Python library designed for efficient management and querying of spatial data utilizing a tree-based data structure. Specifically, RetailTree employs a VP (Vantage Point) tree for optimized spatial data management.

# Key Features

- Nearest Neighbor Search: RetailTree enables finding the nearest neighbors in 2D space.
- Tree-Based Structure: Utilizes a VP tree for optimized spatial data management.
- Top, Right, Left, and Bottom Annotations:
  Supports retrieval of annotations based on their relative positions.
- Annotations within Angle Range: Provides functionality to retrieve annotations within a specified angle range relative to a reference point.

# Installation

You can install retailTree via pip:

```
1) clone the repo
2) cd retailTree
3) pip install retailTree-0.0.1-py3-none-any.whl
```

# Usage

```
from retailTree import retailTree, Annotation
from retailTree.utils.dist_func import manhattan, euclidean

obj = RetailTree()

# Adding annotations
obj.add_annotation(id=1, x_min=1, y_min=1, x_max=1, y_max=1)
obj.add_annotation(id=2, x_min=2, y_min=2, x_max=2, y_max=2)

# Tree Building
obj.build_tree(dist_func=manhattan)

# Get neighbors-annotations within radius
obj.find_neighbors(id=961360402, radius=1)

# Get Top, Bottom, Right, Left annotations
obj.TBLR(id=961360402, radius=1.4)

# Get neighboring annotations within a particular angle range
obj.get_neighbors_within_angle(
        id=963804130, radius=1, min_angle=0, max_angle=90)

```
