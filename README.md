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

```python
pip install retailtree
```

# Usage

### Import necessary modules and functions

```python
# Imports
from retailtree import RetailTree, Annotation
from retailtree.utils.dist_func import manhattan, euclidean
import json
```

### Sample Usage 1: Creating Annotations with Annotation Class using a sample JSON file

```python
# Define the path to the JSON file containing annotations
file_path = './tests/test_data/test_data.json'

# Open and load the JSON file
with open(file_path, 'r') as file:
    annotations = json.load(file)

# Initialize a RetailTree object
rt = RetailTree()

# Iterate over the loaded annotations and create Annotation objects
for ann in annotations:
    # Create an Annotation object with the required properties
    ann_obj = Annotation(id=ann['id'], x_min=ann['x_min'], y_min=ann['y_min'], x_max=ann['x_max'], y_max=ann['y_max'])
    # Add the created Annotation object to the RetailTree
    rt.add_annotation(ann_obj)
```

# OR

### Sample Usage 2: Creating Annotations with Annotation Class

```python
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
```

## Building the Tree and Querying

### Building the Tree

```python
# Build the retail tree structure using the euclidean distance function
rt.build_tree(dist_func=euclidean)
```
### Querying the Tree
```python
# Retrieve and print annotations within a radius.
print(rt.neighbors(id=3, radius=1))

# Retrieve and print the Top, Bottom, Left, and Right neighboring annotations.
print(rt.TBLR(id=3, radius=1, overlap=0.5))

# Retrieve and print neighboring annotations of the annotation.
print(rt.neighbors_wa(id=3, radius=2, amin=0, amax=180))

# Retrieve and print the coordinates of the annotation.
print(rt.get(id=3).get_coords())
```
