"""
Group 4: Margaret Hermanto, Arnav Patel
Assignment: Final Project INST326
Date: 4_7_24

Challenges Encountered:

"""

import tkinter as tk

# Need this for widgets
from tkinter import ttk

# Need this for notifications
from tkinter import messagebox

# Need this for current date
from datetime import date

class User:
    """
    """
    def __init__(self, root):
        self.root = root

        # Page 1 - user inputs their info
        self.p1 = tk.Frame(self.root)
        self.p1.pack()

        # Page 2 - user verifies their info
        self.p2 = tk.Frame(self.root)
        self.p2.pack()

        # Call get_user_info function
        self.get_user_info()

        # Page 3 - user chooses what they want to do
        self.p3 = tk.Frame(self.root)
        self.p3.pack()

        # Call verification function
        self.verification()

        # Page 4 - user gets outcome from what they wanted to do
        self.p4 = tk.Frame(self.root)
        self.p4.pack()

        # Call options function
        self.options()

        # Set up of the available buttons (ttk.Button), input boxes (ttk.Entry), etc.
        pass
        
    def spending_reminders(self):
        """
        Sends reminders to user to spend dining dollars based on the current date.
        """
        # Get current date using date.today()

        # Check how far away current date is to date of dining dollar reset

        # Based on time between current date and date of dining dollar reset, program will send a notification (tkinter.messagebox.showinfo)
        pass

    def threshold_reminders(self):
        """
        Informs users when their dining dollars balance reaches a certain threshold.
        """
        # Program will send a notification (tkinter.messagebox.showinfo)
        pass

    def suggested_spending(self):
        """
        Gives users a suggested average amount of money they could spend daily based on their remaining dining dollar balance.
        """
        # Get current date using date.today()

        # Divide dining dollars balance by amount of days left till date of dining dollars reset
        pass

    def get_user_info(self):
        """
        Gets user information including dining dollar plan, current dining dollar balance, as well as name.
        ^ (the name is irrelevant; it's just if we wanna be like 'Hey [name] you have this many dining dollars in your account' or something) <- just an idea
        """
        # Name entry
        self.name_entry = ttk.Entry(self.p1)
        self.name_entry.pack()
        
        # Enter dining dollar plan
        self.dd_plan = ttk.Entry(self.p1)
        self.dd_plan.pack()

        # Enter current dining dollar balance
        self.balance = ttk.Entry(self.p1)
        self.balance.pack()

        # Proceed button leads to p2; figure out how to navigate to p2 later
        self.proceed = ttk.Button(self.p1, text="Proceed", command=self.p2)
        self.proceed.pack()

    def verification(self):
        """
        Asks user to verify the displayed information concerning them.
        """
        # Display name, dining dollar plan, and dining dollar balance with ttk.Label

        self.yes_verify = ttk.Button(self.p2, text="Yes", command=self.p3)
        self.no_verify = ttk.Button(self.p2, text="No", command=self.p1)

    def options(self):
        """
        Displays a list of options the user can select in order 
        """
        # Add buttons here about what users will be able to do
        pass
        

def main():
    """
    Displays information to the user using User functions
    """
    pass
    

if __name__ == "__main__":
    """
    Calls the main function
    """
    pass

# Keeps Tkinter running
root = tk.Tk()

# Resolution of the window
root.geometry("1400x700")

# Instance of User
user_instance = User(root)

# Keeps Tkinter running
root.mainloop()
