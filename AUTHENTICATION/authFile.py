import hashlib
import os
from termcolor import *
from datetime import datetime
from tabulate import tabulate


def credentialsLog(user=None, logData=None, log_type=None):

    DATE = datetime.today().strftime('%Y-%m-%d')
    TIME = datetime.today().strftime('%I:%M:%S:%p')
    filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/userLogs.txt'

    if user and logData is not None:
        timeStamp = str(datetime.today()).split('.')[0]
        filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/userLogs.txt'
        with open(filePath, 'a') as credFile:
            credFile.write(f"{user} :: {logData} @ {TIME} on {DATE}\n")

    if logData is not None:
        if logData is type(str):
            with open(filePath, 'a') as credFile:
                credFile.write(f"{logData} ::  @ {TIME} ::  on {DATE} \n")

    if str(log_type).lower() == 'manually':
        entryExitLog = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/entryExitLogs.txt'
        with open(entryExitLog, 'a') as credFile:
            credFile.write(f"{logData} @ {TIME} on {DATE}\n")
    else:
        pass

    # Log the data in table format
    with open(filePath, 'r') as data:
        data = data.readlines()
        data = [i.split('::') for i in data]
        tabulatedLog = tabulate(data, headers=['User', 'Log Data', 'Time Stamp'], tablefmt='fancy_grid')


def login() -> str:

    credentialsLog(logData='Login function started!', log_type='manually')
    userID = input("U-ID > ")
    passWD = input("Key-CODE > ")

    # Convert passWD to SHA25 and store it in usersData.txt.txt file
    # Convert userID to SHA25 and store it in usersData.txt.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()

    filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/usersData.txt'

    # Check if the userID and passWD are in the file
    with open(filePath, 'r') as authFile:
        for line in authFile:
            if hashlib.sha256(userID.encode()).hexdigest() in line and passWD in line:
                cprint("Login Successful!!", 'green', attrs=['bold'])
                credentialsLog(userID, logData='Logged In Successfull!')
                credentialsLog(logData='Login function completed! --True', log_type='manually')
                return True
            else:
                cprint("Username or Password is incorrect!", 'red', attrs=['bold'])
                credentialsLog(userID, logData='Login unsuccessful -CR.')
                credentialsLog(logData='Exiting Authentication ECHO', log_type='manually')
                credentialsLog(logData='Login function completed! --False', log_type='manually')
                return False


def createAccount() -> str:

    credentialsLog(logData='Create Account Started', log_type="manually")

    userID = input("UserID > ")
    passWD = input("PassKey > ")

    # Convert passWD & userID to SHA25 and append it in usersData.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()
    userID = hashlib.sha256(userID.encode()).hexdigest()

    # Path to store the data
    filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/usersData.txt'

    with open(filePath, 'a') as authFile:
        authFile.write(f"{userID} : {passWD} \n")
        credentialsLog(userID, logData='Account Created Successfully!')

    # To log the time of user account creation stopped.
    credentialsLog(logData='Create Account Completed!!', log_type='manually')


def logout() -> str:
    os.system('clear')


def startAuthentication():
    credentialsLog(logData="Authentication Started", log_type='manually')
    cprint("""Encrypted by echo's secure computing engine""", 'magenta')
    cprint("""Developed by QUASAR industries -Ajay""", 'magenta')
    cprint("----ECHO Secure Authentication Systems----\n", 'green', attrs=['bold'])

    login()
    credentialsLog(logData="Authentication stopped", log_type='manually')

try:
    startAuthentication()
except KeyboardInterrupt:
    credentialsLog(logData="Authentication FORCE stopped", log_type='manually')
    print("Exiting...")
    exit()


# Create a function to log the credentials for each session in a file including wrong passwords etc


