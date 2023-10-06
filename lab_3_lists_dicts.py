# list
my_list = list() # een bestaand object te "converteren" naar een list

my_list = []

my_list = ["Arie", 40, [1,2,3]]

# %%
my_list = []


# %%
my_list.append("Arie")
# %%
my_list.remove("Arie")

# %%
list_1 = [8, 1,2, 9,3,4,5]
list_2 = [2,6,7, 4, 58,9,0]

#%%
combined_list = list_1 + list_2 + list_1
print(combined_list)

# %%
my_unique_list = list(set(combined_list))

# %%
sorted(my_unique_list, reverse=True)
# %%
my_unique_list.sort(reverse=True)


# %%
ages_list = [11, 45, 23, 9, 50]


ages_list_filtered = [age * 100 for age in ages_list]

ages_list_filtered

# %%
my_car = {}

#%%
my_car["brand"] = "Nissan"
my_car["manufacturing_year"] = 1998
my_car["options"] = ['airco', 'abs', 'airbags', 'autopilot']

# %%
my_car
# %%
[x for x in my_car["options"] if "b" in x]


# %%
my_car


# %%
len(my_car['options'])

# %%
key_types = [type(my_car[x]) for x in my_car.keys()]
# %%
