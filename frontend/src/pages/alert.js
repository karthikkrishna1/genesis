import React from "react";
import './alert.css';

const Alert = ({ alerts }) => {
  if (alerts.length === 0) {
    return null;
  }

  // Only take the last alert for display
  const lastAlert = alerts[alerts.length - 1];

  return (
    <ul className="alerts-container">
      <li>{lastAlert}</li>
    </ul>
  );
};


export default Alert;
