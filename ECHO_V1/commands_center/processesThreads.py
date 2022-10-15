# Operations performed when a command is called from the terminal.
import os
import time
from ECHO_V1.commands_center import commands
from datetime import datetime
from ECHO_V1.assets.assetsInfo import electronicBeeps

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
        from ECHO_V1.this_cpu import processor
        if command in processor.terminalProcessor or command in processor.vehicleProcessor:
            return True
        else:
            return False

    # Function to log the command to a file
    def log(self, command: str):
        log_DATE = datetime.today().strftime('%Y-%m-%d')
        log_TIME = datetime.today().strftime('%I:%M:%S:%p')
        # Log the command to the log file if processes is true
        if self.inspectCommandStage1(command) is True:
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1_LOGS/commandsLogsPassed', 'a') as file:
                file.write(f"{command} @ {log_TIME} on {log_DATE} \n")

        if self.inspectCommandStage1(command) is False:
            with open('/Users/ajay/PycharmProjects/echo/ECHOV1_LOGS/commandsLogsFailed', 'a') as invFile:
                invFile.write(f"{command} @ {log_TIME} on {log_DATE} \n")

    # Function to show the terminal info
    def showTerminalInfo(self):
        from ECHO_V1.functionalEngine import threadsEngine
        time.sleep(1.0)
        threadsEngine.echoThreads.threadEchoIntro(None)

    # Get data from processor
    def signalEcho(self, command: str) -> bool:
        from ECHO_V1.this_cpu import processor
        if command in processor.terminalProcessor:
            processor.terminalProcessor[command]()
        if command in processor.vehicleProcessor:
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
    def stopProcesses(self=None, command: str = None):
        if command in commands.Commands().VALID_TERMINAL_OPERATIONS:
            electronicBeeps.beepSequential('shutdown')
            print("Stopping the processes...")
            time.sleep(1.0)
            print("Exiting the terminal")
            time.sleep(1.0)
            exit(0)
        else:
            return False


