# Phylotaxis
Blender project

The objective is to make 3D printable "organic" objects using 
[SVERCHOK/python](http://nikitron.cc.ua/sverchok_en.html). 

The origin is the [Blendersushi tutorial](https://www.youtube.com/watch?v=YgJTEBAGHGQ&t=278s)
where the result isn't a [non-manifold](https://blender.stackexchange.com/questions/7910/what-is-non-manifold-geometry).

## Recipe

- make a Fibonacci spiral using fib_spiral.py included with Sverchok
- get the Dirichlet cells from the spiral using **Voronoi** node
- use **scriptnode** with [face_gen.py](https://github.com/macbuse/Phylogenesis/blob/master/face_gen.py) as payload to add faces 
- make the mesh non-planar by translating vertices 
- trim extraneous vertices 
- use multi-extrude node to add geometry


## Remarks 

This is the first time I have used Sverchok and it's very convenient for prototyping.

I wrote face_gen.py as a scriptnode essentially to understand the 
[script interface](http://sverchok.readthedocs.io/en/latest/nodes/generators_extended/script3.html).
There is more than one way of adding a scriptnode and I must admit, from the doc, I  don't really see what the developer wants.


## Sample output

![output](https://github.com/macbuse/Phylogenesis/blob/master/Screenshot%202017-08-11%2012.17.26.png)

