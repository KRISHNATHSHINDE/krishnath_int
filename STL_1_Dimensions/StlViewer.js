// src/StlViewer.js
import React, { useRef } from 'react';
import { Canvas, useFrame, useLoader } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import { STLLoader } from 'three-stdlib';

const Model = ({ url }) => {
  const geometry = useLoader(STLLoader, url);
  const ref = useRef();
  useFrame(() => (ref.current.rotation.y += 0.0));

  return (
    <mesh ref={ref} geometry={geometry}>
      <meshStandardMaterial color="grey" />
    </mesh>
  );
};

const StlViewer = ({ fileUrl }) => {
  return (
    <Canvas style={{ height: '100vh', width: '100vw' }}>
      <ambientLight intensity={0.5} />
      <spotLight position={[10, 10, 10]} angle={0.15} penumbra={1} />
      <pointLight position={[-10, -10, -10]} />
      <Model url={fileUrl} />
      <OrbitControls />
    </Canvas>
  );
};

export default StlViewer;
