import cv2
def Take_snapShot ():
    videoCaptureOBJ = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame = videoCaptureOBJ.read()
        cv2.imwrite ("picture.jpg",frame)
        result = False
    videoCaptureOBJ.release()
    cv2.destroyAllWindows()
Take_snapShot()