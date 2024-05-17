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
# Import necessary modules and functions
from retailtree import RetailTree, Annotation
from retailtree.utils.dist_func import manhattan, euclidean
import json

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

# Build the spatial tree structure using the euclidean distance function
rt.build_tree(dist_func=euclidean)

# Retrieve and print annotations within a radius of 1 from the annotation with id=3
print(rt.neighbors(id=3, radius=1))

# Retrieve and print the Top, Bottom, Left, and Right neighboring annotations
# of the annotation with id=3 within a radius of 1 and a minimum overlap of 0.5
print(rt.TBLR(id=3, radius=1, overlap=0.5))

# Retrieve and print neighboring annotations of the annotation with id=3
# within a radius of 1 and angle range from 0 to 180 degrees
print(rt.neighbors_wa(id=3, radius=1, amin=0, amax=180))

# Retrieve and print the coordinates of the annotation with id=3
print(rt.get(id=3).get_coords())
```
