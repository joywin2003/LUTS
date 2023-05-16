from tkinter import *
from tkinter import simpledialog, messagebox
import json
from PIL import ImageTk, Image
from profilecard import ProfileCard
from register import RegistrationPage


def registerPage():
    registration_page = RegistrationPage()
    registration_page.run_page()


def login():
    with open('users.json', 'r') as file:
        data = json.load(file)

    name = simpledialog.askstring("Login", "Enter your name:")
    if name:
        for user in data['User']:
            if user.get("name") == name:
                ProfileCard(name)
        else:
            messagebox.showinfo("Name not found.")
    else:
        messagebox.showinfo("No name entered.")


def run_homepage():
    root = Tk()
    root.title("Library Management System")

    root.geometry("600x400")

    library_img = Image.open("images/library.jpeg")
    library_img = library_img.resize((300, 150), Image.ANTIALIAS)
    library_img = ImageTk.PhotoImage(library_img)

    library_pic_label = Label(root, image=library_img, borderwidth=0, highlightthickness=0)
    library_pic_label.place(x=145, y=20)

    title_label = Label(root, text="Welcome to Library Management System", font=("Helvetica", 24), fg="#3F51B5")
    title_label.place(x=70, y=200)

    description_label = Label(root, text="Manage and keep track of all your books with ease.", font=("Helvetica", 12))
    description_label.place(x=165, y=250)

    register_button = Button(root, text="New Registration", font=("Helvetica", 14), bg="#4CAF50", fg="black",
                             command=registerPage)
    register_button.place(x=215, y=300)

    login_button = Button(root, text="Login", font=("Helvetica", 14), bg="#4CAF50", fg="black", command=login)
    login_button.place(x=250, y=330)

    # Run the GUI
    root.mainloop()
