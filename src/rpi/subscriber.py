"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""
import requests
import sys
import time
import paho.mqtt.client as mqtt
sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')
import grovepi
import grove_rgb_lcd as lcd

LCD_LINE_LEN = 16

# LCD INIT
lcd.setText('')
lcd.setRGB(255,255,255)

color = [0,0,0, 0,0,255, 0,255,0, 255,0,0, 255,255,255]
#nothing, blue, green,red, white

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("hackiot/emotions")

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    emotion = str(msg.payload, "utf-8")
    
    
    if emotion == "positive":
        lcd.setRGB(255,165,0) #orange
        lcd.setText_norefresh('positive')
    elif emotion == "negative":
        lcd.setRGB(255,255,0) #yellow
        lcd.setText_norefresh('negative')
    else: #neutral
        lcd.setRGB(0,0,255) #green
        lcd.setText_norefresh('neutral')

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
            

