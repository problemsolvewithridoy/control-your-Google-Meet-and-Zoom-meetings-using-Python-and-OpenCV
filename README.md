
# Do your online meetings smartly 

we all are use Google Meet and Zoom for online meetings. One of the biggest problems during these online meetings is muting and unmuting the microphone. To solve this problem I created this project using Python and OprnCV.

This system automatically unmuting your microphone when you speak during the meetings and automatically mute when you don't speak.

let's start...............

To make this project you need to follow this step:-










## Installation

Install package with pip

```bash
pip install cvzone==1.4.1
pip install mediapipe==0.8.3.1
```
    
## Deployment

To deploy this project run

```bash
# Please Subscribe my youtube channel "@problemsolvewithridoy"
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
```
## Open Google Meet

Step 01:- Open Google Meet and click 3 dot icon.

Step 02:- Click on the settings option

![Google Meet 01)](https://user-images.githubusercontent.com/123636419/230371358-91e0bf82-a845-48a0-96be-994baba0a79e.png)


Step 03:- Click on the Audio option

Step 04:- Now enable Push to talk option

![Google Meet 02)](https://user-images.githubusercontent.com/123636419/230372478-c8281e19-1200-4956-a48d-0278461913cb.png)

Step 05:- Now close this Pop-up

![Googl Meet 03)](https://user-images.githubusercontent.com/123636419/230372981-d5ab8dae-75fe-4905-a2de-22081d0c472f.png)
# Congratulations your setup is completed.

## You can follow me

Facebook:- https://www.facebook.com/problemsolvewithridoy/

Linkedin:- https://www.linkedin.com/in/ridoyhossain/

YouTube:- https://www.youtube.com/@problemsolvewithridoy

Gmail:- entridoy2@gmail.com

If you have any confusion, please feel free to contact me. Thank you


## License
This script is released under the MIT License. Feel free to use, modify, and distribute it as you wish. If you find any bugs or have any suggestions for improvement, please submit an issue or a pull request on this repository.

