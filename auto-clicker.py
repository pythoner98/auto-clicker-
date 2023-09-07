import pyautogui
import time
import keyboard
import threading

def clicker1a():
    click_duration = 0.0  # You can make it smaller for faster clicks
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break


def clicker2b():
    click_duration = 0.0  # You can make it smaller for faster clicks
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break


def clicker3c():
    click_duration = 0.0  # You can make it smaller for faster clicks
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break


def clicker4a():
    click_duration = 0.0  # You can make it smaller for faster clicks
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break


def clicker5b():
    click_duration = 0.0  # You can make it smaller for faster clicks
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break
def clicker6c():
    click_duration = 0.0  # You can make it smaller for faster clicks
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break
def clicker4d():  # Different name
    click_duration = 0.0
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break
def clicker5e():  # Different name
    click_duration = 0.0
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break
def clicker6f():  # Different name
    click_duration = 0.0
    time.sleep(6)
    while True:
        pyautogui.click(duration=click_duration)    
        if keyboard.is_pressed('q'):
            break

clicker1 = threading.Thread(target=clicker1a)
clicker2 = threading.Thread(target=clicker2b)
clicker3 = threading.Thread(target=clicker3c)
clicker1x = threading.Thread(target=clicker4a)
clicker2x = threading.Thread(target=clicker5b)
clicker3x = threading.Thread(target=clicker6c)
clicker4 = threading.Thread(target=clicker4d)  # Different name
clicker5 = threading.Thread(target=clicker5e)  # Different name
clicker6 = threading.Thread(target=clicker6f)  # Different name

clicker1.start()
clicker2.start()
clicker3.start()
clicker1x.start()
clicker2x.start()
clicker3x.start()
clicker4.start()  # Different name
clicker5.start()  # Different name
clicker6.start() 


clicker1.join()
clicker2.join()
clicker3.join()
clicker1x.join()
clicker2x.join()
clicker3x.join()
clicker4.join()  # Different name
clicker5.join()  # Different name
clicker6.join()  # Different name