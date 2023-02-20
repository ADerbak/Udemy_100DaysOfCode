import smtplib

import pandas as pd
import yaml
import datetime as dt
import random


with open('config.yml','r') as f:
    cfg = yaml.safe_load(f)

my_email = "derbaktest@gmail.com"
password = cfg['email']['password'][1]
test_email = "derbaktest@yahoo.com"
letters = ['letter_1.txt', 'letter_2.txt','letter_3.txt']


df = pd.read_csv('birthdays.csv')
birthdays = df.to_dict(orient='records')

for row in birthdays:

    if dt.datetime.now().month == row['month'] and dt.datetime.now().day == row['day']:
        letter_template = random.choice(letters)
        with open(letter_template, 'r') as f:
             letter = f.read()
             letter = letter.replace('[NAME]', row['name'])
        # quote = random.choice(quotes)

        with smtplib.SMTP("smtp.gmail.com") as connection: # create an SMTP object
        #smtp.mail.yahoo.com
            connection.starttls() # Start secure encryption
            connection.login(user=my_email, password= password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=test_email,
                msg = f"Subject:Happy Birthday!\n\n{letter}"
            )
