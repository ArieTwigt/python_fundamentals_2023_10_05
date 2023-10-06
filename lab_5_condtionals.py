#%%
age = 15
name = "Dirk"
woonplaats = "Enschede"

if age >= 18:
    # code voor True
    print("🍺 Proost")
    print("Nog een regel")
elif name == "Arie":
    print("Dan wel")
elif woonplaats == "Enschede":
    print("Toch maar wel")
else:
    # als het bovenstaande niet True is
    print("Helaas")

print("De rest van de code")


# %%
guests_list = ['Jim', 'James', 'Job']

#%%
name = input("Insert name:\n")

if name in guests_list:
    print("Welcome")
elif name[0].lower() == 'j':
    if name != "Jimmy":
        print("Your name starts with a 'j', welcome")
        guests_list.append(name)
else:
    print("Unfortunately")


#%%
name = "Arie"

if 'r' in name:
    print("Contains 'r'")

# %%
if age > 16 and name == 'Dirk':
    print("Yes")


# %%
donations = 0

donation_amount = 50

donation_limit = 500

while donations <= donation_limit:
    print("Donated")
    
    donations += donation_amount
    print(donations)

# %%

# %%
