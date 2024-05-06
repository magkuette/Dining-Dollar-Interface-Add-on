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

from tkinter import messagebox

# Need this for current date
from datetime import date
import time
from datetime import timedelta
import datetime

class User:
    """ Creates a user object based on an actual program user.

    Attributes
    """

    def __init__(self, root):
        """
        Driver: Margaret Hermanto
        Navigator: Arnav Patel
        """
        self.root = root

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

        # Call get_user_info function (only need to call this first function because the rest of the functions will be called later on throughout the code through buttons)
        self.get_user_info()

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


        self.ask_reminder_enter = ttk.Button(self.p4, text="Enter", command=self.spending_reminders_helper)
        self.ask_reminder_enter.grid(row=4, column=2)

        

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
    
    def spending_reminders_helper(self):
        
        # Page navigation
        self.p4.forget()
        self.p7.pack()

        self.input_reminder = ttk.Label(self.p7)
        self.input_reminder.grid(row=4, column=1)

        self.input_reminder.config(text = f"You wanted reminders every {self.reminder_var.get()} days. Here are the dates you are reminded to spend.")

        if self.reminder_var.get() == 1:
            self.reminder = ttk.Label(self.p7, text="Please mark every date in your calendar from August 28, 2024 to May 17, 2025.")
            self.reminder.grid(row=6, column=1)
        
        elif self.reminder_var.get() == 7:
            date_format = "%m/%d/%Y"

            date_today = time.mktime(time.strptime(self.day.get(), date_format))
            end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
            diff = end_date - date_today
            dates_num = int(diff / 86400)

            self.days_total = dates_num

            dates = dates_num / 7
            dates_to_print = []

            temp = self.day.get()
            temp_string = "%m/%d/%Y"

            for y in range(0, int(dates)):
                
                current_date_temp = datetime.datetime.strptime(temp, temp_string)
                newdate = current_date_temp + datetime.timedelta(days=7)
                dates_to_print.append(newdate)
                temp = str(newdate)
                temp_string = "%Y-%m-%d %H:%M:%S"


            self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:")
            self.reminder.grid(row=10, column=1)

            for x in range(0, len(dates_to_print)):
                self.statement = ttk.Label(self.p7, text=f"{dates_to_print[x]}")
                self.statement.grid(row=11+x, column=1)

        
        elif self.reminder_var.get() == 14:
            date_format = "%m/%d/%Y"

            date_today = time.mktime(time.strptime(self.day.get(), date_format))
            end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
            diff = end_date - date_today
            dates_num = int(diff / 86400)

            self.days_total = dates_num

            dates = dates_num / 14
            dates_to_print = []

            temp = self.day.get()
            temp_string = "%m/%d/%Y"

            for y in range(0, int(dates)):
                
                current_date_temp = datetime.datetime.strptime(temp, temp_string)
                newdate = current_date_temp + datetime.timedelta(days=14)
                dates_to_print.append(newdate)
                temp = str(newdate)
                temp_string = "%Y-%m-%d %H:%M:%S"


            self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:")
            self.reminder.grid(row=10, column=1)

            for x in range(0, len(dates_to_print)):
                self.statement = ttk.Label(self.p7, text=f"{dates_to_print[x]}")
                self.statement.grid(row=11+x, column=1)

        elif self.reminder_var.get() == 30:
            date_format = "%m/%d/%Y"

            date_today = time.mktime(time.strptime(self.day.get(), date_format))
            end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
            diff = end_date - date_today
            dates_num = int(diff / 86400)

            self.days_total = dates_num

            dates = dates_num / 30
            dates_to_print = []

            temp = self.day.get()
            temp_string = "%m/%d/%Y"

            for y in range(0, int(dates)):
                
                current_date_temp = datetime.datetime.strptime(temp, temp_string)
                newdate = current_date_temp + datetime.timedelta(days=30)
                dates_to_print.append(newdate)
                temp = str(newdate)
                temp_string = "%Y-%m-%d %H:%M:%S"


            self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:")
            self.reminder.grid(row=10, column=1)

            for x in range(0, len(dates_to_print)):
                self.statement = ttk.Label(self.p7, text=f"{dates_to_print[x]}")
                self.statement.grid(row=11+x, column=1)

        elif self.reminder_var.get() == 90:
            date_format = "%m/%d/%Y"

            date_today = time.mktime(time.strptime(self.day.get(), date_format))
            end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
            diff = end_date - date_today
            dates_num = int(diff / 86400)

            self.days_total = dates_num

            dates = dates_num / 90
            dates_to_print = []

            temp = self.day.get()
            temp_string = "%m/%d/%Y"

            for y in range(0, int(dates)):
                
                current_date_temp = datetime.datetime.strptime(temp, temp_string)
                newdate = current_date_temp + datetime.timedelta(days=90)
                dates_to_print.append(newdate)
                temp = str(newdate)
                temp_string = "%Y-%m-%d %H:%M:%S"


            self.reminder = ttk.Label(self.p7, text=f"Please mark the following dates in your calendar:")
            self.reminder.grid(row=10, column=1)

            for x in range(0, len(dates_to_print)):
                self.statement = ttk.Label(self.p7, text=f"{dates_to_print[x]}")
                self.statement.grid(row=11+x, column=1)

        self.log_out_path = ttk.Button(self.p7, text="Log out", command=self.navigate_home)
        self.log_out_path.grid(row=12, column=4)  
        self.options_path = ttk.Button(self.p7, text="Back to Options", command=self.navigate_options)
        self.options_path.grid(row=12, column=5)

    def threshold_reminders(self):
        """ Calculates when dining dollar balance has reached certain thresholds based on the current date and date of dining dollar reset.

        Driver: Arnav Patel
        Navigator: Margaret Hermanto

        Returns:
            A label letting users know what thresholds they have passed.
        """

        # page navigation
        self.p3.forget()
        self.p5.pack()

        self.ask_threshold = ttk.Label(self.p5, text="Here are the main quartile thresholds you have passed in dining dollar spending.")
        self.ask_threshold.grid(row=1, column=1)

        money_left = self.balance_var.get() / self.dd_var.get()
        money_spent = 1 - money_left
        spent_percent = money_spent * 100
  
        if money_spent >= 1:
            self.threshold_resp = ttk.Label(self.p5, text="You have used up all of your dining dollars. Don't worry!")
            self.threshold_resp.grid(row=4, column=1)
        elif money_spent >= .75:
            #tkinter label saying user passed 25%, 50%, and 75% threshhold and has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed the 25th, 50th, and 75th percentiles of total dining dollars in your plan. You have used up {spent_percent}% of all of your dining dollars.")
            self.threshold_resp.grid(row=4, column=1)
        elif money_spent >= .50:
            #tkinter label saying user passed 25% and 50% threshhold and has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed the 25th and 50th percentiles of total dining dollars in your plan. You have used up {spent_percent}% of all of your dining dollars.")
            self.threshold_resp.grid(row=4, column=1)
        elif money_spent >= .25:
            #tkinter label saying user passed 25% threshhold and has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed the 25th percentile of total dining dollars in your plan. You have used up {spent_percent}% of all of your dining dollars.")
            self.threshold_resp.grid(row=4, column=1)
        else:
            #tkinter label saying user  has spent ____% of their dining dollars
            self.threshold_resp = ttk.Label(self.p5, text=f"You have passed no remarkable thresholds of spent dining dollars in your plan yet. You have used up {spent_percent}% of all of your dining dollars.")
            self.threshold_resp.grid(row=4, column=1)

        self.log_out_path = ttk.Button(self.p5, text="Log out", command=self.navigate_home)
        self.log_out_path.grid(row=7, column=4)
        self.options_path = ttk.Button(self.p5, text="Back to Options", command=self.navigate_options)
        self.options_path.grid(row=7, column=5)


    def suggested_spending(self):
        """ Calculates a suggested average amount of money they could spend daily based on their remaining dining dollar balance.

        Returns:
            A message letting users know how much money they could spend daily to spend their dining dollar balance.
        """
        # Get current date using date.today()

        # page navigation
        self.p3.forget()
        self.p6.pack()

        date_format = "%m/%d/%Y"

        date_today = time.mktime(time.strptime(self.day.get(), date_format))
        end_date = time.mktime(time.strptime(self.sem_end.get(), date_format))
        diff = end_date - date_today
        dates_num = int(diff / 86400)

        self.days_total = dates_num

        daily_spending = self.balance_var.get() / self.days_total
        daily_spending_rounded = round(daily_spending, 2)

        # Divide dining dollars balance by amount of days left till date of dining dollars reset
        self.ask_suggested = ttk.Label(self.p6, text=f"If you were to spend money every day until your dining dollar plan expired, you would need to spend ${daily_spending_rounded} daily.")
        self.ask_suggested.grid(row=1, column=1)

        self.log_out_path = ttk.Button(self.p6, text="Log out", command=self.navigate_home)
        self.log_out_path.grid(row=2, column=4)
        self.options_path = ttk.Button(self.p6, text="Back to Options", command=self.navigate_options)
        self.options_path.grid(row=2, column=5)

    def get_user_info(self):
        """ Gets user information including dining dollar plan, current dining dollar balance, as well as name.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel

        Returns:
            self.p2 after user clicks Proceed button.
        """
        
        # Name label that indicates where to put name
        self.name_label = ttk.Label(self.p1, text="Name: ")
        self.name_label.grid(row=1, column=1, sticky="e")
        # Name entry
        self.name = ttk.Entry(self.p1, textvariable=self.name_var)
        self.name.grid(row=1, column=2)
        # Will display inputted text from self.name entry
        self.verify_name_label = ttk.Label(self.p2)
        self.verify_name_label.grid(row=2, column=2, pady=2)

        # Dining dollar plan label that indicates where to put dining dollar plan
        self.dd_plan_label = ttk.Label(self.p1, text="Dining Dollar Plan: ")
        self.dd_plan_label.grid(row=2, column=1, sticky="e")
        # Dining dollar plan entry
        self.dd_plan = ttk.Entry(self.p1, textvariable=self.dd_var)
        self.dd_plan.grid(row=2, column=2)
        # Will display inputted text from self.dd_plan entry
        self.verify_dd_plan_label = ttk.Label(self.p2)
        self.verify_dd_plan_label.grid(row=3, column=2)
    
        # Balance label that indicates where to put balance
        self.balance_label = ttk.Label(self.p1, text="Current Dining Dollar Balance: ")
        self.balance_label.grid(row=3, column=1, sticky="e")
        # Balance entry
        self.balance = ttk.Entry(self.p1, textvariable=self.balance_var)
        self.balance.grid(row=3, column=2)
        # Will display inputted text from self.balance entry
        self.verify_balance_label = ttk.Label(self.p2)
        self.verify_balance_label.grid(row=4, column=2)

        # Today's date label that indicates where to put today's date
        self.today_label = ttk.Label(self.p1, text="Today's Date (MM/DD/YYYY): ")
        self.today_label.grid(row=4, column=1, sticky="e")
        # Today's date entry
        self.today = ttk.Entry(self.p1, textvariable=self.day)
        self.today.grid(row=4, column=2)
        # Will display inputted text from self.today entry
        self.verify_today_label = ttk.Label(self.p2)
        self.verify_today_label.grid(row=5, column=2)

        # Semester end label that indicates when to put ending date
        self.sem_end_label = ttk.Label(self.p1, text="Ending Date (MM/DD/YYYY): ")
        self.sem_end_label.grid(row=5, column=1, sticky="e")
        # Semester end entry
        self.sem_end = ttk.Entry(self.p1, textvariable=self.sem_end)
        self.sem_end.grid(row=5, column=2)
        # Will display inputted text from self.sem_end entry
        self.verify_end_label = ttk.Label(self.p2)
        self.verify_end_label.grid(row=6, column=2)

        # Proceed button leads to p2; page navigation is in verification()
        self.proceed = ttk.Button(self.p1, text="Proceed", command=self.verification)
        self.proceed.grid(row=6, column=2)

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
        self.for_verify_name = ttk.Label(self.p2, text="Name:")
        self.for_verify_name.grid(row=2, column=1, sticky="e")
        self.for_verify_dd = ttk.Label(self.p2, text="Dining Dollar Plan:")
        self.for_verify_dd.grid(row=3, column=1, sticky="e")
        self.for_verify_balance = ttk.Label(self.p2, text="Balance:")
        self.for_verify_balance.grid(row=4, column=1, sticky="e")
        self.for_verify_today = ttk.Label(self.p2, text="Today's Date (MM/DD/YYYY):")
        self.for_verify_today.grid(row=5, column=1, sticky="e")
        self.for_verify_end = ttk.Label(self.p2, text="Ending Date (MM/DD/YYYY):")
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

        self.yes_verify = ttk.Button(self.p2, text="Yes", command=self.options)
        self.yes_verify.grid(row=9, column=1)
        self.no_verify = ttk.Button(self.p2, text="No", command=self.navigate_home)
        self.no_verify.grid(row=9, column=2)

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

        # Button that leads to spending_reminders
        self.spending_path = ttk.Button(self.p3, text="Create a spending reminder", command=self.spending_reminders)
        self.spending_path.grid(row=2, column=1)

        # Button that leads to threshold_reminder
        self.threshold_path = ttk.Button(self.p3, text="Show thresholds passed", command=self.threshold_reminders)
        self.threshold_path.grid(row=2, column=2)

        # Button that leads to suggested_spending
        self.suggested_path = ttk.Button(self.p3, text="Get a suggested spending recommendation", command=self.suggested_spending)
        self.suggested_path.grid(row=2, column=3)

        # Button that leads to get_user_info
        self.log_out_path = ttk.Button(self.p3, text="Log out", command=self.navigate_home)
        self.log_out_path.grid(row=2, column=4)  

    def navigate_home(self):
        """ Allows user to navigate to self.p1 from any other page in the program.

        Driver: Margaret Hermanto
        Navigator: Arnav Patel
        """
        self.p1.pack()
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
        """
        self.p3.pack()
        self.p1.forget()
        self.p2.forget()
        self.p4.forget()
        self.p5.forget()
        self.p6.forget()
        self.p7.forget()


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
