import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random
import pandas as pd

pwd = os.getcwd()

load_dotenv() 

APP_PASS = os.getenv("APP_PASS")

with open (f"{pwd}\\wishes.txt") as wish_list:
    wishes = wish_list.readlines()
    
birthdays = pd.read_csv(f"{pwd}\\birthdays.csv")


my_email = "camdoesdata@gmail.com"

subject = "Happy Birthday!"

# Randomly pick a birthday wish to send
wish = random.choice(wishes)


def birthday_email(name, email):
    global subject
    
    if email == None:
        # If I dont have the persons email and ONLY their birthday. Remind myself to wish them happy birthday
        email = my_email
        subject = f"{name}'s Birthday Today"
        message = f"Remember to tell '{name}' Happy Birthday Today. \n\nBirthday Message:\n{wish} "
    else:
        name = name.strip().split()[0]
        message = f"{name}, \n {wish} \n\n Love, \n\n Cameron"
        
    # Use correct port for smtp
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=APP_PASS)
        connection.sendmail(
            from_addr=my_email,
                to_addrs=email, 
            msg = f"Subject:{subject}\n\n{message}"
            )

now = dt.datetime.now()
month = now.month
day = now.day

# Check for birthdays today
birthday_today = birthdays[(birthdays['month'] == month) & (birthdays['day'] == day)]


if not birthday_today.empty:
    # If there are birthdays today, send birthday emails
    for index, row in birthday_today.iterrows():
        name = row['name']
        email = row['email']
        
        # If I dont have their email just send ME a reminder
        if pd.isna(email) or email == '':
            email = None
        birthday_email(name, email)
        
else:
    print("No Birthdays Today!")


