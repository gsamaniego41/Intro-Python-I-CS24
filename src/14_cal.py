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

date = datetime.now()

# input('14_cal.py:')

# check if there is an input
# if no args = return calendar for current month
# if 1 arg,
# exit

if len(sys.argv) == 1:
    print(calendar.month(date.year, date.month))
elif len(sys.argv) == 2:
    if len(sys.argv[1]) > 2 or int(sys.argv[1]) > 12:
        print('Pls enter the correct month format: 1-12')
    else:
        month = int(sys.argv[1])
        print(calendar.month(date.year, month))
elif len(sys.argv) == 3:
    if len(sys.argv[2]) > 4:
        print('Pls enter the correct year format: YYYY')
    else:
        month = int(sys.argv[1])
        year = int(sys.argv[2])
        print(calendar.month(year, month))
else:
    print(
        'Pls enter the correct format: [14_cal.py] [month (1-12)] [year (YYYY)]')
