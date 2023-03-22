# All the valid commands stay here


class Commands:
    VALID_ECHO_COMMANDS = {
        'echo --intro': 'Shows info about the echo prompt \n',
        'echo --time': 'Shows the current time of the echo prompt \n',
        'echo --prepare for launch': 'Prepares the flight for launch. Under a circumstance\n',
        'echo --test for launch': 'Test the flight for launch after preparing. Under a circumstance \n',
        'echo --start -terminal': 'Starts an echo prompt connected to a flight \n',
        'echo --get log data': 'P for passed log data and F for failed logs data \n',
        'echo --exit': 'Prepares to exit the flight \n',
        'echo --clear': 'Clears the terminal and previous commands \n',
        'echo --stop': 'Stop the terminal and end the processes',
    }

    VALID_TERMINAL_OPERATIONS = {
        'start': 'Starts the terminal \n',
        'time': 'Shows the current time of the flight \n',
        'echo --date': 'Shows the current date of the flight \n',
        'show --terminal -info': 'Shows the info about the terminal \n',
        'show --author -credits': 'Shows the credits of the author \n',
    }

    VALID_FLIGHT_OPERATIONS = {
        'start': 'Starts the flight \n',
        'launch': 'Launches the flight \n',
        'abort': 'Aborts the flight \n',
        'status': 'Shows the status of the flight \n',
        'info': 'Shows the info about the flight \n',
        'help': 'Shows the help menu \n',
    }

    VALID_STRICT_COMMAND = {
        'green operation --open -admin console --root': 'Open admin console if conditions satisfied',
    }





