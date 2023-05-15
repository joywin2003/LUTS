# LUTS - Library User Tracking System
LUTS (Library User Tracking System) is a Python application that allows libraries to track users and register borrowed books. The application sends reminders to users via SMS and email using the SMTP and Twilio API, respectively. It was built using Python's Tkinter library for the graphical user interface.

## Features
* User registration: users can register for borrowing books by providing their ID, name, phone number, and email address.
* Book registration: library staff can add new books to the system by providing the book's title, author, and other relevant information.
* Borrowing tracking: the system keeps track of which users have borrowed which books, and when the books are due to be returned.
* Automated reminders: the system can send automated SMS and email reminders to users when their books are due to be returned or when they are overdue.
* Integration with Twilio API: SMS reminders are sent using the Twilio API, which allows for easy and reliable messaging.
* Integration with SMTP protocol: email reminders are sent using the SMTP protocol, which is widely supported and easy to configure.

## Built With
Python 3.6+
Tkinter - Python's de-facto standard GUI (Graphical User Interface) package
SQLite - A lightweight relational database management system
Twilio API - A cloud communication platform that enables users to send and receive SMS and MMS messages using its web service APIs
SMTP (Simple Mail Transfer Protocol) - A protocol used for email transmission over the internet

## Acknowledgments
Special thanks to OpenAI for their excellent language model which helped in writing the readme file.
