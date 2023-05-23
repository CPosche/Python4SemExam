import cv2

video1 = cv2.VideoCapture(1)
video2 = cv2.VideoCapture(0)

while True:
    ret0, frame0 = video1.read()
    ret1, frame1 = video2.read()

    if(ret0):
        cv2.imshow("video1", frame0)
    
    if(ret1):
        cv2.imshow("video2", frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video1.release()
video2.release()
cv2.destroyAllWindows()