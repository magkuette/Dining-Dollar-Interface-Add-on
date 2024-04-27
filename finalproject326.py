"""
Group 4: Margaret Hermanto, Arnav Patel
Assignment: Final Project INST326
Date: 4_7_24

Challenges Encountered:

"""
# last updated 4/27/24 657 pm by Maggie
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
    """ Creates a user object based on an actual program user.

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
        """
        self.root = root

        # Page 1 - get_user_info()
        self.p1 = tk.Frame(self.root)
        self.p1.pack()

        # Page 2 - verification()
        self.p2 = tk.Frame(self.root)

        # Stores entry information for future label configuration
        self.name_var = tk.StringVar()
        self.dd_var = tk.StringVar()
        self.balance_var = tk.StringVar()
        self.reminder_var = tk.StringVar()

        # Call get_user_info function (only need to call this first function because the rest of the functions will be called later on throughout the code through buttons)
        self.get_user_info()

        # Page 3 - options()
        self.p3 = tk.Frame(self.root)

        # Page 4 - user gets outcome of spending reminders
        self.p4 = tk.Frame(self.root)

        # page 5
        self.p5 = tk.Frame(self.root)
        
        # page 6
        self.p6 = tk.Frame(self.root)

# May or may not need but don't delete (it's not in the way of the code rn)
# rn it seems like it's better to navigate pages by directly setting command equal to a function in buttons
    def page_navigation(self, navigate):
        """ Tells the program what pages to go to when a user clicks a button

        Driver: Margaret Hermanto
        Navigator: Arnav Patel
        """
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
        elif navigate == "p3_to_p5":
            self.p3.forget()
            self.p5.pack()
        elif navigate == "p3_to_p6":
            self.p3.forget()
            self.p6.pack()
        
    def spending_reminders(self):
        """ Calculates when to send reminders to user to spend dining dollars based on the current date.

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            A tkinter messagebox with a message reminding users to spend dining dollars.
        """
        # page navigation
        self.p3.forget()
        self.p4.pack()
        # Get current date using date.today()
        # This school year started on August 28, 2023
        # day = date.today()

        # Based on time between current date and date of dining dollar reset, program will send a notification (tkinter.messagebox.showinfo)

        # Ask user how often they want reminders with tkinter prompt (can be any number or set like 1, 7, 14, 30, 90)
        self.ask_reminder = ttk.Label(self.p4, text="How often would you like to receive reminders? (Every 1, 7, 14, 30, or 90 days)")
        self.ask_reminder.grid(row=1, column=1)

        # Enter reminder frequency
        # what the user inputted is stored into self.reminder_var (replace future reminder_days with self.reminder_var. unless u set it equal to that that might work)
        self.ask_reminder_entry = ttk.Entry(self.p4, textvariable=self.reminder_var)
        self.ask_reminder_entry.grid(row=2, column=1)

        self.ask_reminder_enter = ttk.Button(self.p4, text="Enter")

        # MIGHT NOT NEED
        # Check how far away current date is to date of dining dollar reset        
        # num_days = self.numOfDays(self.day, self.sem_end) #should output a positive number
        # num_reminders = num_days / reminder_days
        #

        # Commented out because this was not allowing the GUI to run; figure out later

        # if reminder_days > num_days:
        #     self.error = tk.messagebox.showwarning(title="Error", message="Preferred number of days is larger than number of days left")

        # elif reminder_days == "1":
        #     # Creates daily notifications
        #     pass
        
        # elif reminder_days == "7":
        #     # Creates notifications for every 7 days
        #     pass
        
        # elif reminder_days == "14":
        #     # Creates notifications for every 14 days
        #     pass

        # elif reminder_days == "30":
        #     # Creates notifications for every 30 days
        #     pass

        # elif reminder_days == "90":
        #     # Creates notifications for every 90 days
        #     pass

        # Collect that data and use it to set up date reminder system


    def threshold_reminders(self):
        """ Calculates when dining dollar balance has reached certain thresholds based on the current date and date of dining dollar reset.

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            A label letting users know what thresholds they have passed.
        """
        if User.dining_plan_total == 200:
            money_spent = User.dining_plan_current / User.dining_plan_total

            if money_spent >= 1:
                #tkinter label saying user spent all of their money
                pass
            elif money_spent >= .75:
                #tkinter label saying user passed 25%, 50%, and 75% threshhold and has spent ____% of their dining dollars
                pass
            elif money_spent >= .50:
                #tkinter label saying user passed 25% and 50% threshhold and has spent ____% of their dining dollars
                pass
            elif money_spent >= .25:
                #tkinter label saying user passed 25% threshhold and has spent ____% of their dining dollars
                pass
            else:
                #tkinter label saying user  has spent ____% of their dining dollars
                pass
        
        elif User.dining_plan_total == 300:

            money_spent = User.dining_plan_current / User.dining_plan_total

            if money_spent >= 1:
                #tkinter label saying user spent all of their money
                pass
            elif money_spent >= .75:
                #tkinter label saying user passed 25%, 50%, and 75% threshhold and has spent ____% of their dining dollars
                pass
            elif money_spent >= .50:
                #tkinter label saying user passed 25% and 50% threshhold and has spent ____% of their dining dollars
                pass
            elif money_spent >= .25:
                #tkinter label saying user passed 25% threshhold and has spent ____% of their dining dollars
                pass
            else:
                #tkinter label saying user  has spent ____% of their dining dollars
                pass
        
        elif User.dining_plan_total == 400:
            money_spent = User.dining_plan_current / User.dining_plan_total

            if money_spent >= 1:
                #tkinter label saying user spent all of their money
                pass
            elif money_spent >= .75:
                #tkinter label saying user passed 25%, 50%, and 75% threshhold and has spent ____% of their dining dollars
                pass
            elif money_spent >= .50:
                #tkinter label saying user passed 25% and 50% threshhold and has spent ____% of their dining dollars
                pass
            elif money_spent >= .25:
                #tkinter label saying user passed 25% threshhold and has spent ____% of their dining dollars
                pass
            else:
                #tkinter label saying user  has spent ____% of their dining dollars
                pass
    
    #Python3 program to find number of days between two given dates
    def numOfDays(self, date1, date2):
        """
        Driver: Arnav Patel
        Navigator: Margaret Hermanto
        """
    #check which date is greater to avoid days output in -ve number
        if date2 > date1:   
            return (date2 - date1).days
        else:
            return (date1 - date2).days

    def suggested_spending(self):
        """ Calculates a suggested average amount of money they could spend daily based on their remaining dining dollar balance.

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
        
        # Name label that indicates where to put name
        self.name_label = ttk.Label(self.p1, text="Name")
        self.name_label.grid(row=1, column=1)
        # Name entry
        self.name = ttk.Entry(self.p1, textvariable=self.name_var)
        self.name.grid(row=1, column=2)
        # Will display inputted text from self.name entry
        self.verify_name_label = ttk.Label(self.p2)
        self.verify_name_label.grid(row=4, column=1)

        # Dining dollar plan label that indicates where to put dining dollar plan
        self.dd_plan_label = ttk.Label(self.p1, text="Dining Dollar Plan")
        self.dd_plan_label.grid(row=2, column=1)
        # Dining dollar plan entry
        self.dd_plan = ttk.Entry(self.p1, textvariable=self.dd_var)
        self.dd_plan.grid(row=2, column=2)
        # Will display inputted text from self.dd_plan entry
        self.verify_dd_plan_label = ttk.Label(self.p2)
        self.verify_dd_plan_label.grid(row=5, column=2)

        # Updates global dining plan value to be used in other methods
        # User.dining_plan_total = self.dd_plan
    
        # Balance label that indicates where to put balance
        self.balance_label = ttk.Label(self.p1, text="Current Dining Dollar Balance")
        self.balance_label.grid(row=3, column=1)
        # Balance entry
        self.balance = ttk.Entry(self.p1, textvariable=self.balance_var)
        self.balance.grid(row=3, column=2)
        # Will display inputted text from self.balance entry
        self.verify_balance_label = ttk.Label(self.p2)
        self.verify_balance_label.grid(row=6, column=2)

        # Updates global balance value to be used in other methods
        # User.dining_plan_current = self.balance

        # Proceed button leads to p2; page navigation is in verification()
        self.proceed = ttk.Button(self.p1, text="Proceed", command=self.verification)
        self.proceed.grid(row=4, column=2)

    def verification(self):
        """ Asks user to verify the displayed information concerning them.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            Either self.p1 or self.p3, depending on the user's answer.
        """
        # Page navigation
        self.p1.forget()
        self.p2.pack()

        self.verify_label = ttk.Label(self.p2, text="Is this information correct?")
        self.verify_label.grid(row=1, column=1)

        # Display user name
        self.verify_name_label.config(text=self.name_var.get())
        # Display dining dollar plan
        self.verify_dd_plan_label.config(text=self.dd_var.get())
        # Display balance
        self.verify_balance_label.config(text=self.balance_var.get())

        self.yes_verify = ttk.Button(self.p2, text="Yes", command=self.options)
        self.yes_verify.grid(row=3, column=1)
        self.no_verify = ttk.Button(self.p2, text="No", command=lambda: self.page_navigation("p2_to_p1"))
        self.no_verify.grid(row=3, column=2)

    def options(self):
        """ Displays a list of options the user can select.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            Requested option.
        """
        # page navigation
        # later on we can add an if statement so we can navigate to options from any page not just self.p2
        self.p2.forget()
        self.p3.pack()

        self.ask = ttk.Label(self.p3, text="What would you like to do today?")
        self.ask.grid(row=1, column=1)

        # button 1
        self.spending_path = ttk.Button(self.p3, text="Create a spending reminder", command=self.spending_reminders)
        self.spending_path.grid(row=2, column=1)

        # button 2
        self.threshold_path = ttk.Button(self.p3, text="Show thresholds passed", command=lambda: self.page_navigation("p3_to_p5"))
        self.threshold_path.grid(row=2, column=2)

        # button 3
        self.suggested_path = ttk.Button(self.p3, text="Get a suggested spending recommendation", command=lambda: self.page_navigation("p3_to_p6"))
        self.suggested_path.grid(row=2, column=3)

        # button 4
        self.log_out_path = ttk.Button(self.p3, text="Log out", command=lambda: self.page_navigation("p3_to_p1"))
        self.log_out_path.grid(row=2, column=4)  

def main():
    """ Displays information to the user using User functions

    Returns:
        Message of information user requested.
    """
    
    pass
    

if __name__ == "__main__":
    """ Calls the main function
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