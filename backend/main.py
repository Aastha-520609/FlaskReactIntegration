# main.py
import csv
from datetime import datetime
import cv2
import face_recognition
import numpy as np
import os

# Initialize the camera_active flag
camera_active = False
video_capture = None  # Global variable to hold the video capture object

def initialize_camera():
    global camera_active, video_capture
    camera_active = True
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def stop_camera():
    global camera_active, video_capture
    camera_active = False
    if video_capture:
        video_capture.release()

def video_capturing():
    global camera_active, video_capture
    while camera_active:
        _, _ = video_capture.read()

def process_frame(script_path):
    global camera_active, video_capture

    aastha_image = face_recognition.load_image_file(os.path.join(script_path, "static", "photos", "aastha.jpeg"))
    aastha_encoding = face_recognition.face_encodings(aastha_image)[0]
    tesla_image = face_recognition.load_image_file(os.path.join(script_path, "static", "photos", "tesla.jpeg"))
    tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

    known_face_encoding = [aastha_encoding, tesla_encoding]
    known_faces_names = ["aastha", "tesla"]
    students = known_faces_names.copy()
    face_locations = []
    face_encodings = []
    face_names = []

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    f = open(os.path.join(script_path, current_date + '.csv'), 'w+', newline='')
    lnwriter = csv.writer(f)

    while camera_active:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            face_names.append(name)

            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(frame, name + ' Present',
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

        cv2.imshow("attendance system", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    f.close()

# Rest of your code remains unchanged

""" # main.py
import csv
from datetime import datetime
import cv2
import face_recognition
import numpy as np
import os
import threading

# Initialize the camera_active flag
camera_active = False
video_capture = None  # Global variable to hold the video capture object

def initialize_camera():
    global camera_active, video_capture
    camera_active = True
    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def stop_camera():
    global camera_active, video_capture
    camera_active = False
    if video_capture:
        video_capture.release()

def video_capturing():
    global camera_active, video_capture
    while camera_active:
        _, _ = video_capture.read()

"" def video_capturing():
    global camera_active, video_capture
    while camera_active:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        cv2.imshow("attendance system", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows() ""

def process_frame(script_path):
    global camera_active, video_capture

    aastha_image = face_recognition.load_image_file(os.path.join(script_path, "static", "photos", "aastha.jpeg"))
    aastha_encoding = face_recognition.face_encodings(aastha_image)[0]
    tesla_image = face_recognition.load_image_file(os.path.join(script_path, "static", "photos", "tesla.jpeg"))
    tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

    known_face_encoding = [aastha_encoding, tesla_encoding]
    known_faces_names = ["aastha", "tesla"]
    students = known_faces_names.copy()
    face_locations = []
    face_encodings = []
    face_names = []

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    f = open(os.path.join(script_path, current_date + '.csv'), 'w+', newline='')
    lnwriter = csv.writer(f)

    while camera_active:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            face_names.append(name)

            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(frame, name + ' Present',
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])
        cv2.imshow("attendance system", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

f.close()


    #f.close()

#video_thread = threading.Thread(target=video_capturing)

 """

""" import csv
from datetime import datetime
import cv2
import face_recognition
import numpy as np
import os

# Initialize the camera_active flag
camera_active = False

def run_face_recognition(script_path):
    global camera_active

    video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    aastha_image = face_recognition.load_image_file(os.path.join(script_path, "static", "photos", "aastha.jpeg"))
    aastha_encoding = face_recognition.face_encodings(aastha_image)[0]
    tesla_image = face_recognition.load_image_file(os.path.join(script_path, "static", "photos", "tesla.jpeg"))
    tesla_encoding = face_recognition.face_encodings(tesla_image)[0]

    known_face_encoding = [aastha_encoding, tesla_encoding]
    known_faces_names = ["aastha", "tesla"]
    students = known_faces_names.copy()
    face_locations = []
    face_encodings = []
    face_names = []

    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")

    f = open(os.path.join(script_path, current_date + '.csv'), 'w+', newline='')
    lnwriter = csv.writer(f)

    while camera_active:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
            face_names.append(name)

            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(frame, name + ' Present',
                            bottomLeftCornerOfText,
                            font,
                            fontScale,
                            fontColor,
                            thickness,
                            lineType)

                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

        cv2.imshow("attendance system", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    f.close()

    return "Attendance marking completed." """