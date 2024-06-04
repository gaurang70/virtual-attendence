import cv2
import face_recognition
import os
from datetime import datetime

# Function to get encoding of known faces in the given directory
def get_known_encodings(directory):
    known_encodings = []
    known_names = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            path = os.path.join(directory, filename)
            image = face_recognition.load_image_file(path)
            encoding = face_recognition.face_encodings(image)[0]
            known_encodings.append(encoding)
            known_names.append(os.path.splitext(filename)[0])
    return known_encodings, known_names

# Function to mark attendance
def mark_attendance(name):
    with open("attendance.csv", "a") as file:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{name},{dt_string}\n")

# Main function
def main():
    # Directory containing images of known people
    known_faces_dir = "known_faces"

    # Capture video from the default camera (you can change the argument to use a different camera)
    cap = cv2.VideoCapture(0)

    known_encodings,known_names = get_known_encodings(known_faces_dir)

    while True:
        ret, frame = cap.read()

        # Find face locations in the current frame
        face_locations =face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Check for each face in the frame
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)

            name = "Unknown"

            # If a known face is found, use the name of the first match
            if True in matches:
                first_match_index = matches.index(True)
                name = known_names[first_match_index]

            # Draw a rectangle around the face and display the name
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            
            # Add timestamp to the frame
            now = datetime.now()
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(frame, dt_string, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Mark attendance if a known face is found
            if name != "Unknown":
                mark_attendance(name)

        # Display the resulting frame
        cv2.imshow("Face Attendance System", frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 
