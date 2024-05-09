"""
Group 4: Margaret Hermanto, Arnav Patel
Assignment: Final Project INST326
Date: 5_8_24

Challenges Encountered: Unit testing capabilities with tkinter GUI

"""

# This is a written test procedure for the entirety of the finalproject326.py file. Originally, we tried to integrate
# unit tests to assess the User class in finalproject326.py. However, the challenge we encountered was being unable
# to test our functions without opening up the GUI on the user's device. This feature just makes it more efficient
# to write test cases for the entire file.


""" Test Case #1 for get_user_info function: This is a test case to cover the first page of the Tkinter GUI for
    finalproject326.py. We are testing this feature to show that the initial input section of our GUI work as
    expected. This specific test case tests for error handling on the first page (self.p1).

Raises:
    ValueError: - Invalid date format for today's date.
    ValueError: - Invalid date format for ending date.
    ValueError: - Dining dollar plan must be a number greater than or equal to 0.
    ValueError: - Balance must be a number greater than or equal to 0.
 """

# First, run the finalproject326.py file.

# Once the GUI opens on your device, input the following information into the corresponding fields carefully:

# Name (optional): Your first and last name in this format (First Last)

# Dining Dollar Plan: Any NEGATIVE integer.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Current Dining Dollar Balance: Any NEGATIVE integer.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Today's Date (MM/DD/YYYY): Leave this input box empty or do not enter a date following the MM/DD/YYYY format.

# Ending Date (MM/DD/YYYY): Leave this input box empty or do not enter a date following the MM/DD/YYYY format.

# To see if this test was successful, a window should pop up in the GUI listing the following statements:

# ValueError: - Invalid date format for today's date.
# ValueError: - Invalid date format for ending date.
# ValueError: - Dining dollar plan must be a number greater than or equal to 0.
# ValueError: - Balance must be a number greater than or equal to 0.

# You can now either close out the GUI window and rerun the code to launch the GUI again or delete the input in every field to continue testing.


""" Test Case #2 for get_user_info function: This is a test case to cover the first page (self.p1) of the Tkinter GUI for
    finalproject326.py. We are testing this feature to show that the initial input section of our GUI work as
    expected.

Returns:
    self.p2 after user clicks Proceed button.
 """

# First, run the finalproject326.py file.

# Once the GUI opens on your device, input the following information into the corresponding fields carefully:

# Name (optional): Your first and last name in this format (First Last)

# Dining Dollar Plan: Any POSITIVE integer or float from this list (200, 300, 400). Any positive number value will work, but these are most likely to be inputted as these match the plans on the UMD website.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Current Dining Dollar Balance: Any POSITIVE integer or float. Do not put a larger number for balance than for dining dollar plan. You will receive an error message.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Today's Date (MM/DD/YYYY): Type in today's date in the format provided.

# Ending Date (MM/DD/YYYY): Type in any date in the future in the format provided.

# To see if this test was successful, the GUI should load the next page which is a verification page for the inputted information. 
# The words at the top this page should be "Is this information correct?". The info below that label on this page should also match the exact input you typed in previously.

# You can now either close out the GUI window and rerun the code to launch the GUI again or press the "Yes" or "No" buttons.
# If you press the "Yes" button, go to the Test Case #1 for options function. If you press the "No" button, go to the Test Case #1 for get_user_info function.


""" Test Case #1 for verification function: This is a test case to cover the second page of the tkinter GUI for
    finalproject326.py. We are testing this feature to show that the output and buttons on this page work as expected.

Returns:
    self.p1 if user clicks "No" button.
    self.p3 if user clicks "Yes" button.
 """

# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function.

# Once this verification page loads, please do the following:

# Check if the value for Name is the same as what you previously inputted.

# Check if the value for Dining Dollar Plan is the same as what you previously inputted.

# Check if the value for Balance is the same as what you previously inputted.

# Check if the value for Today's Date (MM/DD/YYYY) is the same as what you previously inputted.

# Check if the value for Ending Date (MM/DD/YYYY) is the same as what you previously inputted.

# To see if this test was successful, the information on this verification page should be identical to what you inputted on the first page.

# You can now either close out the GUI window and rerun the code to launch the GUI again or press the "Yes" or "No" buttons.
# If you press the "Yes" button, go to the Test Case #1 for options function. If you press the "No" button, go to the Test Case #1 for get_user_info function.


""" Test Case #1 for options function: This is a test case to cover the third page of the tkinter GUI for
    finalproject326.py. We are testing this function to show that the buttons on this page work as expected.

Returns:
    self.p4 if user clicks Create a spending reminder button.
    self.p5 if user clicks Show thresholds passed button.
    self.p6 if user clicks Get a suggested spending recommendation button.
 """

# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function 
# and Test Case #1 for the verification function.

# Once this option page loads, please do the following:

# Check to see if there are four buttons:
# The Create a spending reminder button
# The Show thresholds passed button
# The Get a suggested spending recommendation button
# The Log out button

# You will be able to test the first three buttons in their respective later test cases.
# For now, press the Log out button.

# To see if this test was successful, your GUI should finally show the first page (self.p1) which asks for input.

# You can now either close out the GUI window and rerun the code to launch the GUI again or delete the input in every field to continue testing.

# To test that the "Create a spending reminder" button works, do the following:

# Click the button and check to see it leads you to a page that says "How often would you like to receive reminders? (Every 1, 7, 14, 30, or 90 days)"
# Check to see that there is an Entry box and "Enter" button below the question.
# You can now either close out the GUI window and rerun the code to launch the GUI again or press "Enter" to continue testing.
# If you press "Enter", go to the Test Case #1 for spending_reminders function

# To test that the "Show thresholds passed" button works, do the following:

# Click the button and check to see that it leads you to a page that says "Here are the main quartile thresholds you have passed in dining dollar spending."
# Below that should be more information that will be discussed in Test Case #1 for threshold_reminders function

# To test that the "Get a suggested spending recommendation" button works, do the following:

# Click the button and check to see that it leads you to a page that starts off with the words, "If you were to spend money every day until your dining dollar plan expired, you would need to spend..."
# After this should be more information that will be discussed in Test Case #1 for suggested_spending function


""" Test Case #1 for spending_reminders function: This is a test case to cover the fourth page (self.p4) of the tkinter GUI for
    finalproject326.py. We are testing this function to show that clicking the "Create a spending reminder" button on self.p3 successfully
    led to the spending_reminders function.

    Returns:
        self.p7 if user clicks "Enter" after inputting 1, 7, 14, 30, or 90 in the Entry box
        A messagebox that says "Please input a valid number (1, 7, 14, 30, or 90)
"""
# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function and Test Case #1 for options function

# To test this function, please do the following:

# Check to see that it says "How often would you like to receive reminders? (Every 1, 7, 14, 30, or 90 days)" at the top
# Check to see that there is an Entry box
# Check to see that there is an "Enter" button

# Once you have verified the above three, please do the following:

# Input any number other than 1, 7, 14, 30, or 90 and then press "Enter" to see that a messagebox that says "Please input a valid number (1, 7, 14, 30, or 90)" shows up
# Once you have verified the above, please do the following:

# Input "1" and then press "Enter"
# Go to Test Case #1 for the spending_reminders_helper function to continue testing

# Input "7" and then press "Enter"
# Go to Test Case #1 for the spending_reminders_helper function to continue testing

# Input "14" and then press "Enter"
# Go to Test Case #1 for the spending_reminders_helper function to continue testing

# Input "30" and then press "Enter"
# Go to Test Case #1 for the spending_reminders_helper function to continue testing

# Input "90" and then press "Enter"
# Go to Test Case #1 for the spending_reminders_helper function to continue testing

""" Test Case #1 for spending_reminders_helper function: This is a test case to cover the seventh page (self.p7) of the tkinter GUI for
    finalproject326.py. We are testing this function to show that clicking the "Enter" button on self.p4 works as expected.

    Returns:
        spending dates
"""
# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function, Test Case #1 for options function, and Test Case #1 for spending_reminders function

# If you inputted "1" previously in self.p4 and pressed "Enter", please check that the page has the following:

# A Label that says "You wanted reminders every 1 days. Here are the dates you are reminded to spend. Please mark every date in your calendar from [inputted start date] to [inputted end date]."
# A "Back to Options" button and a "Log out" button
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# If you inputted "7" previously in self.p4 and pressed "Enter", please check that the page has the following:

# A Label that says "You wanted reminders every 7 days. Here are the dates you are reminded to spend. Please mark the following dates in your calendar:"
# A date or list of dates. If there are multiple dates, ensure that there are 7 days in between each listed date.
# A "Back to Options" button and a "Log out" button
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function


# If you inputted "14" previously in self.p4 and pressed "Enter", please check that the page has the following:

# A Label that says "You wanted reminders every 14 days. Here are the dates you are reminded to spend. Please mark the following dates in your calendar:"
# A date or list of dates. If there are multiple dates, ensure that there are 14 days in between each listed date.
# A "Back to Options" button and a "Log out" button
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# If you inputted "30" previously in self.p4 and pressed "Enter", please check that the page has the following:

