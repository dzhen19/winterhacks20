import React from "react";
import ReactMapboxGl, { Layer, Feature } from "react-mapbox-gl";

const accessToken =
  "pk.eyJ1IjoiZHpoZW4xIiwiYSI6ImNrZ2lxMXF5czAyMXoyeXJ5dG80YmpyM2YifQ.kKGogS31SlV83QQwp4gGOA";
const style = "mapbox://styles/mapbox/streets-v9";

const MapBox = ReactMapboxGl({
  accessToken,
});

const mapStyle = {
  height: "100vh",
  width: "100vw",
};

export default function Map({ edges, origin }) {
  const nodeStyle = {
    "circle-radius": 7,
    "circle-color": "#223b53",
    "circle-stroke-color": "white",
    "circle-stroke-width": 1,
    "circle-opacity": 0.5,
  };

  const edgeStyle = {
    "line-width": 8,
    "line-opacity": 0.4,
    "line-color": "black",
    // "line-gradient": ['interpolate', ['linear'], 'blue', 0.1, 'yellow', 1],
  };

  return (
    <MapBox style={style} containerStyle={mapStyle} zoom={[18]} center={origin}>
      <Layer type="circle" id="nodes" paint={nodeStyle}>
        {edges.map((edge) => {
          return [
            <Feature coordinates={edge.p1} />,
            <Feature coordinates={edge.p2} />,
          ];
        })}
      </Layer>

      <Layer
        type="symbol"
        id="marker"
        layout={{ "icon-image": "marker-15", "icon-size": 3 }}
      >
        <Feature coordinates={origin} />
      </Layer>

      <Layer type="line" id="edges" paint={edgeStyle}>
        {edges.map((edge, index) => {
          return <Feature key={index} coordinates={[edge.p1, edge.p2]} />;
        })}
      </Layer>
    </MapBox>
  );
}
