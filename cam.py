#pip install opencv-python
import os, json, requests, sys, cv2

#creating an image from webcam returning the path of the image
def get_imagewebcam():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")

    img_name = "opencv.png"
    img_path = str(os.path.split(os.path.abspath(__file__))[0]+"/"+img_name)


    ret, frame = cam.read()

    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    cam.release()
    cv2.destroyAllWindows()
    return(img_path)
"""

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

img_name = "opencv.png"
img_path = str(os.path.split(os.path.abspath(__file__))[0]+"/"+img_name)


ret, frame = cam.read()

cv2.imwrite(img_name, frame)
print("{} written!".format(img_name))
cam.release()
cv2.destroyAllWindows()
print(img_path)"""