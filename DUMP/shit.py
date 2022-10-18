from tabulate import tabulate


def main():
    # Path: ROOT/main.py
    fLogs = '/Users/ajay/PycharmProjects/echo/ECHOV1_LOGS/commandsLogsFailed'
    pLogs = '/Users/ajay/PycharmProjects/echo/ECHOV1_LOGS/commandsLogsPassed'

    # Get the data from the files
    fLogsData = open(fLogs, 'r').readlines()
    pLogsData = open(pLogs, 'r').readlines()


main()

