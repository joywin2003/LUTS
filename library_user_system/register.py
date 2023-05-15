import json
from datetime import datetime, timedelta


class Library:
    def __init__(self, filename):
        self.filename = filename

    def add_user_info(self, name, phno, book_title, email):
        # Get current date and time
        time_now = datetime.now()
        borrow_date = time_now.strftime("%d-%m-%Y")
        due_date = (time_now + timedelta(days=7)).strftime("%d-%m-%Y")
        precise_borrow_date = str(time_now)
        precise_due_date = str(time_now + timedelta(days=7))

        # Create dictionary for user information
        user_info = {
            "name": name,
            "phno": phno,
            "Title of Book": book_title,
            "email": email,
            "Borrow Date": borrow_date,
            "Due Date": due_date,
            "precise borrow date": precise_borrow_date,
            "precise due date": precise_due_date
        }

        # Load existing JSON file and append new user information
        with open(self.filename, 'r') as file:
            data = json.load(file)
        data['User'].append(user_info)

        # Write updated JSON file
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

        print("User information saved to", self.filename)


# Example usage
# lib = Library('users.json')
# lib.add_user_info("Joywin Bennis", "+919353708447", "Fuck You", "joywinbennis0987@gmail.com")
