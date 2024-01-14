import React from 'react';

const OpenButton = ({ onStart, onStop }) => {
  return (
    <div>
      <button onClick={onStart}>Start Attendance</button>
      <button onClick={onStop}>Stop Attendance</button>
    </div>
  );
};

export default OpenButton;
