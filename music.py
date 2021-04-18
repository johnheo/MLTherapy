"""
import time
from soundplayer import SoundPlayer

# Use device with ID 1  (mostly USB audio adapter)
p = SoundPlayer("/home/pi/Downloads/RR-thebox.mp3", 0)        
print ("play for 10 s with volume 0.5")
p.play(0.5) # non-blocking, volume = 0.5
print ("isPlaying:", p.isPlaying())
time.sleep(10)
print ("pause for 5 s")
p.pause()
print ("isPlaying:", p.isPlaying())
time.sleep(5)
print ("resume for 10 s")
p.resume()
time.sleep(10)
print ("stop")
p.stop()
print ("isPlaying:", p.isPlaying())
print ("done")
"""

from __future__ import absolute_import, print_function, unicode_literals

import dbus

bus = dbus.SystemBus()

manager = dbus.Interface(bus.get_object("org.bluez", "/"),
                    "org.freedesktop.DBus.ObjectManager")

def extract_objects(object_list):
    list = ""
    for object in object_list:
        val = str(object)
        list = list + val[val.rfind("/") + 1:] + " "
    return list

def extract_uuids(uuid_list):
    list = ""
    for uuid in uuid_list:
        if (uuid.endswith("-0000-1000-8000-00805f9b34fb")):
            if (uuid.startswith("0000")):
                val = "0x" + uuid[4:8]
            else:
                val = "0x" + uuid[0:8]
        else:
            val = str(uuid)
        list = list + val + " "
    return list

objects = manager.GetManagedObjects()

all_devices = (str(path) for path, interfaces in objects.items() if
                    "org.bluez.Device1" in interfaces.keys())

for path, interfaces in objects.items():
    if "org.bluez.Adapter1" not in interfaces.keys():
        continue

    print("[ " + path + " ]")

    properties = interfaces["org.bluez.Adapter1"]
    for key in properties.keys():
        value = properties[key]
        if (key == "UUIDs"):
            list = extract_uuids(value)
            print("    %s = %s" % (key, list))
        else:
            print("    %s = %s" % (key, value))

    device_list = [d for d in all_devices if d.startswith(path + "/")]

    for dev_path in device_list:
        print("    [ " + dev_path + " ]")

        dev = objects[dev_path]
        properties = dev["org.bluez.Device1"]

        for key in properties.keys():
            value = properties[key]
            if (key == "UUIDs"):
                list = extract_uuids(value)
                print("        %s = %s" % (key, list))
            elif (key == "Class"):
                print("        %s = 0x%06x" % (key, value))
            elif (key == "Vendor"):
                print("        %s = 0x%04x" % (key, value))
            elif (key == "Product"):
                print("        %s = 0x%04x" % (key, value))
            elif (key == "Version"):
                print("        %s = 0x%04x" % (key, value))
            else:
                print("        %s = %s" % (key, value))

    print("")
    
import dbus
bus = dbus.SystemBus()

player = bus.get_object('org.bluez','/org/bluez/hci0/dev_00_42_79_F7_3A_FA/player0')
BT_Media_iface = dbus.Interface(player, dbus_interface='org.bluez.MediaPlayer1')
BT_Media_props = dbus.Interface(player, "org.freedesktop.DBus.Properties")

props = BT_Media_props.GetAll("org.bluez.MediaPlayer1")
print props



