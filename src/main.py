import cv2
from camera import Camera
from hand_tracker import HandTracker
from gesture_utils import (
    get_finger_states,
    classify_gesture,
    SwipeDetector
)
from media_controller import MediaController

def main():
    cam = Camera()
    tracker = HandTracker()
    swipe_detector = SwipeDetector()
    media = MediaController()

    current_gesture = ""

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        result = tracker.detect(frame)

        if result.hand_landmarks:
            hand_landmarks = result.hand_landmarks[0]
            tracker.draw_landmarks(frame, hand_landmarks)

            # Static gesture
            fingers = get_finger_states(hand_landmarks)
            static_gesture = classify_gesture(fingers, hand_landmarks)

            # Swipe gesture
            frame_width = frame.shape[1]
            swipe = swipe_detector.detect_swipe(hand_landmarks, frame_width)

            if swipe == "SWIPE_RIGHT":
                media.next_track()
            elif swipe == "SWIPE_LEFT":
                media.previous_track()
            elif static_gesture == "OPEN_PALM":
                media.play_pause()
            elif static_gesture == "THUMB_UP":
                media.volume_up()
            elif static_gesture == "THUMB_DOWN":
                media.volume_down()

            if swipe:
                current_gesture = swipe
            else:
                current_gesture = static_gesture

            cv2.putText(
                frame,
                f"Gesture: {current_gesture}",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        cv2.imshow("Gesture Media Player - Day 4", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
