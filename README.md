 Drowsiness Detector

A **Real-Time Driver Drowsiness Detection System** built with Python, OpenCV, and MediaPipe. This application continuously monitors a driver's eye movements using a webcam feed. It calculates the Eye Aspect Ratio (EAR) to detect signs of drowsiness. When fatigue is detected, a preloaded alarm sound plays to alert the driver.

This project is part of a broader initiative to improve **vehicle safety** through proactive driver monitoring. Future plans include integrating this system into embedded vehicle units and enhancing it with additional sensors.

 🚀 Features

* 👁️ Real-time EAR calculation using **MediaPipe** facial landmarks
* 🧠 Detection of prolonged eye closure to identify drowsiness
* 🔊 Audio alert via threaded alarm using `playsound`
* 📝 Logs EAR values to a CSV file *(optional)*
* 📸 Captures webcam snapshots during drowsy detection *(optional)*
* 🖥️ Tkinter-based GUI support *(optional)*
* 📦 Packaged as a standalone `.exe` for Windows using **PyInstaller**


 🛠 Technologies Used

* Python 3.10+
* OpenCV
* MediaPipe
* playsound
* threading
* tkinter *(for GUI version)*
* PyInstaller *(for application packaging)*

 💻 Installation

```bash
# Clone the repository
$ git clone https://github.com/aathirithikas/drowsiness-detector.git
$ cd drowsiness-detector

# Install required packages
$ pip install -r requirements.txt

🧠 How It Works

1. Captures video feed from the webcam
2. MediaPipe detects facial landmarks and isolates the eyes
3. EAR (Eye Aspect Ratio) is computed for both eyes
4. If EAR drops below threshold for a fixed duration, an alarm is triggered


📦 Packaging as .exe

To build the app into an executable:

```bash
pip install pyinstaller
pyinstaller --onefile drowsiness_detector.py
```

Your `.exe` will be created in the `dist/` directory.

---

 📁 Project Structure

```
├── drowsiness_detector.py       # Main detection script
├── alarm.mp3                    # Alarm audio file
├── requirements.txt             # List of dependencies
├── README.md                    # Project documentation
└── snapshots/                   # Folder for drowsiness snapshots (optional)

 🧱 Future Enhancements

🧑‍💻 Author

**Aathirithika S** – [GitHub](https://github.com/aathi2005)



✅ **Drive safe. Stay alert. Prevent accidents.**
