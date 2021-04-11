#python3 -m pip install Pillow
import json, os, requests

subscription_key = "008458be2d3a44cdb39a9af14bae9870"
face_api_url = "https://junghwanheo.cognitiveservices.azure.com/" + '/face/v1.0/detect'

image_url = 'https://www.biography.com/.image/t_share/MTQ1MzAyNzYzOTgxNTE0NTEz/john-f-kennedy---mini-biography.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'detectionModel': 'detection_01',
    'returnFaceId': 'true',
    'returnFaceAttributes': 'age,gender,emotion'
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
data = response.json()
print(json.dumps(data, sort_keys=True, indent=2))
emotions = data[0]["faceAttributes"]["emotion"]
print(json.dumps(emotions, sort_keys=True, indent=2))