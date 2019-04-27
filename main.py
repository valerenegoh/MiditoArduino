import tkinter as tk
from tkinter import Label
import serial
from time import sleep
from functools import partial

playlist = {
        1: "Stand By Me",
        2: "Do Re Mi",
        3: "How Deep is your Love"
        }

dict = {
        "48": '0',  # C
        "50": '1',  # D
        "52": '2',  # E
        "53": '3',  # F
        "55": '4',  # G
        "57": '5',  # A
        "59": '6',  # B
        "60": '7',  # C
        "62": '8',  # D
        "64": '9',  # E
        "65": 'a',  # F
        "67": 'b',  # G
        "69": 'c',  # A
        "71": 'd',  # B
        "72": 'e'   # C
        }


# Enter your COM port in the below line
serial = serial.Serial('com5', 9600)
sleep(2)
#print (serial.readline(serial.inWaiting()))

root = tk.Tk()
 
def runSong(num):
    label1.config(text = "Playing " + song)
    sleep(1)
    with open("txt/%d_GI15.txt" %num, "r") as f:
        for line in f:
            notes = line.rstrip("\n").rstrip().split()
#            print(notes)
            if notes:    # beat contains notes
                for i in range(len(notes)):
                    serial.write(dict[notes[i]].encode())
            sleep(0.3)         # tempo of song

#buttons = list()
label1 = Label(root, text = "Choose a song", fg="green")
label1.pack()
for num, song in playlist.items():
    button = tk.Button(root, text = song, command = partial(runSong, num))
    button.pack()

root.mainloop()