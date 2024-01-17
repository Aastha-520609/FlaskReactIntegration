# app.py (Flask)
from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
from main import initialize_camera, stop_camera, process_frame, video_capturing
import os
import threading
from multiprocessing import Process

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
camera_active = False

# Get the absolute path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))

# Define routes
@app.route('/')
def home():
    return render_template('index.html')  # Update this later for your React app

@app.route('/start_attendance', methods=['POST'])
def start_attendance():
    global camera_active
    if not camera_active:
        initialize_camera()

        # Start video capturing in a separate thread
        video_thread = threading.Thread(target=video_capturing)
        video_thread.start()

        process_frame(script_path)
        

        # Start face recognition processing
        stop_camera()  # Ensure the camera_active is set to False after the process is complete
        
        return Response('Camera initialized. Click "Stop Attendance" to end the process.', content_type='text/plain')
    else:
        return "Attendance process is already active."

@app.route('/stop_attendance', methods=['POST'])
def stop_attendance():
    stop_camera()
    return "Attendance process stopped."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True) 

