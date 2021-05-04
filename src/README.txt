Paul Chen/John Heo
Demo:https://www.youtube.com/watch?v=hsNnjNmdU6c
Git:https://github.com/johnheo1128/MLTherapy.git
LCD is connected to the I2C 2 port on the grovepi shield, while the speaker needs to be manually connected and set as default output.  
Both files inside "rpi" folder are supposed to run on a raspberrypi.
File "index.html" inside "jsfolder" folder is supposed to run on a browser on a laptop with webcam. 
"playmusic.py" and "subscriber.py" will only start working once the user confirmed the emotion predicted from "index.html".
External Libs: pygame/ face api/ grovepi
