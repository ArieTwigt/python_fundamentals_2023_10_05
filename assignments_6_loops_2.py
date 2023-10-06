#%%
names_list = ['Arie' ,'Jimmy', 'John', 'Marco', 'Danny', 'Peter']

new_names_list = []

vowels = 'aeouiy'

for name in names_list:
    for vowel in vowels:
        if vowel in name:
            name = name.replace(vowel, "")
    
    new_names_list.append(name)


#%%
new_names_list

# %%
names_list = ['Arie' ,'Jimmy', 'John', 'Marco', 'Danny', 'Peter']

new_names_list = []

vowels = 'aeouiy'

for name in names_list:
    new_name = ""
    for letter in name:
        if letter.lower() not in vowels:
            new_name += letter

    new_names_list.append(new_name)

# %%
from datetime import date, timedelta

current_date = date.today()


for day_num in range(1, 11):
    next_date = current_date + timedelta(days=day_num)
    next_day = next_date.strftime(f"Over {day_num} dagen is het: %A")
    print(next_day)



# %%
