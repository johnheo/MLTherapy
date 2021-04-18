import os, json,requests, sys, cv2
from face import get_emotions
from cam import get_imagewebcam
from publisher import send_mqtt

response = get_emotions(get_imagewebcam())
print(response)
send_mqtt(response)
