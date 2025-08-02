import cv2
import mediapipe as mp
import time
from playsound import playsound
import threading

# EAR thresholds
EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 30
COUNTER = 0
ALARM_ON = False

# Mediapipe FaceMesh setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(max_num_faces=1)
mp_drawing = mp.solutions.drawing_utils

# Eye landmark indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def eye_aspect_ratio(landmarks, eye_points):
    top = (landmarks[eye_points[1]].y + landmarks[eye_points[2]].y) / 2
    bottom = (landmarks[eye_points[4]].y + landmarks[eye_points[5]].y) / 2
    left = landmarks[eye_points[0]].x
    right = landmarks[eye_points[3]].x
    return abs(top - bottom) / abs(left - right)

def play_alarm():
    global ALARM_ON
    if not ALARM_ON:
        ALARM_ON = True
        playsound('alarm.mp3')
        ALARM_ON = False

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE)
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE)
        avg_ear = (left_ear + right_ear) / 2

        if avg_ear < EYE_AR_THRESH:
            COUNTER += 1
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 4)
                if not ALARM_ON:
                    threading.Thread(target=play_alarm).start()
        else:
            COUNTER = 0  # Reset counter if eyes are open

        mp_drawing.draw_landmarks(frame, results.multi_face_landmarks[0],
                                  mp_face_mesh.FACEMESH_CONTOURS)

    cv2.imshow("Drowsiness Detector", frame)
    if cv2.waitKey(5) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
# Ensure the alarm is stopped when exiting
if ALARM_ON:
    ALARM_ON = False
    playsound('alarm.mp3')  



    