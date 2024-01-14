from flask import Flask, render_template, Response
from main import run_face_recognition
import os

app = Flask(__name__)
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
        camera_active = True
        result = run_face_recognition(script_path)  # Pass the script_path to the function
        camera_active = False  # Ensure the camera_active is set to False after the process is complete
        return Response(result, content_type='text/plain')
    else:
        return "Attendance process is already active."

@app.route('/stop_attendance', methods=['POST'])
def stop_attendance():
    global camera_active
    camera_active = False
    return "Attendance process stopped."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
