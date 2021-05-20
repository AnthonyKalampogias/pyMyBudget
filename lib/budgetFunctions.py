from tkinter import ttk, Text, Label, Entry, StringVar
import tkinter as tk
from tkinter.constants import BOTTOM, TOP
from .db import database # Import Database class
import re
import inspect

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

    #otherMonthView(monthWindow, tree, True, "") # Run first time for current month

    monthBtn = tk.Button(
        monthWindow, #obj
        command=lambda:otherMonthView(monthWindow, tree, False, directory.get()), # function
        textvariable= "", font="Calibri",text= "Search" , bg= "#3EA055", fg="white", height=1, width= 15 #style
    )
    monthBtn.pack(pady=15)
    
    
# Each function now calls popUpManager that will check which function called it and manage the values
def addMoney(root):
    try:
        popUpManager(root, "Added a new Income", "Insert amount")
    except:
        error(root, "You have to provide a number to the amount you want to add!!")

def addCost(root):
    try:
        popUpManager(root, "Add a new expense", "Add expense amount")
    except:
        error(root, "You have to provide a number to the amount you want to add!!")

def add2Piggy(root):
    try:
        popUpManager(root, "Add money to your Piggy bank", "Insert amount")
    except:
        error(root, "You have to provide a number to the amount you want to add to your Piggy bank!!")

def getPiggy(root):
    try:
        popUpManager(root, "Get money from your Piggy bank", "Insert amount")
    except:
        error(root, "You have to provide a number to the amount you want to get to your Piggy bank!!")

def oweMoney(root):
    try:
        popUpManager(root, "Add a new dept", "Insert amount")
    except:
        error(root, "You have to provide a number to the amount that you have to pay back!!")


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
        error(root,"Something went wront!\nPlease try again..")


def popUpManager(root, titleVal,labelVal):
    
    popUp = tk.Toplevel(root)
    popUp.title(titleVal)

    label=StringVar()
    label.set(labelVal)
    costLabelSet = Label(popUp, textvariable=label, height=4)
    costLabelSet.pack(side="left")

    userInput=StringVar(None)
    userInput.set(0)
    costValSet = Entry(popUp,textvariable=userInput,width=25)
    costValSet.pack(side="left")

    noteLabel=StringVar()
    noteLabel.set("Add Comment")
    noteLabelSet = Label(popUp, textvariable=noteLabel, height=4)
    noteLabelSet.pack(side="left")

    noteText=StringVar(None)
    noteTextSet = Entry(popUp,textvariable=noteText,width=50)
    noteTextSet.pack(side="left")

    # init values
    ## will only change one of these depending on what transaction the user wants
    income = 0.0
    outcome = 0.0
    toPiggy = 0.0
    fromPiggy = 0.0
    oweMoney = 0.0

    # Now we will get the name of the caller function with the 3 lines here
    # This will store the name of the function to callerFunction
    # which we check with a simple if elif to see which one it was
    # and after that store the amount the user gave to the according variable
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    callerFunction = str(calframe[1][3])
    
    addButton= tk.Button(
        popUp, #obj
        # We now call a function providing all the DB values as well as the string value of the caller function
        # This is because we now need a new check on the Text widget to occur AFTER the button is pressed and check if it's a float
        # if we just pass the data directly to the DB it has NOT updated the value from the text widget, we need a way to re-gain that !!
        command=lambda:addButtonCall(root, callerFunction, str(userInput.get()),income, outcome, toPiggy, fromPiggy, oweMoney, str(noteText.get())), # function
        textvariable= "", font="Calibri",text= "Add Amount" , bg= "#3EA055", fg="white", height=1, width= 15 #style
        )
    addButton.pack(pady= 25,padx= 15)


def addButtonCall(root, callerFunction, userInput, income, outcome, toPiggy, fromPiggy, oweMoney, note):
    # this function is only called from the popUpManager
    # the purpose is once the button is pressed to make it check the Text widgets value and send it to the DB after it checks it

    userInput = float(userInput) # Convert user input to float

    if isinstance(userInput, float):
        if callerFunction == "addMoney":
            income = userInput
        elif callerFunction == "addCost":
            outcome = userInput
        elif callerFunction == "add2Piggy":
            toPiggy = userInput
        elif callerFunction == "getPiggy":
            fromPiggy = userInput
        elif callerFunction == "oweMoney":
            oweMoney = userInput

    valueList = [income, outcome, toPiggy, fromPiggy, oweMoney]
    if not all(isinstance(x, float) for x in valueList):
        error(root, "You have to provide a number to the amount you want to add!!") 
        print(1/0)
    else:
        add2DB(root, income, outcome, toPiggy, fromPiggy, oweMoney, note)

def error(root, text):
    errorWindow = tk.Toplevel(root, width=300, height=300)
    errorWindow.title("Error")
    header = tk.Label(errorWindow, text = text).pack()
    exit_button = tk.Button(errorWindow, text="Exit", command=errorWindow.destroy)
    exit_button.pack(pady=20)