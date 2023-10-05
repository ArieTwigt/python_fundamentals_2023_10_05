#
from datetime import date

print("Welcome to the birthday calculator")

birthday_year  = int(input("Insert your birthday year:\n"))
birthday_month = int(input("Insert your birthday month:\n"))
birthday_day   = int(input("Insert your birthday day:\n"))

my_birthday_date = date(birthday_year, birthday_month, birthday_day)

# get the date of today
current_date = date.today()
current_year = current_date.year

# birthday this year
birthday_this_year = date(current_year, birthday_month, birthday_day)

# 
next_year = current_year + 1
birthday_next_year = date(next_year, birthday_month, birthday_day)

#
difference = (birthday_this_year - current_date)
difference_days = difference.days

# check if it is negative
if difference_days > 0:
    difference_days
    print(f"🎁 Your birthday is in {difference_days} days.")
else:
    difference_days
    difference = (current_date - birthday_this_year)
    difference_days = difference.days
    print(f"🎁 Your birthday is in {difference_days} days)
pass