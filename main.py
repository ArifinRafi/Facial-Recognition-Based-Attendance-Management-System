from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
import sys
from camera import Camera
import face_recognition as fr

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI
        uic.loadUi("main.ui", self)

        # Initialize the camera
        try:
            self.camera = Camera()
        except Exception as e:
            print(f"Camera initialization failed: {e}")
            sys.exit()
        
        # Load and encode the reference face
        try:
            self.arifin1 = fr.load_image_file("images/aa.jpg")
            faceloct1 = fr.face_locations(self.arifin1, model='hog')
            if not faceloct1:
                raise ValueError("No face detected in the reference image.")
            self.faceencode1 = fr.face_encodings(self.arifin1, known_face_locations=faceloct1)[0]
        except Exception as e:
            print(f"Error in face encoding: {e}")
            sys.exit()

        # Set up the timer for video updates
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 ms

        # Button actions
        self.SignInBtn.clicked.connect(self.SignInTask)
        self.SignOutBtn.clicked.connect(self.SignOutTask)

        self.show()

    def update_frame(self):
        """Fetch the current frame and display it."""
        try:
            frame = self.camera.get_frame(self.faceencode1)
            if frame is not None:
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.videoLabel.setPixmap(QPixmap.fromImage(q_image))
        except Exception as e:
            print(f"Error in updating frame: {e}")

    def SignInTask(self):
        name = "Md Arifin Ahmed Rafi"
        id = "1024343A"
        intime = "10:34"
        self.nameLabel.setText(f"Name: {name}")
        self.IdLabel.setText(f"ID: {id}")
        self.SignInTime.setText(f"Sign In Time: {intime}")

    def SignOutTask(self):
        print("SignOut print")

    def closeEvent(self, event):
        """Release the camera on close."""
        self.camera.release()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
