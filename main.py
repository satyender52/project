import csv
import keyboard
import cv2
import face_recognition
import numpy as np
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# Your code here

if __name__ == "__main__":
    # Your code here

    # Load known faces
    image1_jpg = face_recognition.load_image_file("C:\\Users\\rozer\\Downloads\\IMG_20230618_105923.jpg")
    image1_encoding = face_recognition.face_encodings(image1_jpg)[0]

    image2_jpg = face_recognition.load_image_file("C:\\Users\\rozer\\Downloads\\IMG_20231006_003750.jpg")
    image2_encoding = face_recognition.face_encodings(image2_jpg)[0]

    known_face_encodings = [image1_encoding, image2_encoding]
    known_face_names = ["image1", "image2"]

    students = known_face_names.copy()

    face_locations = []
    face_encodings = []

    # get the current date and time

    now = datetime.now()
    current_date = now.strftime("%y-%m-%d")

    f = open(f"{current_date}.csv", "w+", newline="")
    lnwriter = csv.writer(f)

    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Recognize faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            mathes = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)

            if (mathes[best_match_index]):
                name = known_face_names[best_match_index]
            # add the text if a persion is present
                if name in known_face_names:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    bottomLeftCornerOfText = (10,100)
                    fontScale = 1.5
                    fontColor = (255,0,0)
                    thickness = 3
                    lineType = 2
                    cv2.putText(frame,name + "present", bottomLeftCornerOfText, font,fontScale,fontColor,thickness,lineType)

                    if name in students:
                        students.remove(name)
                        current_time = now.strftime("&H-%M%S")
                        lnwriter.writerow([name, current_time])

                cv2.imshow("Attendance", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):

                    break


    video_capture.release()
    cv2.destroyALLWindow()
    f.close()











