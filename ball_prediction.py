import cv2
from ball_detector import BallDetector
from kalmanfilter import KalmanFilter

cap = cv2.VideoCapture(r"C:\Users\nkhoa\project\CS370Project\MOT\Multi-Object-Tracking-with-Kalman-Filter\ball.mp4");
# Load detector
od = BallDetector()

# Load Kalman filter to predict the trajectory
kf = KalmanFilter()

while True:
    ret, frame = cap.read()
    roi = frame[200:300, 0:960] 
    if ret is False:
        break

    ball_bbox = od.detect(roi)
    x, y, x2, y2 = ball_bbox
    cx = int((x + x2) / 2)
    cy = int((y + y2) / 2)


    predicted = kf.predict(cx, cy)
    #cv2.rectangle(roi, (x, y), (x2, y2), (255, 0, 0), 4)

    #Red Circle for ball object detection
    cv2.circle(roi, (cx, cy), 20, (0, 0, 255), 4)
    #Blue Circle for ball predicted using kalman filter
    cv2.circle(roi, (predicted[0], predicted[1]), 20, (255, 0, 0), 4)
    
    #cv2.imshow("Roi", roi)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(150)
    if key == 27:
        break