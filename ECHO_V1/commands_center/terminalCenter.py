# Main terminal center
import os
from datetime import datetime
from ECHO_V1.commands_center import processesThreads
from ECHO_V1.this_cpu import processor
from termcolor import *
from ECHO_V1.assets import assetsInfo

DATE = datetime.today().strftime('%Y-%m-%d')
TIME = datetime.today().strftime('%H:%M:%S:%p')
# ECHO = cprint("ECHO", 'green', attrs=['bold'])
# (f"ECHO -> {DATE} @ {TIME} > ")

# assetsInfo.electronicBeeps.beepSequential('startup') Turn it on later on
cprint(f"ECHO V1 started on {DATE} at {TIME} \n", 'green', attrs=['bold'])
while True:
    DATE = datetime.today().strftime('%Y-%m-%d')
    TIME = datetime.today().strftime('%H:%M:%S:%p')
    try:
        command = input((f"ECHO -> {DATE} @ {TIME} > "))
        # If command inspected is true: do the necessary operations
        if processesThreads.Processes().inspectCommandStage1(command) is True:
            processesThreads.Processes().log(command)

            # Command processing and executing
            if command in processor.terminalProcessor:
                processor.terminalProcessor[command]()
            elif command in processor.vehicleProcessor:
                processor.vehicleProcessor[command]()
            else:
                print("Command not found")

    except KeyboardInterrupt:
        print(colored(f"\nECHO V1 ended on {DATE}, at {TIME}", 'red'))
        exit(0)


