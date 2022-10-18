# All the valid commands stay here


class Commands:
    VALID_ECHO_COMMANDS = {
        'echo --intro': 'echoThreads.threadEchoIntro() \n',
        'echo --time': 'echoThreads.threadEchoTime() \n',
        'echo --prepareForLaunch': 'echoThreads.prepareForLaunch() \n',
        'echo --testForLaunch': 'echoThreads.testForLaunch() \n',
        'echo --start -terminal': 'echoThreads.startTerminal() \n',
        'echo --get log data': 'processes.getLogsData() \n',
        'echo --exit': 'echoThreads.threadEchoExit() \n',
    }

    VALID_TERMINAL_OPERATIONS = {
        'start': 'kernel.showTerminalInfo()',
        'time': 'kernel.showTerminalTime()',
        'date': 'kernel.showTerminalDate()',
        'clear': 'kernel.clearTerminal()',
        'exit': 'kernel.exitTerminal()',
        'show terminal info': 'kernel.showTerminalInfo()',
    }

    VALID_FLIGHT_OPERATIONS = {
        'start': 'kernel.startFlight()',
        'launch': 'kernel.launch()',
        'abort': 'kernel.abort()',
        'status': 'kernel.status()',
        'info': 'kernel.info()',
        'help': 'kernel.help()',
    }





