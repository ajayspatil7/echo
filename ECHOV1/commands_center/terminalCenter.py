# Main terminal center
import importlib
import os
from termcolor import *
from datetime import datetime
from ECHOV1.this_cpu import processor
from ECHOV1.assets.assetsInfo import termOut
from ECHOV1.commands_center import processesThreads


DATE = datetime.today().strftime('%Y-%m-%d')
TIME = datetime.today().strftime('%I:%M:%S:%p')
# ECHO = cprint("ECHO", 'green', attrs=['bold'])
# (f"ECHO -> {DATE} @ {TIME} > ")
termOut.echoLabel()
# assetsInfo.electronicBeeps.beepSequential('startup') Turn it on later on
cprint(f"ECHO V1 started on {DATE} at {TIME} \n", 'green', attrs=['bold'])
processesThreads.Processes().entryExitLogger('ENTRY')
while True:
    DATE = datetime.today().strftime('%Y-%m-%d')
    TIME = datetime.today().strftime('%I:%M:%S:%p')
    try:
        command = input(f"ECHO -> {DATE} @ {TIME} > ")
        processesThreads.Processes().log(command)
        # If command inspected is true: do the necessary operations
        if processesThreads.Processes().inspectCommandStage1(command) is True:
            processesThreads.Processes().log(command)
            processesThreads.Processes().inspectCommandStage2(command)
            processesThreads.Processes().log(command)
            processesThreads.Processes().signalEcho(command)

    except KeyboardInterrupt:
        DATE = datetime.today().strftime('%Y-%m-%d')
        TIME = datetime.today().strftime('%H:%M:%S:%p')
        print(colored(f"\nECHO V1 ended on {DATE}, at {TIME}", 'red'))
        processesThreads.Processes().entryExitLogger('FORCE-EXIT')
        exit(0)


