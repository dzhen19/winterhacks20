import React, { useState, useEffect } from "react";
import Map from "../components/map";
import Sidebar from "../components/sidebar";
import { geolocated } from "react-geolocated";

const edges = [
  { p1: [-83.23794, 42.56964], p2: [-83.236046, 42.571995] },
  { p1: [-83.23406, 42.570696], p2: [-83.233975, 42.570642] },
  { p1: [-83.23389, 42.570631], p2: [-83.234849, 42.571496] },
];

function Dashboard({ coords }) {
  const [origin, setOrigin] = useState([
    parseFloat(localStorage.getItem("longitude")) || -83.237938,
    parseFloat(localStorage.getItem("latitude")) || 42.569641,
  ]);
  useEffect(() => {
    if (coords) {
        console.log(coords)
      setOrigin([coords.longitude, coords.latitude]);
      localStorage.setItem("longitude", coords.longitude);
      localStorage.setItem("latitude", coords.latitude);
    }
  }, [coords]);

  return (
    <div style={{ display: "flex" }}>
      <Map edges={edges} origin={origin} />
      <Sidebar edges={edges} />
    </div>
  );
}

export default geolocated({
  positionOptions: {
    enableHighAccuracy: false,
  },
  userDecisionTimeout: 5000,
})(Dashboard);