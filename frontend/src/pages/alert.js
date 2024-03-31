import React from "react";

const Alert = ({ alerts }) => {
  return (
    <ul>
      {alerts.map((alert) => (
        <li>{alert}</li>
      ))}
    </ul>
  );
};

export default Alert;
