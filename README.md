# factorymaker

# LOGIC

1. If the paths can be regarded as areas attached to the buidlings with the minimum lenght of the path as the added width(x) or lenght(y)of the building, the problem can be reduced to the fitting the rectangles trying to minimize the bounding box area and satisfying the constraints on the adjacency of the buildings which are connected by paths.

2.


## Installation

- Install the theme with pip:


```
pip install shapely
```
- After the theme is installed, edit your `mkdocs.yml` file and set the theme name to `simple-blog`:

```
theme:
    name: simple-blog
```

## Example
-> input.json -> factorymaker.py -> output.json -> plot.py


##Selected solutions


![](../../figures/id1.png)
Arrangament 1
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
![](../../figures/id23.png)
Arrangament 23

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
