import random as randy
import pyautogui as gui
import pyperclip as pc
import time


amount = gui.prompt(text='how many times?', title='funny spam bot' , default=69)
num2 = int(amount)

loop = 0
gui.alert(text='prepare yourself you have 5 secodnds to click the text bar for discord', title='', button='im prepared')
time.sleep(5)
while loop <= num2:
    time.sleep(1)
    number = randy.randint(0, 10000)
    pc.copy(number)
    paste = pc.paste()
    print(paste)
    gui.hotkey('command', 'v')
    gui.hotkey('enter')
    print(loop)
    loop = loop + 1
    