from ultralytics import YOLO
import cv2
import cvzone
import math
import PokerHandFunction

model = YOLO("./playingcards.pt")

classNames = ['10C', '10D', '10H', '10S',
              '2C', '2D', '2H', '2S',
              '3C', '3D', '3H', '3S',
              '4C', '4D', '4H', '4S',
              '5C', '5D', '5H', '5S',
              '6C', '6D', '6H', '6S',
              '7C', '7D', '7H', '7S',
              '8C', '8D', '8H', '8S',
              '9C', '9D', '9H', '9S',
              'AC', 'AD', 'AH', 'AS',
              'JC', 'JD', 'JH', 'JS',
              'KC', 'KD', 'KH', 'KS',
              'QC', 'QD', 'QH', 'QS']

cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    success1, img1 = cap1.read()
    success2, img2 = cap2.read()
    
    
    hand1 = []
    hand2 = []
    result1 = ()
    result2 = ()
    hand1result = ""
    hand2result = ""


    if(success1):
        results1 = model(img1, stream=True)
        for r in results1:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2-x1, y2-y1
                cvzone.cornerRect(img1, (x1, y1, w, h))
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])

                cvzone.putTextRect(img1, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

                if conf > 0.5:
                    hand1.append(classNames[cls])


        print(hand1)
        hand1 = list(set(hand1))
        print(hand1)
        if(len(hand1) == 5):
            result1 = PokerHandFunction.findpokerhand(hand1)
            cvzone.putTextRect(img1, f'{result1[1]}', (300, 75), scale=3, thickness=5)

    if(success2):
        results2 = model(img2, stream=True)
        for r in results2:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2-x1, y2-y1
                cvzone.cornerRect(img2, (x1, y1, w, h))
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = int(box.cls[0])

                cvzone.putTextRect(img2, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

                if conf > 0.5:
                    hand2.append(classNames[cls])


        print(hand2)
        hand2 = list(set(hand2))
        print(hand2)
        if(len(hand2) == 5):
            result2 = PokerHandFunction.findpokerhand(hand2)
            cvzone.putTextRect(img2, f'{result2[1]}', (300, 75), scale=3, thickness=5)

        if(len(hand1) == 5 and len(hand2) == 5):
            if(result1[0] > result2[0]):
                hand1result = "WINNER"
                hand2result = "LOSER"
            elif(result1[0] < result2[0]):
                hand1result = "LOSER"
                hand2result = "WINNER"
            else:
                hand1result = "DRAW"
                hand2result = "DRAW"
            cvzone.putTextRect(img1, f'{hand1result}', (300, 125), scale=3, thickness=5)
            cvzone.putTextRect(img2, f'{hand2result}', (300, 125), scale=3, thickness=5)
        cv2.imshow("image1", img1)
        cv2.imshow("image2", img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()



