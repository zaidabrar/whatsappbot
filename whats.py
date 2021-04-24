import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(10)
for i in range(200):
    pyautogui.press("h")
    pyautogui.press("e")
    pyautogui.press("y")
    pyautogui.press("enter")
