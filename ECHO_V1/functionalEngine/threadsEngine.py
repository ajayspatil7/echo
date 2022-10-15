# Functions module for ECHO - created by AJAY S P (not for open source)
# Holds all the threads for Command processing
import os
import termcolor
from termcolor import *
from ECHO_V1.commands_center import processesThreads
from _datetime import datetime
from ECHO_V1.commands_center import commands
import time
from ECHO_V1.assets.assetsInfo import electronicBeeps

# defaultElectronicBeep1 = '/Users/ajay/PycharmProjects/echo/assets/electronicBeep8.mp3'
# _electronicBeep2 = '/Users/ajay/PycharmProjects/echo/assets/electronicBeep6.mp3'
# _electronicBeep3 = '/Users/ajay/PycharmProjects/echo/assets/electronicBeep1.wav'


class EchoThreads:

    def threadEchoIntro(self=None):
        print('\nGetting info...')
        electronicBeeps.beepSequential('loading1', interval=0.09, loop=3)
        time.sleep(2.0)
        termColor = termcolor

        termColor.cprint(
            "ECHO_V1 is a space flight simulator that is designed to simulate a real rocket controls and flight.", attrs=['bold'])
        termColor.cprint("ECHO_V1 is the first version of the ECHO series of space flight control simulators.", attrs=['bold'])
        termColor.cprint("ECHO_V1 is a command line based simulator that is designed to be used on a terminal.", attrs=['bold'])
        termColor.cprint("ECHO_V1 is designed to be used on a Mac OS X above & Linux terminal.", attrs=['bold'])
        termColor.cprint("-" * 95, 'green', attrs=['blink'])
        termColor.cprint("Overview of ECHO_V1:", 'green', attrs=['bold'])
        termColor.cprint("- From flight preparations to launch, ECHO does it all.")
        termColor.cprint("- It is safe and secure to use.")
        termColor.cprint("- Designed for professionals by professionals.")
        termColor.cprint("- ECHO_V1 is a free and open source software.")
        termColor.cprint("- Everything is logged and can be accessed at any time.")
        termColor.cprint("- As it is a CLI based, you got all your controls at your fingertips.")
        termColor.cprint("- Not just that, ECHO_V1 is a flight control system which can be connected with a real rocket.")
        termColor.cprint("- You can test your rocket and its controls with ECHO_V1.")
        termColor.cprint("- We have got you covered with all the flight preparations.")
        termColor.cprint(colored("-" * 95, 'green'))
        processesThreads.Processes().log(self)

    def threadEchoTime(self=None):
        electronicBeeps.beepSequential('startup')
        cprint(f"{datetime.today().strftime('%Y-%m-%d')}", attrs=['bold'])
        cprint(f"{datetime.today().strftime('%H:%M:%S:%p')}", attrs=['bold'])

    def threadEchoPrepareForLaunch(self=None):
        print(commands.Commands.VALID_ECHO_COMMANDS['echo --prepareForLaunch'])

    def threadEchoTestForLaunch(self=None):
        print(commands.Commands.VALID_ECHO_COMMANDS['echo --testForLaunch'])

    def threadEchoStartTerminal(self=None):
        print(commands.Commands.VALID_ECHO_COMMANDS['echo --start -terminal'])

    def threadClearTerminal(self):
        os.system('clear')


class FlightThreads:

    def startFlight(self=None):
        electronicBeeps.beepSequential('startup')
        cprint("Flight starting...\n", attrs=['bold'])
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint("Starting HARD Flight Checks...", 'cyan', attrs=['bold'])
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking flight systems...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking emergency systems...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking electrical systems...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking fuel systems...")
        time.sleep(2.5)

        electronicBeeps.beepSequential('startup')
        cprint("Hard Flight Checks complete ✓", 'yellow', attrs=['bold'])
        time.sleep(1.5)

        electronicBeeps.beepSequential('loading1')
        cprint("\n Starting HARD Avionics check...", 'cyan', attrs=['bold'])
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking comms...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking flight controls...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking flight status...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking flight info...")
        time.sleep(1.5)
        electronicBeeps.beepSequential('loading1')
        cprint(" - Checking flight help...")
        time.sleep(2.5)
        electronicBeeps.beepSequential('startup')
        cprint("HARD Avionics check complete ✓ \n", 'yellow', attrs=['bold'])

        time.sleep(2.5)
        print(" - Flight preparations complete.")
        electronicBeeps.beepSequential('loading1')
        time.sleep(1.0)
        cprint("\nAll necessary checks complete you are ready to go!!  ✓ \n", 'green', attrs=['bold'])
        electronicBeeps.beepSequential('startup')

    def launchFlight(self=None):
        cprint("Function -launch flight started...", 'cyan', attrs=["blink"])
        time.sleep(1.5)
        cprint("Launch preparations started...", 'cyan')
        time.sleep(1.5)
        cprint("Checking comms...", 'cyan')
        time.sleep(1.5)
        cprint("Checking ")

    def abortFlight(self=None):
        pass

    def flightStatus(self=None):
        pass

    def flightInfo(self=None):
        pass

    def flightHelp(self=None):
        pass
