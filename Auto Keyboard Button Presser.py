from pynput.keyboard import Key, Controller, Listener, KeyCode
import time
import pynput
import threading

delay = 0.001 # change this to change the delay between keypresses in seconds
key = "3" # change this to change which key is pressed
start_stop_key = KeyCode(char='®') # change this to change what combination of keypresses activates this
exit_key = KeyCode(char='≈') # change this to change what combination of keypresses terminates the running of the code

class PressKey(threading.Thread):

    def __init__(self, delay, key):
        super().__init__()
        self.delay = delay
        self.key = key
        self.running = False
        self.program_running = True

    def start_pressing(self):
        self.running = True

    def stop_pressing(self):
        self.running = False

    def exit(self):
        self.stop_pressing()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(self.key)
                keyboard.release(self.key)
                time.sleep(self.delay)

    



keyboard = Controller()
press_thread = PressKey(delay, key)
press_thread.start()


def on_press(key):
    if key == start_stop_key:
        if press_thread.running:
            press_thread.stop_pressing()
        else:
            press_thread.start_pressing()
    elif key == exit_key:
        press_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()

