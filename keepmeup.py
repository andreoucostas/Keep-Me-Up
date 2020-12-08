import time, pyautogui
import PySimpleGUI as sg
import multiprocessing

sg.theme('Dark')
layout = [
    [sg.Text(
'''Keep-Me-Up is now running.
You can keep it minised, and it will continue running.
Close it to disable it.''')]
]

window = sg.Window('Keep-Me-Up', layout)

def KeepUI():
    p2.start()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            if p2.is_alive(): 
                p2.terminate()
            break

def dontsleep():
    while True:
        pyautogui.press('volumedown')
        time.sleep(1)
        pyautogui.press('volumeup')
        time.sleep(300)

p1 = multiprocessing.Process(target = KeepUI)
p2 = multiprocessing.Process(target = dontsleep)

if __name__ == '__main__':
    p1.start()
