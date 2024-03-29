"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup
beep1 = '/Users/ajay/PycharmProjects/echo/ECHOV1/assets/assets_beeps/electronicBeep1.wav'
beep2 = '/Users/ajay/PycharmProjects/echo/ECHOV1/assets/assets_beeps/electronicBeep6.mp3'
beep3 = '/Users/ajay/PycharmProjects/echo/ECHOV1/assets/assets_beeps/electronicBeep8.mp3'
beep4 = '/Users/ajay/PycharmProjects/echo/ECHOV1/assets/assets_beeps/electronicShortBeep.mp3'
beep5 = '/Users/ajay/PycharmProjects/echo/ECHOV1/assets/assets_beeps/shutdown.mp3'
beep6 = '/Users/ajay/PycharmProjects/echo/ECHOV1/assets/assets_beeps/trStartupBeep.mp3'
APP = ['echov1.py']
DATA_FILES = [beep1, beep2, beep3, beep4, beep5, beep6]
OPTIONS = {}
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
