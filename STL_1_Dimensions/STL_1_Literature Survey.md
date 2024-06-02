## Literature Survey on STL Files, Format and Calculation of Dimensions

## Introduction

 - STL files are the cornerstone in the field of 3D printing and Computer Aided Design(CAD).
 - The STL file is derived from the word STereoLithography and is a format created by Charles Hull for the first commercial AM process, produced by the US company 3D Systems in the late 1980s. 
 -  Some literature has suggested that STL stands for Stereolithography Tessellation Language or Standard Triangle Language. 
 - STL files are generated from 3D CAD data within the CAD system. 
 - The output is a boundary representation that is approximated by a mesh of triangles.
 - They store information about the surface geometry of 3D objects without any representation of color, texture, or other attributes. 
 - This literature survey explores the evolution of STL files, their structure, methods to extract dimensions, calculation of area and volume, and the generation of STL files using generative AI.
 

## Evolution of STL Files

 - STL files were introduced by 3D Systems in 1987 as part of the
   stereolithography CAD software.  
 - The format was designed to be simple and to facilitate the process of 3D printing. 
  - Over the years STL files have become the de facto standard for 3D printing and rapid
   prototyping due to their simplicity and widespread support across
   various software platforms.

**Key Developements:**

 -  **1987**: Introduction of STL files by 3D Systems.
-   **1990s**: Widespread adoption in 3D printing and prototyping industries.
-   **2000s**: Development of more sophisticated file formats like OBJ and AMF, but STL remains popular.
-   **2010s**: Integration with more advanced CAD software and use in generative design processes.

## File Format of STL

 - STL files can be output as either **Binary** or **ASCII (American Standard Code for Information Interchange - text)** format. 
 - The ASCII format is less common (due to the larger file sizes) but easier to understand and is generally used for illustration.
 - To reduce the file size, STL files can be saved in binary format instead of ASCII format. ASCII files are readable by humans, but binary files are about 1/6th the size of the same file saved in ASCII format (typically 1:5.65 when saving as binary).
 - STL files only show approximations of the surface or solid entities, and so any information concerning the color, material, build layers, or history is ignored during the conversion process. 
 
 - **Structure:**
   - An STL file consists of lists of triangular facets. Each triangular facet is uniquely identified by a unit normal vector and three vertices. 
   - The STL file itself holds no dimensions, so the AM machine operator must know whether the dimensions are mm, inches, or some other unit. 
   - Since each vertex also has 3 numbers, there are a total of 12 numbers to describe each triangle.
   - The file begins with an object name delimited as a solid. Triangles can be in any order, each delimited as a facet.
   - The facet line also includes the normal vector for that triangle. 
   - This normal is calculated from any convenient location on the triangle and may be from one of the vertices or from the center of the triangle.
   - It is defined that the normal is perpendicular to the triangle and is of unit length. 
   - The normal is used to define the outside of the surface of the solid, essentially pointing away from the part.
   - The group of three vertices defining the triangle is delimited by the terms “outer loop” and “endloop.”
   
   ![enter image description here](https://www.fabbers.com/_file/_/~fabbers/image/FabData/StL-ASCII.gif)
   ![Triangle Representation](https://web-objects.markforged.com/craft/common/_small/STL-triangle.png)
	 

## Extracting Dimensions from STL Files

### Dimensions

 - To extract dimensions from STL files, one must parse the vertex coordinates and compute the bounding box of the model. 
 - The bounding box gives the minimum and maximum extents in all three dimensions (x, y, z).
 - **Steps:**
   -  **Parse the File:** Read the vertex coordinates from the STL File.
   - **Compute Min/Max Values:** Identify the minimum  and maximum values for x,yz and z coordinates.
   - **Calculate Dimensions:** The dimensions of the object are given by the difference b/w the max and min values in each direction.

### Surface Area and Volume

 - The surface area and volume of the object can be calculated using the triangular facets described in the STL file.
 - **Surface Area:**
   - The area of each triangle can be calculated using the vertices, and the total surface area is the sum of all the areas of the triangles.
   - **Area= 1/2 [​ ∑(  i=1-N) ​∥(v2i​−v1i​)×(v3i​−v1i​)∥ ]**
  - **Volume:** 
  - The volume enclosed by the triangulated surface can be computed using the divergence theorem, often implemented by summing the signed volumes of tetrahedrons formed by each triangle and the origin.
  - **Volume = 1/6 [ ∑ (i=1-N​) v1i​⋅(v2i​×v3i​) ]**

