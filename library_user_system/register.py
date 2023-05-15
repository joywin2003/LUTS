import json
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog,messagebox
import random
import string



class Library:
    def __init__(self, filename):
        self.filename = filename

    def add_user_info(self, id, name, profile_pic, phno, book_title, email, department, college_year):
        # Get current date and time
        time_now = datetime.now()
        borrow_date = time_now.strftime("%d-%m-%Y")
        due_date = (time_now + timedelta(days=7)).strftime("%d-%m-%Y")
        precise_borrow_date = str(time_now)
        precise_due_date = str(time_now + timedelta(days=7))

        # Create dictionary for user information
        user_info = {
            "ID": id,
            "name": name,
            "profile pic": profile_pic,
            "phno": phno,
            "Title of Book": book_title,
            "email": email,
            "department": department,
            "college year": college_year,
            "Borrow Date": borrow_date,
            "Due Date": due_date,
            "precise borrow date": precise_borrow_date,
            "precise due date": precise_due_date,
        }

        # Load existing JSON file and append new user information
        with open(self.filename, 'r') as file:
            data = json.load(file)
        data['User'].append(user_info)

        # Write updated JSON file
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

        print("User information saved to", self.filename)

def nextPage():
    root.destroy()
    import homepage

def generate_student_id():
    # Define the length of the student ID
    id_length = 6

    # Generate a random alphanumeric ID
    student_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=id_length))

    # Add 'SE' as the initial characters
    student_id = 'SE' + student_id

    return student_id


def select_profile_pic():
    filetypes = (("Image files", "*.png *.jpg *.jpeg"), ("All files", "*.*"))
    profile_pic_path = filedialog.askopenfilename(filetypes=filetypes)
    profile_pic_entry.delete(0, tk.END)
    profile_pic_entry.insert(0, profile_pic_path)


def register():
    name = name_entry.get()
    profile_pic = profile_pic_entry.get()
    email = email_entry.get()
    phone_number = phone_number_entry.get()
    department = department_entry.get()
    college_year = college_year_entry.get()
    book_title = book_title_entry.get()

    # Perform registration logic here

    # Clear input fields after registration
    name_entry.delete(0, tk.END)
    profile_pic_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)
    college_year_entry.delete(0, tk.END)
    book_title_entry.delete(0, tk.END)
    library = Library("users.json")
    student_id = generate_student_id()
    library.add_user_info(student_id, name, profile_pic, phone_number, book_title, email, department, college_year)
    messagebox.showinfo("Registration", f"Registration Complete your ID is {student_id}")
    file_path = "homepage.py"
    nextPage()

root = tk.Tk()
root.title("LUTS")

# Set window size and position
window_width = 400
window_height = 350
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create frame
frame = tk.Frame(root)
frame.pack(pady=20)

# Create title label inside frame
title_label = tk.Label(frame, text="New Registration", font=("Arial", 24), fg="red")
title_label.grid(row=0, columnspan=4, pady=15)

# Create and arrange labels
name_label = tk.Label(frame, text="Name:")
name_label.grid(row=1, column=0, sticky=tk.W)

profile_pic_label = tk.Label(frame, text="Profile Pic:")
profile_pic_label.grid(row=2, column=0, sticky=tk.W)

email_label = tk.Label(frame, text="Email:")
email_label.grid(row=3, column=0, sticky=tk.W)

phone_number_label = tk.Label(frame, text="Phone Number:")
phone_number_label.grid(row=4, column=0, sticky=tk.W)

department_label = tk.Label(frame, text="Department:")
department_label.grid(row=5, column=0, sticky=tk.W)

college_year_label = tk.Label(frame, text="College Year:")
college_year_label.grid(row=6, column=0, sticky=tk.W)

book_title_label = tk.Label(frame, text="Title of Book:")
book_title_label.grid(row=7, column=0, sticky=tk.W)

# Create and arrange entry fields
name_entry = tk.Entry(frame)
name_entry.grid(row=1, column=1)

profile_pic_entry = tk.Entry(frame)
profile_pic_entry.grid(row=2, column=1)

profile_pic_button = tk.Button(frame, text="Select", command=select_profile_pic)
profile_pic_button.grid(row=2, column=2)

email_entry = tk.Entry(frame)
email_entry.grid(row=3, column=1)

phone_number_entry = tk.Entry(frame)
phone_number_entry.grid(row=4, column=1)

department_entry = tk.Entry(frame)
department_entry.grid(row=5, column=1)

college_year_entry = tk.Entry(frame)
college_year_entry.grid(row=6, column=1)

book_title_entry = tk.Entry(frame)
book_title_entry.grid(row=7, column=1)

# Create register button
register_button = tk.Button(root, text="Register", command=register)
register_button.pack(pady=10)

root.mainloop()



