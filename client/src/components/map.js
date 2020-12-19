import React, { Component } from 'react';
import ReactMap from 'react-mapbox-gl';
const accessToken= "pk.eyJ1IjoiZHpoZW4xIiwiYSI6ImNrZ2lxMXF5czAyMXoyeXJ5dG80YmpyM2YifQ.kKGogS31SlV83QQwp4gGOA"
const style = "mapbox://styles/mapbox/streets-v9";

const Map = ReactMap({
  accessToken
});

const mapStyle = {
  height: '100vh',
  width: '70%'
};

class App extends Component {
  render() {
    return (
      <Map
        style={style}
        containerStyle={mapStyle}
      />
    );
  }
}

export default App;
