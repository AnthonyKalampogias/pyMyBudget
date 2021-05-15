from tkinter import font
import tkinter as tk
from .db import database # Import Database class
import re

databaseConnector = database() # Database object

def monthView(root):
    # newWindow = tk.Toplevel(root)
    month2Query = otherMonthView(root, "MAYkk ") # Can't parse, no year
    month2Query = otherMonthView(root, "MAYkk 2021") # Will parse, works!
    MonthInfo = databaseConnector.getFromDB(month2Query)
    month = tk.Label(root, text= MonthInfo)
    print("______________________________________________")
    for date in MonthInfo:
        print("| ", end = '')
        for value in date:
            print(str(value)+" | ", end = '')
        print()
    print("______________________________________________")
    
    
def addMoney(root):
    print("dababby??")

def addCost(root):
    print("dababby??")

def add2Piggy(root):
    print("dababby??")

def getPiggy(root):
    print("dababby??")

def oweMoney(root):
    print("dababby??")


def otherMonthView(root,usrInput):
    parsedMonth = dateParse(usrInput)
    return parsedMonth

def dateParse(provided):
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    try:
        if provided.find(" "):
            provided = provided.split(" ")

            # Check Year
            match = re.match(r'.*([1-3][0-9]{3})', provided[1]) # Check if second part of the string was a year
            if match is None:
                print(1/0) # Force to go to exception block

            # Check Month 
            provided[0] = provided[0].lower()
            correctMonth = False # Flag to check at the end of the for loop if the parser found a month
            for month in months:
                if month in provided[0]:
                    provided[0] = month
                    correctMonth = True
                    break
            if not correctMonth:
                print(1/0)

            return str(provided[0]+provided[1])

        else:
            print(1/0)

    except:
        print("Something went wrong...\nPlease check your format and try again...\nExample: For may of 2021 type 'may 2021' !!")
        return("")