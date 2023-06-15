####### Imports #######
import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import Image, ImageDraw, ImageTk
import subprocess
from tkinter import messagebox
import customtkinter
import sqlite3
import sv_ttk

customtkinter.set_appearance_mode("Dark")

####### Class Code #######

class User:
    def __init__(self, email, password, name, dob):
        self.email = email
        self.password = password
        self.name = name
        self.dob = dob
# ...

def error_login():
    messagebox.showerror('Login Error', 'Error: Login or password are incorrect!')

def login():
    email = email_entered.get().strip()
    password = password_entred.get().strip()

    # Establish a connection to the database
    conn = sqlite3.connect('user_details.db')
    # Create a cursor object
    cursor = conn.cursor()

    # Execute an SQL statement to retrieve the user details for the entered email
    cursor.execute("SELECT email, password FROM users WHERE email=?", (email,))
    user = cursor.fetchone()  # Retrieve the first matching row

    if user is not None:
        stored_email, stored_password = user

        print(f"Entered email: {email}")
        print(f"Entered password: {password}")
        print(f"Stored email: {stored_email}")
        print(f"Stored password: {stored_password}")

        if password == stored_password:
            print("Login successful")
            root.destroy()
            subprocess.Popen(["python", "Program_Home_page.py"])
        else:
            error_login()
    else:
        error_login()

    # Close the connection
    conn.close()

def sign_up():
    email = email_entry_signup.get()
    password = password_entry_signup.get()
    name = name_entry_signup.get()
    dob = dob_entry_signup.get()

    # Establish a connection to the database
    conn = sqlite3.connect('user_details.db')
    # Create a cursor object
    cursor = conn.cursor()
    # Execute an SQL statement to create a table
    cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT, name TEXT, dob TEXT, pr_squat INTEGER DEFAULT 0, pr_bench INTEGER DEFAULT 0, pr_deadlift INTEGER DEFAULT 0)")

    # Execute SQL statement to insert user details
    cursor.execute("INSERT INTO users (email, password, name, dob) VALUES (?, ?, ?, ?)", (email, password, name, dob))

    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()

    root.destroy()
    subprocess.Popen(["python", "Program_Home_page.py"])

    # Establish a connection to the database
    workouts = [
    ('Calf Raises', 'Legs', 15, 50, 4),
    ('Leg-Press', 'Legs', 12, 180, 3),
    ('Squat', 'Legs', 15, 80, 4),
    ('Walking Lunges', 'Legs', 15, 30, 4),
    ('Leg Extension', 'Legs', 15, 30, 5),
    ('Hack Squat', 'Legs', 12, 60, 4),
    ('Romanian Deadlift', 'Legs', 8, 40, 4),
    ('Deadlift', 'Legs', 8, 100, 3),
    ('Hamstring Curl', 'Legs', 15, 30, 4),
    ('Bicep Curl', 'Arms', 15, 25, 4),
    ('Ben-Over Rows', 'Arms', 12, 20, 4),
    ('Hammer Curl', 'Arms', 15, 20, 5),
    ('Dips', 'Arms', 12, 0, 3),
    ('Push-Downs', 'Arms', 15, 30, 4),
    ('Tricep Extension', 'Arms', 15, 15, 3),
    ('Shoulder Press', 'Arms', 12, 20, 4),
    ('Lateral Raises', 'Arms', 8, 10, 3),
    ('Incline Bicep Curl', 'Arms', 12, 10, 4),
    ('Pull-Ups', 'Arms', 15, 0, 4),
    ('Bench-Press', 'Chest', 12, 25, 4),
    ('Chest-Fly', 'Chest', 15, 25, 4),
    ('Push-Ups', 'Chest', 30, 25, 3),
    ('Cable Crossovers', 'Chest', 12, 25, 4),
    ('Tricep Extension', 'Chest', 12, 25, 4),
    ('Chest Dip', 'Chest', 15, 25, 4),
    ('Overhead Press', 'Chest', 12, 25, 4),
    ('Wide Grip Bench-Press', 'Chest', 12, 25, 4),
    ('Decline Push-Ups', 'Chest', 30, 25, 2)
]

# Establish a connection to the database
    conn = sqlite3.connect('workouts.db')
# Create a cursor object
    cursor = conn.cursor()
