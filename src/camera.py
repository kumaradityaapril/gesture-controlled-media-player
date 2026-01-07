import cv2

class Camera:
    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

    def get_frame(self):
        success, frame = self.cap.read()
        if not success:
            return None

        # Flip for mirror effect
        frame = cv2.flip(frame, 1)
        return frame

    def release(self):
        self.cap.release()
