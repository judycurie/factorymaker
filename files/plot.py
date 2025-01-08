# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:36:56 2025

@author: judyt
"""
import itertools

# Buildings data
buildings = [
    {"name": "Building 1", "dimensions": [2800, 3300]},
    {"name": "Building 2", "dimensions": [600, 850]},
    {"name": "Building 3", "dimensions": [1500, 2450]},
    {"name": "Building 4", "dimensions": [400, 740]},
]

# Function to generate permutations of dimensions
def generate_permutations(dimensions):
    return list(itertools.permutations(dimensions))

# Recursive function to create the graph
def build_graph(buildings, index=0):
    if index >= len(buildings):
        return None  # Base case: no more buildings to process

    building = buildings[index]
    name = building["name"]
    permutations = generate_permutations(building["dimensions"])
    
    # Node for the current building
    node = {
        "name": name,
        "permutations": []
    }
    
    # Generate child nodes for each permutation
    for perm in permutations:
        child_node = {
            "dimensions": perm,
            "children": build_graph(buildings, index + 1),  # Recurse for the next building
        }
        node["permutations"].append(child_node)
    
    return node

# Sort buildings by area (descending)
sorted_buildings = sorted(buildings, key=lambda b: b["dimensions"][0] * b["dimensions"][1], reverse=True)

# Build the graph starting from the largest building
building_graph = build_graph(sorted_buildings)

# Function to visualize the graph (optional, for debugging purposes)
def print_graph(node, depth=0):
    if node is None:
        return
    indent = "  " * depth
    print(f"{indent}Building: {node['name']}")
    for perm in node["permutations"]:
        print(f"{indent}  Dimensions: {perm['dimensions']}")
        if perm["children"]:
            print(f"{indent}  Children:")
            print_graph(perm["children"], depth + 2)

# Print the graph
print_graph(building_graph)

