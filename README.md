# 🤖 WhatsApp Auto Message Bot

![Hero_image](https://camo.githubusercontent.com/7c5e1164814ebee5701bb59400d2d4186a45586fdf27b7218f6886227b147f9b/68747470733a2f2f692e6962622e636f2f787430794c6674732f4f50504f5254554e49544945532d312e706e67)

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
pip install pyperclip
```

---

## 💡 How It Works

This script simulates keyboard input to repeatedly send a message in a selected WhatsApp chat.

---

## 📜 Script (`whatsapp_bot.py`)

```python
import pyautogui
import time
import pyperclip  # Required to copy message with emoji to clipboard

def send_whatsapp_bot():
    try:
        print("⏳ You have 10 seconds to open WhatsApp Web and select the chat where messages should be sent...")
        time.sleep(10)

        message = "I miss you ❤️"

        for i in range(1000):
            pyperclip.copy(message)                # Copy message to clipboard
            pyautogui.hotkey("ctrl", "v")          # Paste the message
            pyautogui.press("enter")               # Press Enter to send
            time.sleep(0.1)                        # Slight delay to avoid freezing or detection

    except KeyboardInterrupt:
        pass  # Just silently stop without printing anything

# Run the function
send_whatsapp_bot()
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

## ❤️ Fun Use-Case Idea

Did your **girlfriend or crush get mad at you**? 😢  
Win her back with some harmless charm! Just replace the message with something like:

```python
pyautogui.typewrite("I'm really sorry 😔❤️ Please talk to me")
```

## 👨‍💻 Created By

Made with ❤️ by Amit Das — a Python and web enthusiast.
Feel free to connect for more cool automation scripts and tools!
