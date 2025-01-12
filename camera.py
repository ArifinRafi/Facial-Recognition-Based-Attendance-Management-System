import cv2 as cv

class Camera:
    def __init__(self):
        self.cam = cv.VideoCapture(0)
        if not self.cam.isOpened():
            raise Exception("Could not find the Camera.")

    def get_frame(self):
        ret, frame = self.cam.read()
        if not ret:
            return None
        return cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert frame to RGB for PyQt5

    def release(self):
        self.cam.release()
