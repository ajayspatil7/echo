import hashlib


def login() -> str:

    userID = input("UserID > ")
    passWD = input("PassKey > ")

    # Convert passWD to SHA25 and store it in usersData.txt.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()
    filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/usersData.txt'

    # Check if the userID and passWD are in the file
    with open(filePath, 'r') as authFile:
        for line in authFile:
            if userID in line and passWD in line:
                print("Login Successful!!")
                return True
            else:
                print("Username or Password is incorrect")
                return False


def createAccount() -> str:

    userID = input("UserID > ")
    passWD = input("PassKey > ")

    # Convert passWD to SHA25 and append it in usersData.txt.txt file
    passWD = hashlib.sha256(passWD.encode()).hexdigest()

    filePath = '/Users/ajay/PycharmProjects/echo/AUTHENTICATION/usersData.txt'

    with open(filePath, 'a') as authFile:
        authFile.write(f"{userID} : {passWD} \n")


def logout() -> str:
    pass

