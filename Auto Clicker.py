"""
Auto Clicker by Jminding, with some code taken from a tutorial
"""
import pynput
import threading
import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 0.001 # change this to change the delay in milliseconds
button = Button.left # change this to change which mouse button is clicked
start_stop_key = KeyCode(char='®') # change this to determine which button starts and stops the presses
exit_key = KeyCode(char='≈') # change this to determine which button makes the code stop running

class ClickMouse(threading.Thread):

    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        

with Listener(on_press=on_press) as listener:
    listener.join()
