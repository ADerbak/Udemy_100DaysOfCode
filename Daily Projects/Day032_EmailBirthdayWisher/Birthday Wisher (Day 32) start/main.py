import smtplib
import yaml
import datetime as dt
import random


with open('config.yml','r') as f:
    cfg = yaml.safe_load(f)

my_email = "derbaktest@gmail.com"
password = cfg['email']['password'][1]
test_email = "derbaktest@yahoo.com"

if dt.datetime.now().weekday() == 6:
    with open('quotes.txt', 'r') as f:
        quotes = f.readlines()

    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection: # create an SMTP object
    #smtp.mail.yahoo.com
        connection.starttls() # Start secure encryption
        connection.login(user=my_email, password= password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=test_email,
            msg = f"Subject:Your Monday Motivation!\n\n{quote}"
        )
