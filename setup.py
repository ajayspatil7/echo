"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['echov1.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': '/Users/ajay/PycharmProjects/echo/APPICONS/Assets.xcassets/AppIcon.appiconset/mainIcon.png'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
