import json
from messages import Library
import time
from datetime import datetime, timedelta
import homepage

with open('users.json', 'r') as file:
    data = json.load(file)

while True:
    for user_data in data['User']:
        library = Library(user_data['name'], user_data['Title of Book'], user_data['phno'], user_data['email'])

        due_date_str = user_data['precise due date']
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S.%f")
        days_until_due = (due_date - datetime.now()).days
        print(days_until_due)
        if days_until_due < 0:
            library.send_email(message_file="overdue", borrow_date=user_data["Borrow Date"], due_date=user_data["Due Date"])
            print("Book is overdue for user:", user_data['name'])
        elif days_until_due == 0:
            library.send_email(message_file="return", borrow_date=user_data["Borrow Date"], due_date=user_data["Due Date"])
            print("Reminder email sent for returning the book for user:", user_data['name'])
        elif days_until_due == 5:
            library.send_email(message_file="remainder", borrow_date=user_data["Borrow Date"], due_date=user_data["Due Date"])
            print("Reminder email sent for returning the book for user:", user_data['name'])

    time.sleep(86400)

