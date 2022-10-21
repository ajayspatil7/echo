from tabulate import tabulate


def main():
    # Path: ROOT/echov1.py
    fLogs = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/commandsLogsFailed'
    pLogs = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/commandsLogsPassed'

    # Get the data from the files
    fLogsData = open(fLogs, 'r').readlines()
    pLogsData = open(pLogs, 'r').readlines()



