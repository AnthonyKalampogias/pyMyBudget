from tkinter import font
import tkinter as tk
from .db import database # Import Database class
import re

databaseConnector = database() # Database object

def monthView(root):
    # newWindow = tk.Toplevel(root)
    # month2Query = otherMonthView("MAYkk ") # Can't parse, no year
    month2Query = otherMonthView("MAYkk 2021") # Will parse, works!
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
    # newWindow = tk.Toplevel(root)
    # Temp Values 
    income= 150
    outcome= 0
    toPiggy= 0
    fromPiggy= 0
    oweMoney= 0
    note = "Birthday Gift"
    add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)

def addCost(root):
    # Temp Values 
    income= 0
    outcome= 150
    toPiggy= 0
    fromPiggy= 0
    oweMoney= 0
    note = "Hotel checkout"
    add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)

def add2Piggy(root):
     # Temp Values 
    income= 0
    outcome= 0
    toPiggy= 100
    fromPiggy= 0
    oweMoney= 0
    note = "Added to piggy!"
    add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)

def getPiggy(root):
     # Temp Values 
    income= 0
    outcome= 0
    toPiggy= 0
    fromPiggy= 15
    oweMoney= 0
    note = "Got Money from your piggy!"
    add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)

def oweMoney(root):
     # Temp Values 
    income= 0
    outcome= 150
    toPiggy= 0
    fromPiggy= 0
    oweMoney= 1000
    note = "You owe {} !".format(oweMoney)
    add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)


def otherMonthView(usrInput): # Check if the user provided a string, if so give to the parser to check it
    parsedMonth = ""
    if usrInput != "":
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


def add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note):
    # Is be used by every button that adds to the table
    income = databaseConnector.addToDatabase(
        income,  #Income
        outcome,  # Outcome
        toPiggy, # Piggy In/out
        fromPiggy,  # Owed Money
        oweMoney, # Note
        note
    )
    monthView(root)