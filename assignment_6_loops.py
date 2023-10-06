#%% Assignment 1a - Create a loop that removes the vowels from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] .
# Add the results to a new list.
vowels = 'aeoui'

names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']
new_names_list = []


for name in names_list:
    # print the old name
    print(name)
    for letter in name:
        if letter in vowels:
            name = name.replace(letter, "")
    
    # print the new name
    print(name)
    # add the new name to the list
    new_names_list.append(name)



#%% Assignment 1b - Create a loop that removes the vowels from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] .
# Add the results to a new list.
vowels = 'aeoui'

names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']
new_names_list = []


for name in names_list:
    # print the old name
    print(name)
    new_name = ""
    for letter in name:
        if letter not in vowels:
            new_name += letter
    
    print(new_name)
    # print the new name
    print(name)
    # add the new name to the list
    new_names_list.append(name)


# %% Assignment 2 - Create a loop that prints the name of the day for the following 10 days
from datetime import date, timedelta
import locale

# in het nederlands
locale.setlocale(locale.LC_ALL, locale="nl_NL")

current_date = date.today()


for num_day in range(1, 11):
    next_date = current_date + timedelta(days=num_day)
    next_date_day = next_date.strftime("%A")
    print(next_date_day)


# %%
