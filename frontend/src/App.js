import React, { useState } from 'react';
import OpenButton from './components/OpenButton';
import './components/OpenButton.css';

function App() {
  const [message, setMessage] = useState('');

  const handleStartClick = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/start_attendance', {
        method: 'POST',
      });

      if (response.ok) {
        setMessage('Attendance process started.');
      } else {
        setMessage('Failed to start attendance process.');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('Error occurred.');
    }
  };

  const handleStopClick = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/stop_attendance', {
        method: 'POST',
      });

      if (response.ok) {
        setMessage('Attendance process stopped.');
      } else {
        setMessage('Failed to stop attendance process.');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('Error occurred.');
    }
  };

  return (
    <div className="App">
      <h1>Face Recognition App</h1>
      <OpenButton onStart={handleStartClick} onStop={handleStopClick} />
      <p>{message}</p>
    </div>
  );
}

export default App;
