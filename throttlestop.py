#This program will set the Throttlestop mode to Game, Performance or Cooling as specified.
#It uses the pyautogui and sys module.

import sys
import pyautogui

mode_name = sys.argv[1]

#All necessary postions
taskbar_icon = 1769, 1049
throttlestop = 1770, 900
game = 1800, 785
performance = 1800, 760
cooling = 1800, 910

modes = {'performance':performance, 'game':game, 'cooling':cooling}

if mode_name in modes.keys():
    pyautogui.moveTo(taskbar_icon) #1
    pyautogui.click()

    pyautogui.moveTo(throttlestop) #2
    pyautogui.click(button='right')

    pyautogui.moveTo(modes[mode_name]) #3
    pyautogui.click()








