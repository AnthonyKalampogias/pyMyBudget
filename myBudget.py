from tkinter import font
from tkinter.constants import COMMAND
from lib.budgetFunctions import * # Import Apps functionality 
import getpass
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("PyMyBudget - The python Expenses Tracker")

    root.geometry('1280x720')

    # Main page header
    header = tk.Label(root, text = "\n      Hello "+ getpass.getuser() + " what are we doing today?", font=("Garamond",20))
    header.pack()

    # View Month button
    logsBtnText = tk.StringVar()
    logsBtn = tk.Button(
        root, #obj
        command=lambda:monthView(root), # function
        textvariable= logsBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    logsBtnText.set("View your Month")
    logsBtn.pack(pady= 10)

    # Add Income button
    inBtnText = tk.StringVar()
    inBtn = tk.Button(
        root, #obj
        command=lambda:addMoney(root), # function
        textvariable= inBtnText, font="Calibri", bg= "#3EA055", fg="white", height=2, width= 25 #style
    )
    inBtnText.set("Add Money")
    inBtn.pack(pady= 10)


    # Outcome button
    outBtnText = tk.StringVar()
    outBtn = tk.Button(
        root, #obj
        command=lambda:addCost(root), # function
        textvariable= outBtnText, font="Calibri", bg= "#FF7F50", fg="white", height=2, width= 25 #style
    )
    outBtnText.set("Add Bill")
    outBtn.pack(pady= 10)


    # Add to piggy button
    piginBtnText = tk.StringVar()
    piginsBtn = tk.Button(
        root, #obj
        command=lambda:add2Piggy(root), # function
        textvariable= piginBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    piginBtnText.set("Add Money to your Piggy")
    piginsBtn.pack(pady= 10)


    # Get from piggy button
    pigoutBtnText = tk.StringVar()
    pigoutBtn = tk.Button(
        root, #obj
        command=lambda:getPiggy(root), # function
        textvariable= pigoutBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    pigoutBtnText.set("Get Money from your piggy")
    pigoutBtn.pack(pady= 10)


    # Add owed button
    oweBtnText = tk.StringVar()
    oweBtn = tk.Button(
        root, #obj
        command=lambda:oweMoney(root), # function
        textvariable= oweBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
    )
    oweBtnText.set("Add Money you owe")
    oweBtn.pack(pady= 10)

    root.mainloop()

if __name__ == "__main__":
    main()