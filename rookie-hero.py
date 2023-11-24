# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:12:04 2023

@author: user
"""

import pyautogui
import sys
from time import time
from winsound import Beep


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
    if pyautogui.pixel(xpos, ypos) == color:
        return True
    return False


def pause():
    print('pause')
    while True:
        check_start()
        pyautogui.sleep(0.001)


def click(xpos, ypos):
    check_exit()
    check_pause()
    pyautogui.moveTo(xpos, ypos)
    sleep(0.001)
    pyautogui.mouseDown()
    sleep(0.05)
    pyautogui.mouseUp()
    sleep(0.001)


def click_left(xpos, ypos):
    pyautogui.moveTo(xpos, ypos)
    sleep(0.001)
    pyautogui.mouseDown(button='secondary')
    sleep(0.05)
    pyautogui.mouseUp(button='secondary')
    sleep(0.001)


def smart_click(xpos, ypos, color, sleep_time):
    if check_color(xpos, ypos, color):
        sleep(sleep_time)
        click(xpos, ypos)
        return True
    return False


def wait(xpos, ypos, color, timeout=0):
    timer = time()
    while not check_color(xpos, ypos, color):
        check_exit()
        check_pause()
        if time() - timer > timeout and timeout:
            print('timeout')
            break
        pyautogui.sleep(0.001)


def wait_click(xpos, ypos, color, sleep_time, timeout=0):
    wait(xpos, ypos, color, timeout=timeout)
    smart_click(xpos, ypos, color, sleep_time)


def sleep(sleep_time):
    timer = time()
    while time() - timer < sleep_time:
        pyautogui.sleep(0.001)
        check_exit()
        check_pause()


def press_key(key, sleep_time=0):
    pyautogui.keyDown(key)
    Beep(1000, 100)
    pyautogui.keyUp(key)
    sleep(sleep_time)


def format_time(seconds):
    minutes = 0
    hours = 0
    if seconds > 3600:
        hours = int(seconds // 3600)
        seconds = seconds % 3600
    if seconds > 60:
        minutes = int(seconds // 60)
        seconds %= 60
    return f'{hours}h {minutes:02d}m {seconds:.2f}s'


def carrots():
    # carrot guy
    click(487, 298)
    sleep(3)
    # buy carrot
    click(564, 412)
    sleep(2)
    click(582, 411)
    sleep(2)
    click(665, 304)
    sleep(1)
    # use carrot
    click_left(665, 304)
    sleep(1)
    click(846, 404)
    sleep(1)
    click(395, 457)
    sleep(1)
    click_left(395, 457)
    sleep(1)
    click_left(395, 457)
    sleep(1)


def skip_carrots():
    wait(693, 415, (243, 244, 227))
    sleep(0.2)
    click(358, 31)  # go back
    wait(1000, 721, (251, 251, 232))
    sleep(0.2)
    click(675, 37)  # go back (again)
    sleep(1)


def heal_after_battle(sleep_time, heal=False):
    press_key('x', sleep_time)

    if heal:
        press_key('z', sleep_time)
        press_key('z', sleep_time)
        press_key('x', sleep_time)

    # save
    press_key('up', sleep_time)
    press_key('up', sleep_time)
    press_key('z', sleep_time)
    press_key('z', sleep_time)

    press_key('x', sleep_time)


def start():

    count = 0
    run_time = time()
    buy_carrots = False
    sleep(0.5)
    print('start')

    while True:
        check_exit()
        check_pause()
        wait(445, 141, (255, 255, 255))
        sleep(0.2)
        click(682, 364)  # map

        wait_click(1061, 690, (146, 194, 93), 0.1)  # over sign

        # battle
        wait_click(316, 516, (206, 232, 255), 0.1)  # attack

        wait_click(430, 378, (117, 221, 160), 0.1)  # slime in battle
        wait(316, 516, (206, 232, 255))  # wait for turn

        # repeat
        wait_click(316, 516, (206, 232, 255), 0.1)  # attack

        wait_click(430, 378, (117, 221, 160), 0.1)  # slime in battle

        wait(228, 152, (255, 255, 255))  # victory screen

        count += 1
        print(f'Total runs: {count}\nRun time: ' +
              f'{format_time(time() - run_time)}\n')
        click(228, 152)   # end battle
        sleep(0.05)
        click(228, 152)   # end battle
        sleep(0.1)

        wait(693, 415, (243, 244, 227))
        sleep(0.2)
        heal_after_battle(0.2)

        if buy_carrots:
            carrots()
            click(539, 152)  # exit forest
            sleep(2)
            click(676, 154)  # exit forest
            sleep(3)
        else:
            skip_carrots()


pause()
