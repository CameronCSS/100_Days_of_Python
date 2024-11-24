import smtplib
from dotenv import load_dotenv
import os

pwd = os.getcwd()

load_dotenv() 

APP_PASS = os.getenv("APP_PASS")


# Use correct port for smtp
smtplib.SMTP("smtp.gmail.com", port=587)


# Check pass was pulled from .env file
print(APP_PASS)
