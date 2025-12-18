import cv2
import mediapipe as mp
import numpy as np

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.canvas = None
        self.prev_point = None
        
    def count_fingers(self, hand_landmarks):
        """Count raised fingers"""
        fingers = []
        tip_ids = [4, 8, 12, 16, 20]
        
        # Thumb
        if hand_landmarks[tip_ids[0]].x < hand_landmarks[tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)
        
        # Other fingers
        for id in range(1, 5):
            if hand_landmarks[tip_ids[id]].y < hand_landmarks[tip_ids[id] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
        
        return sum(fingers)
    
    def run(self):
        cap = cv2.VideoCapture(0)
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame = cv2.flip(frame, 1)
            h, w, c = frame.shape
            
            if self.canvas is None:
                self.canvas = np.zeros_like(frame)
            
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)
            
            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                finger_count = self.count_fingers(hand_landmarks.landmark)
                
                index_tip = hand_landmarks.landmark[8]
                x, y = int(index_tip.x * w), int(index_tip.y * h)
                
                if finger_count == 1:  # Draw
                    if self.prev_point:
                        cv2.line(self.canvas, self.prev_point, (x, y), (0, 255, 0), 5)
                    self.prev_point = (x, y)
                    cv2.putText(frame, "DRAW", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
                elif finger_count == 5:  # Delete
                    self.canvas = np.zeros_like(frame)
                    self.prev_point = None
                    cv2.putText(frame, "DELETE", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                else:
                    self.prev_point = None
            
            output = cv2.addWeighted(frame, 1, self.canvas, 0.7, 0)
            cv2.imshow("Gesture Detection", output)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detector = GestureDetector()
    detector.run()