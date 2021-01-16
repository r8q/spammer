import pyautogui, time
f=open("message.txt",'r')
time.sleep(5)
for word in f:
    pyautogui.typewrite(word)
pyautogui.press("enter")
