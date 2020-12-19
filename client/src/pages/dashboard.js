import React, { useState, useEffect } from "react";
import Map from "../components/map";
import Sidebar from "../components/sidebar";
import Search from "../components/search";
import { geolocated } from "react-geolocated";
import CircularProgress from "@material-ui/core/CircularProgress";

function Dashboard({ coords }) {
  const [edges, setEdges] = useState([
    { p1: [-83.23794, 42.56964], p2: [-83.236046, 42.571995] },
    { p1: [-83.23406, 42.570696], p2: [-83.233975, 42.570642] },
    { p1: [-83.23389, 42.570631], p2: [-83.234849, 42.571496] },
  ]);

  const [origin, setOrigin] = useState([
    parseFloat(localStorage.getItem("longitude")) || -83.237938,
    parseFloat(localStorage.getItem("latitude")) || 42.569641,
  ]);

  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // only run effect if no cached coords are detected
    if (coords & !localStorage.getItem("longitude")) {
      console.log(coords);
      setOrigin([coords.longitude, coords.latitude]);
      localStorage.setItem("longitude", coords.longitude);
      localStorage.setItem("latitude", coords.latitude);
    }
  }, [coords]);

  // write the query for ways
  const getRoutes = () => {
    setLoading(true);
    fetch(`/api/edges?lat=${origin[1]}&lng=${origin[0]}`)
      .then((res) => {
        console.log(res);
        return res.json();
      })
      .then((data) => {
        const routes = data["routes"].map((route) => {
          return {
            p1: [route.longitude1, route.latitude1],
            p2: [route.longitude2, route.latitude2],
          };
        });
        // console.log(routes)
        setEdges(routes)
        setLoading(false);
      });
  };

  useEffect(() => {
    if (loading) {
      console.log(loading);
    }
  }, [loading]);

  return (
    <div>
      <div
        style={{
          display: "flex",
          zIndex: "-1",
          filter: loading ? "brightness(50%)" : "brightness(100%)",
        }}
      >
        <Map edges={edges} origin={origin} />
        <Search origin={origin} setOrigin={setOrigin} getRoutes={getRoutes} />
        <Sidebar edges={edges} />
        <CircularProgress
          style={{
            color: "orange",
            opacity: loading ? "100%" : "0%",
            height: "2rem",
            left: "45%",
            top: "45%",
            position: "absolute",
          }}
        />
      </div>
    </div>
  );
}

export default geolocated({
  positionOptions: {
    enableHighAccuracy: false,
  },
  userDecisionTimeout: 5000,
})(Dashboard);
