"""
Group 4: Margaret Hermanto, Arnav Patel
Assignment: Final Project INST326
Date: 5_9_24
"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from datetime import date
import time
from datetime import timedelta
import datetime

class User:
    """ Creates a user object based on an actual program user.

    Attributes:
        self.name_var: a global variable for the inputted user name.
        self.dd_var: a global variable for the inputted dining dollar plan amount.
        self.balance_var: a global variable for the inputted balance remaining.
        self.reminder_var: a global variable for how often the user wants spending reminders.
        self.day: a global variable for the current date.
        self.sem_end: a global variable for the ending date.
        self.days_total: a global variable for the total number of days between the starting and ending dates.
    """

    def __init__(self, root):
        """ Initializes the GUI and sets up all of the program's pages (self.p1 - self.p7). Only packs self.p1.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Args:
            root: the window that all of the Frames (self.p1 - self.p7) are packed into for this Tkinter GUI
        
        Side effects:
            Updates the value of self.name_var to user input.
            Updates the value of self.dd_var to user input.
            Updates the value of self.balance_var to user input.
            Updates the value of self.reminder_var to user input.
            Updates the value of self.day to user input.
            Updates the value of self.sem_end to user input.
        """
        self.root = root

        self.banner = tk.Label(self.root, text="Dining Dollar Interface", bg="#5F6F52", width=1400, height=2, font=("Times New Roman", 14), fg="#FFE2E0")
        self.banner.pack(side="bottom")
        
        # get_user_info()
        self.p1 = tk.Frame(self.root)
        self.p1.pack()

        # verification()
        self.p2 = tk.Frame(self.root)

        # Stores entry information for future label configuration
        self.name_var = tk.StringVar()
        self.dd_var = tk.IntVar()
        self.balance_var = tk.IntVar()
        self.reminder_var = tk.IntVar()
        self.day = tk.StringVar()
        self.sem_end = tk.StringVar()
        self.days_total = 0

        # options()
        self.p3 = tk.Frame(self.root)
        # spending_reminders()
        self.p4 = tk.Frame(self.root)
        # threshold_reminders()
        self.p5 = tk.Frame(self.root)
        # suggested_spending()    
        self.p6 = tk.Frame(self.root)
        # spending_reminders_helper
        self.p7 = tk.Frame(self.root)    

        # Call get_user_info function (only need to call this first function because the rest of the functions will be called later on throughout the code through buttons)
        self.get_user_info()
        
    def spending_reminders(self):
        """ Takes user input to determine what values are to be plugged into spending_reminders_helper

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            self.p7 after user clicks "Enter" button.
        """
        # Page navigation
        self.p3.forget()
        self.p4.pack()

        # Ask user how often they want reminders (can be any number or set like 1, 7, 14, 30, 90)
        self.ask_reminder = ttk.Label(self.p4, text="How often would you like to receive reminders? (Every 1, 7, 14, 30, or 90 days)", font=("Verdana", 15))
        self.ask_reminder.grid(row=1, column=1)

        # Deletes any previously-inputted user input from self.ask_reminder_entry
        self.reminder_var.set("")

        # User enters reminder frequency
        self.ask_reminder_entry = ttk.Entry(self.p4, textvariable=self.reminder_var, font=("Verdana", 12))
        self.ask_reminder_entry.grid(row=2, column=1)
        
        # "Enter" button that will lead to spending_reminders_helper
        self.ask_reminder_enter = tk.Button(self.p4, text="Enter", command=self.spending_reminders_helper, font=("Verdana", 12))
        self.ask_reminder_enter.grid(row=4, column=2)

    def spending_reminders_helper(self):
        """ Calculates when the user should set reminders to spend dining dollars based on the current date.

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            A list of dates corresponding to the values that the user inputted in spending_reminders.
        """
        
        # If the user input something other than 1, 7, 14, 30, or 90, the program will show a messagebox
        if (self.reminder_var.get() != 1) and (self.reminder_var.get() != 7) and (self.reminder_var.get() != 14) and (self.reminder_var.get() != 30) and (self.reminder_var.get() != 90) :
            messagebox.showerror(title="Error", message="Please input a valid number (1, 7, 14, 30, or 90)")
        else:
            # Page navigation
            self.p4.forget()
            self.p7.pack()

            self.input_reminder = ttk.Label(self.p7, text=f"You wanted reminders every {self.reminder_var.get()} days. Here are the dates you are reminded to spend.", font=("Verdana", 12))
            self.input_reminder.grid(row=4, column=1)

            # Output if user inputs 1 in spending_reminders
            if self.reminder_var.get() == 1:
                self.reminder = ttk.Label(self.p7, text=f"Please mark every date in your calendar from {self.day.get()} to {self.sem_end.get()}.", font=("Verdana", 12))
                self.reminder.grid(row=6, column=1)
            
            # Output if user inputs 7 in spending_reminders
            elif self.reminder_var.get() == 7:
                date_format = "%m/%d/%Y"

                # Parses the date string into a time tuple and then into a float to be able to do operations
                date_today = time.mktime(time.strptime(self.day.get(), date_format))
                end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
                diff = end_date - date_today
                # Divides total seconds between dates by seconds in 24 hours to figure out how many days the user should be reminded
                dates_num = int(diff / 86400)

                self.days_total = dates_num

                dates = dates_num / 7
                self.dates_to_print = []

                temp = self.day.get()
                temp_string = "%m/%d/%Y"

                # Adds elements to a list based on how many days after the value of the current date it is
                for y in range(0, int(dates)):
                    
                    current_date_temp = datetime.datetime.strptime(temp, temp_string)
                    newdate = current_date_temp + datetime.timedelta(days=7)
                    self.dates_to_print.append(newdate)
                    temp = str(newdate)
                    temp_string = "%Y-%m-%d %H:%M:%S"


                self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:", font=("Verdana", 12))
                self.reminder.grid(row=10, column=1)

                # Prints elements of list out 1 line at a time on GUI page
                for x in range(0, len(self.dates_to_print)):
                    self.statement = ttk.Label(self.p7, text=f"{self.dates_to_print[x]}")
                    self.statement.grid(row=11+x, column=1)

            # Output if user inputs 14 in spending_reminders
            elif self.reminder_var.get() == 14:
                date_format = "%m/%d/%Y"

                # Parses the date string into a time tuple and then into a float to be able to do operations
                date_today = time.mktime(time.strptime(self.day.get(), date_format))
                end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
                diff = end_date - date_today
                # Divides total seconds between dates by seconds in 24 hours to figure out how many days the user should be reminded
                dates_num = int(diff / 86400)

                self.days_total = dates_num

                dates = dates_num / 14
                self.dates_to_print = []

                temp = self.day.get()
                temp_string = "%m/%d/%Y"

                # Adds elements to a list based on how many days after the value of the current date it is
                for y in range(0, int(dates)):
                    
                    current_date_temp = datetime.datetime.strptime(temp, temp_string)
                    newdate = current_date_temp + datetime.timedelta(days=14)
                    self.dates_to_print.append(newdate)
                    temp = str(newdate)
                    temp_string = "%Y-%m-%d %H:%M:%S"

                self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:", font=("Verdana", 12))
                self.reminder.grid(row=10, column=1)

                # Prints elements of list out 1 line at a time on GUI page
                for x in range(0, len(self.dates_to_print)):
                    self.statement = ttk.Label(self.p7, text=f"{self.dates_to_print[x]}")
                    self.statement.grid(row=11+x, column=1)
            
            # Output if user inputs 30 in spending_reminders
            elif self.reminder_var.get() == 30:
                date_format = "%m/%d/%Y"

                # Parses the date string into a time tuple and then into a float to be able to do operations
                date_today = time.mktime(time.strptime(self.day.get(), date_format))
                end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
                diff = end_date - date_today
                # Divides total seconds between dates by seconds in 24 hours to figure out how many days the user should be reminded
                dates_num = int(diff / 86400)

                self.days_total = dates_num

                dates = dates_num / 30
                self.dates_to_print.clear()

                temp = self.day.get()
                temp_string = "%m/%d/%Y"

                # Adds elements to a list based on how many days after the value of the current date it is
                for y in range(0, int(dates)):
                    
                    current_date_temp = datetime.datetime.strptime(temp, temp_string)
                    newdate = current_date_temp + datetime.timedelta(days=30)
                    self.dates_to_print.append(newdate)
                    temp = str(newdate)
                    temp_string = "%Y-%m-%d %H:%M:%S"

                self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:", font=("Verdana", 12))
                self.reminder.grid(row=10, column=1)

                # Prints elements of list out 1 line at a time on GUI page
                for x in range(0, len(self.dates_to_print)):
                    self.statement = ttk.Label(self.p7, text=f"{self.dates_to_print[x]}")
                    self.statement.grid(row=11+x, column=1)

                self.dates_to_print.clear()
                self.reminder_var.config(text="")

            # Output if user inputs 90 in spending_reminders
            elif self.reminder_var.get() == 90:
                date_format = "%m/%d/%Y"

                # Parses the date string into a time tuple and then into a float to be able to do operations
                date_today = time.mktime(time.strptime(self.day.get(), date_format))
                end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
                diff = end_date - date_today
                # Divides total seconds between dates by seconds in 24 hours to figure out how many days the user should be reminded
                dates_num = int(diff / 86400)

                self.days_total = dates_num

                dates = dates_num / 90
                self.dates_to_print = []

                temp = self.day.get()
                temp_string = "%m/%d/%Y"
                
                # Adds elements to a list based on how many days after the value of the current date it is
                for y in range(0, int(dates)):
                    
                    current_date_temp = datetime.datetime.strptime(temp, temp_string)
                    newdate = current_date_temp + datetime.timedelta(days=90)
                    self.dates_to_print.append(newdate)
                    temp = str(newdate)
                    temp_string = "%Y-%m-%d %H:%M:%S"

                self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:", font=("Verdana", 12))
                self.reminder.grid(row=10, column=1)
                
                # Prints elements of list out 1 line at a time on GUI page
                for x in range(0, len(self.dates_to_print)):
                    self.statement = ttk.Label(self.p7, text=f"{self.dates_to_print[x]}")
                    self.statement.grid(row=11+x, column=1)

        # Buttons to navigate to page 1 (self.p1) and page 3 (self.p3) of the GUI, respectively
        self.log_out_path = tk.Button(self.p7, text="Log out", command=self.navigate_home, font=("Verdana", 12))
        self.log_out_path.grid(row=13, column=3)  
        self.options_path = tk.Button(self.p7, text="Back to Options", command=self.navigate_options, font=("Verdana", 12))
        self.options_path.grid(row=12, column=3)

    def threshold_reminders(self):
        """ Calculates when dining dollar balance has reached certain thresholds based on the current date and date of dining dollar reset.

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            A label letting users know what thresholds they have passed.
        """

        # Page navigation
        self.p3.forget()
        self.p5.pack()

        self.ask_threshold = ttk.Label(self.p5, text="Here are the main quartile thresholds you have passed in dining dollar spending.", font=("Verdana", 12))
        self.ask_threshold.grid(row=1, column=1)

        money_left = self.balance_var.get() / self.dd_var.get()
        money_spent = 1 - money_left
        spent_percent = money_spent * 100
  
        if money_spent >= 1:
            self.threshold_resp = ttk.Label(self.p5, text="You have used up all of your dining dollars. Don't worry!", font=("Verdana", 12))
            self.threshold_resp.grid(row=4, column=1)
        elif money_spent >= .75:
            # Tkinter label saying user passed 25%, 50%, and 75% threshhold and has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed the 25th, 50th, and 75th percentiles of total dining dollars in your plan. You have used up {spent_percent}% of all of your dining dollars.", font=("Verdana", 12))
            self.threshold_resp.grid(row=4, column=1)
        elif money_spent >= .50:
            # Tkinter label saying user passed 25% and 50% threshhold and has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed the 25th and 50th percentiles of total dining dollars in your plan. You have used up {spent_percent}% of all of your dining dollars.", font=("Verdana", 12))
            self.threshold_resp.grid(row=4, column=1)
        elif money_spent >= .25:
            # Tkinter label saying user passed 25% threshhold and has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed the 25th percentile of total dining dollars in your plan. You have used up {spent_percent}% of all of your dining dollars.", font=("Verdana", 12))
            self.threshold_resp.grid(row=4, column=1)
        else:
            # Tkinter label saying user  has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed no remarkable thresholds of spent dining dollars in your plan yet. You have used up {spent_percent}% of all of your dining dollars.", font=("Verdana", 12))
            self.threshold_resp.grid(row=4, column=1)

        # Buttons to navigate to page 1 (self.p1) and 3 (self.p3) of the GUI, respectively
        self.log_out_path = tk.Button(self.p5, text="Log out", command=self.navigate_home, font=("Verdana", 12))
        self.log_out_path.grid(row=8, column=3)
        self.options_path = tk.Button(self.p5, text="Back to Options", command=self.navigate_options, font=("Verdana", 12))
        self.options_path.grid(row=7, column=3)

    def suggested_spending(self):
        """ Calculates a suggested average amount of money they could spend daily based on their remaining dining dollar balance.

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            A message letting users know how much money they could spend daily to spend their dining dollar balance.
        """
        # Page navigation
        self.p3.forget()
        self.p6.pack()

        date_format = "%m/%d/%Y"

        # Parses the date string into a time tuple and then into a float to be able to do operations
        date_today = time.mktime(time.strptime(self.day.get(), date_format))
        end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
        diff = end_date - date_today
        # Divides total seconds between dates by seconds in 24 hours to figure out how many days the user should be reminded
        dates_num = int(diff / 86400)

        self.days_total = dates_num

        # Finds average by taking balance and dividing it by total days between the start and end date
        daily_spending = self.balance_var.get() / self.days_total
        daily_spending_rounded = round(daily_spending, 2)

        self.ask_suggested = ttk.Label(self.p6, text=f"If you were to spend money every day until your dining dollar plan expired,\nyou would need to spend ${daily_spending_rounded} daily.", font=("Verdana", 12))
        self.ask_suggested.grid(row=1, column=1)

        # Buttons to navigate to page 1 (self.p1) and 3 (self.p3) of the GUI, respectively
        self.log_out_path = tk.Button(self.p6, text="Log out", command=self.navigate_home, font=("Verdana", 12))
        self.log_out_path.grid(row=3, column=3)
        self.options_path = tk.Button(self.p6, text="Back to Options", command=self.navigate_options, font=("Verdana", 12))
        self.options_path.grid(row=2, column=3)
        
    def get_user_info(self):
        """ Gets user information including dining dollar plan, current dining dollar balance, as well as name.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            self.p2 after user clicks Proceed button.
        """
        self.welcome_label = ttk.Label(self.p1, text="Welcome to our Dining Dollar Interface", font=("Verdana", 25))
        self.welcome_label.grid(row=1, column=2)

        self.directions_label = ttk.Label(self.p1, text="Please input your login information.", font=("Verdana", 15))
        self.directions_label.grid(row=2, column=2, pady=10)
        # Name label that indicates where to put name
        self.name_label = ttk.Label(self.p1, text="Name: ", font=("Verdana", 12, "bold"))
        self.name_label.grid(row=4, column=2, pady=(15, 0))
        # Name entry
        self.name = ttk.Entry(self.p1, textvariable=self.name_var, font=("Verdana", 12))
        self.name.grid(row=5, column=2)
        # Will display inputted text from self.name entry
        self.verify_name_label = ttk.Label(self.p2, font=("Verdana", 12))
        self.verify_name_label.grid(row=2, column=2, sticky="w")

        # Dining dollar plan label that indicates where to put dining dollar plan
        self.dd_plan_label = ttk.Label(self.p1, text="Dining Dollar Plan: ", font=("Verdana", 12, "bold"))
        self.dd_plan_label.grid(row=7, column=2, pady=(20, 0))
        # Dining dollar plan entry
        self.dd_plan = ttk.Entry(self.p1, textvariable=self.dd_var, font=("Verdana", 12))
        self.dd_plan.grid(row=8, column=2)
        # Will display inputted text from self.dd_plan entry
        self.verify_dd_plan_label = ttk.Label(self.p2, font=("Verdana", 12))
        self.verify_dd_plan_label.grid(row=3, column=2, sticky="w")
    
        # Balance label that indicates where to put balance
        self.balance_label = ttk.Label(self.p1, text="Current Dining Dollar Balance: ", font=("Verdana", 12, "bold"))
        self.balance_label.grid(row=9, column=2, pady=(20, 0))
        # Balance entry
        self.balance = ttk.Entry(self.p1, textvariable=self.balance_var, font=("Verdana", 12))
        self.balance.grid(row=10, column=2)
        # Will display inputted text from self.balance entry
        self.verify_balance_label = ttk.Label(self.p2, font=("Verdana", 12))
        self.verify_balance_label.grid(row=4, column=2, sticky="w")

        # Today's date label that indicates where to put today's date
        self.today_label = ttk.Label(self.p1, text="Today's Date (MM/DD/YYYY): ", font=("Verdana", 12, "bold"))
        self.today_label.grid(row=11, column=2, pady=(20, 0))
        # Today's date entry
        self.today = ttk.Entry(self.p1, textvariable=self.day, font=("Verdana", 12))
        self.today.grid(row=12, column=2)
        # Will display inputted text from self.today entry
        self.verify_today_label = ttk.Label(self.p2, font=("Verdana", 12))
        self.verify_today_label.grid(row=5, column=2, sticky="w")

        # Semester end label that indicates when to put ending date
        self.sem_end_label = ttk.Label(self.p1, text="Ending Date (MM/DD/YYYY): ", font=("Verdana", 12, "bold"))
        self.sem_end_label.grid(row=13, column=2, pady=(20, 0))
        # Semester end entry
        self.sem_end = ttk.Entry(self.p1, textvariable=self.sem_end, font=("Verdana", 12))
        self.sem_end.grid(row=14, column=2)
        # Will display inputted text from self.sem_end entry
        self.verify_end_label = ttk.Label(self.p2, font=("Verdana", 12))
        self.verify_end_label.grid(row=6, column=2, sticky="w")

        # Proceed button leads to self.p2; page navigation is in verification()
        self.proceed = tk.Button(self.p1, text="Proceed", command=self.verification, font=("Verdana", 12))
        self.proceed.grid(row=15, column=2, pady=(20, 0))   

    def verification(self):
        """ Asks user to verify the displayed information concerning them.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            Either self.p1 or self.p3, depending on the user's answer.

        Raises:
            ValueError: - Invalid date format for today's date.
            ValueError: - Invalid date format for ending date.
            ValueError: - Dining dollar plan must be a number greater than or equal to 0.
            ValueError: - Balance must be a number greater than or equal to 0.
        """
        # Error messages will be appended to this list
        error_list = []

        # Append error message if dining dollar plan (self.dd_var) is less than 0 or not an integer
        if self.dd_var.get() < 0:
            error_list.append("- Dining dollar plan must be a number greater than or equal to 0.")

        # Append error message if balance (self.balance_var) is less than 0 or not an integer
        if self.balance_var.get() < 0:
            error_list.append("\n- Balance must be a number greater than or equal to 0.")

        # Append error message if balance (self.balance_var) is greater than dining dollar plan
        if self.balance_var.get() > self.dd_var.get():
            error_list.append("\n- Balance must not be greater than dining dollar plan.")

        # Append error message if self.date is not in the format of date_format
        date_format = "%m/%d/%Y"
        try:
            time.mktime(time.strptime(self.day.get(), date_format))
        except ValueError:
            error_list.append("\n- Invalid date format for today's date")

        # Append error message if self.sem_end is not in the format of date_format
        try:
            time.mktime(time.strptime(self.sem_end.get(), date_format))
        except ValueError:
            error_list.append("\n- Invalid date format for ending date.")

        # Convert error_list to str to display in messagebox message
        error_str = "".join(error_list)

        # If len(error_str) == 0, this means there are no errors. This means the program can proceed.
        if len(error_str) == 0:
            self.p1.forget()
            self.p2.pack()

            self.verify_label = ttk.Label(self.p2, text="Is this information correct?", font=("Verdana", 15))
            self.verify_label.grid(row=1, column=1, pady=(0, 10))
            self.for_verify_name = ttk.Label(self.p2, text="Name: ", font=("Verdana", 12, "bold"))
            self.for_verify_name.grid(row=2, column=1, sticky="e")
            self.for_verify_dd = ttk.Label(self.p2, text="Dining Dollar Plan: ", font=("Verdana", 12, "bold"))
            self.for_verify_dd.grid(row=3, column=1, sticky="e")
            self.for_verify_balance = ttk.Label(self.p2, text="Balance: ", font=("Verdana", 12, "bold"))
            self.for_verify_balance.grid(row=4, column=1, sticky="e")
            self.for_verify_today = ttk.Label(self.p2, text="Today's Date (MM/DD/YYYY): ", font=("Verdana", 12, "bold"))
            self.for_verify_today.grid(row=5, column=1, sticky="e")
            self.for_verify_end = ttk.Label(self.p2, text="Ending Date (MM/DD/YYYY): ", font=("Verdana", 12, "bold"))
            self.for_verify_end.grid(row=6, column=1, sticky="e")

            # Display user name
            self.verify_name_label.config(text=self.name_var.get())
            # Display dining dollar plan
            self.verify_dd_plan_label.config(text=self.dd_var.get())
            # Display balance
            self.verify_balance_label.config(text=self.balance_var.get())
            # Display start date
            self.verify_today_label.config(text=self.day.get())
            # Display end date
            self.verify_end_label.config(text=self.sem_end.get())

            # self.yes_verify is a button that leads to self.options when clicked
            self.yes_verify = tk.Button(self.p2, text="Yes", command=self.options, font=("Verdana", 12))
            self.yes_verify.grid(row=9, column=1, pady=(10,0))
            # self.no_verify is a button that, when clicked, leads to self.navigate_home, which will navigate to self.p1 (page 1)
            self.no_verify = tk.Button(self.p2, text="No", command=self.navigate_home, font=("Verdana", 12))
            self.no_verify.grid(row=9, column=2, pady=(10,0))
        else:
            # Displays error(s) in a messagebox
            messagebox.showerror(title="Error", message=error_str)

    def options(self):
        """ Displays a list of options the user can select.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            Requested option and its corresponding page in the GUI.
        """
        # Page navigation
        self.p2.forget()
        self.p3.pack()

        self.ask = ttk.Label(self.p3, text="What would you like to do today?", font=("Verdana", 15))
        self.ask.grid(row=1, column=1)

        # Button that leads to spending_reminders
        self.spending_path = tk.Button(self.p3, text="Create a spending reminder", command=self.spending_reminders, font=("Verdana", 12))
        self.spending_path.grid(row=2, column=1, pady=(20, 20))

        # Button that leads to threshold_reminders
        self.threshold_path = tk.Button(self.p3, text="Show thresholds passed", command=self.threshold_reminders, font=("Verdana", 12))
        self.threshold_path.grid(row=3, column=1, pady=(0, 20))

        # Button that leads to suggested_spending
        self.suggested_path = tk.Button(self.p3, text="Get a suggested spending recommendation", command=self.suggested_spending, font=("Verdana", 12))
        self.suggested_path.grid(row=4, column=1, pady=(0, 20))

        # Button that leads to navigate_home which will lead to get_user_info
        self.log_out_path = tk.Button(self.p3, text="Log out", command=self.navigate_home, font=("Verdana", 12))
        self.log_out_path.grid(row=5, column=1)
    
    def navigate_home(self):
        """ Allows user to navigate to self.p1 from any other page in the program.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            self.p1 after user clicks "Log out" button.
        """
        # Pack self.p1
        self.p1.pack()
        # Forget all other frames
        self.p2.forget()
        self.p3.forget()
        self.p4.forget()
        self.p5.forget()
        self.p6.forget()
        self.p7.forget()
    
    def navigate_options(self):
        """ Allows user to navigate to self.p3 from any other page in the program.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            self.p3 after user clicks "Back to Options" button.
        """
        # Pack self.p3
        self.p3.pack()

        # Forget all other frames
        self.p1.forget()
        self.p2.forget()
        self.p4.forget()
        self.p5.forget()
        self.p6.forget()
        self.p7.forget()

# Keeps Tkinter running
root = tk.Tk()

# Resolution of the window
root.geometry("1400x700")

# Call User
user_instance = User(root)

# Keeps Tkinter running
root.mainloop()
