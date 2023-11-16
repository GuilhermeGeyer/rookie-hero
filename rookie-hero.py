# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:12:04 2023

@author: user
"""

import pyautogui
import sys
from time import time


def exit():
    sys.exit()


def check_start():
    if pyautogui.position()[0] == 0:
        start()


def check_pause():
    if pyautogui.position()[1] == 0:
        pause()


def check_exit():
    if pyautogui.position() == (0, 0):
        exit()


def check_color(xpos, ypos, color):
    # print(f'{pyautogui.pixel(xpos, ypos)}\n{color}\n')
    if pyautogui.pixel(xpos, ypos) == color:
        return True
    return False


def pause():
    print('pause')
    while True:
        check_start()
    pyautogui.sleep(0.01)


def click(xpos, ypos):
    check_exit()
    check_pause()
    pyautogui.moveTo(xpos, ypos)
    pyautogui.sleep(0.001)
    pyautogui.mouseDown()
    pyautogui.sleep(0.05)
    pyautogui.mouseUp()
    pyautogui.sleep(0.001)


def click_left(xpos, ypos):
    pyautogui.moveTo(xpos, ypos)
    pyautogui.sleep(0.001)
    pyautogui.mouseDown(button='secondary')
    pyautogui.sleep(0.05)
    pyautogui.mouseUp(button='secondary')
    pyautogui.sleep(0.001)


def smart_click(xpos, ypos, color, sleep_time):
    if check_color(xpos, ypos, color):
        pyautogui.sleep(sleep_time)
        click(xpos, ypos)
        return True
    return False


def wait(xpos, ypos, color, timeout):
    timer = time()
    print('wait')
    while not check_color(xpos, ypos, color):
        check_exit()
        check_pause()
        # print(time() - timer, timeout)
        if time() - timer > timeout:
            break
        pyautogui.sleep(0.001)


def carrots():
    # guy
    # smart_click(487, 298, (125, 86, 67), 0.1)
    click(487, 298)
    pyautogui.sleep(3)
    # buy carrot
    # smart_click(564, 412, (155, 141, 132), 0.1)
    click(564, 412)
    # click(564, 412)
    pyautogui.sleep(2)
    # smart_click(582, 411, (145, 128, 126), 0.1)
    click(582, 411)
    pyautogui.sleep(2)
    # smart_click(665, 304, (57, 42, 50), 0.1)
    click(665, 304)
    pyautogui.sleep(1)
    # use carrot
    click_left(665, 304)
    pyautogui.sleep(1)
    # smart_click(846, 404, (255, 255, 255), 0.1)
    click(846, 404)
    pyautogui.sleep(1)
    # smart_click(395, 457, (255, 255, 255), 0.1)
    click(395, 457)
    pyautogui.sleep(1)
    click_left(395, 457)
    pyautogui.sleep(1)
    click_left(395, 457)
    pyautogui.sleep(1)


def start():

    pyautogui.sleep(0.5)
    print('start')
    # finished = False
    while True:
        check_exit()
        check_pause()
        smart_click(675, 454, (53, 64, 72), 0.1)  # map
        # click(681, 458)  # map
        # print(f'{pyautogui.pixel(681, 458)}\n{(108, 216, 32)}')
        # smart_click(1083, 726, (173, 208, 47), 0.1)
        if check_color(1156, 736, (28, 132, 90)):
            click(1011, 736)  # (slime) over sign
            pyautogui.sleep(3)
        # smart_click(1104, 731, (28, 132, 90), 0.1)  # slime
        smart_click(325, 581, (206, 232, 255), 0.1)  # attack
        # smart_click(457, 475, (28, 132, 90), 0.1)  # slime in battle
        smart_click(451, 460, (118, 221, 161), 0.1)  # slime in battle
        if smart_click(841, 734, (255, 128, 255), 0.1):  # or finished:  # end battle
            # finished = True
            # print(f'end fight {time()}')
            '''pyautogui.moveTo(100, 100)
            pyautogui.sleep(0.1)
            if check_color(841, 734, (255, 128, 255)):
                break'''

            # pyautogui.sleep(0.001)
            # click(841, 734)

            pyautogui.sleep(3)

            carrots()

            click(539, 152)  # exit forest
            pyautogui.sleep(2)
            click(676, 154)  # exit forest
            pyautogui.sleep(3)

            '''wait(347, 149, (184, 126, 80), 5)
            smart_click(347, 149, (184, 126, 80), 0.1)  # go back
            pyautogui.sleep(3)
            wait(680, 147, (184, 126, 80), 5)
            if smart_click(680, 147, (184, 126, 80), 0.1):  # go back (again)
                finished = False'''
        '''if check_color(681, 458, (108, 216, 32)):
            pyautogui.sleep(0.1)
            click(681, 458)'''


pause()
