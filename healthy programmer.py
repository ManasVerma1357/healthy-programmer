''' 13.10.20 - 18.10.20
author - manas verma
healthy programmer

Instructions:

The task is to create a program that plays mp3 audio until the programmer enters the input which
implies that he has done the task.

For Water, the user should enter “Drank”
For Eye Exercise, the user should enter “EyDone”
For Physical Exercise, the user should enter “ExDone”
After the user entered the input, a file should be created for every task separately,
 which contains the details about the time when the user performed a certain task.

Challenge:

You will have to manage the clashes between the reminders. Such that no two reminders play at the same time.
Use pygame module to play audio '''

from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('E:\downloads\Blue_Hai_Pani_Pani.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('E:\downloads\Ankhiyon Se Goli Mare.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('E:\downloads\Drum Track 90 BPM - Rock Groove Drum Beat - Full Song Style Loop #340 (1).mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")



















