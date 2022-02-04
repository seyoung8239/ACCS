import React, { useState, useEffect } from 'react';
import axios from 'axios';

import { shelter } from '../../routeAPI';

import { StaticMap } from 'react-map-gl';
import { AmbientLight, PointLight, LightingEffect } from '@deck.gl/core';
import { HexagonLayer } from '@deck.gl/aggregation-layers';
import DeckGL from '@deck.gl/react';
import mapboxgl from 'mapbox-gl';
import 'mapbox-gl/dist/mapbox-gl.css';


// eslint-disable-next-line
mapboxgl.workerClass = require('worker-loader!mapbox-gl/dist/mapbox-gl-csp-worker').default;
const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1Ijoic2V5b3VuZzgyMzkiLCJhIjoiY2tyNHNjdmRvMnl1bDJxcWF3eWhxNG5jbSJ9.sicqPlkDhRVSsvO29xXo3Q';

const ambientLight = new AmbientLight({
  color: [255, 255, 255],
  intensity: 1.0
});

const pointLight1 = new PointLight({
  color: [255, 255, 255],
  intensity: 0.8,
  position: [-0.144528, 49.739968, 80000]
});

const pointLight2 = new PointLight({
  color: [255, 255, 255],
  intensity: 0.8,
  position: [-3.807751, 54.104682, 8000]
});

const INITIAL_VIEW_STATE = {
  longitude: 129.5,
  latitude: 36.5,
  zoom: 6.3,
  minZoom: 5,
  maxZoom: 15,
  pitch: 30,
  bearing: 0
};

const lightingEffect = new LightingEffect({ ambientLight, pointLight1, pointLight2 });

const colorRange = [
  [1, 152, 189],
  [73, 227, 206],
  [216, 254, 181],
  [254, 237, 177],
  [254, 173, 84],
  [209, 55, 78]
];

const material = {
  ambient: 0.64,
  diffuse: 0.6,
  shininess: 32,
  specularColor: [51, 51, 51]
};

function getTooltip({ object }) {
  if (!object) {
    return null;
  }
  const lat = object.position[1];
  const lng = object.position[0];
  const count = object.points.length;

  return `\
    latitude: ${Number.isFinite(lat) ? lat.toFixed(6) : ''}
    longitude: ${Number.isFinite(lng) ? lng.toFixed(6) : ''}
    ${count} Places`;
}

const DeckMap = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async()=> {
      try {
        const res = await axios.get(shelter);
        const tempData = res.data.map(d => [Number(d.lo), Number(d.la)])
        setData(tempData);
      } catch(e) {
        console.log(e);
      }
    }
    fetchData();
  }, []);
  console.log(data)

  const layers = [
    new HexagonLayer({
      id: 'heatmap',
      colorRange,
      coverage: 1.2,
      data,
      elevationRange: [0, 3000],
      elevationScale: data && data.length ? 50 : 0,
      extruded: true,
      getPosition: d => d,
      pickable: true,
      radius: 1000,
      upperPercentile: 99.7,
      material,
      transitions: {
        elevationScale: 3000
      }
    })
  ];

  return (
    <DeckGL
      layers={layers}
      effects={[lightingEffect]}
      initialViewState={INITIAL_VIEW_STATE}
      controller={true}
      getTooltip={getTooltip}
      style={{ 'position': 'static' }}
    >
      <StaticMap mapboxApiAccessToken={MAPBOX_ACCESS_TOKEN} />
    </DeckGL>
  );
}

export default DeckMap;