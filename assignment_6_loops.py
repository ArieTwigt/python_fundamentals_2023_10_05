#%% Assignment 1 - Create a loop that removes the vowels from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] .
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
    

# %% Assignment 2 - Create a loop that prints the name of the day for the following 10 days


