from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
import numpy as np
from stl import mesh

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'stl'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            return redirect(url_for('process_file', filename=filename))
    return render_template('index.html')

@app.route('/process/<filename>')
def process_file(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Load the STL file
    your_mesh = mesh.Mesh.from_file(filepath)

    # Bounding Box Dimensions
    minx = your_mesh.x.min()
    maxx = your_mesh.x.max()
    miny = your_mesh.y.min()
    maxy = your_mesh.y.max()
    minz = your_mesh.z.min()
    maxz = your_mesh.z.max()
    
    x_dim = maxx - minx
    y_dim = maxy - miny
    z_dim = maxz - minz

    # Surface Area Calculation
    def calculate_surface_area(stl_mesh):
        triangles = stl_mesh.vectors
        a = triangles[:, 1] - triangles[:, 0]
        b = triangles[:, 2] - triangles[:, 0]
        cross_product = np.cross(a, b)
        area = np.linalg.norm(cross_product, axis=1) / 2
        return np.sum(area)

    # Volume Calculation
    def calculate_volume(stl_mesh):
        triangles = stl_mesh.vectors
        a = triangles[:, 0]
        b = triangles[:, 1]
        c = triangles[:, 2]
        volume = np.abs(np.einsum('ij,ij->i', a, np.cross(b, c))) / 6
        return np.sum(volume)

    surface_area = calculate_surface_area(your_mesh)
    volume = calculate_volume(your_mesh)

    return render_template('result.html', x_dim=x_dim, y_dim=y_dim, z_dim=z_dim, surface_area=surface_area, volume=volume, filename=filename)

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
