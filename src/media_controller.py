import pyautogui
import time

class MediaController:
    def __init__(self, cooldown=1.0):
        self.cooldown = cooldown
        self.last_action_time = 0

    def can_trigger(self):
        return time.time() - self.last_action_time > self.cooldown

    def play_pause(self):
        if self.can_trigger():
            pyautogui.press("playpause")
            self.last_action_time = time.time()

    def volume_up(self):
        if self.can_trigger():
            pyautogui.press("volumeup")
            self.last_action_time = time.time()

    def volume_down(self):
        if self.can_trigger():
            pyautogui.press("volumedown")
            self.last_action_time = time.time()

    def next_track(self):
        if self.can_trigger():
            pyautogui.press("nexttrack")
            self.last_action_time = time.time()

    def previous_track(self):
        if self.can_trigger():
            pyautogui.press("prevtrack")
            self.last_action_time = time.time()
