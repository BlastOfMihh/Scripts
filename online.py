#!/usr/bin/env python3
import pynput
import string
from pynput.mouse import Button
from datetime import datetime as dt
import datetime
import time
import os
import argparse
parser = argparse.ArgumentParser(prefix_chars='-+/', description="argumente")
parser.add_argument("-now")
parser.add_argument("+a", "++add")
parser.add_argument("-s", "--sub")
parser.add_argument("/d", "//dir")
args = parser.parse_args()


print("Mihh's gmeet script has started!")

mouse = pynput.mouse.Controller()
browser = "env BAMF_DESKTOP_FILE_HINT=/var/lib/snapd/desktop/applications/brave_brave.desktop /var/lib/snapd/snap/bin/brave %U"
day = datetime.date.weekday(dt.now())
active_in_meet=False

orar = [
    [21, 22], #Luni
    [9, 10, 11, 14], #Marti
    [8, 9, 13], #Miercuri
    [11, 12, 13], #Azi e JOI!
    [8], #Vineri
    [], #Sambata
    [], #Duminica
]

def goto_n_click(array, sleep_time=5):
    time.sleep(sleep_time)
    mouse.position=array
    mouse.click(Button.left)

def join_meet():
    active_in_meet=True
    elements_pos={
        "sound":[615, 754],
        "camera":[717, 754],
        "participa":[1368, 599]
    }
    os.system("pkill stretchly")
    meet_link="https://meet.google.com/dfj-rjgp-vbe"
    os.system(browser + " " + meet_link + " & ")
    # goto_n_click([1389, 585]) #Lectii online 12A
    goto_n_click(elements_pos["sound"]) #sound off
    goto_n_click(elements_pos["camera"] ,0) #camera off
    goto_n_click(elements_pos["participa"]) #Participa acum
    os.system("stretchly &")

#args
if args.now=="NOW":
    orar[day].append(dt.now().hour+1)
    if active_in_meet==False:
        join_meet()

def exit_meet():
    active_in_meet=False
    os.system("pkill brave")


while 1:
    for h in orar[day]:
        if active_in_meet==False and dt.now().hour==h-1 and dt.now().minute==59:
            join_meet()
            print(active_in_meet)
            print(dt.now().minute)
            print(dt.now().second)
        elif active_in_meet==True and dt.now().hour==h and dt.now().minute==55:
            exit_meet()
            print(active_in_meet)
            print(dt.now().minute)
            print(dt.now().second)
            # print(time.ctime()+"hello")
            # print(dt.now().minute)
    time.sleep(1)
