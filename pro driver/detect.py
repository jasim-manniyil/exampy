import cv2
import mediapipe as mp
import winsound  # for Windows system beep, for Linux/macOS, consider alternative methods

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Initialize Video Capture
cap = cv2.VideoCapture(0)

# Define a function to beep and print alert
def alert(message):
    print(message)
    winsound.Beep(1000, 200)  # Beep sound

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the image to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Detect faces
    results = face_detection.process(frame_rgb)
    
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)
            
            # Check if eyes are closed
            if detection.score > 0.5:
                alert("Driver is possibly sleeping!")  # Trigger alert if face detection confidence is high
            
    # Example: Check if seatbelt is detected (you need to implement this part)
    seatbelt_detected = False  # Replace with your seatbelt detection logic
    if not seatbelt_detected:
        alert("Driver is not wearing a seatbelt!")
            
    cv2.imshow('Frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
