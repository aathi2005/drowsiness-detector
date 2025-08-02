Drowsiness Detector Project
================================

INSTRUCTIONS:
1. Install requirements:
   pip install opencv-python dlib imutils playsound scipy

2. Download the following file manually:
   - shape_predictor_68_face_landmarks.dat from: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

3. Place all files in the same folder.

4. Run:
   python drowsiness_detector.py

Note:
- Ensure 'alarm.mp3' is a real sound file.
- This project uses a webcam to detect drowsiness based on eye aspect ratio (EAR).
