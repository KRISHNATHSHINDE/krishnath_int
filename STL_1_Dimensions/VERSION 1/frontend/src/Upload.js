// src/Upload.js
import React, { useState } from 'react';
import axios from 'axios';
import { Canvas } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';

const Upload = () => {
  const [file, setFile] = useState(null);
  const [properties, setProperties] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', file);
  
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
  
      console.log(response.data);
      setProperties(response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload</button>
      {properties && (
        <div>
          <p>X Dimensions: {properties.x_dimensions}</p>
          <p>Y Dimensions: {properties.y_dimensions}</p>
          <p>Z Dimensions: {properties.z_dimensions}</p>
          <p>Surface Area: {properties.surface_area}</p>
          <p>Volume: {properties.volume}</p>
        </div>
      )}
      {/* Placeholder for 3D Viewer */}
      <Canvas>
        <ambientLight />
        <pointLight position={[10, 10, 10]} />
        {/* Replace with your 3D model component */}
        {/* <Model /> */}
        <OrbitControls />
      </Canvas>
    </div>
  );
};

export default Upload;
