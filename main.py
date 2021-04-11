from face import get_emotions
from cam import get_imagewebcam
import json

print(json.dumps(get_emotions(get_imagewebcam()), sort_keys=True, indent=2))