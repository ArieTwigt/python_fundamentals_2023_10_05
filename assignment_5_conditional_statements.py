#%% Assignment 1. - Create a conditional statement that indicates if your name starts with an "A or not

name = "Arie"

if name[0].lower():
    print(f"Your name starts with an 'A': {name}")
else:
    print(f"Your name does not with an 'A': {name}")



#%% Assignment 2a.

vowels = "aeoui"

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
non_vowels = string.ascii_lowercase
non_vowels = [letter for letter in non_vowels if letter not in vowels]

# get a random letter
name = "Dirk"

first_letter = name[0]

if first_letter.lower() in vowels:
    random_letter = random.choice(vowels)
    new_name = name.replace(first_letter, random_letter.upper())
    print(f"{name} -> {new_name}")
else:
    random_letter = random.choice(non_vowels)
    new_name = name.replace(first_letter, random_letter.upper())
    print(f"{name} -> {new_name}")


#%% Assignment 3. -
