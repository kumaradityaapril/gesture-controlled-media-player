import cv2
import time
from camera import Camera
from hand_tracker import HandTracker
from gesture_utils import (
    get_finger_states,
    classify_gesture,
    SwipeDetector,
    GestureStabilizer
)
from media_controller import MediaController

def main():
    cam = Camera()
    tracker = HandTracker()
    swipe_detector = SwipeDetector()
    media = MediaController()
    gesture_stabilizer = GestureStabilizer(window_size=5)

    current_gesture = ""
    prev_time = 0

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

            raw_gesture = swipe if swipe else static_gesture
            stable_gesture = gesture_stabilizer.update(raw_gesture)

            if stable_gesture:
                current_gesture = stable_gesture

        # FPS calculation
        curr_time = time.time()
        fps = int(1 / (curr_time - prev_time)) if prev_time != 0 else 0
        prev_time = curr_time

        cv2.putText(
            frame,
            f"Gesture: {current_gesture}",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"FPS: {fps}",
            (30, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 0),
            2
        )

        cv2.imshow("Gesture Media Player - Day 4", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
