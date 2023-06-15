import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
import subprocess
import customtkinter
import sv_ttk

customtkinter.set_appearance_mode("Dark")

class User:
    def __init__(self, email, password, name, dob, pr_squat, pr_bench, pr_deadlift):
        self.email = email
        self.password = password
        self.name = name
        self.dob = dob
        self.pr_squat = pr_squat
        self.pr_bench = pr_bench
        self.pr_deadlift = pr_deadlift

    def save_to_database(self):
        print("jeandre")
        conn = sqlite3.connect("user_details.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (email, password, name, dob, pr_squat, pr_bench, pr_deadlift) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (self.email, self.password, self.name, self.dob, self.pr_squat, self.pr_bench, self.pr_deadlift)
        )
        conn.commit()
        conn.close()

def change_details():
    email = email_value_entry.get()
    password = password_value_entry.get()
    name = name_value_entry.get()
    dob = dob_value_entry.get()
    pr_squat = pr_squat_value_entry.get()
    pr_bench = pr_bench_value_entry.get()
    pr_deadlift = pr_deadlift_value_entry.get()

    conn = sqlite3.connect("user_details.db")
    cursor = conn.cursor()

    # Update the user's details based on their email
    cursor.execute(
        "UPDATE users SET password=?, name=?, dob=?, pr_squat=?, pr_bench=?, pr_deadlift=? WHERE email=?",
        (password, name, dob, pr_squat, pr_bench, pr_deadlift, email)
    )

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

# Print the rows
    for row in rows:
        print(row)
# Close the connection
    conn.commit()
    conn.close()

# Save the changes to the database
    User(email, password, name, dob, pr_squat, pr_bench, pr_deadlift).save_to_database()

    # Clear the entry fields
    email_value_entry.delete(0, END)
    password_value_entry.delete(0, END)
    name_value_entry.delete(0, END)
    dob_value_entry.delete(0, END)
    pr_squat_value_entry.delete(0, END)
    pr_bench_value_entry.delete(0, END)
    pr_deadlift_value_entry.delete(0, END)


# Rest of the code remains the same...

#menu defs
def go_to_homepage():
    root.destroy()
    subprocess.Popen(["python", "Program_Home_page.py"])

def go_to_datapage():
    root.destroy()
    subprocess.Popen(["python", "Program_Data_page.py"])

def go_to_informationpage():
    root.destroy()
    subprocess.Popen(["python", "Program_Information_page.py"])


####### GUI code #######

root = Tk()
root.geometry("640x960")
root.title("Data page")
root.resizable(width=False, height=False)

background_image = tk.PhotoImage(file="assets/Project Walpaper.png")
background_label = ttk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

info_title = ttk.Label(root, text="Your Info:", font=("Helvetica", 30))  # underline
info_title.grid(row=0, column=1, columnspan=3, padx=25, pady=20, sticky="NW")

data_frame = ttk.LabelFrame(root)
data_frame.grid(row=1, column=0, columnspan=3, padx=10)

name_label = ttk.Label(data_frame, text="Name:", font=("Helvetica", 16))
name_label.grid(row=0, column=0, padx=30, pady=10)

email_label = ttk.Label(data_frame, text="Email:", font=("Helvetica", 16))
email_label.grid(row=1, column=0, padx=30, pady=10)

password_label = ttk.Label(data_frame, text="Password:", font=("Helvetica", 16))
password_label.grid(row=2, column=0, padx=30, pady=10)

dob_label = ttk.Label(data_frame, text="Date of Birth:", font=("Helvetica", 16))
dob_label.grid(row=3, column=0, padx=30, pady=10)

pr_squat_label = ttk.Label(data_frame, text="PR Squat:", font=("Helvetica", 16))
pr_squat_label.grid(row=4, column=0, padx=30, pady=10)

pr_bench_label = ttk.Label(data_frame, text="PR Bench:", font=("Helvetica", 16))
pr_bench_label.grid(row=5, column=0, padx=30, pady=10)

pr_deadlift_label = ttk.Label(data_frame, text="PR Deadlift:", font=("Helvetica", 16))
pr_deadlift_label.grid(row=6, column=0, padx=30, pady=10)

name_value_entry = ttk.Entry(data_frame)
name_value_entry.grid(row=0, column=1, padx=20)

email_value_entry = ttk.Entry(data_frame)
email_value_entry.grid(row=1, column=1, padx=20)

password_value_entry = ttk.Entry(data_frame)
password_value_entry.grid(row=2, column=1, padx=20)

dob_value_entry = ttk.Entry(data_frame)
dob_value_entry.grid(row=3, column=1, padx=20)

pr_squat_value_entry = ttk.Entry(data_frame)
pr_squat_value_entry.grid(row=4, column=1, padx=20)

pr_bench_value_entry = ttk.Entry(data_frame)
pr_bench_value_entry.grid(row=5, column=1, padx=20)

pr_deadlift_value_entry = ttk.Entry(data_frame)
pr_deadlift_value_entry.grid(row=6, column=1, padx=20)

importance_frame = ttk.LabelFrame(root)
importance_frame.grid(row=2, column=0, columnspan=3, pady=10, padx=38)

importance_label = ttk.Label(importance_frame, text="Importance:", font=("Helvetica", 16))
importance_label.grid(row=0, column=0, columnspan=1, padx=10, pady=10)

# Create a variable to hold choice in
preference_choice = StringVar()

# Create the different choices of the radio button
radio_button_strength = ttk.Radiobutton(importance_frame, text="Want to improve my overall strength in the gym!",
                                        variable=preference_choice, value="Option 1")
radio_button_strength.grid(row=0, column=3, padx=10, pady=10, sticky="NW")

radio_button_recovery = ttk.Radiobutton(importance_frame, text="Want to recover from a recent injury!",
                                        variable=preference_choice, value="Option 2")
radio_button_recovery.grid(row=1, column=3, padx=10, pady=10, sticky="NW")

radio_button_endurance = ttk.Radiobutton(importance_frame,
                                         text="Want to improve my muscular endurance through longer sets!",
                                         variable=preference_choice, value="Option 3")
radio_button_endurance.grid(row=2, column=3, padx=10, pady=10, sticky="NW")

# submit button
change_button = customtkinter.CTkButton(root, text="Change", command=change_details, fg_color=("black", "black"))
change_button.grid(row=3, column=1, columnspan=3, pady=20, padx=80, sticky="W")

# menu
menu_frame = ttk.Frame(root)
menu_frame.grid(sticky="S", columnspan=1, column=1, row=5, pady=25)

# Load the images for the menu items
data_image1 = Image.open("assets/Data logo menu.png")
data_image1 = data_image1.resize((40, 40))
data_photo1 = ImageTk.PhotoImage(data_image1)

home_image2 = Image.open("assets/DDT logo homepage.png")
home_image2 = home_image2.resize((40, 40))
home_photo2 = ImageTk.PhotoImage(home_image2)

information_image3 = Image.open("assets/Information logo menu.png")
information_image3 = information_image3.resize((40, 40))
information_photo3 = ImageTk.PhotoImage(information_image3)

# Create menu buttons with images
button1 = ttk.Button(menu_frame, image=data_photo1, command=go_to_datapage)
button1.grid(column=0, row=0)

button2 = ttk.Button(menu_frame, image=home_photo2, command=go_to_homepage)
button2.grid(column=1, row=0)

button3 = ttk.Button(menu_frame, image=information_photo3, command=go_to_informationpage)
button3.grid(column=2, row=0)

root.mainloop()
