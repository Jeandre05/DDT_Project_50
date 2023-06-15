import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
import sqlite3
import subprocess
import customtkinter
import sv_ttk
import random

customtkinter.set_appearance_mode("Dark")

class User:
    def __init__(self, name):
        self.name = name

def generate_legs():

    # Connect to the SQLite database
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()

    # Fetch all the workouts of the "Legs" category from the table
    cursor.execute("SELECT name, type, reps, weight, sets FROM workouts WHERE type=?", ("Legs",))
    legs_workouts = cursor.fetchall()

    random_workout_legs = random.choice(legs_workouts)
   
    workout_name, workout_type, reps, weight, sets = random_workout_legs

    legs_workout_name = ttk.Label(legs_frame, textvariable=workout_name, font=("Helvetica", 12))
    legs_workout_name.grid(row=3, column=1)

    print(workout_name)
    print(workout_type)

    legs_workout_type = ttk.Label(root, textvariable=workout_type, font=("Helvetica", 12),foreground="blue4")
    legs_workout_type.grid(row=4, column=0)

    legs_workout_reps = ttk.Label(legs_frame, textvariable=reps, font=("Helvetica", 12))
    legs_workout_reps.grid(row=5, column=1)

    legs_workout_weight = ttk.Label(legs_frame, textvariable=weight, font=("Helvetica", 12))
    legs_workout_weight.grid(row=6, column=1)

    legs_workout_sets = ttk.Label(legs_frame, textvariable=sets, font=("Helvetica", 12))
    legs_workout_sets.grid(row=7, column=1)


    
    # Close the connection
    conn.close()

def generate_arms():
    
    # Connect to the SQLite database
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()

    # Fetch all the workouts of the "Arms" category from the table
    cursor.execute("SELECT name, type, reps, weight, sets FROM workouts WHERE type=?", ("Arms",))
    arm_workouts = cursor.fetchall()

    random_workout_arms = random.choice(arm_workouts)
   
    # Close the connection
    conn.close()
    workout_name, workout_type, reps, weight, sets = random_workout_arms

    arm_workout_name = ttk.Label(arms_frame, textvariable=workout_name, font=("Helvetica", 12))
    arm_workout_name.grid(row=3, column=1)

    print(workout_name)
    print(workout_type)

    arm_workout_type = ttk.Label(arms_frame, textvariable=workout_type, font=("Helvetica", 12))
    arm_workout_type.grid(row=4, column=1)

    arm_workout_reps = ttk.Label(arms_frame, textvariable=reps, font=("Helvetica", 12))
    arm_workout_reps.grid(row=5, column=1)

    arm_workout_weight = ttk.Label(arms_frame, textvariable=weight, font=("Helvetica", 12))
    arm_workout_weight.grid(row=6, column=1)

    arm_workout_sets = ttk.Label(arms_frame, textvariable=sets, font=("Helvetica", 12))
    arm_workout_sets.grid(row=7, column=1)

def generate_chest():
    # Connect to the SQLite database
    conn = sqlite3.connect('workouts.db')
    cursor = conn.cursor()

    # Fetch all the workouts of the "Chest" category from the table
    cursor.execute("SELECT name, type, reps, weight, sets FROM workouts WHERE type=?", ("Chest",))
    chest_workouts = cursor.fetchall()

    random_workout_chest = random.choice(chest_workouts)
   
    # Close the connection
    conn.close()
    workout_name, workout_type, reps, weight, sets = random_workout_chest

    chest_workout_name = ttk.Label(chest_frame, textvariable=workout_name, font=("Helvetica", 12))
    chest_workout_name.grid(row=3, column=1)

    print(workout_name)
    print(workout_type)

    chest_workout_type = ttk.Label(chest_frame, textvariable=workout_type, font=("Helvetica", 12))
    chest_workout_type.grid(row=4, column=1)

    chest_workout_reps = ttk.Label(chest_frame, textvariable=reps, font=("Helvetica", 12))
    chest_workout_reps.grid(row=5, column=1)

    chest_workout_weight = ttk.Label(chest_frame, textvariable=weight, font=("Helvetica", 12))
    chest_workout_weight.grid(row=6, column=1)

    chest_workout_sets = ttk.Label(chest_frame, textvariable=sets, font=("Helvetica", 12))
    chest_workout_sets.grid(row=7, column=1)

def go_to_homepage():
    root.destroy()
    subprocess.Popen(["python", "Program_Home_page.py"])

def go_to_datapage():
    root.destroy()
    subprocess.Popen(["python", "Program_Data_page.py"])

def go_to_informationpage():
    root.destroy()
    subprocess.Popen(["python", "Program_Information_page.py"])

