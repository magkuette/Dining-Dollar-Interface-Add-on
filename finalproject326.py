"""
Group 4: Margaret Hermanto, Arnav Patel
Assignment: Final Project INST326
Date: 4_7_24

Challenges Encountered:

"""

import tkinter

# Need this for widgets
from tkinter import ttk

# Need this for notifications
from tkinter import messagebox

# Need this for current date
from datetime import date

class User:
    """
    """
    def __init__(self, master):
        # Parent widget
        self.master = master

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
        # Set up of input boxes for user info (ttk.Entry)
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
root = tkinter.Tk()

# Resolution of the window
root.geometry("1400x700")

# Instance of User
user_instance = User(root)

# Keeps Tkinter running
root.mainloop()
