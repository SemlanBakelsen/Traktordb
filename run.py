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
    print("Enter a new traktor to the system")
    print("Data entered should be seperated by commas in this format:")
    print(f"<name>, <year>, <color>, <model>\nExample: \"Ford, 2001, blue, F-310\"")

    data_str = input("Enter the data: ")
    print(f"the data enterer is \"{data_str}\"")

add_traktors()