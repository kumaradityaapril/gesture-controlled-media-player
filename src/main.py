import cv2
from camera import Camera
from hand_tracker import HandTracker
from gesture_utils import get_finger_states

def main():
    cam = Camera()
    tracker = HandTracker()

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        result = tracker.detect(frame)

        if result.hand_landmarks:
            hand_landmarks = result.hand_landmarks[0]
            tracker.draw_landmarks(frame, hand_landmarks)

            fingers = get_finger_states(hand_landmarks)
            print(fingers)

        cv2.imshow("Gesture Media Player - Day 2", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
