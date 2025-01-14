import cv2 as cv
import face_recognition as fr

class Camera:
    def __init__(self):
        self.cam = cv.VideoCapture(0)  # Open the default camera
        if not self.cam.isOpened():
            raise Exception("Could not find the Camera.")
        
    def get_frame(self, faceencode1):
        """Fetch a frame from the camera and compare faces."""
        ret, frame = self.cam.read()
        if not ret:
            print("Failed to read from the camera.")
            return None
        
        # Detect face locations
        live_faces = fr.face_locations(frame, model='hog')
        if live_faces:
            live_faceencode = fr.face_encodings(frame, known_face_locations=live_faces)[0]
            # Compare the faces
            match = fr.compare_faces([faceencode1], live_faceencode)
            print(f"Are the faces matching? {match[0]}")
        else:
            print("No faces detected.")

        return cv.cvtColor(frame, cv.COLOR_BGR2RGB)  # Convert to RGB format for PyQt5

    def release(self):
        """Release the camera."""
        self.cam.release()
        cv.destroyAllWindows()
