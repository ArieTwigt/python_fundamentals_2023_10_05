#%% Assignment 1. - Create a conditional statement that indicates if your name starts with an "A or not

name = "Arie"

if name[0].lower() == 'a':
    print(f"Your name starts with an 'A': {name}")
else:
    print(f"Your name does not with an 'A': {name}")



#%% Assignment 2a.

vowels = ['a', 'e', 'i', 'u', 'o']

name = "Dirk"

first_letter = name[0]

if first_letter.lower() in vowels:
    print(name)
    new_name = name.replace(first_letter, "B")
    print(new_name)
else:
    print(name)
    new_name = name.replace(first_letter, "A")
    print(new_name)







# %% Assignment b. Random
import string
import random

# create the vowels and non-vowels
vowels = "aeoui"
letters = string.ascii_lowercase
non_vowels = [letter for letter in letters if letter not in vowels]

# get a random letter
name = "Arie"

first_letter = name[0]

if first_letter.lower() in vowels:
    random_letter = random.choice(non_vowels)
    new_name = name.replace(first_letter, random_letter.upper())
    print(f"{name} -> {new_name}")
else:
    random_letter = random.choice(vowels)
    new_name = name.replace(first_letter, random_letter.upper())
    print(f"{name} -> {new_name}")






#%% Assignment 3. - Create a conditional statement that indicates if your age is between 18 and 68.

age = 34


if 18 <= age <= 68:
    print("You are between 18 and 68")
else:
    print("You are not") 

# %%
if age >= 18 and age <= 68:
    print("You are between 18 and 68")
else:
    print("You are not") 


# %%
if age in range(18, 69):
    print("You are between 18 and 68")
else:
    print("You are not") 
# %%
