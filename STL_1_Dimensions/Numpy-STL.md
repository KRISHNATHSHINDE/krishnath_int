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


### Evaluating Mesh Properties
- Importing
  - import numpy as np
  - from stl import mesh

 - Using an existing closed stl file:
   - your_mesh = mesh.Mesh.from_file('some_file.stl')

 - Evaluating
   - volume, cog, inertia = your_mesh.get_mass_properties()
   - print("Volume                                  = {0}".format(volume))
   - print("Position of the center of gravity (COG) = {0}".format(cog))
   - print("Inertia matrix at expressed at the COG  = {0}".format(inertia[0,:]))
   - print("                                          {0}".format(inertia[1,:]))
   - print("                                          {0}".format(inertia[2,:]))


### Cube Generation
 - Importing
   - import numpy as np
    - from stl import mesh

- Define the 8 vertices of the cube
  - vertices = np.array([\
    [-1, -1, -1],
    [+1, -1, -1],
    [+1, +1, -1],
    [-1, +1, -1],
    [-1, -1, +1],
    [+1, -1, +1],
    [+1, +1, +1],
    [-1, +1, +1]])
 - Define the 12 triangles composing the cube
    - faces = np.array([\
    [0,3,1],
    [1,3,2],
    [0,4,7],
    [0,7,3],
    [4,5,6],
    [4,6,7],
    [5,1,2],
    [5,2,6],
    [2,3,6],
    [3,7,6],
    [0,1,5],
    [0,5,4]])

- Create the mesh
   - cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
   - for i, f in enumerate(faces):
   - for j in range(3):
   - cube.vectors[i][j] = vertices[f[j],:]

- Write the mesh to file "cube.stl"
   - cube.save('cube.stl')

## To-Do
- Generate STL Files from input i.e vertices and faces
- Display the STL Files on a UI
- Extract Dimensions from STL Files, it's properties like surface areaa and volume.
- Deploy it using React and Flask