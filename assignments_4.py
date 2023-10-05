#%% Assignment 1a
from datetime import date

birthday_date = date(2024, 4, 1)
today_date = date.today()
difference = birthday_date - today_date
difference_days = difference.days
print(f"My birthday is in {difference_days} days.")

#%% Assignment 1b.



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
os.path.isdir("my_script.py")
# %%
import os

current_files_folders = os.listdir()
file_or_folder = ["dir" if os.path.isdir() else "file" for x in current_files_folders ]

# %% create dict to indicate if it is a file or dir
dict_file_dirs = dict(zip(current_files_folders, file_or_folder))
dict_file_dirs

# %%
folder_name = "mijn_map"

current_files_folders = os.listdir()

if folder_name not in current_files_folders:
    os.mkdir("mijn_map")
else:
    print("Map bestaat al")

# %%
