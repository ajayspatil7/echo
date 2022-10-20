# Import all files from commands_center folder
from ECHOV1.commands_center.processesThreads import Processes
from ECHOV1.commands_center import processesThreads, commands
from ECHOV1.functionalEngine import threadsEngine

# TODO: Implement the processor
# TODO: Process all the commands here and send the output to the terminalCenter

processes = processesThreads.Processes  # Process threads
E_threads = threadsEngine.EchoThreads  # Echo threads
V_threads = threadsEngine.FlightThreads  # Flight threads

terminalProcessor = {
    'echo --intro': E_threads.threadEchoIntro,
    'echo --time': E_threads.threadEchoTime,
    'echo --prepare for launch': E_threads.threadEchoPrepareForLaunch,
    'echo --exit': E_threads.threadEchoExit,
    'echo --get log data': processes.getLogsData,
    'echo --clear': E_threads.threadClearTerminal
}

vehicleProcessor = {
    'start': V_threads.startFlight,
    'launch': V_threads.launchFlight,
    'abort': V_threads.abortFlight,
    'status': V_threads.flightStatus,
    'info': V_threads.flightInfo,
    'help': processes.helpEcho
}

commandsStorage = [terminalProcessor, vehicleProcessor, processes]
