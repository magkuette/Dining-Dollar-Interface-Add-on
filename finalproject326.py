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
from datetime import timedelta
import datetime

class User:
    """
    Creates a user object based on an acual program user.

    Attributes
    """

    dining_plan_total = 0
    dining_plan_current = 0
    day = date.today()
    sem_end = datetime.datetime(2024, 5, 17)

    def __init__(self, root):
        """
        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Args:
            root
        """
        self.root = root

        # Page 1 - user inputs their info
        self.p1 = tk.Frame(self.root)
        self.p1.pack()

        # Page 2 - user verifies their info
        self.p2 = tk.Frame(self.root)
        # self.p2.pack()

        # Call get_user_info function
        self.get_user_info()

        # Page 3 - user chooses what they want to do
        self.p3 = tk.Frame(self.root)
        # self.p3.pack()

        # Call verification function
        self.verification()

        # Page 4 - user gets outcome of spending reminders
        self.p4 = tk.Frame(self.root)

        self.spending_reminders()

        # page 5
        self.p5 = tk.Frame(self.root)

        self.threshold_reminders
        
        # self.p4.pack()

        # Call options function
        self.options()    

    def page_navigation(self, navigate):
        if navigate == "p1_to_p2":
            self.p1.forget()
            self.p2.pack()
        elif navigate == "p2_to_p1":
            self.p2.forget()
            self.p1.pack()
        elif navigate == "p2_to_p3":
            self.p2.forget()
            self.p3.pack()
        elif navigate == "p3_to_p1":
            self.p3.forget()
            self.p1.pack()
        elif navigate == "p3_to_p4":
            self.p3.forget()
            self.p4.pack()
        
    def spending_reminders(self):
        """ Calculates when to send reminders to user to spend dining dollars based on the current date.

        Returns:
            A tkinter messagebox with a message reminding users to spend dining dollars.
        """

        # Get current date using date.today()
        # This school year started on August 28, 2023
        # day = date.today()

        # Based on time between current date and date of dining dollar reset, program will send a notification (tkinter.messagebox.showinfo)

        # Ask user how often they want reminders with tkinter prompt (can be any number or set like 1, 7, 14, 30, 90)
        self.ask_reminder = ttk.Label(self.p4, text="How often would you like to receive reminders? (Every 1, 7, 14, 30, or 90 days)")
        self.ask_reminder.grid(row=1, column=1)

        self.ask_reminder_entry = ttk.Entry(self.p4)
        self.ask_reminder_entry.grid(row=2, column=1)
        reminder_days = self.ask_reminder_entry

        self.ask_reminder_enter = ttk.Button(self.p4, text="Enter") # maybe add command=lambda: get and then the variable with the answer

        # MIGHT NOT NEED
        # Check how far away current date is to date of dining dollar reset        
        num_days = self.numOfDays(self.day, self.sem_end) #should output a positive number
        # num_reminders = num_days / reminder_days
        #

        if reminder_days > num_days:
            self.error = tk.messagebox.showwarning(title="Error", message="Preferred number of days is larger than number of days left")

        elif reminder_days == "1":
            # Creates daily notifications
            pass
        
        elif reminder_days == "7":
            # Creates notifications for every 7 days
            pass
        
        elif reminder_days == "14":
            # Creates notifications for every 14 days
            pass

        elif reminder_days == "30":
            # Creates notifications for every 30 days
            pass

        elif reminder_days == "90":
            # Creates notifications for every 90 days
            pass

        # Collect that data and use it to set up date reminder system


    def threshold_reminders(self):
        """
        Calculates when dining dollar balance has reached certain thresholds based on the current date and date of dining dollar reset.

        Returns:
            A message letting users know what thresholds they have passed.
        """
        if User.dining_plan_total == 200:
            money_spent = User.dining_plan_current / User.dining_plan_total

            
   
    #Python3 program to find number of days between two given dates
    def numOfDays(date1, date2):
    #check which date is greater to avoid days output in -ve number
        if date2 > date1:   
            return (date2 - date1).days
        else:
            return (date1 - date2).days

    def suggested_spending(self):
        """
        Calculates a suggested average amount of money they could spend daily based on their remaining dining dollar balance.

        Returns:
            A message letting users know how much money they could spend daily to spend their dining dollar balance.
        """
        # Get current date using date.today()

        # Divide dining dollars balance by amount of days left till date of dining dollars reset
        pass

    def get_user_info(self):
        """ Gets user information including dining dollar plan, current dining dollar balance, as well as name.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            self.p2 after user clicks Proceed button.
        """
        # Name entry and label
        self.name = ttk.Entry(self.p1)
        user_name = self.name

        self.name_label = ttk.Label(self.p1, text="Name")
        # Place name entry and label on screen
        self.name.grid(row=1, column=2)
        self.name_label.grid(row=1, column=1)
        
        # Dining dollar entry and label
        self.dd_plan = ttk.Entry(self.p1)

        # Updates global dining plan value to be used in other methods
        User.dining_plan_total = self.dd_plan

        self.dd_plan_label = ttk.Label(self.p1, text="Dining Dollar Plan")
        # Place dining dollar entry and label on screen
        self.dd_plan.grid(row=2, column=2)
        self.dd_plan_label.grid(row=2, column=1)

        # Dining dollar balance entry and label
        self.balance = ttk.Entry(self.p1)

        # Updates global balance value to be used in other methods
        User.dining_plan_current = self.balance

        self.balance_label = ttk.Label(self.p1, text="Current Dining Dollar Balance")
        # Place dining dollar balance entry and label on screen
        self.balance.grid(row=3, column=2)
        self.balance_label.grid(row=3, column=1)

        # Proceed button leads to p2; figure out how to navigate to p2 later
        self.proceed = ttk.Button(self.p1, text="Proceed", command=lambda: self.page_navigation("p1_to_p2"))
        self.proceed.grid(row=4, column=2)

    def verification(self):
        """
        Asks user to verify the displayed information concerning them.

        Returns:
            Either self.p1 or self.p3, depending on the user's answer.
        """
        user_name = tk.StringVar()
        name = user_name.get()

        # Display name, dining dollar plan, and dining dollar balance with ttk.Label
        self.verify_label = ttk.Label(self.p2, text="Is this information correct?")
        self.verify_label.grid(row=1, column=1)
        # name
        name_label = tk.Label(self.p2, text="")
        name_label.grid(row=2, column=1)

        self.verify_name_label = ttk.Label(self.p2, text="")
        self.verify_name_label.grid(row=2, column=2)


        self.yes_verify = ttk.Button(self.p2, text="Yes", command=lambda: self.page_navigation("p2_to_p3"))
        self.yes_verify.grid(row=3, column=1)
        self.no_verify = ttk.Button(self.p2, text="No", command=lambda: self.page_navigation("p2_to_p1"))
        self.no_verify.grid(row=3, column=2)

    def options(self):
        """
        Displays a list of options the user can select.

        Returns:
            Requested option.
        """
        # Add buttons here about what users will be able to do
        self.ask = ttk.Label(self.p3, text="What would you like to do today?")
        self.ask.grid(row=1, column=1)

        # button 1
        self.spending_path = ttk.Button(self.p3, text="Create a spending reminder", command=lambda: self.page_navigation("p3_to_p4"))
        self.spending_path.grid(row=2, column=1)

        # button 2
        self.threshold_path = ttk.Button(self.p3, text="Show thresholds passed", command=lambda: self.page_navigation("p3_to_p5"))
        self.threshold_path.grid(row=2, column=2)

        # button 3
        self.suggested_path = ttk.Button(self.p3, text="Get a suggested spending recommendation")
        self.suggested_path.grid(row=2, column=3)

        # button 4
        self.log_out_path = ttk.Button(self.p3, text="Log out", command=lambda: self.page_navigation("p3_to_p1"))
        self.log_out_path.grid(row=2, column=4)  

def main():
    """
    Displays information to the user using User functions

    Returns:
        Message of information user requested.
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
