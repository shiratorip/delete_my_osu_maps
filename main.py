import pyautogui
import time
import keyboard

def perform_macro(star):
    paste = "played>99999 mode=o star<"
    increment= 0.05
    star += increment
    value = paste + str(round(star, 2))

    time.sleep(0.5)
    keyboard.press('p')
    time.sleep(0.2)
    keyboard.release('p')
    time.sleep(0.2)
    keyboard.press('p')
    time.sleep(0.2)
    keyboard.release('p')
    time.sleep(0.2)
    keyboard.press('p')
    time.sleep(0.2)
    keyboard.release('p')
    time.sleep(0.2)
    pyautogui.typewrite(value)
    time.sleep(3)

    keyboard.press('f3')
    time.sleep(0.4)
    keyboard.release('f3')
    time.sleep(0.4)
    keyboard.press('2')
    time.sleep(0.4)
    keyboard.release('2')
    time.sleep(0.4)
    keyboard.press('3')
    time.sleep(0.4)
    keyboard.release('3')
    time.sleep(0.2)
    keyboard.press('1')
    time.sleep(0.4)
    keyboard.release('1')
    time.sleep(0.4)

    print(star,"waiting for action: 1-proceed or 2-cancel")
    while True:
        if keyboard.is_pressed('1'):
            time.sleep(0.2)
            keyboard.press('esc')
            time.sleep(0.2)
            keyboard.release('esc')
            time.sleep(0.2)
            keyboard.press('esc')
            time.sleep(0.2)
            keyboard.release('esc')
            time.sleep(0.2)
            perform_macro(star)
        if keyboard.is_pressed('2'):
            return

while True:
    if keyboard.is_pressed('space'):
        perform_macro(4.55)

    time.sleep(0.1)
