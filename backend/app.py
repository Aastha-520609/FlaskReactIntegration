from flask import Flask, render_template, Response
from main import run_face_recognition

app = Flask(__name__)
camera_active = False

# Define routes
@app.route('/')
def home():
    return render_template('index.html')  # Update this later for your React app

@app.route('/start_attendance', methods=['POST'])
def start_attendance():
    global camera_active
    if not camera_active:
        camera_active = True
        result = run_face_recognition()
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
