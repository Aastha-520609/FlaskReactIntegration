// App.js (React)s
import React, { useState, useEffect} from 'react';
import OpenButton from './components/OpenButton';
import './components/OpenButton.css';

function App() {
  const [message, setMessage] = useState('');
  const [mediaStream, setMediaStream] = useState(null); 

  const handleStartClick = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      setMediaStream(stream);
    } catch (error) {
      console.error('Error requesting camera access:', error);
    }

    try {
      const response = await fetch('http://127.0.0.1:5000/start_attendance', {
        method: 'POST',
      });

      if (response.ok) {
        setMessage('Camera initialized. Click "Stop Attendance" to end the process.');
      } else {
        setMessage('Failed to initialize camera.');
      }
    } catch (error) {
      console.error('Error:', error);
      setMessage('Error occurred.');
    }
  };

  const handleProcessClick = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/start_processing', {
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
    if (mediaStream) {
      // Get all tracks from the media stream and stop them
      mediaStream.getTracks().forEach((track) => track.stop());
      setMediaStream(null); // Clear the media stream from state
    }

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

  useEffect(() => {
    // Example comment: Camera access is intentionally handled in handleStartClick.
    // Uncomment and customize this block if you need to include additional useEffect logic.
    /*
    const requestCameraAccess = async () => {
      try {
        await navigator.mediaDevices.getUserMedia({ video: true });
      } catch (error) {
        console.error('Error requesting camera access:', error);
      }
    };

    requestCameraAccess();
    */
  }, []);

  return (
    <div className="App">
      <h1>Face Recognition App</h1>
      <OpenButton onStart={handleStartClick} onStop={handleStopClick} onProcess={handleProcessClick} />
      <p>{message}</p>
    </div>
  );
}

export default App; 