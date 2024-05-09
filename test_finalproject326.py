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


""" Test Case #1 for get_user_info function: This is a test case to cover the first page of the tkinter GUI for
    finalprojectGUI.py. We are testing this feature to show that the initial input section of our GUI work as
    expected. This specific test case tests for error handling on the first page.

Raises:
    ValueError: - Invalid date format for today's date.
    ValueError: - Invalid date format for ending date.
    ValueError: - Dining dollar plan must be a number greater than or equal to 0.
    ValueError: - Balance must be a number greater than or equal to 0.
 """

# First, run the finalproject326.py file.

# Once the GUI opens on your device, input the following information into the corresponding fields carefully:

# Name: Your first and last name in this format (First Last)

# Dining Dollar Plan: Any NEGATIVE integer or float.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Current Dining Dollar Balance: Any NEGATIVE integer or float.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Today's Date (MM/DD/YYYY): Leave this input box empty.

# Ending Date (MM/DD/YYYY): Leave this input box empty.

# To see if this test was successful, a window should pop up in the GUI listing the following statements:

# ValueError: - Invalid date format for today's date.
# ValueError: - Invalid date format for ending date.
# ValueError: - Dining dollar plan must be a number greater than or equal to 0.
# ValueError: - Balance must be a number greater than or equal to 0.

# You can now either close out the GUI window and rerun the code to launch the GUI again or delete the input in every field to continue testing.


""" Test Case #2 for get_user_info function: This is a test case to cover the first page of the tkinter GUI for
    finalprojectGUI.py. We are testing this feature to show that the initial input section of our GUI work as
    expected.

Returns:
    self.p2 after user clicks Proceed button.
 """

# First, run the finalproject326.py file.

# Once the GUI opens on your device, input the following information into the corresponding fields carefully:

# Name: Your first and last name in this format (First Last)

# Dining Dollar Plan: Any POSITIVE integer or float from this list (200, 300, 400). Any positive number value will work, but these are most likely to be inputted as these match the plans on the UMD website.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Current Dining Dollar Balance: Any POSITIVE integer or float. Do not put a larger number for balance than for dining dollar plan. You will receive an error message.
# NO STRINGS WILL WORK FOR THIS INPUT BOX!

# Today's Date (MM/DD/YYYY): Type in today's date in the format provided.

# Ending Date (MM/DD/YYYY): Type in any date in the future in the formate provided.

# To see if this test was successful, the GUI should load the next page which is a verification page for the inputted information. 
# The title of this page should be "Is this information correct?". The info on this page should also match the exact input you typed in previously.

# You can now either close out the GUI window and rerun the code to launch the GUI again or press the "Yes" or "No" buttons.
# If you press the "Yes" button, go to the Test Case #1 for options function. If you press the "No" button, go to the Test Case #1 for get_user_info function.


""" Test Case #1 for verification function: This is a test case to cover the second page of the tkinter GUI for
    finalprojectGUI.py. We are testing this feature to show that the output and buttons on this page work as expected.

Returns:
    self.p1 if user clicks No button.
    self.p3 if user clicks Yes button.
 """

# This test case assumes the code is already running and you have gone through either Test Case #1 or Test Case #2 for the get_user_info function.

# Once this verification page loads, please do the following:

# Check if the value for Name is the same that you previously inputted.

# Check if the value for Dining Dollar Plan is the same that you previously inputted.

# Check if the value for Balance is the same that you previously inputted.

# Check if the value for Today's Date (MM/DD/YYYY) is the same that you previously inputted.

# Check if the value for Ending Date (MM/DD/YYYY) is the same that you previously inputted.

# To see if this test was successful, the information on this verification page should be identical to what you inputted on the first page.

# You can now either close out the GUI window and rerun the code to launch the GUI again or press the "Yes" or "No" buttons.
# If you press the "Yes" button, go to the Test Case #1 for options function. If you press the "No" button, go to the Test Case #1 for get_user_info function.


""" Test Case #1 for options function: This is a test case to cover the third page of the tkinter GUI for
    finalprojectGUI.py. We are testing this feature to show that the  buttons on this page work as expected.

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

# To see if this test was successful, your GUI should finally show the first page which asks for input.

# You can now either close out the GUI window and rerun the code to launch the GUI again or delete the input in every field to continue testing.
