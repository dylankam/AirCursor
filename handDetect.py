import cv2
import pyautogui

fistCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'fist.xml')
leftHandCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lpalm.xml')
rightHandCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'rpalm.xml')
pointDownCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'pointDown.xml')

#Create VideoCapture Object with default webcam
def detectHands():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        #Convert to grayscale for simpler processing
        greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #MultiScale to detect objects of different size 
        fist = fistCascade.detectMultiScale(greyFrame, scaleFactor=1.4, minNeighbors=2, minSize=(100,100))
        leftHand = leftHandCascade.detectMultiScale(greyFrame, scaleFactor = 1.4, minNeighbors=1, minSize=(30,30))
        rightHand = rightHandCascade.detectMultiScale(greyFrame, scaleFactor = 1.4, minNeighbors=1, minSize=(30,30))
        pointDown = pointDownCascade.detectMultiScale(greyFrame, scaleFactor = 1.5, minNeighbors=5, minSize=(100,100))
        #Returns rectangle with x,y coordinate, width, height
        for (x,y,w,h) in fist:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
            pyautogui.click(clicks=2, interval=1)
        for (x,y,w,h) in leftHand: 
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
            moveMouse(x,y,w,h,frame)
        for (x,y,w,h) in rightHand: 
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) 
            moveMouse(x,y,w,h,frame)
        for (x,y,w,h) in pointDown:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 255), 2)
        #frame = cv2.resize(frame, (200, 100))
        cv2.imshow("Hand Frame", frame)
        cv2.putText(frame, "Press 'q' to quit", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 10, (0, 0, 255), 2, cv2.LINE_AA)
        #Set q to be the quit button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows

def moveMouse(x,y,w,h,frame):
    #Calculate Centre coordinates of rectangleq
    centreX, centreY = x + w // 2, y + h // 2
    #Get dimensions of screen
    screenWidth, screenHeight = pyautogui.size()
    #Scale x to match screen size, shape attribute holds array of height, width, numChannels
    scaledX = (centreX / frame.shape[1] * screenWidth)
    #Invert x coordinate to account for flipped webcam
    realX = screenWidth - scaledX
    #Scale y to match screen size
    realY = int(centreY / frame.shape[0]*screenHeight)
    pyautogui.moveTo(realX, realY)

detectHands()


