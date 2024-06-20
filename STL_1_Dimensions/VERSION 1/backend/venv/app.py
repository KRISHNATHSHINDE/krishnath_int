from flask import Flask, request, jsonify
from stl import mesh
import numpy as np

app = Flask(__name__)

def calculate_surface_area(stl_mesh):
    triangles = stl_mesh.vectors
    a = triangles[:, 1] - triangles[:, 0]
    b = triangles[:, 2] - triangles[:, 0]
    cross_product = np.cross(a, b)
    area = np.linalg.norm(cross_product, axis=1) / 2
    return np.sum(area)

def calculate_volume(stl_mesh):
    triangles = stl_mesh.vectors
    a = triangles[:, 0]
    b = triangles[:, 1]
    c = triangles[:, 2]
    volume = np.abs(np.einsum('ij,ij->i', a, np.cross(b, c))) / 6
    return np.sum(volume)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_path = 'uploaded_file.stl'
        file.save(file_path)
        your_mesh = mesh.Mesh.from_file(file_path)

        # Dimensions -> Bounding Box
        minx = your_mesh.x.min()
        maxx = your_mesh.x.max()
        miny = your_mesh.y.min()
        maxy = your_mesh.y.max()
        minz = your_mesh.z.min()
        maxz = your_mesh.z.max()

        x_dimensions = maxx - minx
        y_dimensions = maxy - miny
        z_dimensions = maxz - minz

        # Surface Area and Volume
        surface_area = calculate_surface_area(your_mesh)
        volume = calculate_volume(your_mesh)

        return jsonify({
            'x_dimensions': x_dimensions,
            'y_dimensions': y_dimensions,
            'z_dimensions': z_dimensions,
            'surface_area': surface_area,
            'volume': volume
        })

if __name__ == '__main__':
    app.run(debug=True)
