import cv2 as cv
from ultralytics import YOLO
model = YOLO("yolov8n.pt")

#sample=cv.imread("images.jpg")
#detection=model(sample)
#cv.imshow("Objects", detection[0].plot())
# To change source from webcam to webcam use int from 0 
#To change source to video file use name in ""
def yolodetection(frame):
    result=model(frame)
    return result[0]

    