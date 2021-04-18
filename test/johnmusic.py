"""Paul Chen/ John Heo
https://github.com/usc-ee250-spring2021/lab05-johnheo-paulchen_lab5.git"""

import paho.mqtt.client as mqtt
import time
import pygame
import random
import os
from pygame import mixer
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("hackiot/emotions")
    client.message_callback_add("hackiot/emotions", callback_emotions)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

def callback_emotions(client, userdata, msg):
    data = str(msg.payload, "utf-8")
    print("emotions: "  + data)
    mixer.music.stop()
    playmusic(data)

def playmusic(genre):
  path="/home/pi/Desktop/Musics/" + genre
  files=os.listdir(path)
  d=random.choice(files)
  print ("now playing " + d)
  # Starting the mixer
  mixer.init()
  # Loading the song
  mixer.music.load(path)
  # Setting the volume
  mixer.music.set_volume(0.5)
  # Start playing the song
  mixer.music.play()
  while pygame.mixer.music.get_busy() == True:
    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input("  ")
    if query == 'p':
      # Pausing the music
      mixer.music.pause()     
    elif query == 'r':
      # Resuming the music
      mixer.music.unpause()
    elif query == 'e':
      # Stop the mixer
      mixer.music.stop()
      break


if __name__ == '__main__':
    emotion = ""
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
      time.sleep(1)
