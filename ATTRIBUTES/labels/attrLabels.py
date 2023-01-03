# All the labels and text appearing on the terminal should be fetched from here
# Path: ATTRIBUTES/labels/attrLabels.py
from termcolor import cprint

def echoIntroLabels():

    prime_labels = [
        'ECHOV1 is a space flight simulator that is designed to simulate a real rocket controls and flight.',
        'ECHOV1 is a command line based simulator that is designed to be used on a terminal.',
        'ECHOV1 is designed to be used on a Mac OS X above & Linux terminal.'
    ]

    second_labels = [
        '_' * 95,
        '\nOverview of ECHOV1',
    ]

    third_labels = [
        '\n- From flight preparations to launch, ECHO does it all.',
        '- It is safe and secure to use.',
        '- Designed for professionals by professionals.',
        '- ECHOV1 is a free and open source software.',
        '- Everything is logged and can be accessed at any time.',
        '- As it is a CLI based, you got all your controls at your fingertips.',
        '- Not just that, ECHOV1 is a flight control system which can be connected with a real rocket.',
        '- You can test your rocket and its controls with ECHOV1.',
        '- We have got you covered with all the flight preparations.',
        '_' * 95
        ]

    for x in prime_labels:
        cprint(x, 'green', attrs=['bold'])
    for y in second_labels:
        cprint(y, attrs=['bold'])
    for z in third_labels:
        cprint(z, attrs=['bold'])



