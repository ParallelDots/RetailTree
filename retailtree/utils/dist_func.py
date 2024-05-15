import math


# Function to calculate euclidean distance
def euclidean(p1, p2):
    return math.sqrt(pow((p2[0]-p1[0]), 2) + pow((p2[1]-p1[1]), 2))


# Function to calculate manhattan distance
def manhattan(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
