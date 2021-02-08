"""A vaccination calculator."""

__author__ = "730287108"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population_size: int = int(input("Population: "))
doses_so_far: int = int(input("Doses administered: "))
dose_rate: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

current_percent_of_doses: float = (doses_so_far / 2) / population_size
percent_doses_still_needed: float = (target_percent / 100) - current_percent_of_doses
number_of_people_who_need_doses: float = percent_doses_still_needed * population_size
number_of_doses_needed: float = number_of_people_who_need_doses * 2
days_needed: int = round(number_of_doses_needed / dose_rate)

days_needed_timedelta: timedelta = timedelta(days_needed)
today: datetime = datetime.today()
target_date: datetime = today + days_needed_timedelta

print("We will reach " + str(target_percent) + "% " + "vaccination in " + str(days_needed) + " days, which falls on " + target_date.strftime("%B %d, %Y") + ".")  
