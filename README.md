# factorymaker

## LOGIC

1. If the paths can be regarded as areas attached to the buidlings with the minimum lenght of the path as the added width(x) or lenght(y)of the building, the problem can be reduced to the fitting the rectangles trying to minimize the bounding box area and satisfying the constraints on the adjacency of the buildings which are connected by paths.

2. As the task is similar to packing problem, it is recommended to start with the larger objects. Therefore for each pair of the building connected with the path, to the smaller one the additional area is added -> this will help to fit all the rectangles.

3. By adding the minimal lenght of the path to the connecting building, all the solutions will be at minimum of objective 1, therefore it minimizes the time for search and guarantee high quality solutions.

4. While the problem when the rotation of the buildings is fair simple and all permuations as a graph structure can be drawn by hand (please check files/graph.jpg), when adding possible rotations the problem gets trickier.

![](../files/graph.jpg)

5. The program should be scalable by adding additional buildings to input.json, however adding additional paths would require adjustements to make it work.


## Installation

- Install all necessary librariries


```
pip install shapely
```



## Example
-> input.json -> factorymaker.py -> output.json -> plot.py
1. Store all the files in one directory.
2. Open factorymaker.py, generate permutations and best fits for them, export them to output.json.


##Selected solutions


![](../figures/id1.png)
Arrangament 1-> figures/id1.png
```
{'arrangement_id': 1,
  'buildings': [
  {'name': 'Building 1', 'location': (0, 0), 'dimensions': [2800, 3300]}, {'name': 'Building 3', 'location': (2800, 0), 'dimensions': [1500, 2450]}, {'name': 'Building 2', 'location': (2800, 2450), 'dimensions': [610, 850]}, {'name': 'Building 4', 'location': (3410, 2450), 'dimensions': [400, 850]}
  ],
  'paths': [
  {'name': 'Path 1', 'length': 10, 'connected_buildings': ['Building 1', 'Building 2']},
  {'name': 'Path 2', 'length': 100, 'connected_buildings': ['Building 3', 'Building 4']}],
  'total_area': 14190000,
  'objectives': {'objective_1': 110, 'objective_2': 14190000}
  },
```
![](../figures/id23.png)
Arrangament 23> figures/id23.png

```
{'arrangement_id': 23,
 'buildings': [
  {'name': 'Building 1', 'location': (0, 0), 'dimensions': [2800, 3300]},
  {'name': 'Building 3', 'location': (0, 3300), 'dimensions': [2450, 1500]}, {'name': 'Building 2', 'location': (2450, 3300), 'dimensions': [600, 860]}, {'name': 'Building 4', 'location': (2450, 4160), 'dimensions': [850, 400]}
  ],
  'paths': [
  {'name': 'Path 1', 'length': 10, 'connected_buildings': ['Building 1', 'Building 2']},
  {'name': 'Path 2', 'length': 100, 'connected_buildings': ['Building 3', 'Building 4']}
  ],
  'total_area': 15840000,
  'objectives': {'objective_1': 110, 'objective_2': 15840000}}

```
