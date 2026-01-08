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

    # ✊ Fist (all fingers closed)
    if not any(fingers.values()):
        return "FIST"

    # ✋ Open Palm (all fingers open)
    if all(fingers.values()):
        return "OPEN_PALM"

    # 👍 Thumb Up
    if fingers["thumb"] and not fingers["index"] and not fingers["middle"] \
       and not fingers["ring"] and not fingers["pinky"]:
        if landmarks[4].y < landmarks[2].y:
            return "THUMB_UP"

    # 👎 Thumb Down
    if fingers["thumb"] and not fingers["index"] and not fingers["middle"] \
       and not fingers["ring"] and not fingers["pinky"]:
        if landmarks[4].y > landmarks[2].y:
            return "THUMB_DOWN"

    return "UNKNOWN"