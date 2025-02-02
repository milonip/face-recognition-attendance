import face_recognition
import os

# Load the training images
training_images = []
training_encodings = []

for filename in os.listdir("training_images"):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        image = face_recognition.load_image_file(os.path.join("training_images", filename))
        face_encodings = face_recognition.face_encodings(image)
        
        # Check if there are face encodings in the list
        if face_encodings:
            # Use the first face encoding (index 0) if available
            training_encodings.append(face_encodings[0])
            training_images.append(image)

# Rest of your training code
