#!/usr/bin/python3

import tkinter as tk
from time import time
#import RPi.GPIO as GPIO
import lib8inputs as inputs

# GPIO-Pins für die Taster
#START_PIN = 17
#STOP_PIN = 18
#RESET_PIN = 27
START_CH = 7
STOP_CH = 8
RESET_CH = 6
STACK = 0


# Globale Variablen
start_time = 0
elapsed_time = 0
running = False

# GPIO-Initialisierung
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(START_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(STOP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(RESET_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Callback-Funktionen für die Taster
def start_timer():
    global start_time, running
    if not running:
        start_time = time()
        running = True

def stop_timer():
    global elapsed_time, running
    if running:
        elapsed_time += time() - start_time
        running = False

def reset_timer():
    global elapsed_time, running
    elapsed_time = 0
    running = False

# Timer-Funktion
def update_timer():
    if running:
        current_time = time() - start_time + elapsed_time
    else:
        current_time = elapsed_time

    # Formatierung in Sekunden und Millisekunden
    seconds = int(current_time)
    milliseconds = int((current_time - seconds) * 100)

    # Aktualisierung des Timer-Textes
    timer_label.config(text="{:02d}:{:02d}".format(seconds, milliseconds))

    # Timer alle 10 Millisekunden aktualisieren
    timer_label.after(10, update_timer)

# GUI erstellen
window = tk.Tk()
window.title("Timer")
window.attributes('-fullscreen', True)
window.configure(bg="black")

timer_label = tk.Label(window, text="00:00", font=("Arial", 400), fg="white", bg="black")
timer_label.pack(expand=True, fill="both")

# GPIO-Event-Handler hinzufügen
#GPIO.add_event_detect(START_PIN, GPIO.FALLING, callback=start_timer, bouncetime=200)
#GPIO.add_event_detect(STOP_PIN, GPIO.FALLING, callback=stop_timer, bouncetime=200)
#GPIO.add_event_detect(RESET_PIN, GPIO.FALLING, callback=reset_timer, bouncetime=200)

#Channel-Event-Handler
def event_handler():
    if inputs.get_opto(STACK, START_CH) == 1:
        start_timer()

    if inputs.get_opto(STACK, STOP_CH) == 1:
        stop_timer()

    if inputs.get_opto(STACK, RESET_CH) == 1:
        reset_timer()

    # der event handler wird bei dem window objekt hinterlegt und alle 10ms aufgerufen
    window.after(10, event_handler)


# Timer starten
update_timer()

# Event Handler aktivieren
event_handler()

# Hauptprogrammschleife
window.mainloop()

# GPIO-Pins freigeben
#GPIO.cleanup()
