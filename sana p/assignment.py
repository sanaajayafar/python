import tkinter as tk
from tkinter import messagebox

# Function for submit button
def submit():
    name = name_entry.get()
    age = age_entry.get()
    course = course_entry.get()
    gender = gender_var.get()

    messagebox.showinfo(
        "Submitted",
        "Name: " + name +
        "\nAge: " + age +
        "\nCourse: " + course +
        "\nGender: " + gender
    )

# Main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("300x250")

# Name
name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Age
age_label = tk.Label(root, text="Age")
age_label.grid(row=1, column=0, padx=10, pady=5)

age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# Course
course_label = tk.Label(root, text="Course")
course_label.grid(row=2, column=0, padx=10, pady=5)

course_entry = tk.Entry(root)
course_entry.grid(row=2, column=1)

# Gender
gender_label = tk.Label(root, text="Gender")
gender_label.grid(row=3, column=0, padx=10, pady=5)

gender_var = tk.StringVar()

male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male.grid(row=3, column=1, sticky="w")

female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female.grid(row=4, column=1, sticky="w")

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=5, column=1, pady=10)

# Run the window
root.mainloop()