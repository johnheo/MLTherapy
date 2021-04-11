from PIL import Image, ImageDraw
import os, json,requests, sys, cv2

subscription_key = "008458be2d3a44cdb39a9af14bae9870"
face_api_url = 'https://junghwanheo.cognitiveservices.azure.com/face/v1.0/detect'

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,' +
    'emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'}

#getting the emotions from api
def get_emotions(img_path): 

    image_data = open(img_path, "rb")
    response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
    response.raise_for_status()
    data = response.json()

    try: 
        emotions = data[0]["faceAttributes"]["emotion"]
        #print(json.dumps(emotions, sort_keys=True, indent=2))
        neutral = emotions["neutral"]
        contempt = emotions["contempt"]
        sadness = emotions["sadness"]
        happiness = emotions["happiness"]
        mood = ['negative', 'positive', 'neutral']
        if (contempt > .4 or sadness > .4 or contempt+sadness >.4):
            return mood[0]
        elif (happiness >.5):
            return mood[1]
        else:
            return mood[2]
    except:
        if not data:
            print("no face... ")
        else:
            print(json.dumps(emotions, sort_keys=True, indent=2))
        return 0