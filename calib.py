import pyautogui
import time

print("Move your mouse to the TOP-LEFT corner of the circle...")
time.sleep(4)
top_left = pyautogui.position()
print("Top-left:", top_left)

print("Now move to the BOTTOM-RIGHT corner of the circle...")
time.sleep(4)
bottom_right = pyautogui.position()
print("Bottom-right:", bottom_right)

x = top_left.x
y = top_left.y
w = bottom_right.x - x
h = bottom_right.y - y

print(f"REGION = ({x}, {y}, {w}, {h})")
class Coord():
  return x,y,w,h
