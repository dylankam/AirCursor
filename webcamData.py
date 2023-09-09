import cv2
import os
import time

filePath = "C:/Users/Dylan/OneDrive/Desktop/positives"
cameraBrightness = 190
#Save every 10th Frame
frameNumber = 10 
minBlur = 500
grayImage = False
saveDataFlag = True
showImageFlag = True
imgWidth = 180
imgHeight= 120

cap = cv2.VideoCapture(0)
cap.set(10, cameraBrightness)
count = 0
countSave = 0

def saveData():
    global countFolder
    countFolder = 0
    while os.path.exists(filePath + str(countFolder)):
        countFolder += 1
    os.makedirs(filePath + str(countFolder))

if saveDataFlag: 
    saveData()

while True: 
    ret, img = cap.read()
    img = cv2.resize(img, (imgWidth, imgHeight))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if saveDataFlag:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % frameNumber == 0 and blur > minBlur:
            currentTime = time.time()
            cv2.imwrite(filePath + str(countFolder) + '/'
                        + str(countSave) + "_" + str(int(blur)) + "_" + str(currentTime) + ".png", img)
            countSave += 1
        count += 1
    if showImageFlag:
        cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