# A Label that says "You wanted reminders every 30 days. Here are the dates you are reminded to spend. Please mark the following dates in your calendar:"
# A date or list of dates. If there are multiple dates, ensure that there are 30 days in between each listed date.
# A "Back to Options" button and a "Log out" button
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# If you inputted "90" previously in self.p4 and pressed "Enter", please check that the page has the following:

# A Label that says "You wanted reminders every 90 days. Here are the dates you are reminded to spend. Please mark the following dates in your calendar:"
# A date or list of dates. If there are multiple dates, ensure that there are 90 days in between each listed date.
# A "Back to Options" button and a "Log out" button
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

""" Test Case #1 for threshold_reminders function: This is a test case to cover the fifth page (self.p5) of the tkinter GUI for
    finalproject326.py. We are testing this function to show that clicking the "Show thresholds passed" button works as expected.

    Returns:
        thresholds passed
"""
# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function and Test Case #1 for options function

# To test this function, please do the following:

# Input a number for "Dining Dollar Plan" on self.p1
# Input "0" for "Current Dining Dollar Balance" on self.p1
# Navigate to the options page (self.p3) and click the "Show thresholds passed"
# Check that it says "You have used up all of your dining dollars. Don't worry!"
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# Input a number for "Dining Dollar Plan" and a number for "Current Dining Dollar Balance" on self.p1 that corresponds to this equation: (balance - dining dollar plan)/dining dollar plan = a number from 0.75 to 0.99
# Navigate to the options page (self.p3) and click the "Show thresholds passed"
# Check that it says "You have passed the 25th, 50th, and 75th percentiles of total dining dollars in your plan. You have used up [a number from 0.75 to 0.99 (multipled by 100)]% of all of your dining dollars.
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# Input a number for "Dining Dollar Plan" and a number for "Current Dining Dollar Balance" on self.p1 that corresponds to this equation: (balance - dining dollar plan)/dining dollar plan = a number from 0.5 to 0.74
# Navigate to the options page (self.p3) and click the "Show thresholds passed"
# Check that it says "You have passed the 25th, and 50th percentiles of total dining dollars in your plan. You have used up [a number from 0.5 to 0.74 (multipled by 100)]% of all of your dining dollars.
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# Input a number for "Dining Dollar Plan" and a number for "Current Dining Dollar Balance" on self.p1 that corresponds to this equation: (balance - dining dollar plan)/dining dollar plan = a number from 0.5 to 0.49
# Navigate to the options page (self.p3) and click the "Show thresholds passed"
# Check that it says "You have passed the 25th percentile of total dining dollars in your plan. You have used up [a number from 0.25 to 0.49 (multipled by 100)]% of all of your dining dollars.
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function

# Input a number for "Dining Dollar Plan" and a number for "Current Dining Dollar Balance" on self.p1 that corresponds to this equation: (balance - dining dollar plan)/dining dollar plan = a number from 0 to 0.24
# Navigate to the options page (self.p3) and click the "Show thresholds passed"
# Check that it says "You have passed no remarkable thresholds of spent dining dollars in your plan yet. You have used up [a number from 0 to 0.24]% of all of your dining dollars.
# You can now either close out the GUI window and rerun the code to launch the GUI again, press "Back to Options" to test Test Case #1 for options, or press "Log out" to test Test Case #1 or Test Case #2 for get_user_info function


""" Test Case #1 for suggested_spending function: This is a test case to cover the sixth page of the tkinter GUI for
    finalproject326.py. We are testing this function to show that the output and buttons on this page work as expected.

Returns:
    A message letting users know how much money they could spend daily to spend their dining dollar balance.
    self.p1 if user clicks Log out button.
    self.p3 if user clicks Back to Options button.
 """

# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function and Test Case #1 for options function.

# Now, you should be on the options page. From here, click the "Get a suggested spending recommendation" button.
# This should take you to page 6 of the GUI. There is no input required for this page.

# To see if this test was successful, the GUI should load a message following this syntax: 
# ""If you were to spend money every day until your dining dollar plan expired, you would need to spend $___ daily."

# You can now either close out the GUI window and rerun the code to launch the GUI again or press the "Log out" or "Back to Options" buttons.
# If you press the "Log out" button, go to the Test Case #1 or #2 for get_user_info function. If you press the "Back to Options" button, go to the Test Case #1 for options function.



# These are all of the test cases we have written for the program. They cover all of the user functionality for this tkinter GUI.


