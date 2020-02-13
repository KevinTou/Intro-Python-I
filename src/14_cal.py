"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# if input == "":
# Render the calendar for the current month

# if only one argument (assume month)
# Render the calendar for the current year

# if two arguments (assume month and year)

# else:
# print a usage statement for the correct format

# exit

x = input(f"14_cal.py month [year]: ")


def get_calendar(user_input):
    # Creates a list from the user_input string
    month_year = user_input.split()

    # Set current month and year
    selected_month = datetime.now().month
    selected_year = datetime.now().year

    if len(month_year) > 2:
        print(f'Wrong format...\nExpecting 14_cal.py month [year]: MM YYYY')
    elif len(month_year) == 2:
        selected_month = int(month_year[0])
        selected_year = int(month_year[1])
        print(calendar.month(selected_year, selected_month))
    elif len(month_year) == 1:
        selected_month = int(month_year[0])
        print(calendar.month(selected_year, selected_month))
    else:
        print(calendar.month(selected_year, selected_month))


get_calendar(x)
