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
        textvariable= "", font="Calibri",text= "Search" , bg= "#3EA055", fg="white", height=2, width= 15 #style
    ).pack()
    
    
def addMoney(root):
    incomeWindow = tk.Toplevel(root)
    incomeWindow.title("Added a new Income")
    
    incomeLabel=StringVar()
    incomeLabel.set("Insert amount")
    incomeLabelSet = Label(incomeWindow, textvariable=incomeLabel, height=4)
    incomeLabelSet.pack(side="left")

    incomeVal=StringVar(None)
    incomeVal.set(0)
    incomeValSet = Entry(incomeWindow,textvariable=incomeVal,width=25)
    incomeValSet.pack(side="left")

    noteLabel=StringVar()
    noteLabel.set("Add Comment")
    noteLabelSet = Label(incomeWindow, textvariable=noteLabel, height=4)
    noteLabelSet.pack(side="left")

    noteText=StringVar(None)
    noteTextSet = Entry(incomeWindow,textvariable=noteText,width=50)
    noteTextSet.pack(side="left",pady=50)
    
    outcome = 0.0
    toPiggy = 0.0
    fromPiggy = 0.0
    oweMoney = 0.0

    try:
        incomeBtn = tk.Button(
            incomeWindow, #obj
            command=lambda:add2DB(root, float(incomeVal.get()), outcome, toPiggy, fromPiggy, oweMoney, str(noteText.get())), # function
            textvariable= "", font="Calibri",text= "Add Amount" , bg= "#3EA055", fg="white", height=2, width= 15 #style
            )
        incomeBtn.pack(padx= 50, pady=50)
    except:
        error(root, "You have to provide a number to the amount you want to add!!")

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
        error(root,"Something went wrong...\nPlease check your format and try again...\nExample: For may of 2021 type 'may 2021' !!")
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


def add2DB(root, income: float, outcome: float, toPiggy: float, fromPiggy: float, oweMoney: float, note: str):
    try:
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
    except:
        error(root,"You have to provide a number to the amount you want to add!!")

def error(root, text):
    errorWindow = tk.Toplevel(root, width=300, height=300)
    errorWindow.title("Error")
    header = tk.Label(errorWindow, text = text).pack()
    exit_button = tk.Button(errorWindow, text="Exit", command=errorWindow.destroy)
    exit_button.pack(pady=20)