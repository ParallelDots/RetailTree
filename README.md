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
pip install retailtree
```

# Usage

```
from retailtree import RetailTree, Annotation
from retailtree.utils.dist_func import manhattan, euclidean

# Create annotation object
ann1 = Annotation(id=1, x_min=2, y_min=1, x_max=3, y_max=2)
    ann2 = Annotation(id=2, x_min=1, y_min=2, x_max=2, y_max=3)
    ann3 = Annotation(id=3, x_min=2, y_min=2, x_max=3, y_max=3)
    ann4 = Annotation(id=4, x_min=3, y_min=2, x_max=4, y_max=3)
    ann5 = Annotation(id=5, x_min=2, y_min=3, x_max=3, y_max=4)

annotations = [ann1, ann2, ann3, ann4, ann5]

# Create retailtree object
rt = RetailTree()

# Adding annotations to retailtree
for ann in annotations:
  rt.add_annotation(ann)


# Build tree
rt.build_tree(dist_func=euclidean)

# Get neighbors-annotations within radius
print(rt.neighbors(id=3, radius=1))

# Get Top, Bottom, Right, Left annotations
print(rt.TBLR(id=3, radius=1, overlap=0.5))

# Get neighboring annotations within a particular angle range
print(rt.neighbors_wa(id=3, radius=1, amin=0, amax=180))

# Get annotation properties
print(rt.get(id=3).get_coords())

```
