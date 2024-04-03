import pyautogui
import time
import threading
import clipboard

# Function to continuously listen for the middle mouse button click
def middle_click_listener():
    pyautogui.FAILSAFE = False
    while True:
        if pyautogui.mouseInfo() == 'Middle':
            paste_clipboard()
            time.sleep(0.2)  # Avoid accidental double-clicks

# Function to paste clipboard

def paste_clipboard():
    content = clipboard.paste()
    pyautogui.typewrite(content)

# Start a new thread to listen for middle mouse button clicks
thread = threading.Thread(target=middle_click_listener)
thread.daemon = True
thread.start()

# Keep the main thred running
while True:
    time.sleep(1)