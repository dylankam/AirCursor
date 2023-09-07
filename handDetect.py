import cv2

fistCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'fist.xml')
leftHandCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'lpalm.xml')
rightHandCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'rpalm.xml')
#Create VideoCapture Object with default webcam
def detectHands():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        #Convert to grayscale for simpler processing
        greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fist = fistCascade.detectMultiScale(greyFrame, scaleFactor=1.6, minNeighbors=1)
        leftHand = leftHandCascade.detectMultiScale(greyFrame, scaleFactor = 1.6, minNeighbors=1)
        rightHand = rightHandCascade.detectMultiScale(greyFrame, scaleFactor = 1.6, minNeighbors=1)
        for (x,y,w,h) in fist:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
        for (x,y,w,h) in leftHand: 
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
        for (x,y,w,h) in rightHand: 
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) 

        cv2.imshow("Hand Frame", frame)
        #Set q to be the quit button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows

detectHands()