# Execute an SQL statement to create a table
    cursor.execute("CREATE TABLE IF NOT EXISTS workouts (id INTEGER PRIMARY KEY, name TEXT, type TEXT, reps INTEGER, weight INTEGER, sets INTEGER)")

# Execute SQL statement to insert workouts
    cursor.executemany("INSERT INTO workouts (name, type, reps, weight, sets) VALUES (?, ?, ?, ?, ?)", workouts)

# Commit the changes
    conn.commit()
# Close the connection
    conn.close()

    user = User(email, password, name, dob)
    user.save_to_file()
    root.destroy()
    subprocess.Popen(["python","Program_Home_page.py"])


####### GUI code #######

root = Tk()
root.geometry("640x960")
root.title("Login/Sign-up page")
root.resizable(width=False, height=False)
sv_ttk.set_theme("dark")

background_image = tk.PhotoImage(file="assets/Project Walpaper.png")
background_label = ttk.Label(root, image=background_image)
background_label.place(x=0, y=0,relwidth=1,relheight=1)



logo_image = tk.PhotoImage(file="assets/DDT Wireframe Homepage.png")
logo_label = ttk.Label(root, image=logo_image)
logo_label.grid(row=0, column= 1, columnspan=2, pady = 50, padx = "220")


top_frame = LabelFrame(root, text="Login")
top_frame.grid(row=7, column=1, padx=10, pady=10, sticky="N",columnspan=4)

email_label = ttk.Label(top_frame, text = "Email:", wraplength=250)
email_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
email_entered = StringVar()

email_entry = ttk.Entry(top_frame, textvariable = email_entered)
email_entry.grid(row=3, column=0, columnspan=2,padx=5, pady=5, ipadx = 45)

password_label = ttk.Label(top_frame, text = "Password:",wraplength=250)
password_label.grid(row=4, column=0, columnspan =2, padx=5, pady=5, rowspan=1)
password_entred = StringVar()

password_entry = ttk.Entry(top_frame, textvariable = password_entred, show="*")
password_entry.grid(row=5, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

#command 
login_radio_button =customtkinter.CTkButton(top_frame, text="Login", command=login, fg_color=("black", "black"))
login_radio_button.grid(row=6, column=0 ,pady=10, columnspan=2 )

bottom_frame = ttk.LabelFrame(root, text="Sign-Up")
bottom_frame.grid(row=10, column=1, pady=10, sticky="N", padx=220)

email_label_signup = ttk.Label(bottom_frame, text = "Email:", wraplength=250)
email_label_signup.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
email_entered_signup = StringVar()

email_entry_signup = ttk.Entry(bottom_frame, textvariable = email_entered_signup)
email_entry_signup.grid(row=1, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

password_label_signup = ttk.Label(bottom_frame, text = "Password:", wraplength=250)
password_label_signup.grid(row=2, column=0, columnspan =2, padx=5, pady=5)
password_entred_signup = StringVar()

password_entry_signup = ttk.Entry(bottom_frame, textvariable = password_entred_signup, show="*")
password_entry_signup.grid(row=3, column=0, columnspan =2, padx=5, pady=5, ipadx = 45)

name_label_signup = ttk.Label(bottom_frame,text="Name:", wraplength=250)
name_label_signup.grid(row=4 ,column=0, columnspan =2, padx=5, pady = 5)
name_entered_signup = StringVar()

name_entry_signup = ttk.Entry(bottom_frame, textvariable=name_entered_signup)
name_entry_signup.grid(row=5, column=0, padx= 5, pady =5 , ipadx = 45)

dob_label_signup = ttk.Label(bottom_frame,text="Date of birth:", wraplength=250)
dob_label_signup.grid(row=6 ,column=0, columnspan =2, padx=5, pady = 5)
label_under_dob = ttk.Label(bottom_frame, text="Day/Month/Year", font=("Helvetica", 12))
label_under_dob.grid(row = 7, pady=4)

# Change the font size of the label's text
label_under_dob.config(font=("Helvetica",8))
dob_entered_signup = StringVar()

dob_entry_signup = ttk.Entry(bottom_frame, textvariable=dob_entered_signup)
dob_entry_signup.grid(row=8, column=0, padx= 5, pady =5 , ipadx = 45)

#command 
signup_button = customtkinter.CTkButton(bottom_frame, text="Sign-Up", command=sign_up,  fg_color=("black", "black"))
signup_button.grid(row=9, column=0 ,pady=10, columnspan=2 )

root.mainloop()

