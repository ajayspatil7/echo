import hashlib
import os
from termcolor import *
from datetime import datetime
from tabulate import tabulate

# This function is used to log the credentials with time and date at specific events.
# The user parameter is used to log the user who is performing the action.
# The logData parameter is used to log the data of the action performed by the user. Eg; what command was executed.
# The log_type parameter is used to log the type of log. Eg; manually or automatically.


def credentialsLog(user=None, logData=None, log_type=None):
    DATE = datetime.today().strftime('%Y-%m-%d')
    TIME = datetime.today().strftime('%I:%M:%S:%p')
    filePath = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/userLogs.txt'

    # To monitor login and logout activities
    if user and logData is not None:
        timeStamp = str(datetime.today()).split('.')[0]
        filePath = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/userLogs.txt'
        with open(filePath, 'a') as credFile:
            # Append to the file with exact width spacing
            credFile.write(f"{user:20s}::{logData:20s} -> {TIME:5s} -> {DATE}\n")

    # To monitor the start and stop of authentication
    if logData is not None:
        if logData is type(str):
            with open(filePath, 'a') as credFile:
                credFile.write(f"{logData:20s} @ {TIME:20s} -> {DATE} \n")

    if str(log_type).lower() == 'manually':
        entryExitLog = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/authEntryExitLogs.txt'
        with open(entryExitLog, 'a') as credFile:
            credFile.write(f"{logData:35s} @ {TIME:10s} -> {DATE} \n")
    else:
        pass

    # Log the data in table format
    with open(filePath, 'r') as data:
        data = data.readlines()
        data = [i.split('::') for i in data]
        tabulatedLog = tabulate(data, headers=['User', 'Log Data', 'Time Stamp'], tablefmt='fancy_grid')


def login() -> bool:
    credentialsLog(logData='<Login function started!>', log_type='manually')
    userID = input("U-ID > ")
    passWD = input("Key-CODE > ")

    # Convert passWD to SHA25 and store it in usersData.txt file
    # Convert userID to SHA25 and store it in usersData.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()
    userID = hashlib.sha256(userID.encode()).hexdigest()

    filePath = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/usersData.txt'
    # Check the userID and passWD in usersData.txt file and return true if found else return false
    with open(filePath) as authFile:
        for i in authFile.readlines():
            if i.split(":")[0].strip() == userID and i.split(":")[1].strip() == passWD:
                credentialsLog(user=userID, logData='Login Successful')
                print(True)
                credentialsLog(logData='<Login function completed!>', log_type='manually')
                return True

            # login
        else:
            credentialsLog(user=userID, logData='Login Failed')
            print(False)
            credentialsLog(logData='<Login function completed!>', log_type='manually')
            return False
    # incorrect creds

        # for i in authFile.readlines():
        #     temp = i.split(':')
        #     if userID == temp[0] and passWD == temp[1].strip():
        #         credentialsLog(user=userID, logData='Login Successful!')
        #         print("Found")
        #         return True
        #     else:
        #         credentialsLog(user=userID, logData='Login Failed!')
        #         print("Not Found")
        #         return False

            # if userID in i and passWD in i:
            #     credentialsLog(user=userID, logData='Login Successfull!')
            #     print("Login Successfull!")
            #     return True
            # else:
            #     print("Login Failed!")
            #     return False\


def createAccount() -> bool:
    credentialsLog(logData='<Create Account Started>', log_type="manually")

    userID = input("UserID > ")
    passWD = input("PassKey > ")

    # Convert passWD & userID to SHA25 and append it in usersData.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()
    userID = hashlib.sha256(userID.encode()).hexdigest()

    # Path to store the data
    filePath = '/Users/ajay/PycharmProjects/echo/ECHOV1LOGS/usersData.txt'

    with open(filePath, 'a') as authFile:
        authFile.write(f"{userID} : {passWD}\n")
        cprint(f"Account Created Successfully!", 'green')
        credentialsLog(logData='<Account Created Successfully!>')

    # To log the time of user account creation stopped.
    credentialsLog(logData='<Create Account Completed!!>', log_type='manually')
    return True


def logout() -> str:
    credentialsLog(logData='<Logout function started!>', log_type='manually')
    os.system('clear')
    credentialsLog(logData='<Logout function completed!>', log_type='manually')


authenticationMap = {
    'login': login,
    'create': createAccount,
    'logout': logout
}


def startAuthentication():
    credentialsLog(logData="<Authentication Started>", log_type='manually')
    cprint("----ECHO Secure Authentication Systems----\n", 'green', attrs=['bold'])
    cprint("1. Login\n2. Create Account\n3. Exit\n", 'cyan', attrs=['underline'])

    count = 0
    choice = input("Type your choice (login for Login) > ")

    while choice != 'exit':
        if choice in authenticationMap.keys():
            authenticationMap[choice]()
            break
        else:
            cprint("Invalid Choice!!", 'red', attrs=['bold'])
            count += 1
            if count == 3:
                cprint("Too many invalid choices! Exiting...", 'red', attrs=['bold'])
                break
        choice = input("Type your choice (login for Login) > ")

    choice = choice.lower()
    # Dictonary comprehension to call the values
    if choice in authenticationMap.keys():
        authenticationMap[choice]()

    credentialsLog(logData="<Authentication stopped>", log_type='manually')


def initiateAuthentication() -> bool:
    try:
        startAuthentication()
    except KeyboardInterrupt:
        credentialsLog(logData="<Authentication FORCE stopped>", log_type='manually')
        cprint("Authentication Stopped!", 'red', attrs=['bold'])
        print("\nExiting...")
        exit()


