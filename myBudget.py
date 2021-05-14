from tkinter import font
from lib.db import database # Import Database class
from lib.budgetFunctions import * # Import Apps functionality 
import getpass
import tkinter as tk

def main():

    databaseConnector = database() # Database object
    root = tk.Tk()
    root.title("PyMyBudget - The python Expenses Tracker")
    
    root.geometry('1280x720')

    # Main page header
    header = tk.Label(root, text = "\n      Hello "+ getpass.getuser() + " what are we doing today?", font=("Garamond",20))
    header.grid(column=0,row=0)

    # View Month button
    logsBtnText = tk.StringVar()
    logsBtn = tk.Button(
        root, #obj
        command=lambda:monthView(), # function
        textvariable= logsBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    logsBtnText.set("View your Month")
    logsBtn.grid(column=1,row=2)

    # Add Income button
    inBtnText = tk.StringVar()
    inBtn = tk.Button(
        root, #obj
        command=lambda:addMoney(), # function
        textvariable= inBtnText, font="Calibri", bg= "#3EA055", fg="white", height=2, width= 25 #style
    )
    inBtnText.set("Add Money")
    inBtn.grid(column=1,row=3)


    # Outcome button
    outBtnText = tk.StringVar()
    outBtn = tk.Button(
        root, #obj
        command=lambda:addCost(), # function
        textvariable= outBtnText, font="Calibri", bg= "#FF7F50", fg="white", height=2, width= 25 #style
    )
    outBtnText.set("Add Bill")
    outBtn.grid(column=1,row=4)
    

    # Add to piggy button
    piginBtnText = tk.StringVar()
    piginsBtn = tk.Button(
        root, #obj
        command=lambda:add2Piggy(), # function
        textvariable= piginBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    piginBtnText.set("Add Money to yout Piggy")
    piginsBtn.grid(column=1,row=5)
    

    # Get from piggy button
    pigoutBtnText = tk.StringVar()
    pigoutBtn = tk.Button(
        root, #obj
        command=lambda:getPiggy(), # function
        textvariable= pigoutBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    pigoutBtnText.set("Get Money from your piggy")
    pigoutBtn.grid(column=1,row=6)
    

    # Add owed button
    oweBtnText = tk.StringVar()
    oweBtn = tk.Button(
        root, #obj
        command=lambda:oweMoney(), # function
        textvariable= oweBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    oweBtnText.set("Add Money you owe")
    oweBtn.grid(column=1,row=7)

    root.mainloop()

if __name__=="__main__":
    main()