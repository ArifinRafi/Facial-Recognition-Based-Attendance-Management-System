import cv2 as cv
import face_recognition as fr
import numpy as np

# Load the images
arifin1 = fr.load_image_file("images/elon1.jpeg")
arifin1 = cv.cvtColor(arifin1, cv.COLOR_BGR2RGB)

arifin2 = fr.load_image_file("images/elon2.jpg")
arifin2 = cv.cvtColor(arifin2, cv.COLOR_BGR2RGB)

# Detect face locations
faceloct1 = fr.face_locations(arifin1, model="hog")  # Detect face in the first image
faceloct2 = fr.face_locations(arifin2, model="hog")  # Detect face in the second image

if not faceloct1 or not faceloct2:
    print("No faces detected in one or both images.")
else:
    # Encode the faces
    facencode1 = fr.face_encodings(arifin1, known_face_locations=faceloct1)[0]
    facencode2 = fr.face_encodings(arifin2, known_face_locations=faceloct2)[0]

    # Compare the faces
    compare = fr.compare_faces([facencode1], facencode2)
    distance = fr.face_distance([facencode1], facencode2)

    print(f"Are the faces matching? {compare[0]}")
    print(f"Face distance: {distance[0]}")

    # Draw rectangles around the detected faces
    for (top, right, bottom, left) in faceloct1:
        cv.rectangle(arifin1, (left, top), (right, bottom), (0, 255, 0), 2)

    for (top, right, bottom, left) in faceloct2:
        cv.rectangle(arifin2, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the images
    cv.imshow("Elon 1", arifin1)
    cv.imshow("Elon 2", arifin2)
    cv.waitKey(0)
    cv.destroyAllWindows()
