import React from "react";
import Map from "../components/map";
import Sidebar from "../components/sidebar";

export default function Dashboard() {
  return (
    <div style={{ display: "flex" }}>
      <Map />
      <Sidebar />
    </div>
  );
}
