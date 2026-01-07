import cv2
from camera import Camera
from hand_tracker import HandTracker

def main():
    cam = Camera()
    tracker = HandTracker()

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        frame = tracker.detect_and_draw(frame)

        cv2.imshow("Gesture Controlled Media Player - Day 1", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
