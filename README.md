# 🎵 Gesture-Controlled Media Player

A real-time hand gesture recognition system that allows users to control media playback
(play/pause, volume, next/previous track) using intuitive hand gestures captured through a webcam.

Built using **Python, OpenCV, and MediaPipe Tasks API**.

---

## 🚀 Features

- ✋ **Open Palm** → Play / Pause  
- 👍 **Thumb Up** → Volume Up  
- 👎 **Thumb Down** → Volume Down  
- 👉 **Swipe Right** → Next Track  
- 👈 **Swipe Left** → Previous Track  
- Gesture stability using multi-frame confirmation  
- FPS counter for real-time performance monitoring  

---

## 🧠 How It Works

1. Webcam captures live video frames using OpenCV  
2. MediaPipe Tasks API detects **21 hand landmarks**  
3. Finger states are extracted from landmark positions  
4. Static and dynamic gestures are classified  
5. Gestures are stabilized using an N-frame sliding window  
6. Media actions are triggered using OS-level automation  

---

## 🏗️ Project Architecture

gesture-controlled-media-player/
│
├── models/
│ └── hand_landmarker.task
│
├── src/
│ ├── camera.py # Webcam handling
│ ├── hand_tracker.py # Hand landmark detection
│ ├── gesture_utils.py # Gesture logic & stability
│ ├── media_controller.py # Media key automation
│ └── main.py # Application entry point
│
├── requirements.txt
├── README.md
└── venv/

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd gesture-controlled-media-player
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy code
python src/main.py
🧪 Supported Gestures
Gesture	Action
Open Palm	Play / Pause
Thumb Up	Volume Up
Thumb Down	Volume Down
Swipe Right	Next Track
Swipe Left	Previous Track

📈 Performance
Real-time hand tracking

FPS counter displayed on screen

Optimized gesture stability to reduce false positives

📌 Future Enhancements
Gesture-controlled virtual mouse

Smart home device integration

Custom gesture training using ML models

