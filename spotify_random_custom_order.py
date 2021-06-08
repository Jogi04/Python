#!/bin/python

import random
import time
import pyautogui


class SpotifyRandomPlaylistOrder:
    def __init__(self, iterations):
        self.iterations = iterations
        time.sleep(3)           # sleep for 3 seconds to give user time to switch to spotify window
        self.drag_song()

    def drag_song(self):
        for i in range(self.iterations):
            pyautogui.moveTo(1000, random.randrange(300, 900, 35), 1)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(1000, random.randrange(300, 900, 35), 1)
            pyautogui.mouseUp(button='left')
            pyautogui.scroll(random.randint(-20, 20))
            if i % 10 == 0:
                pyautogui.scroll(random.choice([50, -50]))
            elif i % 20 == 0:
                pyautogui.scroll(random.choice([100, -100]))


if __name__ == '__main__':
    custom_order = SpotifyRandomPlaylistOrder(5)
