import tkinter as tk
from tkinter import messagebox
from datetime import date


def calculate_age():
    try:
        dob = entry_dob.get()

        month, day, year = map(int, dob.split('/'))

        birth_date = date(year, month, day)
        today = date.today()


        age = today.year - birth_date.year


        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        label_result.config(text=f"Your age is {age} years")
    except ValueError:
        messagebox.showerror("Error", "Please enter date in format: MM/DD/YYYY")
    except:
        messagebox.showerror("Error", "Invalid date entered")


def clear():
    entry_dob.delete(0, tk.END)
    label_result.config(text="")



root = tk.Tk()
root.title("Age Calculator")
root.geometry("400x300")
root.configure(bg="#FFF3E0")


title_label = tk.Label(
    root,
    text="Age Calculator",
    font=("Arial", 20, "bold"),
    bg="#FFF3E0",
    fg="#E65100"
)
title_label.pack(pady=30)


input_frame = tk.Frame(root, bg="#FFF3E0")
input_frame.pack(pady=20)

label_dob = tk.Label(
    input_frame,
    text="Enter Date of Birth\n(MM/DD/YYYY):",
    font=("Arial", 12),
    bg="#FFF3E0"
)
label_dob.pack(side=tk.LEFT, padx=10)

entry_dob = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry_dob.pack(side=tk.LEFT, padx=10)


button_frame = tk.Frame(root, bg="#FFF3E0")
button_frame.pack(pady=20)

btn_calculate = tk.Button(
    button_frame,
    text="Calculate Age",
    font=("Arial", 12, "bold"),
    bg="#FF9800",
    fg="white",
    width=15,
    command=calculate_age
)
btn_calculate.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#607D8B",
    fg="white",
    width=15,
    command=clear
)
btn_clear.pack(side=tk.LEFT, padx=5)


label_result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#FFF3E0",
    fg="#E65100"
)
label_result.pack(pady=20)

root.mainloop()