# Operations performed when a command is called from the terminal.
import os
import time
import signal
import termcolor
from ECHOV1.commands_center import commands
from datetime import datetime
from ECHOV1.assets.assetsInfo import electronicBeeps
from termcolor import *


class Processes:

    def __init__(self):
        self.command = None

    # Function to validate the command from Valid commands
    def inspectCommandStage1(self, command: str) -> bool:
        commandInit = command
        commandsComms = commands.Commands()
        # Inspect the command and check if it is valid
        if command in commandsComms.VALID_ECHO_COMMANDS or command in commandsComms.VALID_TERMINAL_OPERATIONS or command in commandsComms.VALID_FLIGHT_OPERATIONS:
            # print(commandInit)
            return True
        else:
            # print(commandInit)
            return False

    def inspectCommandStage2(self, command: str) -> bool:
        # Check if the command is in processor.terminalProcessor and processor.vehicleProcessor
        from ECHOV1.this_cpu import processor
        if command in processor.terminalProcessor or command in processor.vehicleProcessor or command in processor.processes:
            return True
        else:
            return False

    # Function to log the command to a file
    def log(self, command):
        log_DATE = datetime.today().strftime('%Y-%m-%d')
        log_TIME = datetime.today().strftime('%I:%M:%S:%p')

        # Log the command to a file in a table format
        # Log the command to the log file if processes is true
        if self.inspectCommandStage1(command) is True:
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/commandsLogsPassed', 'a') as file:
                file.write(f"{command}|@ {log_TIME} on {log_DATE} \n")

        if self.inspectCommandStage1(command) is False:
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/commandsLogsFailed', 'a') as invFile:
                invFile.write(f"{command}|@ {log_TIME} on {log_DATE} \n")

    # Function to show the terminal info

    def showTerminalInfo(self):
        from ECHOV1.functionalEngine import threadsEngine
        time.sleep(1.0)
        threadsEngine.echoThreads.threadEchoIntro(None)

    # Get data from processor
    def signalEcho(self, command: str) -> bool:
        from ECHOV1.this_cpu import processor
        if command in processor.terminalProcessor:
            processor.terminalProcessor[command]()
        elif command in processor.vehicleProcessor:
            processor.vehicleProcessor[command]()

    # Does nothing as of now
    def getSignal(self, command: str) -> bool:
        self.command = command
        if self.inspectCommandStage1(command):
            print('-' * 60)
        # Send the commands to X file for processing
        else:
            return command, False

    # Stop the processes and exit the terminal

    def entryExitLogger(self, command: str):
        DATE = datetime.today().strftime('%Y-%m-%d')
        TIME = datetime.today().strftime('%I:%M:%S:%p')

        if command == 'ENTRY':
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/entryExitLogs.txt', 'a') as file:
                file.write(f"[{command:1s}-> @ {TIME:5s} > {DATE}")
        elif command == 'EXIT':
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/entryExitLogs.txt', 'a') as file:
                file.write(f" > PROTECTED {command:1s}  @ {TIME:10s} on {DATE}] \n")
        elif command == 'FORCE-EXIT':
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/entryExitLogs.txt', 'a') as file:
                file.write(f" > {command:1s}      @ {TIME:10s} on {DATE}] \n")

    def getLogsData(self=None):

        fLogs = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/commandsLogsFailed'
        pLogs = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/commandsLogsPassed'

        # Get the data from the files
        fLogsData = open(fLogs, 'r').readlines()
        pLogsData = open(pLogs, 'r').readlines()

        logType = input("Log file type (P/F)? > ")

        if logType == 'P':
            for x in pLogsData:
                termcolor.cprint(x, 'blue', attrs=['bold'])

        elif logType == 'F':
            for x in fLogsData:
                termcolor.cprint(x, 'blue', attrs=['bold'])

    # Function to print about the author in the terminal
    def credits(self=None):
        cprint("\nAuthor : AJAY S PATIL", 'green', attrs=['bold'])
        cprint("Project name : ECHO", 'green', attrs=['bold'])
        cprint("Version : 1.0", 'green', attrs=['bold'])
        cprint("Date : Oct 2022", 'green', attrs=['bold'])

    # Function to print the help menu
    def helpEcho(self=None):
        # Print the help commands menue, where the user can see the commands and their description
        # Get all the commands from commands.py file
        from ECHOV1.commands_center import commands
        from tabulate import tabulate

        commandsComms = commands.Commands()

        cprint(tabulate(commandsComms.VALID_ECHO_COMMANDS.items(), headers=['Command', 'Description'], tablefmt='psql'),
               'magenta')
        cprint(tabulate(commandsComms.VALID_TERMINAL_OPERATIONS.items(), headers=['Command', 'Description'],
                        tablefmt='psql'), 'magenta')
        cprint(tabulate(commandsComms.VALID_FLIGHT_OPERATIONS.items(), headers=['Command', 'Description'],
                        tablefmt='psql'), 'magenta')

        # for x in commandsComms.VALID_ECHO_COMMANDS.keys():
        #     print(f"{x}: {commandsComms.VALID_ECHO_COMMANDS[x]}")
        # Get all the commands usage from
        pass
