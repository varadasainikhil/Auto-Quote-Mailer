import datetime as dt
import smtplib
import random

current_day_time = dt.datetime.now()
today = current_day_time.weekday()

sender_mail = ""
sender_password = ""
receiver_mail = ""

if today == 0:
    with open("quotes.txt", "r") as file:
        list_of_quotes = file.readlines()
        quote_of_the_day = random.choice(list_of_quotes)
        print(quote_of_the_day)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Starts TLS encoding
        connection.login(user=sender_mail, password=sender_password)
        connection.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=f"Subject:MONDAY MOTIVATION \n\n{quote_of_the_day}")
