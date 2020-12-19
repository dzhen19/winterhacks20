import React from "react";

export default function sidebar({ edges }) {
  return (
    <div style={{ width: "20%" }}>
      {edges.map((edge, index) => {
        return (
          <div>
            Route {index}
            <br />
            {edge.p1[0]} {edge.p1[1]}
            <br />
            {edge.p2[0]} {edge.p2[1]}
            <br />
            <br />
          </div>
        );
      })}
    </div>
  );
}
