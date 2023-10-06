#%%
from datetime import date, datetime, timedelta


#%%
date.today()

# %%
datetime.now()

# %%
christmas_date = date(2023, 12, 25)
# %%
today_date = date.today()

# %%
difference = christmas_date - today_date
# %%
difference.days

# %%
today_date + timedelta(days=1045)


# %%
christmas_date.strftime("%A, %B year: %Y")

# %% isocalendar
christmas_date.isocalendar()[1]

# %%
christmas_date.day

#%% From string to date time
from datetime import datetime

my_date = "01-12-2023"

my_date_dt = datetime.strptime(my_date, "%m-%d-%Y")

my_date_dt
# %%
