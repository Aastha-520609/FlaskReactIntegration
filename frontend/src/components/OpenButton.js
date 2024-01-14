import React, { useState } from 'react';
import './OpenButton.css';

const OpenButton = () => {
  const [cameraActive, setCameraActive] = useState(false);

  const handleStartClick = async () => {
    setCameraActive(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/start_attendance', {
        method: 'POST',
      });

      if (response.ok) {
        console.log('Attendance marked successfully!');
      } else {
        console.error('Failed to mark attendance.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleStopClick = async () => {
    setCameraActive(false);

    try {
      const response = await fetch('http://127.0.0.1:5000/stop_attendance', {
        method: 'POST',
      });

      if (response.ok) {
        console.log('Attendance process stopped successfully!');
      } else {
        console.error('Failed to stop attendance process.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="button-container">
      <button onClick={handleStartClick} disabled={cameraActive}>
        Start Attendance
      </button>
      <button onClick={handleStopClick} disabled={!cameraActive}>
        Stop Attendance
      </button>
    </div>
  );
};

export default OpenButton;
