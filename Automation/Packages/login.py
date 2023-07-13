#####################################################################################################################################################################################
# File:         login.py
# Version:      1.0
# Author:       Aldo_Fonts
# Description:  The current file has the functions and the tools to login on Jira
#####################################################################################################################################################################################
# Package(s)
import os
# Function(s)
def getCredentials():
    # Read the file "credentials.txt" wich has the user and password to use Jira
    with open(os.getcwd() + "/files/credentials.txt",'r') as passwordFile:
        lines = [] 
        for line in passwordFile:
            lines.append(line)
    # Delete the line break for the user
    user = lines[0].split("\n")
    # Put the user and the password in variables
    user = user[0]
    password = lines[1]
    # Close the file
    passwordFile.close()
    # It returns the password and the user, they will be used later
    return user, password

def putCredentials(user, password):
    return

def saveCredentials(remember, user, password):
    # If the user decided to save the credentials, it will be saved in the file "credentials.txt"
    if(remember == True):
        # Rewrite the file "credentials.txt" erasing the last saved credentails
        with open(os.getcwd() + "/files/credentials.txt",'w') as passwordFile:
            # Write the current credentials in the file
            passwordFile.write(user + "\n")
            passwordFile.write(password)
        # Close the file
        passwordFile.close()

