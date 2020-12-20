import React, { useState } from "react";
import PlacesAutocomplete, {
  geocodeByAddress,
  getLatLng,
} from "react-places-autocomplete";

export default function Search({ setOrigin, getRoutes }) {
  const [address, setAddress] = useState("");

  const handleChange = (newAddress) => {
    setAddress(newAddress);
  };

  const handleSelect = (address) => {
    geocodeByAddress(address)
      .then((results) => getLatLng(results[0]))
      .then((latLng) => {
        console.log("Success", latLng);
        getRoutes([latLng.lng, latLng.lat]);
        setOrigin([latLng.lng, latLng.lat]);
      })
      .catch((error) => console.error("Error", error));
  };

  return (
    <div style={{ position: "fixed", margin:'10px'}}>
      <PlacesAutocomplete
        value={address}
        onChange={handleChange}
        onSelect={handleSelect}
      >
        {({ getInputProps, suggestions, getSuggestionItemProps, loading }) => (
          <div>
            <input
              type="text"
              class="form-control"
              aria-label="Default"
              style={{ fontSize: "24px", width:'30vw'}}
              aria-describedby="inputGroup-sizing-default"
              {...getInputProps({
                placeholder: "Enter Address",
                className: "location-search-input",
              })}
            />
            <div className="autocomplete-dropdown-container">
              {loading && <div>Loading...</div>}
              {suggestions.map((suggestion) => {
                const className = suggestion.active
                  ? "suggestion-item--active"
                  : "suggestion-item";
                // inline style for demonstration purpose
                const style = suggestion.active
                  ? { backgroundColor: "#fafafa", cursor: "pointer" }
                  : { backgroundColor: "#ffffff", cursor: "pointer" };
                return (
                  <div
                    {...getSuggestionItemProps(suggestion, {
                      className,
                      style,
                    })}
                  >
                    <span>{suggestion.description}</span>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </PlacesAutocomplete>
      {/* <input
        type="text"
        placeholder="Enter an address"
        style={{ width: "300px" }}
      ></input> */}
    </div>
  );
}
