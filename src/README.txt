Members: Paul Chen/John Heo
Demo: https://www.youtube.com/watch?v=xHlj1xn_f4o
Git: https://github.com/johnheo1128/MLTherapy.git

Instructions:
On the RPi end, first connect the LCD to the I2C port 2. Next, pair the bluetooth speaker by selecting 'audio output' from the RPi Desktop. Run "playmusic.py" and "subscriber.py" in two separate terminals.
On the webapp frontend, drag and drop "index.html" file into a Chrome browser to run the JS code locally. To host it in a localhost server, download the npm module by 'npm install --global http-server' and run 'http-server' in your terminal under the 'jsfolder' directory.

External libraries:
- paho.mqtt.client
- pygame
- playsound
- random
- grovepi & grove_rgb_lcd
- cv2 