root = Tk()
root.geometry("640x960")
root.title("Home page")
root.resizable(width=False, height=False)

background_image = tk.PhotoImage(file="assets/Project Walpaper.png")
background_label = ttk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_frame = ttk.LabelFrame(root)
title_frame.grid(row=0, column=1, pady=10, padx=10, sticky="NW")

app_title = ttk.Label(title_frame, text="iGym", font=("Arial", 20))
app_title.grid(row=1, column=2, sticky="NESW", pady=5, padx=20)

logo_pic = Image.open("assets/DDT logo homepage.png")
resized = logo_pic.resize((50, 50), Image.ANTIALIAS)
logo_final_pic = ImageTk.PhotoImage(resized)

logo_image_label = Label(title_frame, image=logo_final_pic)
logo_image_label.grid(row=1, column=1, padx=10, pady=7)

# Connect to the user_details database
conn = sqlite3.connect('user_details.db')
cursor = conn.cursor()

# Execute an SQL statement to retrieve the user's name
cursor.execute("SELECT name FROM users")
name = cursor.fetchone()[0]

# Close the database connection
conn.close()

# Create a User instance and set the name attribute
user = User(name)

welcome_label_text = "Let's get started, " + user.name + "!"
welcome_message = ttk.Label(root, text=welcome_label_text, font=("Arial", 18))
welcome_message.grid(row=3, column=1, sticky="NW")

legs_frame = ttk.LabelFrame(root)
legs_frame.grid(row=4, column=1)

legs_label_home = ttk.Label(legs_frame, text="Workout for Legs", wraplength=250)
legs_label_home.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

legs_pic = Image.open("assets/Legs Image homepage.jpg")
resized = legs_pic.resize((250, 170), Image.ANTIALIAS)
legs_final_pic = ImageTk.PhotoImage(resized)

legs_image_label = Label(root, image=legs_final_pic)
legs_image_label.grid(row=4, column=0, padx=10, pady=5)

generate_button_legs = customtkinter.CTkButton(legs_frame, text="Generate", command=generate_legs, fg_color=("black", "black"))
generate_button_legs.grid(row=2, column=1, columnspan=1)

arms_frame = ttk.LabelFrame(root)
arms_frame.grid(row=6, column=1)

arms_label_home = ttk.Label(arms_frame, text="Workout for Arms", wraplength=250)
arms_label_home.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

arms_pic = Image.open("assets/Arms Image homepage.jpg")
resized = arms_pic.resize((250, 170), Image.ANTIALIAS)
arms_final_pic = ImageTk.PhotoImage(resized)

arms_image_label = Label(root, image=arms_final_pic)
arms_image_label.grid(row=6, column=0, padx=10, pady=5)

generate_button_arms = customtkinter.CTkButton(arms_frame, text="Generate", command=generate_arms, fg_color=("black", "black"))
generate_button_arms.grid(row=2, column=1, columnspan=1)

chest_frame = ttk.LabelFrame(root)
chest_frame.grid(row=7, column=1)

chest_label_home = ttk.Label(chest_frame, text="Workout for Chest", wraplength=250)
chest_label_home.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

chest_pic = Image.open("assets/Chest Image homepage.jpg")
resized = chest_pic.resize((250, 170), Image.ANTIALIAS)
chest_final_pic = ImageTk.PhotoImage(resized)

chest_image_label = Label(root, image=chest_final_pic)
chest_image_label.grid(row=7, column=0, padx=10, pady=5)

generate_button_chest = customtkinter.CTkButton(chest_frame, text="Generate", command=generate_chest, fg_color=("black", "black"))
generate_button_chest.grid(row=2, column=1, columnspan=1)

menu_frame = customtkinter.CTkFrame(root)
menu_frame.grid(sticky="SW", columnspan=1, column=1, row=8, pady=60)

data_image1 = Image.open("assets/Data logo menu.png")
data_image1 = data_image1.resize((40, 40))
data_photo1 = ImageTk.PhotoImage(data_image1)

home_image2 = Image.open("assets/DDT logo homepage.png")
home_image2 = home_image2.resize((40, 40))
home_photo2 = ImageTk.PhotoImage(home_image2)

information_image3 = Image.open("assets/Information logo menu.png")
information_image3 = information_image3.resize((40, 40))
information_photo3 = ImageTk.PhotoImage(information_image3)

button1 = ttk.Button(menu_frame, image=data_photo1, command=go_to_datapage)
button1.grid(column=0, row=0)

button2 = ttk.Button(menu_frame, image=home_photo2, command=go_to_homepage)
button2.grid(column=1, row=0)

button3 = ttk.Button(menu_frame, image=information_photo3, command=go_to_informationpage)
button3.grid(column=2, row=0)

root.mainloop()
