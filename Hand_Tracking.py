import cv2
import mediapipe as mp
import time
import math
import vgamepad as vg

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
with mpHands.Hands(static_image_mode=False,
                      max_num_hands=4,
                      min_detection_confidence=0.6,
                      min_tracking_confidence=0.6) as hands :
    mpDraw = mp.solutions.drawing_utils

    pTime = 0
    cTime = 0
    gamepad = vg.VX360Gamepad()
    
    while cap.isOpened():
        success, img = cap.read()
        img.flags.writeable = False
        img = cv2.flip(img,1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)
        if results.multi_hand_landmarks:
            PalmR , PalmL = [] , [] 
            for idx,handLms in enumerate(results.multi_hand_landmarks):
                if len(results.multi_hand_landmarks) == 2 :

                    lmlistL =[]
                    lmlistR =[]
                    lbl = results.multi_handedness[idx].classification[0].label
                    # Left Hand
                    if lbl == "Left" :
                        myLHand = results.multi_hand_landmarks[idx]
                        for id, lm in enumerate(myLHand.landmark):
                            h, w, c = img.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            lmlistL.append([id, cx, cy])
                        if len(lmlistL) !=0:
                            PalmL = (lmlistL[5][1],lmlistL[5][2])
                            cv2.putText(img, "Left", (lmlistL[0][1],lmlistL[0][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA)
                            cv2.putText(img, "Left", (lmlistL[0][1],lmlistL[0][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                        # # Distance between land mark 4 and 6    
                        dis46Left = ((lmlistL[4][1] -  lmlistL[6][1])**2 + (lmlistL[4][2] -  lmlistL[6][2])**2)**0.5
                        if dis46Left:
                            dis46Left=30 if dis46Left <30 else dis46Left
                            dis46Left=85 if dis46Left >85 else dis46Left
                            # Source https://pypi.org/project/vgamepad/
                            # normalize  between 0 and 255 
                            range = 85-30
                            LeftTtr = ((dis46Left-30)/(range))*255
                            gamepad.left_trigger(value=int(LeftTtr))
                            gamepad.update()

                    # Right Hand
                    if lbl == "Right":
                        myRHand = results.multi_hand_landmarks[idx]
                        for id, lm in enumerate(myRHand.landmark):
                            h, w, c = img.shape
                            cx, cy= int(lm.x * w), int(lm.y * h) 
                            lmlistR.append([id, cx, cy])
                        
                        if len(lmlistR) !=0:
                            PalmR = (lmlistR[5][1],lmlistR[5][2])
                            cv2.putText(img, "Right", (lmlistR[0][1],lmlistR[0][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3, cv2.LINE_AA)
                            cv2.putText(img, "Right", (lmlistR[0][1],lmlistR[0][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                        # Distance between land mark 4 and 6
                        dis46Right = ((lmlistR[4][1] -  lmlistR[6][1])**2 + (lmlistR[4][2] -  lmlistR[6][2])**2)**0.5
                        if dis46Right:
                            dis46Right=30 if dis46Right <30 else dis46Right
                            dis46Right=85 if dis46Right > 85 else dis46Right
                            # Source https://pypi.org/project/vgamepad/
                            # normalize  between 0 and 255 
                            range = 85-30
                            RightTri = ((dis46Right-30)/(range))*255
                            gamepad.right_trigger(value=int(RightTri))
                            gamepad.update()
                                                    
                    if len(PalmR) != 0 and len(PalmL) != 0 :
                    
                        # Find center of line
                        Line_center = (int((PalmR[0]+PalmL[0])/2),int((PalmR[1]+PalmL[1])/2))
                        cv2.circle(img,Line_center,20,(0,255,0),-1)
                        # find Angle 
                        if (PalmR[0]-Line_center[0]) != 0: # Check divide by 0

                            x= (PalmR[1]-Line_center[1])/(PalmR[0]-Line_center[0])
                            ang = math.atan(x)
                            ang = (math.degrees(ang))
                            # Limit angle between -threshold and threshold
                            threshold = 50
                            ang = -threshold if ang < -threshold else ang
                            ang = threshold if ang > threshold else ang
                            # normalize  between -32768 and 32767 
                            range = threshold*2
                            a = (ang+threshold)/(threshold*2)
                            range2 = 32767 *2
                            a = (a*range2) -32767
                        cv2.line(img, PalmR, PalmL, (255,0,0), 10)
                        gamepad.left_joystick(x_value= int(a) , y_value=0) # values between -32768 and 32767
                        gamepad.update()
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                
        # Show FPS 
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        # Show image
        cv2.imshow("Image", img)
        if cv2.waitKey(5) & 0xFF == ord("q"):
            break
cap.release()
