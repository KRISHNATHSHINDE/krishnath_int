## Documentation for numpy-stl

- Simple library to make working with STL files (and 3D objects in general) fast and easy.
- Due to all operations heavily relying on numpy this is one of the fastest STL editing libraries for Python available.

- Links:
- [The Source]( https://github.com/WoLpH/numpy-stl)
- [Project Page]( https://pypi.python.org/pypi/numpy-stl)
- [Documentation](http://numpy-stl.readthedocs.org/en/latest/)
- [Cube Example](https://micronote.tech/2020/12/Generating-STL-Models-with-Python/)

### QuickStart
 - Importing
    - import numpy
   - from stl import mesh
  
 - Using Existing STL File
   - your_mesh = mesh.Mesh.from_file('some_file.stl')
  
 - Creating an STL File
   - VERTICE_COUNT = 100
   - data = numpy.zeros(VERTICE_COUNT, dtype=mesh.Mesh.dtype)
    - your_mesh = mesh.Mesh(data, remove_empty_areas=False)
  
 - Accessing mesh normals and vectors
   - your_mesh.normals
   - your_mesh.v0, your_mesh.v1, your_mesh.v2
  
 - Accessing individual points (concatenation of v0, v1 and v2 in triplets)
   - assert (your_mesh.points[0][0:3] == your_mesh.v0[0]).all()
   - assert (your_mesh.points[0][3:6] == your_mesh.v1[0]).all()
   - assert (your_mesh.points[0][6:9] == your_mesh.v2[0]).all()
  
 - Saving STL File
    - your_mesh.save('new_stl_file.stl')
  

### Plotting using MatPlotlib
- Importing
   - from stl import mesh
   - from mpl_toolkits import mplot3d
   - from matplotlib import pyplot

 - Create a new plot
   - figure = pyplot.figure()
   - axes = figure.add_subplot(projection='3d')

- Load the STL files and add the vectors to the plot
   - your_mesh = mesh.Mesh.from_file('tests/stl_binary/HalfDonut.stl')
   -  axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

 - Auto scale to the mesh size
   - scale = your_mesh.points.flatten()
   - axes.auto_scale_xyz(scale, scale, scale)

- Show the plot to the screen
   - pyplot.show()
 
### 


### Cube Example



