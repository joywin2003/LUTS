from tkinter import *
from tkinter import messagebox, simpledialog
from PIL import ImageTk, Image, ImageOps
import json
from register import Library

from PIL.ImageDraw import ImageDraw


class ProfileCard():
    # Create a window
    def __init__(self, name):
        self.name = name
        self.find_user()

    def borrow_book(self):
        global user
        with open('users.json', 'r') as file:
            data = json.load(file)
        for user_data in data['User']:
            if user_data['name'] == self.name:
                user = user_data
        if user["Title of Book"] == "No book borrowed" or user["Title of Book"] == "":
            book_title = simpledialog.askstring("Borrow Book", "Enter the book title:")
            if book_title:
                library = Library("users.json")
                library.add_user_info(user["ID"], user["name"], user["profile pic"], user["phno"], book_title,
                         user["email"], user["department"], user["college year"])
                self.book_title_value_label.config(text=book_title)
            else:
                messagebox.showinfo("Borrow Book", "No book title entered.")
        else:
            messagebox.showinfo("Return Book", "Please return the book before borrowing a new one.")

    def returnbook(self):
        global user
        with open('users.json', 'r') as file:
            data = json.load(file)
        for user_data in data['User']:
            if user_data['name'] == self.name:
                user = user_data
        if user["Title of Book"] != "No book borrowed":
            user["Title of Book"] = "No book borrowed"
            user["Borrow Date"] = ""
            user["Due Date"] = ""
            with open('users.json', 'w') as file:
                json.dump(data, file, indent=4)
            self.book_title_value_label.config(text="No book borrowed")
            self.borrow_date_value_label.config(text="")
            self.due_date_value_label.config(text="")
            messagebox.showinfo("Book Returned", "Thank you have a good day")
        else:
            messagebox.showinfo("No Books to Return", "There are currently no books borrowed.")

    def registerPage(self):
        self.root.destroy()
        import homepage

    def create_page(self, id, name, profile_pic, phno, book_title, email, department, college_year, borrow_date="",
                    due_date=""):
        self.root = Toplevel()
        self.root.title("User Profile Card")

        # Set the size of the window
        self.root.geometry("450x680")

        # Load and resize the profile picture
        self.profile_img = Image.open(profile_pic)
        self.profile_img = ImageOps.fit(self.profile_img, (150, 150), method=Image.LANCZOS)

        # Create a circular mask
        mask = Image.new("L", (150, 150), 0)
        draw = ImageDraw(mask)
        draw.ellipse((0, 0, 150, 150), fill=255)

        # Apply the circular mask to the profile image
        self.profile_img = ImageOps.fit(self.profile_img, (150, 150))
        self.profile_img.putalpha(mask)

        self.profile_img = ImageTk.PhotoImage(self.profile_img)

        profile_pic_label = Label(self.root, image=self.profile_img, borderwidth=0, highlightthickness=0)
        profile_pic_label.place(x=140, y=30)

        # Create a label for the name
        name_label = Label(self.root, text="Name:", font=("Helvetica", 16), fg="white")
        name_label.place(x=70, y=200)

        id_label = Label(self.root, text="ID:", font=("Helvetica", 16), fg="white")
        id_label.place(x=70, y=240)

        # Create a label for the email
        email_label = Label(self.root, text="Email:", font=("Helvetica", 16), fg="white")
        email_label.place(x=70, y=280)

        # Create a label for the phone number
        phone_label = Label(self.root, text="Phone:", font=("Helvetica", 16), fg="white")
        phone_label.place(x=70, y=320)

        book_title_label = Label(self.root, text="BookTitle:", font=("Helvetica", 16), fg="white")
        book_title_label.place(x=70, y=360)

        department_label = Label(self.root, text="Department:", font=("Helvetica", 16), fg="white")
        department_label.place(x=70, y=400)

        college_year_label = Label(self.root, text="College Year:", font=("Helvetica", 16), fg="white")
        college_year_label.place(x=70, y=440)

        name_value_label = Label(self.root, text=name, font=("Helvetica", 16), fg="#777")
        name_value_label.place(x=180, y=200)

        id_value_label = Label(self.root, text=id, font=("Helvetica", 16), fg="#777")
        id_value_label.place(x=180, y=240)

        # Create a label for the email value
        email_value_label = Label(self.root, text=email, font=("Helvetica", 16), fg="#777")
        email_value_label.place(x=180, y=280)

        # Create a label for the phone value
        phone_value_label = Label(self.root, text=phno, font=("Helvetica", 16), fg="#777")
        phone_value_label.place(x=180, y=320)

        self.book_title_value_label = Label(self.root, text=book_title, font=("Helvetica", 16), fg="#777")
        self.book_title_value_label.place(x=180, y=360)

        department_value_label = Label(self.root, text=department, font=("Helvetica", 16), fg="#777")
        department_value_label.place(x=180, y=400)

        year_value_label = Label(self.root, text=college_year, font=("Helvetica", 16), fg="#777")
        year_value_label.place(x=180, y=440)

        if borrow_date != "" and due_date != "":
            borrow_date_label = Label(self.root, text="Borrow Date:", font=("Helvetica", 16), fg="white")
            borrow_date_label.place(x=70, y=480)

            due_date_label = Label(self.root, text="Return Date:", font=("Helvetica", 16), fg="white")
            due_date_label.place(x=70, y=520)

            self.borrow_date_value_label = Label(self.root, text=borrow_date, font=("Helvetica", 16), fg="#777")
            self.borrow_date_value_label.place(x=180, y=480)

            self.due_date_value_label = Label(self.root, text=due_date, font=("Helvetica", 16), fg="#777")
            self.due_date_value_label.place(x=180, y=520)

        borrow_button = Button(self.root, text="Borrow a New Book", font=("Helvetica", 14), bg="#4CAF50", fg="black",
                               command=self.borrow_book)
        borrow_button.place(x=113, y=560)

        return_button = Button(self.root, text="Return a Book", font=("Helvetica", 14), bg="#4CAF50", fg="black",
                               command=self.returnbook)
        return_button.place(x=127, y=600)

        homepage_button = Button(self.root, text="Go to Homepage", font=("Helvetica", 14), bg="#4CAF50", fg="black",
                               command=self.registerPage)
        homepage_button.place(x=121, y=640)

        # Run the GUI
        self.root.mainloop()

    def find_user(self):
        global user
        with open('users.json', 'r') as file:
            data = json.load(file)
        for user_data in data['User']:
            if user_data['name'] == self.name:
                user = user_data
                break
        else:
            raise ValueError("User not found")
        self.create_page(user["ID"], user["name"], user["profile pic"], user["phno"], user["Title of Book"],
                         user["email"], user["department"], user["college year"], user["Borrow Date"], user["Due Date"])





