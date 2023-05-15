import csv
import smtplib
import key
from twilio.rest import Client


class Library:
    def __init__(self, user, book, phno, email):
        self.email = key.my_email
        self.password = key.password
        self.user = user
        self.book = book
        self.phno = phno
        self.to_addr = email

    def send_email(self, message_file, borrow_date="", due_date=""):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            with open(f'messages/{message_file}.txt', 'r') as file:
                email_body = file.read()
                email_body = f"Subject:Your Recent Library Book Borrowing Activity\n\n{email_body}"
                email_body = email_body.replace('[Title of Book]', self.book).replace('[User]', self.user).replace(
                    '[Borrow Date]', borrow_date).replace('[Due Date]', due_date)
            connection.sendmail(from_addr=self.email, to_addrs=self.to_addr, msg=email_body)

        client = Client(key.account_sid, key.auth_token)

        client.messages.create(
            to=self.phno,
            from_=key.twilio_no,
            body=email_body,
        )

