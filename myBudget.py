from tkinter import font
from tkinter.constants import COMMAND
from lib.budgetFunctions import * # Import Apps functionality 
import getpass
import tkinter as tk

def btnTrigger(btnHandler):
    #btnTrigger is called from the functions at their start and finish to enable/disable the other buttons
    logsBtn["state"] = "disabled"
    inBtn["state"] = "disabled"
    outBtn["state"] = "disabled"
    piginsBtn["state"] = "disabled"
    pigoutBtn["state"] = "disabled"
    oweBtn["state"] = "disabled"
    # Switches in python aren't actual switches, they map the available options and 
    # by "getting" one you just pick that but it has executed each option so if I leave them as function calls its like I press every button
    # So I just turn them to a string and after getting that specific string that has the desired function execute it
    switch = {
        1: "monthView(root)",
        2: "addMoney(root)",
        3: "addCost(root)",
        4: "add2Piggy(root)",
        5: "getPiggy(root)",
        6: "oweMoney(root)"
    }
    func = switch.get(btnHandler)
    exec(func)
    logsBtn["state"] = "normal"
    inBtn["state"] = "normal"
    outBtn["state"] = "normal"
    piginsBtn["state"] = "normal"
    pigoutBtn["state"] = "normal"
    oweBtn["state"] = "normal"
    return func

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
    command=lambda:btnTrigger(1), # function
    textvariable= logsBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
)
logsBtnText.set("View your Month")
logsBtn.grid(column=1,row=2,pady= 10)

# Add Income button
inBtnText = tk.StringVar()
inBtn = tk.Button(
    root, #obj
    command=lambda:btnTrigger(2), # function
    textvariable= inBtnText, font="Calibri", bg= "#3EA055", fg="white", height=2, width= 25 #style
)
inBtnText.set("Add Money")
inBtn.grid(column=1,row=3,pady= 10)


# Outcome button
outBtnText = tk.StringVar()
outBtn = tk.Button(
    root, #obj
    command=lambda:btnTrigger(3), # function
    textvariable= outBtnText, font="Calibri", bg= "#FF7F50", fg="white", height=2, width= 25 #style
)
outBtnText.set("Add Bill")
outBtn.grid(column=1,row=4,pady= 10)


# Add to piggy button
piginBtnText = tk.StringVar()
piginsBtn = tk.Button(
    root, #obj
    command=lambda:btnTrigger(4), # function
    textvariable= piginBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
)
piginBtnText.set("Add Money to your Piggy")
piginsBtn.grid(column=1,row=5,pady= 10)


# Get from piggy button
pigoutBtnText = tk.StringVar()
pigoutBtn = tk.Button(
    root, #obj
    command=lambda:btnTrigger(5), # function
    textvariable= pigoutBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
)
pigoutBtnText.set("Get Money from your piggy")
pigoutBtn.grid(column=1,row=6,pady= 10)


# Add owed button
oweBtnText = tk.StringVar()
oweBtn = tk.Button(
    root, #obj
    command=lambda:btnTrigger(6), # function
    textvariable= oweBtnText, font="Calibri", bg= "#737CA1", fg="white", height=2, width= 25 #style
)
oweBtnText.set("Add Money you owe")
oweBtn.grid(column=1,row=7,pady= 10)

root.mainloop()