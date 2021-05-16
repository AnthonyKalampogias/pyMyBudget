import sqlite3
from datetime import datetime


class database:

    def __init__(self):
        self.connectionString = sqlite3.connect("budget.db")
        self.cursor = self.connectionString.cursor()
        self.currentDate = datetime.now().strftime('%B') + str(datetime.now().year)
        # Check if the current month table exists
        # if the count is not 1, then table doesn't exists
        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+ self.currentDate +"' ")
        if self.cursor.fetchone()[0]!=1 :
            self.cursor.execute("CREATE TABLE "+ self.currentDate + " (date TEXT, income REAL, outcome REAL, toPiggy REAL, fromPiggy REAL, oweMoney REAL, note TEXT)")
        
    def addToDatabase(self, income, outcome, toPiggy, fromPiggy, oweMoney, note):
        self.cursor.execute("INSERT INTO "+ self.currentDate +" VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (   str(datetime.now().day)+'/'+str(datetime.now().month), 
                        income, 
                        outcome, 
                        toPiggy,
                        fromPiggy,
                        oweMoney,
                        note
                    )
                )
        self.connectionString.commit()
    
    def getFromDB(self, requestedDate = "", toQuery = ""):
        
        if requestedDate == "": # If there is not a date provided check for current month
            requestedDate = self.currentDate

        if (toQuery == ""):
            self.cursor.execute('SELECT * FROM ' + requestedDate )
            data = self.cursor.fetchall()
        else:
            self.cursor.execute("select "+ toQuery +" from "+ requestedDate)
            data = self.cursor.fetchall()
        return data