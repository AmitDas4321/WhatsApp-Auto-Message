import pyautogui
import time
import pyperclip  # Required to copy message with emoji to clipboard

def send_whatsapp_bot():
    try:
        print("⏳ You have 10 seconds to open WhatsApp Web and select the chat where messages should be sent...")
        time.sleep(10)

        message = "Sorry"

        for i in range(1000):
            pyperclip.copy(message)                # Copy message to clipboard
            pyautogui.hotkey("ctrl", "v")          # Paste the message
            pyautogui.press("enter")               # Press Enter to send
            time.sleep(0.1)                        # Slight delay to avoid freezing or detection

    except KeyboardInterrupt:
        pass  # Just silently stop without printing anything

# Run the function
send_whatsapp_bot()
