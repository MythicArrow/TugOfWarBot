import pyautogui
import numpy as np
import cv2
import time
from pynput.keyboard import Controller
from calib import Region

# Change this after using calibration script
REGION = (x, y, w, h)  # (left, top, width, height)

keyboard = Controller()

def capture_frame(region):
    img = pyautogui.screenshot(region=region)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img

def detect_blue_and_red(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Blue arrow HSV range
    blue_lower = np.array([100, 150, 100])
    blue_upper = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    # Red target HSV ranges (red wraps around hue circle)
    red_lower1 = np.array([0, 100, 100])
    red_upper1 = np.array([10, 255, 255])
    red_lower2 = np.array([160, 100, 100])
    red_upper2 = np.array([179, 255, 255])
    red_mask1 = cv2.inRange(hsv, red_lower1, red_upper1)
    red_mask2 = cv2.inRange(hsv, red_lower2, red_upper2)
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)

    return blue_mask, red_mask

def should_press(blue_mask, red_mask, threshold=15):
    overlap = cv2.bitwise_and(blue_mask, red_mask)
    count = cv2.countNonZero(overlap)
    return count > threshold

def press_space():
    keyboard.press(' ')
    keyboard.release(' ')

def main():
    print("Starting Tug of War bot...")
    time.sleep(2)
    print("Running. Press Q to stop.")

    try:
        while True:
            frame = capture_frame(REGION)
            blue_mask, red_mask = detect_blue_and_red(frame)

            if should_press(blue_mask, red_mask):
                press_space()
                print("Pressed SPACE")
                time.sleep(0.2)  # Prevent spam press

            time.sleep(0.01)
    except KeyboardInterrupt:
        print("Bot stopped.")

if __name__ == "__main__":
    main()
