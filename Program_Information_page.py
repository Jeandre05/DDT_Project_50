####### Imports #######
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
from PIL import Image, ImageDraw
import subprocess
import customtkinter
import sqlite3



####### Class Code #######

class Details:
   pass


####### Functions and Setup #######
def generate():
    selected_category = category_combobox.get()
    selected_workout = workouts_combobox.get()

    # Establish a connection to the database
    conn = sqlite3.connect('workouts.db')
    # Create a cursor object
    cursor = conn.cursor()

    # Execute a SELECT statement to retrieve the workout information
    cursor.execute("SELECT name, type, reps, weight, sets FROM workouts WHERE type=? AND name=?", (selected_category, selected_workout))
    workout_data = cursor.fetchone()

    # Close the connection
    conn.close()

    # Display the retrieved workout information
    if workout_data:
        name, type, reps, weight, sets = workout_data

        name_var.set(name)
        type_var.set(type)
        reps_var.set(reps)
        weight_var.set(weight)
        sets_var.set(sets)

        bottom_frame = ttk.LabelFrame(root)
        bottom_frame.grid(row = 2, column=1, columnspan=3, sticky="N", padx=65,pady=30)

        workout_name = ttk.Label(bottom_frame, textvariable=name_var, font=("Helvetica", 35))
        workout_name.grid(row=3, column=1,pady=30, sticky="NE")

        workout_type_label = ttk.Label(bottom_frame, text="Type:", font=("Helvetica", 18))
        workout_type_label.grid(row=4,column=0,padx=20)

        workout_type = ttk.Label(bottom_frame, textvariable=type_var, font=("Helvetica", 18))
        workout_type.grid(row=4, column=1,padx=20)

        workout_reps_label = ttk.Label(bottom_frame, text="Reps:", font=("Helvetica", 18))
        workout_reps_label.grid(row=5,column=0,padx=20)

        workout_reps = ttk.Label(bottom_frame, textvariable=reps_var, font=("Helvetica", 18))
        workout_reps.grid(row=5, column=1)

        workout_weight_label = ttk.Label(bottom_frame, text="Weight:", font=("Helvetica", 18))
        workout_weight_label.grid(row=6,column=0,padx=20)

        workout_weight = ttk.Label(bottom_frame, textvariable=weight_var, font=("Helvetica", 18))
        workout_weight.grid(row=6, column=1)

        workout_sets_label = ttk.Label(bottom_frame, text="Sets:", font=("Helvetica", 18))
        workout_sets_label.grid(row=7,column=0,padx=20)

        workout_sets = ttk.Label(bottom_frame, textvariable=sets_var, font=("Helvetica", 18))
        workout_sets.grid(row=7, column=1)

#menu defs
def go_to_homepage():
  root.destroy()
  subprocess.Popen(["python","Program_Home_page.py"])

def go_to_datapage():
   root.destroy()
   subprocess.Popen(["python","Program_Data_page.py"])

def go_to_informationpage():
   root.destroy()
   subprocess.Popen(["python","Program_Information_page.py"])


def update_second_combo(event):
    selected_item = category_combobox.get()
    workouts_combobox['values'] = combo_values[selected_item]

# Define the values for the second combo box based on the selection in the first combo box
combo_values = {
    'Legs': ['Calf Raises', 'Leg-Press', 'Squat','Walking Lunges','Leg Extension','Hack Squat','Romanian Deadlift','Deadlift','Hamstring Curl'],
    'Arms': ['Bicep Curl', 'Bent-Over Rows', 'Hammer Curl','Dips','Push-Downs','Tricep Extension','Shoulder Press','Lateral Raises','Incline Bicep Curl','Pull-Ups'],
    'Chest': ['Bench-Press', 'Chest-Fly', 'Push-Ups','Cable Crossovers','Tricep Extension','Chest Dip','Overhead Press','Tricep Dips','Wide Grip Bench-Press','Decline Push-Ups'],
}

####### GUI code #######

root = Tk()
root.geometry("640x960")
root.title("Data page")
root.resizable(width=False, height=False)

name_var = StringVar()
type_var = StringVar()
reps_var = IntVar()
weight_var = IntVar()
sets_var = IntVar()

background_image = tk.PhotoImage(file="assets/Project Walpaper.png")
background_label = ttk.Label(root, image=background_image)
background_label.place(x=0, y=0,relwidth=1,relheight=1)

info_title = ttk.Label(root, text= "Information:", font=("Helvetica", 30)) #underline
info_title.grid(row=0, column=1, columnspan=3, padx=10, pady=20, sticky="N")

#Resize the image for logo 
#Open image
logo_pic = Image.open("assets/DDT logo homepage.png")
#Resize image to 
resized = logo_pic.resize((50,50), Image.ANTIALIAS)
logo_final_pic = ImageTk.PhotoImage(resized)
#Paste image
logo_image_label = Label(root, image=logo_final_pic)
logo_image_label.grid(row=0,column=3,pady=7)


top_frame = ttk.LabelFrame(root)
top_frame.grid(row = 1, column=1, columnspan=3, sticky="N", padx=73)

catagory_label = ttk.Label(top_frame,text="Catagory:", font=("Helvetica", 18))
catagory_label.grid(row=0, column=0 , padx=20, pady=5)

workout_label = ttk.Label(top_frame,text="Workout:", font=("Helvetica", 18))
workout_label.grid(row=0, column=2 , padx=20, pady=5)

generate_button = customtkinter.CTkButton(top_frame,text="Generate",command=generate,fg_color=("black", "black"))
generate_button.grid(row=2, column=1)

#create a drop down box for catagories
categories = ["Legs", "Arms", "Chest"]
category_combobox = ttk.Combobox(top_frame,values=list(combo_values.keys()) ,state='readonly')
category_combobox.bind('<<ComboboxSelected>>', update_second_combo)
category_combobox.grid(row=1, column=0, padx=10, pady=10)

#create a drop down box for catagories
#workouts set for now (objects later)

workouts_combobox = ttk.Combobox(top_frame, state='readonly')
workouts_combobox.grid(row=1, column=2, padx=10, pady=10)

#menu
menu_frame = ttk.Frame(root)
menu_frame.grid(sticky="SE",column=2,row=8 ,pady = 60)

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
button1.grid(column=0,row=0)

button2 = ttk.Button(menu_frame, image=home_photo2,command=go_to_homepage)
button2.grid(column=1, row=0)

button3 = ttk.Button(menu_frame, image=information_photo3, command=go_to_informationpage)
button3.grid(column=2, row=0)

root.mainloop()

