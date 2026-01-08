# 🎵 Gesture-Controlled Media Player

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Tasks%20API-orange.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

A **real-time gesture-controlled media player** that allows users to control system media  
(play/pause, volume, next/previous track) using **hand gestures captured via webcam**.

This project demonstrates **computer vision, real-time processing, gesture recognition, and OS-level automation** using Python.

---

## 🚀 Key Features

- ✋ **Open Palm** → Play / Pause  
- 👍 **Thumb Up** → Volume Up  
- 👎 **Thumb Down** → Volume Down  
- 👉 **Swipe Right** → Next Track  
- 👈 **Swipe Left** → Previous Track  
- 🧠 Gesture stability using multi-frame confirmation  
- ⚡ Real-time performance with FPS counter  
- 🖥️ OS-level media control (works with Spotify, YouTube, VLC, etc.)

---

## 🧠 System Workflow

Webcam Feed
->
OpenCV Frame Processing
->
MediaPipe Tasks API (21 Hand Landmarks)
->
Finger State Detection
->
Static & Dynamic Gesture Classification
->
Gesture Stabilization (N-frame window)
->
Media Control via PyAutoGUI

---

## Project Architecture
gesture-controlled-media-player/
├── models/
│ └── hand_landmarker.task # MediaPipe hand landmark model
│
├── src/
│ ├── camera.py # Webcam handling (OpenCV)
│ ├── hand_tracker.py # Hand landmark detection (MediaPipe)
│ ├── gesture_utils.py # Gesture logic, swipe detection, stability
│ ├── media_controller.py # OS-level media automation
│ └── main.py # Application entry point
│
├── requirements.txt # Project dependencies
├── README.md # Project documentation
└── venv/ # Virtual environment (ignored in Git)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone <your-repo-url>
cd gesture-controlled-media-player

2️⃣ Create & Activate Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run Application

python src/main.py
🧪 Supported Gestures
Gesture	Action
Open Palm	Play / Pause
Thumb Up	Volume Up
Thumb Down	Volume Down
Swipe Right	Next Track
Swipe Left	Previous Track

---

📈 Performance & Stability
Real-time hand tracking using MediaPipe Tasks API

FPS counter for performance monitoring

Gesture stabilization using sliding window (N-frame confirmation)

Cooldown & debounce logic to prevent accidental triggers

---

🧠 Technical Highlights (Resume Keywords)
Computer Vision

Real-Time Video Processing

Hand Landmark Detection

Gesture Recognition

MediaPipe Tasks API

OpenCV

OS Automation

Performance Optimization

Modular Python Design

---

📌 Future Enhancements
Gesture-controlled virtual mouse

Smart home device integration

Custom gesture training using ML models

Cross-platform support (Linux/macOS)

# 👨‍💻 Author
## Kumar Aditya
📌 Aspiring Software / Full Stack / Computer Vision Developer

