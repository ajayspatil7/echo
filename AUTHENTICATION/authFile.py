# This is authentication file responsible to keep track of the user's credentials

# Create a function to convert string to SHA-256 value and hash value to string
# This function will be used to convert the password to hash value and store it in the file
# This function will also be used to convert the hash value to string and compare it with the user's input


# Create a function to add a new user to the file
# This function will be used to add a new user to the file
# This function will also be used to add the user's credentials to the file

# Class to handle the authentication process
# This class will be used to handle the authentication process
# This class will also be used to handle the user's credentials

class Authentication:
    def __init__(self):
        self.password = None
        self.username = None
        self.file = open("/Users/ajay/PycharmProjects/echo/AUTHENTICATION/authFile.txt", "r+")
        self.fileContent = self.file.readlines()
        self.file.close()

    def authenticate(self):
        # Authenticate the user
        # This function will be used to authenticate the user
        # This function will also be used to authenticate the user's credentials
        self.file = open("/Users/ajay/PycharmProjects/echo/AUTHENTICATION/authFile.txt", "r+")
        self.fileContent = self.file.readlines()
        self.file.close()

        # Get the user's input
        self.username = input("Username: ")
        self.password = input("Password: ")

        # Check if the user's input is in the file
        if f"{self.username}:{self.password}" in self.fileContent:
            print("Authentication successful")
            return True
        else:
            print("Authentication failed")
            return False

    def addNewUser(self):
        # Add a new user to the file
        # This function will be used to add a new user to the file
        # This function will also be used to add the user's credentials to the file
        self.file = open("/Users/ajay/PycharmProjects/echo/AUTHENTICATION/authFile.txt", "r+")
        self.fileContent = self.file.readlines()
        self.file.close()

        # Get the user's input
        self.username = input("Username: ")
        self.password = input("Password: ")

        # Check if the user's input is in the file
        if f"{self.username}:{self.password} " in self.fileContent:
            print("User already exists")
        else:
            self.file = open("/Users/ajay/PycharmProjects/echo/AUTHENTICATION/authFile.txt", "a")
            self.file.write(f"{self.username}:{self.password}")
            self.file.close()
            print("User added successfully")

auth = Authentication()


