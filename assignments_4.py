#%% Assignment 1
from datetime import date

birthday_date = date(2024, 4, 1)
today_date = date.today()
difference = birthday_date - today_date
difference_days = difference.days
print(f"My birthday is in {difference_days} days.")

# %% Assignment 2
from math import pow, pi

diameter = 10
radius = diameter / 2
size = pow(radius, 2) * pi
size_rounded = round(size, 2)
print(size_rounded)

# %% Assignment 3
import os

current_files_folders = os.listdir()
print(current_files_folders)

# %% Assignment 4
os.mkdir("our_functions")
# %%
