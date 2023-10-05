#%% Assignment 1
full_name = "Erling Haaland"

full_name_new = f"{full_name} .Jr"

print(full_name_new)

# %% Assignment 2a.
full_name_short = full_name_new.replace("Erling", "E.")
print(full_name_short)

# %% Assignment 2b.
full_name_split = full_name_new.split(" ")
first_name = full_name_split[0]
last_name = full_name_split[1]
abbrv = full_name_split[2]
first_letter = first_name[0]
name_abbrv = f"{first_letter}."

full_name_new_abbrv = f"{name_abbrv} {last_name} {abbrv}"
print(full_name_new_abbrv)

# %%
nationality = "Norway"

sentence = f"{full_name_new_abbrv} -  Nationality: {nationality}"
print(sentence)
# %%
