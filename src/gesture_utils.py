import time
from collections import deque

# ---------- FINGER STATE LOGIC ----------

def get_finger_states(landmarks):
    fingers = {}

    fingers["index"] = landmarks[8].y < landmarks[6].y
    fingers["middle"] = landmarks[12].y < landmarks[10].y
    fingers["ring"] = landmarks[16].y < landmarks[14].y
    fingers["pinky"] = landmarks[20].y < landmarks[18].y

    # Thumb opens sideways
    fingers["thumb"] = landmarks[4].x > landmarks[3].x

    return fingers

# ---------- STATIC GESTURE CLASSIFICATION ----------

def classify_gesture(fingers, landmarks):
    open_finger_count = sum(fingers.values())

    # ✊ Fist
    if open_finger_count == 0:
        return "FIST"

    # ✋ Open Palm
    if open_finger_count >= 4:
        return "OPEN_PALM"

    # 👍 Thumb Up
    if fingers["thumb"] and open_finger_count == 1:
        if landmarks[4].y < landmarks[2].y:
            return "THUMB_UP"

    # 👎 Thumb Down
    if fingers["thumb"] and open_finger_count == 1:
        if landmarks[4].y > landmarks[2].y:
            return "THUMB_DOWN"

    return "UNKNOWN"

# ---------- SWIPE DETECTION ----------

class SwipeDetector:
    def __init__(self, threshold=150, cooldown=1.0):
        self.threshold = threshold
        self.cooldown = cooldown
        self.positions = deque(maxlen=10)
        self.last_swipe_time = 0

    def detect_swipe(self, landmarks, frame_width):
        current_time = time.time()

        # Cooldown
        if current_time - self.last_swipe_time < self.cooldown:
            return None

        wrist_x = int(landmarks[0].x * frame_width)
        self.positions.append(wrist_x)

        if len(self.positions) < self.positions.maxlen:
            return None

        movement = self.positions[-1] - self.positions[0]

        if movement > self.threshold:
            self.positions.clear()
            self.last_swipe_time = current_time
            return "SWIPE_RIGHT"

        if movement < -self.threshold:
            self.positions.clear()
            self.last_swipe_time = current_time
            return "SWIPE_LEFT"

        return None

# ---------- GESTURE STABILITY ----------

class GestureStabilizer:
    def __init__(self, window_size=5):
        self.gestures = deque(maxlen=window_size)

    def update(self, gesture):
        self.gestures.append(gesture)

        if len(self.gestures) == self.gestures.maxlen:
            if len(set(self.gestures)) == 1:
                return gesture

        return None