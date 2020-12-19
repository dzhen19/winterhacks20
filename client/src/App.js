import React from "react";
import Dashboard from "./pages/dashboard";
import logo from './slots.png'
import { AppBar } from "@material-ui/core";

export default function App() {
  return (
    <div>
      <nav class="navbar sticky-top navbar-light bg-light">
        <a class="navbar-brand" href="#">
          <img
            src={logo}
            width="40"
            height="30"
            class="d-inline-block align-top"
            alt=""
            style={{marginRight:"10px"}}
          />
          GPSled
        </a>
      </nav>
      <Dashboard />
    </div>
  );
}
