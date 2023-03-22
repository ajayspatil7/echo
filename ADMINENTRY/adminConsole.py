from AUTHENTICATION import authFile
from termcolor import cprint
from datetime import datetime
from ECHOV1.commands_center import processesThreads

# This is the main function that runs the admin console program


def adminConsole() -> bool:
    DATE = datetime.today().strftime('%Y-%m-%d')
    TIME = datetime.today().strftime('%I:%M:%S:%p')

    cprint(f"\nADMIN CONSOLE STARTED {DATE} at {TIME} \n", 'green', attrs=['bold'])
    processesThreads.Processes().entryExitLogger('ENTRY')

    while True:
        DATE = datetime.today().strftime('%Y-%m-%d')
        TIME = datetime.today().strftime('%I:%M:%S:%p')
        logPath = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/adminLogs.txt'
        try:
            command = input(f"{DATE} @ {TIME} ::: ADMIN > ")
            processesThreads.Processes().log(command, logPath)
            # If command inspected is true: do the necessary operations
            if processesThreads.Processes().inspectCommandStage1(command):
                processesThreads.Processes().log(command)
                processesThreads.Processes().inspectCommandStage2(command)
                processesThreads.Processes().log(command)
                processesThreads.Processes().signalEcho(command)

            else:
                cprint("Invalid command.", 'red')

        except KeyboardInterrupt:
            DATE = datetime.today().strftime('%Y-%m-%d')
            TIME = datetime.today().strftime('%I:%M:%S:%p')
            print(cprint(f"\nECHO V1 ended on {DATE}, at {TIME}", 'red'))
            processesThreads.Processes().entryExitLogger('FORCE-EXIT')
            exit()


# Path: ADMINENTRY/adminConsole.py

adminConsole()