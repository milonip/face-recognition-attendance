import cv2
import face_recognition
from openpyxl import Workbook
from datetime import datetime
import os

workbook = Workbook()
worksheet = workbook.active
worksheet.append(["Name", "Date", "Time"]) 

headers = ["Present name"]

known_face_encodings = []
known_face_names = []


for filename in os.listdir("training_images"):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        image = face_recognition.load_image_file(os.path.join("training_images", filename))
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(os.path.splitext(filename)[0])
        

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            
            current_date = datetime.now().strftime("%Y-%m-%d")
            current_time = datetime.now().strftime("%H:%M:%S")

            worksheet.append([name, current_date, current_time])

        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        worksheet.append([name])
        workbook.save("attendance.xlsx")

    cv2.imshow("Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
