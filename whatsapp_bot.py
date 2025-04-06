import pyautogui  # Automates keyboard and mouse actions
import time       # Adds delays between actions

# Prompt user to get ready
print("⏳ You have 10 seconds to open WhatsApp Web and select the chat where messages should be sent...")

# Delay to allow manual chat selection
time.sleep(10)

# Message sending loop
for i in range(1000):  # Adjust the number as needed
    pyautogui.typewrite("Sorry")  # Message to be sent
    pyautogui.press("enter")      # Press Enter to send
    time.sleep(0.1)               # Slight delay to avoid freezing or detection
