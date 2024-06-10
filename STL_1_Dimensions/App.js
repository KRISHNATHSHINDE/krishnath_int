// src/App.js
import React from 'react';
import StlViewer from './StlViewer';
import './App.css';

function App() {
  const fileUrl = '/cube.stl'; // Ensure the path is correct and the file is in the public folder

  return (
    <div className="App">
      <StlViewer fileUrl={fileUrl} />
    </div>
  );
}

export default App;
