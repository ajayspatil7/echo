import time
import playsound
from termcolor import *


defaultElectronicBeep1 = '/Users/ajay/PycharmProjects/echo/ECHO_V1/assets/assets_beeps/electronicBeep8.mp3'
defaultElectronicBeep2 = '/Users/ajay/PycharmProjects/echo/ECHO_V1/assets/assets_beeps/trStartupBeep.mp3'
defaultElectronicShutdown = '/Users/ajay/PycharmProjects/echo/ECHO_V1/assets/assets_beeps/shutdown.mp3'

_electronicBeep2 = '/Users/ajay/PycharmProjects/echo/ECHO_V1/assets/assets_beeps/electronicBeep6.mp3'
_electronicBeep3 = '/Users/ajay/PycharmProjects/echo/ECHO_V1/assets/assets_beeps/electronicBeep1.wav'
_electronicBeep4 = '/Users/ajay/PycharmProjects/echo/ECHO_V1/assets/assets_beeps/electronicShortBeep.mp3'


def beepSequential(level: str, interval: float = None, loop: str = None):

    if level == 'loading3':
        for x in range(3):
            playsound.playsound(defaultElectronicBeep1)
            time.sleep(0.1)
            playsound.playsound(defaultElectronicBeep1)
            time.sleep(0.5)

    elif level == 'startup':
        for y in range(1):
            playsound.playsound(defaultElectronicBeep2)

    elif level == 'warning':
        for y in range(3):
            playsound.playsound(_electronicBeep3)
            time.sleep(0.5)
            playsound.playsound(_electronicBeep3)
            time.sleep(0.5)

    elif level == 'shutdown':
        playsound.playsound(defaultElectronicShutdown)

    elif level == 'loading1':
        if loop is not None and interval is not None:
            for x in range(loop):
                playsound.playsound(defaultElectronicBeep1)
                time.sleep(interval)
        else:
            playsound.playsound(defaultElectronicBeep1)

    else:
        cprint("Invalid beep level.", 'red')

