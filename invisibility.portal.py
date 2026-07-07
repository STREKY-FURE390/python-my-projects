import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

# Capture background
ret, background = cap.read()
if not ret:
    print("Cannot access webcam")
    exit()

print("✅ Invisibility Portal Started!")
print("Pinch thumb + index finger to create portal")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Mirror
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        
        h, w = frame.shape[:2]
        tx = int(thumb_tip.x * w)
        ty = int(thumb_tip.y * h)
        ix = int(index_tip.x * w)
        iy = int(index_tip.y * h)
        
        distance = np.hypot(ix - tx, iy - ty)
        
        if distance < 40:  # Pinch detected
            mask = np.zeros(frame.shape[:2], dtype=np.uint8)
            cv2.circle(mask, (ix, iy), 90, 255, -1)  # Portal size
            mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            frame = np.where(mask_3ch == 255, background, frame)
    
    cv2.imshow("AI Magic Invisibility Portal", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
