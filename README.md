# polygonlite

polygonlite is a lighweight, yet powerful (um, robust?) library for the usual Point, Edge and Polygon operations in Python.

  - Point class which encompasses methods like project on edge, etc.
  - Edge class which has more powerful features like angle between edges, intersection of edges, etc.
  - Polygon class, which is still under construction.

# New Features!

  - polygon.area()


# Features

On Polygon objects, you can:
  - polygon.contains(point)
  - polygon.flip()
  - polygon.simplify()
  - polygon.area()
  - polygon.is_clockwise()
  - polygon.is_anticlockwise()
  - polygon.as_array()
  - polygon.as_linked_list()



On Edge objects, you can:
  - edge.angle_between(anotherEdge)
  - edge.is_parallel(anotherEdge)
  - edge.intersect(anotherEdge)
  - edge.on_segment(point)
  - edge.project_point(point)
  - edge.slope()
  - edge.length()
  - edge.vector()
  - edge.unit_vector()
  - edge.y_intercept()
  - edge.midpoint()
  - edge.as_array()



On Point objects, you can:
  - point.distance(anotherPoint)
  - point.project(edge)
  - point.as_array()
 

More methods are coming soon, and examples will also be updated soon.


## Fixes

 - polygon.is_clockwise() and polygon.is_anticlockwise() now work even for concave polygons.

## Installation

polygonlite runs on Python. (Python2 tested, Python3 under-testing).

You can simply install using **pip**.

```
pip install polygonlite
```


## Usage
Firstly, you need to import `polygonlite`.
```
from polygonlite import Polygon, Edge, Point
```

### Point
#### Initialization
```
origin = Point(0, 0)
point1 = Point([0, 1])
point2 = Point(x = 2, y = 0)
```

#### Simple use cases
```
distance = origin.distance(point1)
```


### Edge
#### Initialization
```
edge1 = Edge([0, 0], [5, 5])
edge2 = Edge([5, 0], [0, 5])
edge3 = Edge([5, 5], [10, 0])
```

#### Simple use cases
```
common_point = edge1.intersect(edge2)
angle = edge1.angle_between(edge3)
edge1_edge2_parallel = edge1.is_parallel(edge2)
origin_lies_on_edge = edge1.on_segment(origin)
length_of_edge1 = edge1.length()
vector_of_edge1 = edge1.vector()
slope_of_edge1 = edge1.slope()
mid_of_edge1 = edge1.midpoint(0)
```


### Polygon
#### Initialization
```
polygon = Polygon([[0, 0], [0, 5], [0, 10], [10, 10], [10, 0]])
simplified = polygon.simplify()
polygon_contains_origin = simplified.contains(origin)
is_it_clockwise = polygon.is_clockwise()
reversed = polygon.flip()
```

## Development

Want to contribute? Great! No prerequisites. You're welcome, go on!


## Todos

 - More operations on Polygon class
 - Add tests

License
----

MIT


**Free Software, Hell Yeah!**