import face_recognition
import cv2

known_image = face_recognition.load_image_file("1.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

face_locations = []
face_encodings = []
face_names = []

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([known_face_encoding], face_encoding)

        name = "Unknown"

        if True in matches:
            name = "Known Person"  

        face_names.append(name)

    
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
