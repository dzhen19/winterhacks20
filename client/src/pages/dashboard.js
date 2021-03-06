import React, { useState, useEffect } from "react";
import Map from "../components/map";
import Sidebar from "../components/sidebar";
import Search from "../components/search";
import { geolocated } from "react-geolocated";
import CircularProgress from "@material-ui/core/CircularProgress";

function Dashboard({ coords }) {
  // const testCache = localStorage.getItem("-83.2379912999999942.5696067")
  //   ? JSON.parse(localStorage.getItem("-83.2379912999999942.5696067"))
  //   : [];

  const [edges, setEdges] = useState([]);
  // origin = [longitude, latitude]
  const [origin, setOrigin] = useState([
    parseFloat(localStorage.getItem("longitude")) || -75.35461,
    parseFloat(localStorage.getItem("latitude")) || 39.90419,
  ]);

  const [loading, setLoading] = useState(false);
  const [selected, setSelected] = useState(false);

  useEffect(() => {
    // only run effect if no cached coords are detected
    if (coords & !localStorage.getItem("longitude")) {
      console.log(coords);
      setOrigin([coords.longitude, coords.latitude]);
      localStorage.setItem("longitude", coords.longitude);
      localStorage.setItem("latitude", coords.latitude);
    }
  }, [coords]);

  //point = (long, lat)
  const getRoutes = (point) => {
    setLoading(true);
    const cache = localStorage.getItem(
      point[0].toString() + point[1].toString()
    );
    if (cache) {
      setEdges(JSON.parse(cache));
      setLoading(false);
    } else {
      fetch(`/api/edges?lat=${point[1]}&lng=${point[0]}`)
        .then((res) => {
          console.log(res);
          return res.json();
        })
        .then((data) => {
          const routes = data["routes"].map((route) => {
            return {
              p1: [route.longitude1, route.latitude1],
              p2: [route.longitude2, route.latitude2],
              elevation: route.delta_elevation.toPrecision(3),
              distance: route.distance.toPrecision(4),
              address1: route.address1,
              address2: route.address2,
            };
          });
          // console.log(routes)
          setEdges(routes);
          localStorage.setItem(
            point[0].toString() + point[1].toString(),
            JSON.stringify(routes)
          );
          setLoading(false);
        });
    }
  };

  useEffect(() => {
    if (loading) {
      console.log(loading);
    }
  }, [loading]);

  useEffect(() => {
    if (selected) {
      console.log(edges[selected]["p1"]);
      setOrigin(edges[selected]["p1"])
    }
  }, [selected]);

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
        <Sidebar edges={edges} selected={selected} setSelected={setSelected} />
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
