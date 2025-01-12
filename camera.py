import cv2 as cv
import numpy as np

def showVideo():
        cam = cv.VideoCapture(0)

        if not cam.isOpened():
                print("Could not find the Camera")
                exit()
        
        while True:
                _, frame = cam.read()
        
                cv.imshow("frame", frame)
                if cv.waitKey(1) == ord('q'):
                        break
        cam.release()
        cv.destroyAllWindows()
        
if __name__ == '__main__':
        showVideo()