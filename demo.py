import cv2

# Create a VideoCapture object to access the camera (usually 0 for the built-in camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    cv2.imshow('Camera Feed', frame)  # Display the frame
    
    # Add your face recognition logic here

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Release the camera when done
cv2.destroyAllWindows()
