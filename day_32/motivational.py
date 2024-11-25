import smtplib
from dotenv import load_dotenv
import os
import datetime as dt
import random

pwd = os.getcwd()

load_dotenv() 

APP_PASS = os.getenv("APP_PASS")

with open (f"{pwd}\\quotes.txt") as quotes_list:
    quotes = quotes_list.readlines()
    

my_email = "camdoesdata@gmail.com"

to_email = "cameronseamons@yahoo.com"

subject = "Monday Motivation"

# Randomly pick a quote to send
quote = random.choice(quotes)

message = f"{quote}"

def send_motivation():
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=APP_PASS)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=to_email, 
                msg = f"Subject:{subject}\n\n{message}"
                )
    except Exception as e:
        print(f"Error: {e}. Message not sent.")
      
    else:  
        print(f"Message Sent: \n {message}")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    send_motivation()
