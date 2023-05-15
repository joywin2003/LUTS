from tkinter import *
from PIL import ImageTk, Image, ImageOps

# Create a window
root = Tk()
root.title("User Profile Card")

# Set the size of the window
root.geometry("400x500")

# Load and resize the profile picture
profile_img = Image.open("images/profile.webp")
profile_img = ImageOps.fit(profile_img, (100, 100), method=Image.LANCZOS)
profile_img = ImageTk.PhotoImage(profile_img)

# Create a label for the profile picture
profile_pic_label = Label(root, image=profile_img, borderwidth=0, highlightthickness=0)
profile_pic_label.place(x=140, y=50)

# Create a label for the name
name_label = Label(root, text="Name:", font=("Helvetica", 16), fg="white")
name_label.place(x=70, y=200)

id_label = Label(root, text="ID:", font=("Helvetica", 16), fg="white")
id_label.place(x=70, y=240)

# Create a label for the email
email_label = Label(root, text="Email:", font=("Helvetica", 16), fg="white")
email_label.place(x=70, y=280)

# Create a label for the phone number
phone_label = Label(root, text="Phone:", font=("Helvetica", 16), fg="white")
phone_label.place(x=70, y=320)

# Create a label for the name value
name_value_label = Label(root, text="Gabimaru", font=("Helvetica", 16), fg="#777")
name_value_label.place(x=140, y=200)

id_value_label = Label(root, text="SE123432", font=("Helvetica", 16), fg="#777")
id_value_label.place(x=140, y=240)

# Create a label for the email value
email_value_label = Label(root, text="hellparadise@gmail.com", font=("Helvetica", 16), fg="#777")
email_value_label.place(x=140, y=280)

# Create a label for the phone value
phone_value_label = Label(root, text="555-555-5555", font=("Helvetica", 16), fg="#777")
phone_value_label.place(x=140, y=320)

# Create a button to borrow a new book
borrow_button = Button(root, text="Borrow a New Book", font=("Helvetica", 14), bg="#4CAF50", fg="black")
borrow_button.place(x=113, y=400)
borrow_button = Button(root, text="Return a Book", font=("Helvetica", 14), bg="#4CAF50", fg="black")
borrow_button.place(x=127, y=440)

# Run the GUI
root.mainloop()
