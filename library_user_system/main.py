import json
from messages import Library
import time
from datetime import datetime, timedelta

# Load user data from JSON file
with open('users.json', 'r') as file:
    data = json.load(file)

# Find user in data by name
username = "Joywin"
for user_data in data['User']:
    if user_data['name'] == username:
        user = user_data
        break
else:
    raise ValueError("User not found")

# Initialize library object with user data
library = Library(user['name'], user['Title of Book'], user['phno'], user["email"])

# Calculate remaining days until due date
due_date_str = user['precise due date']
due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S.%f")
days_until_due = (due_date - datetime.now()).days
print(datetime.now())
while True:
    print(days_until_due)
    # Check if book is overdue or due soon
    if days_until_due < 0:
        library.send_email(message_file="overdue",borrow_date=user["Borrow Date"],due_date=user["Due Date"])
        print("Book is overdue!")
    elif days_until_due == 0:
        library.send_email(message_file="return",borrow_date=user["Borrow Date"],due_date=user["Due Date"])
        print("Reminder email sent for returning the book1")
    elif days_until_due == 2:
        library.send_email(message_file="remainder",borrow_date=user["Borrow Date"],due_date=user["Due Date"])
        print("Reminder email sent for returning the book")

    # Sleep for a day before running the code again
    time.sleep(86400)
