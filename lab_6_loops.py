#%%
flower_list = ['lily', 'gerbera', 'tulip', 'rose', 'orchid']

#%%
for flower in flower_list:
    print(flower.upper())

# %% 
for index, value in enumerate(flower_list):
    print(index)
    print(value)
    print(f"{value} staat op plek {index}")

# %%

flower_list = ['lily', 'gerbera', 'tulip', 'rose', 'orchid']

flower_list_upper = []


#%%
for flower in flower_list:
    flower_upper = flower.upper()
    flower_list_upper.append(flower_upper)

# %%
exlude_flowers = ['lily']
flower_list_upper_2 = [flower
                       if flower not in flower_list else "Arie"
                       for flower in flower_list ]

flower_list_upper_2
# %% random list of 20 numbers
numbers_list = [10, 4, 5, 7, 10, 2, 4, 8, 4, 1]

numbers_list_filtered = [number for number in numbers_list if number > 5]

numbers_list_filtered

#%%
flower_list = ['lily', 'gerbera', 'tulip', 'rose', 'orchid']

for flower in flower_list:
    print(flower)
    for letter in flower:
        print(letter)
        print("-"*10)

# %%
