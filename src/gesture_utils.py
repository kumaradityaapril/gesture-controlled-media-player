import time
from collections import deque

def get_finger_states(landmarks):
    """
    Returns a dictionary showing which fingers are open.
    """
    fingers = {}

    # Index, Middle, Ring, Pinky
    fingers["index"] = landmarks[8].y < landmarks[6].y
    fingers["middle"] = landmarks[12].y < landmarks[10].y
    fingers["ring"] = landmarks[16].y < landmarks[14].y
    fingers["pinky"] = landmarks[20].y < landmarks[18].y

    # Thumb (x-axis logic because thumb opens sideways)
    fingers["thumb"] = landmarks[4].x > landmarks[3].x

    return fingers
def classify_gesture(fingers, landmarks):
    """
    Classifies static hand gestures based on finger states.
    """

    # Count open fingers
    open_finger_count = sum(fingers.values())

    # ✊ Fist (no fingers open)
    if open_finger_count == 0:
        return "FIST"

    # ✋ Open Palm (4 or more fingers open)
    if open_finger_count >= 4:
        return "OPEN_PALM"

    # 👍 Thumb Up (only thumb open + direction)
    if fingers["thumb"] and open_finger_count == 1:
        if landmarks[4].y < landmarks[2].y:
            return "THUMB_UP"

    # 👎 Thumb Down
    if fingers["thumb"] and open_finger_count == 1:
        if landmarks[4].y > landmarks[2].y:
            return "THUMB_DOWN"

    return "UNKNOWN"

class SwipeDetector:
    def __init__(self, threshold=150, cooldown=1.0):
        self.threshold = threshold          # pixels
        self.cooldown = cooldown
        self.positions = deque(maxlen=10)   # last 10 frames
        self.last_swipe_time = 0

    def detect_swipe(self, landmarks, frame_width):
        current_time = time.time()

        # Cooldown check
        if current_time - self.last_swipe_time < self.cooldown:
            return None

        # Wrist landmark (0)
        wrist_x = int(landmarks[0].x * frame_width)
        self.positions.append(wrist_x)

        # Need enough history
        if len(self.positions) < self.positions.maxlen:
            return None

        movement = self.positions[-1] - self.positions[0]

        # Swipe Right
        if movement > self.threshold:
            self.positions.clear()
            self.last_swipe_time = current_time
            return "SWIPE_RIGHT"

        # Swipe Left
        if movement < -self.threshold:
            self.positions.clear()
            self.last_swipe_time = current_time
            return "SWIPE_LEFT"

        return None