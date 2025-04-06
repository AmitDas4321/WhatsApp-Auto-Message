# 🤖 WhatsApp Auto Message Bot

A fun and lightweight Python script that automates sending a custom message repeatedly on WhatsApp Web. Perfect for harmless pranks with friends (with their consent 😄) or simply exploring Python automation.

> ⚠️ **For educational and personal use only**

---

## ⚠️ Disclaimer

- This script is meant **strictly for educational and personal use**.
- Do **NOT** use it for spam, harassment, or any activity that violates [WhatsApp's Terms of Service](https://www.whatsapp.com/legal/terms-of-service).
- The developer is **not responsible** for any misuse of this script.

---

## 📦 Requirements

Make sure you have the following before running the script:

- 🖥️ Operating System: Windows / macOS / Linux  
- 🐍 Python 3.x installed  
- 🧑‍💻 Code Editor: [VS Code](https://code.visualstudio.com/) or any of your choice  
- 💬 A WhatsApp account with [WhatsApp Web](https://web.whatsapp.com)  
- 📦 Python module: `pyautogui`

Install the required library with:

```bash
pip install pyautogui
```

---

## 💡 How It Works

This script simulates keyboard input to repeatedly send a message in a selected WhatsApp chat.

---

## 📜 Script (`whatsapp_bot.py`)

```python
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
```

> 💡 Tip: You can replace `"Sorry"` with any custom message of your choice.

---

## ▶️ Running the Script

1. Open [WhatsApp Web](https://web.whatsapp.com) in your browser.
2. Select the chat where you want to send the message.
3. Run the script using:

```bash
python whatsapp_bot.py
```

4. Sit back and watch the bot do its thing!

---

## 🛑 To Stop the Script

To stop the message loop midway, simply press `Ctrl + C` in the terminal.

---

## 💬 Customization

Want to customize the script? You can:
- Change the message content
- Adjust the number of repetitions
- Modify the time delay between messages

Example:

```python
for i in range(500):
    pyautogui.typewrite("Hey, just checking in!")
    pyautogui.press("enter")
    time.sleep(0.2)
```

---

## 👨‍💻 Created By

Made with ❤️ by Amit Das — a Python and web enthusiast.
Feel free to connect for more cool automation scripts and tools!
