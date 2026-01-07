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
