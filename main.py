import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
cap.set(3, 720)
cap.set(4, 420)

detector = HandDetector(detectionCon=0.7, maxHands=2)
keyboard = Controller()

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        keyboard.press(Key.space)
    else:
        keyboard.release(Key.space)

    cv2.imshow("Meeting controller", img)
    if cv2.waitKey(1) == ord("q"):
        break