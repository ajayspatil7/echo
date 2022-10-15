import termcolor


def outText(text: str, level: str):
    if level == 'info':
        termcolor.cprint(text, 'green')
    elif level == 'warning':
        termcolor.cprint(text, 'yellow')
    elif level == 'error':
        termcolor.cprint(text, 'red')
    else:
        termcolor.cprint("Invalid level.", 'red')


def echoLabel():
    print("""

███████╗ ░█████╗  ██╗  ██╗ ░█████╗
██╔════╝ ██╔══██  ██║  ██║ ██╔══██╗
█████╗   ██║  ██  ███████║ ██║░░██║
██       ██║  ██╗ ██╔══██║ ██║░░██║
███████╗ ╚█████╔╝ ██║  ██║ ╚█████╔╝
╚══════╝  ╚════╝  ╚═╝  ╚═╝  ╚════╝  Version 1.0.0
    """)