from tkinter import ttk, Text
import tkinter as tk
from .db import database # Import Database class

import re

databaseConnector = database() # Database object

def monthView(root):

    monthWindow = tk.Toplevel(root, width=1100, height=500)
    monthWindow.title("Expenses Calendar for {}".format(databaseConnector.currentDate))
    
    # Setup the output Tree
    tree = ttk.Treeview(monthWindow, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Date")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Incomes")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Expenses")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Added to Piggy")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Got from Piggy")
    tree.column("#6", anchor=tk.CENTER)
    tree.heading("#6", text="Owed Money")
    tree.column("#7", anchor=tk.CENTER)
    tree.heading("#7", text="Comments")

    # Get records from DB
    MonthInfo = databaseConnector.getFromDB()
    for date in MonthInfo:
        tree.insert("", tk.END, values=date)
    
    tree.pack(fill="x")
    
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
    outcome= 0
    toPiggy= 0
    fromPiggy= 0
    oweMoney= 1000
    note = "You owe {} !".format(oweMoney)
    add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)


def otherMonthView(usrInput): 
    # Check if the user provided a string, if so give to the parser to check it
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
            match = re.match(r'.*([1-3][0-9]{3})', provided[1]) # Check if second part of the string is a year
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
    # Is used by every button that adds to the database
    income = databaseConnector.addToDatabase(
        income,  #Income
        outcome,  # Outcome
        toPiggy, # Piggy In/out
        fromPiggy,  # Owed Money
        oweMoney, # Note
        note
    )
    monthView(root)