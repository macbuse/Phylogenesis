# Phylogenesis
Blender project


The objective is to make 3D printable "organic" objects using 
[SVERCHOK/python](http://nikitron.cc.ua/sverchok_en.html). 

## Recipe

- make a Fibonacci spiral
- get the Dirichlet cells from the spiral using Voronoi node
- use **scriptnode** with face_gen.py as payload to add faces 
- make the mesh non-planar by translating vertices 
- use multi-extrude node to add geometry

