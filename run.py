# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('TraktorDb')

def add_traktors():
    """
    gets new traktor data from the user
    """
    while True:
        print("Enter a new traktor to the system")
        print("Data entered should be seperated by comma and a space in this format:")
        print("<name>, <year>, <color>, <model>\nExample: \"Ford, 2001, blue, F-310\"")

        data_str = input("Enter the data: ")

        traktors_data = data_str.split(", ")

        if validate_data(traktors_data):
            print("Data enterd is valid.")
            break
    
    return traktors_data

def validate_data(values):
    """
    Checks if there are 4 strings,
    raise error if there are more or less strings
    """

    try:
        if len(values) != 4:
            raise ValueError(
                f"Four values excepted, {len(values)} was entered."
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    return True

data = add_traktors()