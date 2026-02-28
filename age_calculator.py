from datetime import datetime

greeting="Hello"
name=input("What is your name? ")
dob=input("What is your date of birth? (YYYY-MM-DD) ")
current_year = datetime.now().year
dob_year = int(dob.split("-")[0])
age = current_year - dob_year
age_in_months = age * 12
age_in_days = age * 365
print(f"{greeting}, {name}, you are {age} years old, {age_in_months} months old, and {age_in_days} days old.")