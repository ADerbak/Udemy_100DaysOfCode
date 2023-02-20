import smtplib
import yaml
with open('config.yml','r') as f:
    cfg = yaml.safe_load(f)

my_email = "derbaktest@gmail.com"
password = cfg['email']['password'][1]
test_email = "derbaktest@yahoo.com"

connection = smtplib.SMTP("smtp.gmail.com") # create an SMTP object
#smtp.mail.yahoo.com

connection.starttls() # Start secure encryption
connection.login(user=my_email, password= password)
connection.sendmail(from_addr=my_email, to_addrs=test_email, msg = "Subject:Hello!\n\nThis is the body of my email")
connection.close()