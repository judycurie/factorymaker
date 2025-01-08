# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
author: Judy Curie
date: 08.01.2025
"""

import json
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from shapely.geometry import Polygon
import itertools


# Open the JSON file
with open('input.json') as f:
    data = json.load(f)

    
# Sort buildings by size (area)
sorted_buildings = sorted(
    data["buildings"],
    key=lambda b: b["dimensions"][0] * b["dimensions"][1],  # Calculate area as width * height
    reverse=True  # Largest area first
    )


path1 = 10 #Path 1 minimal lenght
path2 = 100 #Path 2 minimal lenght

# Function to generate additional permutations
def generate_permutations_with_additions(buildings, path1=10, path2=100):
    
    # Create dimension permutations (original and rotated) for each building
    dimension_permutations = [
        
        [
            {"name": building["name"], "dimensions": building["dimensions"]},  # Original orientation
            {"name": building["name"], "dimensions": building["dimensions"][::-1]},  # Rotated orientation
        ]
        if building["name"] == "Building 1" or building["name"] == "Building 3"
        else [
            
            {"name": building["name"], "dimensions": [building["dimensions"][0] + path1, building["dimensions"][1]]},  # Add 10 to first dimension of Building 2
            {"name": building["name"], "dimensions": [building["dimensions"][0], building["dimensions"][1] + path1]},  # Add 10 to second dimension of Building 2
            {"name": building["name"], "dimensions": [building["dimensions"][1],building["dimensions"][0] + path1]},  # Rotated orientation
            {"name": building["name"], "dimensions": [building["dimensions"][1]+ path1,building["dimensions"][0]]},  # Rotated orientation
        ]
        if building["name"] == "Building 2" 
        
        else [
           
            {"name": building["name"], "dimensions": [building["dimensions"][0] + path2, building["dimensions"][1]]},  # Add 100 to first dimension of Building 4
            {"name": building["name"], "dimensions": [building["dimensions"][0], building["dimensions"][1] + path2]},  # Add 100 to second dimension of Building 4
            {"name": building["name"], "dimensions": [building["dimensions"][1],building["dimensions"][0] + path2]},  # Rotated orientation
            {"name": building["name"], "dimensions": [building["dimensions"][1]+ path2,building["dimensions"][0]]},  # Rotated orientation
        ]
        
        for building in buildings
    ]
    
    # Combine all dimension permutations without changing the order of buildings
    all_permutations = list(itertools.product(*dimension_permutations))
    return all_permutations

# Generate all permutations with the new additions
all_permutations = generate_permutations_with_additions(sorted_buildings,path1,path2)

# Display results
for i, permutation in enumerate(all_permutations[:36], start=1):  # Display first 5 permutations for brevity
    print(f"Permutation {i}:")
    for building in permutation:
        print(f"  {building['name']} - {building['dimensions']}")
    print()

# Total permutations
print(f"Total permutations generated: {len(all_permutations)}")

# BEST-FIT ALGORITHM
def best_fit_pack(buildings):
    positions = []  # Store the bottom-left coordinates of each building
    occupied = []  # Track occupied spaces as rectangles
    max_width = 0  # Bounding box width
    max_height = 0  # Bounding box height

    for building in buildings:
        width, height = building["dimensions"]

        # Initialize best position and score
        best_x, best_y = 0, 0
        best_score = float("inf")

        # Try to fit the building at each position in the current layout
        for x, y, w, h in occupied:
            # Check to the right of the current rectangle
            new_x, new_y = x + w, y
            if not intersects(new_x, new_y, width, height, occupied):
                score = max(max_width, new_x + width) * max(max_height, new_y + height)
                if score < best_score:
                    best_x, best_y = new_x, new_y
                    best_score = score

            # Check above the current rectangle
            new_x, new_y = x, y + h
            if not intersects(new_x, new_y, width, height, occupied):
                score = max(max_width, new_x + width) * max(max_height, new_y + height)
                if score < best_score:
                    best_x, best_y = new_x, new_y
                    best_score = score

        # If no position fits, place it at the bottom-left corner of a new row
        if best_score == float("inf"):
            best_x = max_width
            best_y = 0

        # Update layout
        positions.append((best_x, best_y))
        occupied.append((best_x, best_y, width, height))
        max_width = max(max_width, best_x + width)
        max_height = max(max_height, best_y + height)
         

    return positions, max_width * max_height

# Helper function to check if a building intersects with the layout
def intersects(x, y, w, h, occupied):
    for ox, oy, ow, oh in occupied:
        if not (x + w <= ox or x >= ox + ow or y + h <= oy or y >= oy + oh):
            return True
    return False

print("Best FIt")
print(best_fit_pack(list(all_permutations[0])))

# Create Arragnement Function
def create_arrangement_dict(arrangement_id, buildings, paths, total_area, objective_1, objective_2):
    arrangement = {
        "arrangement_id": arrangement_id,
        "buildings": [
            {
                "name": building["name"],
                "location": building["location"],
                "dimensions": building["dimensions"]
            }
            for building in buildings
        ],
        "paths": [
            {
                "name": path["name"],
                "length": path["length"],
                "connected_buildings": path["connected_buildings"]
            }
            for path in paths
        ],
        "total_area": total_area,
        "objectives": {
            "objective_1": objective_1,
            "objective_2": objective_2
        }
    }
    return arrangement

# Helper function to get the center of a building
def get_center(location, dimensions):
     return [location[0] + dimensions[0] / 2, location[1] + dimensions[1] / 2]

# Generetate Arragements

a=[]
for i, permutation in enumerate(all_permutations[:len(all_permutations)-1], start=0):  # Display first 5 permutations for brevity
    arrangement_id = i
    
    buildings = []
    j=0
    for building in permutation:
       
        buildings.append({"name": building['name'], "location": best_fit_pack(list(all_permutations[i]))[0][j], "dimensions": building['dimensions']})
       
        j+=1
    
    paths = [
        {"name": "Path 1", "length": path1, "connected_buildings": ["Building 1", "Building 2"]},
        {"name": "Path 2", "length": path2, "connected_buildings": ["Building 3", "Building 4"]},
    ]
  
       
    total_area = best_fit_pack(list(all_permutations[i]))[1]
    objective_1 = path1+path2 # Length of paths
    objective_2 = total_area # Total area

    arrangement_dict = create_arrangement_dict(arrangement_id, buildings, paths, total_area, objective_1, objective_2)
    a.append(arrangement_dict)
    

# Display the result
print(a)
print(len(a))
# Write the arrangements to json
with open('output.json', 'w') as f:
    json.dump(a, f)



