from tkinter import ttk, Text, Label, Entry, StringVar
import tkinter as tk
from .db import database # Import Database class
import re

databaseConnector = database() # Database object

def monthView(root):

    monthWindow = tk.Toplevel(root, width=900, height=500)
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

    tree.pack(fill="x")

    monthLabel=StringVar()
    monthLabel.set("Search records from other months ")
    labelDir=Label(monthWindow, textvariable=monthLabel, height=4)
    labelDir.pack(side="left")

    directory=StringVar(None)
    dirname=Entry(monthWindow,textvariable=directory,width=50)
    dirname.pack(side="left")

    otherMonthView(monthWindow, tree, True, "") # Run first time for current month

    monthBtn = tk.Button(
        monthWindow, #obj
        command=lambda:otherMonthView(monthWindow, tree, False, directory.get()), # function
        textvariable= "", font="Calibri",text= "Search" , bg= "#3EA055", fg="white", height=2, width= 25 #style
    ).pack()
    
    
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


def otherMonthView(root, tree, initFLG, usrInput = ""): 
    # Check if the user provided a string, if so give to the parser to check it
    parsedMonth = ""
    if usrInput != "":
        parsedMonth = dateParse(usrInput)

    if parsedMonth == "" and not initFLG:
        errorWindow = tk.Toplevel(root, width=300, height=300)
        header = tk.Label(errorWindow, text = "Something went wrong...\nPlease check your format and try again...\nExample: For may of 2021 type 'may 2021' !!").pack()
        exit_button = tk.Button(errorWindow, text="Exit", command=errorWindow.destroy)
        exit_button.pack(pady=20)
    else:
        MonthInfo = databaseConnector.getFromDB(parsedMonth,"")
        for date in MonthInfo:
            tree.insert("", tk.END, values=date)


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