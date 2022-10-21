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
            credFile.write(f"{user}         ::         {logData} @ {TIME} on {DATE}\n")

    if logData is not None:
        if logData is type(str):
            with open(filePath, 'a') as credFile:
                credFile.write(f"{logData}       ::         @ {TIME} ::  on {DATE} \n")

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


def login():
    credentialsLog(logData='Login function started!', log_type='manually')
    userID = input("U-ID > ")
    passWD = input("Key-CODE > ")

    # Convert passWD to SHA25 and store it in usersData.txt file
    # Convert userID to SHA25 and store it in usersData.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()
    userID = hashlib.sha256(userID.encode()).hexdigest()

    filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/usersData.txt'
    searchFormat = f"{userID} : {passWD}"
    # Check the userID and passWD in usersData.txt file and return true if found else return false
    # with open(filePath) as authFile:
    #     for i in authFile.readlines():
    #         if i in searchFormat:
    #             print("Login Successful!")
    #             return True
    #         else:
    #             print("Login Failed!")
    #             #credentialsLog(userID, logData='Login Failed!')
    #             #credentialsLog(logData='Login function stopped', log_type='manually')
    #             return False

    file = open('/Users/ajay/PycharmProjects/echo/AUTHENTICATION/usersData.txt', 'r')

    for x in file:
        if searchFormat in x:
            print("Login Successful!")
        else:
            print("-Login Failed!")


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
        authFile.write(f"{userID} : {passWD}\n")
        credentialsLog(logData='Account Created Successfully!')

    # To log the time of user account creation stopped.
    credentialsLog(logData='Create Account Completed!!', log_type='manually')


def logout() -> str:
    os.system('clear')


def startAuthentication():
    # credentialsLog(logData="Authentication Started", log_type='manually')
    # cprint("""Encrypted by echo's secure computing engine""", 'magenta')
    # cprint("""Developed by QUASAR industries -Ajay""", 'magenta')
    cprint("----ECHO Secure Authentication Systems----\n", 'green', attrs=['bold'])

    login()

    credentialsLog(logData="Authentication stopped", log_type='manually')


try:
    startAuthentication()
except KeyboardInterrupt:
    credentialsLog(logData="Authentication FORCE stopped", log_type='manually')
    print("Exiting...")
    exit()


