import requests
from datetime import datetime
import smtplib
import yaml
import time

MY_LAT = 38.635360  # Your latitude
MY_LONG = -90.200990  # Your longitude


def iss_in_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_latitude <= iss_latitude


# Your position is within +5 or -5 degrees of the ISS position.

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.
    # BONUS: run the code every 60 seconds.

    return time_now >= sunset or time_now <= sunrise

searching = True

while searching:
    time.sleep(3000)
    if iss_in_position() and is_night():
        with open('config.yml', 'r') as f:
            cfg = yaml.safe_load(f)

        my_email = "derbaktest@gmail.com"
        password = cfg['email']['password'][1]
        test_email = "andrewderbak@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:  # create an SMTP object
            # smtp.mail.yahoo.com
            connection.starttls()  # Start secure encryption
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=test_email,
                msg=f"Subject:ISS is close!\n\nThe ISS is now flying overhead! You should be able to see it with your telescope!"
            )
        searching = False
