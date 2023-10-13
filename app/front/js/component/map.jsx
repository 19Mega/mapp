import React from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

const MapaGoogle = () => {
  const mapContainerStyle = {
    width: '400px',
    height: '400px',
  };

  const center = {
    lat: 37.7749,
    lng: -122.4194,
  };

  return (
    <LoadScript googleMapsApiKey="TU_API_KEY">
      <GoogleMap
        mapContainerStyle={mapContainerStyle}
        center={center}
        zoom={10}
      />
    </LoadScript>
  );
};

export default MapaGoogle;