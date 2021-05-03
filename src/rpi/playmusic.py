import paho.mqtt.client as mqtt
import time
import pygame
import random
import os
from pynput import keyboard
#from soundplayer import SoundPlayer
import playsound 

data = ""
i = 0
psong = ""
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("hackiot/emotions")
    client.message_callback_add("hackiot/emotions", callback_emotions)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def callback_emotions(client, userdata, msg):
    global data
    data = str(msg.payload, "utf-8")
    print("emotions: "  + data)
    global i
    i = 1
    print(str(i) +"from callback")

def playmusic(genre):
    path="/home/pi/Desktop/Music/" + genre
    files=os.listdir(path)
    d=random.choice(files)
    global psong
    while (d==psong):
        d=random.choice(files)
    print ("now playing " + d)
    pygame.mixer.init()
    pygame.mixer.music.load(path+"/"+d)
    psong = d
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    global i
    i = 2
    while pygame.mixer.music.get_busy() == True:
        #print(str(i) +"from callback")
        if (i != 2):
            pygame.mixer.music.stop()
            break
    if (i == 2 or i == 3):
        playmusic(genre)
    
def on_press(key):
    try: 
        k = key.char # single-char keys
    except: 
        k = key.name # other keys
    global i
    if (i ==2):
        if k == 'p':
        # Pausing the music
            pygame.mixer.music.pause()     
        elif k == 'r':
          # Resuming the music
            pygame.mixer.music.unpause()
        elif k == 'e':
          # Stop the mixer
            pygame.mixer.music.stop()
            i = 0
        elif k == 'c':
          # Stop the mixer
            i = 3
    print()
if __name__ == '__main__':
    lis = keyboard.Listener(on_press=on_press)
    lis.start()
    print("Press 'p' to pause, 'r' to resume, c to change")
    print("Press 'e' to stop music")
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        if (i == 1):
            #print ("play music")
            playmusic(data)
            #emotion = data

        time.sleep(1)
