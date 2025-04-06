import pyautogui
import time

print("You have 10 seconds to open WhatsApp Web and select the chat...")
time.sleep(10)

for i in range(1000):
    pyautogui.typewrite("Sorry")
    pyautogui.press("enter")
    time.sleep(0.1)
