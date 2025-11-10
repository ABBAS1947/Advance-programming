import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit():
    try:
        celsius = float(entry_temp.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(entry_temp.get())
        celsius = (fahrenheit - 32) * 5/9
        label_result.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def clear():
    entry_temp.delete(0, tk.END)
    label_result.config(text="Result: ")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.configure(bg="#E3F2FD")

# Title
title_label = tk.Label(
    root,
    text="Temperature Converter",
    font=("Arial", 20, "bold"),
    bg="#E3F2FD",
    fg="#1976D2"
)
title_label.pack(pady=20)

# Input frame
input_frame = tk.Frame(root, bg="#E3F2FD")
input_frame.pack(pady=20)

label_temp = tk.Label(
    input_frame,
    text="Enter Temperature:",
    font=("Arial", 12),
    bg="#E3F2FD"
)
label_temp.pack(side=tk.LEFT, padx=5)

entry_temp = tk.Entry(input_frame, font=("Arial", 12), width=15)
entry_temp.pack(side=tk.LEFT, padx=5)

# Button frame
button_frame = tk.Frame(root, bg="#E3F2FD")
button_frame.pack(pady=20)

btn_c_to_f = tk.Button(
    button_frame,
    text="Celsius → Fahrenheit",
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=18,
    height=2,
    command=celsius_to_fahrenheit
)
btn_c_to_f.pack(pady=5)

btn_f_to_c = tk.Button(
    button_frame,
    text="Fahrenheit → Celsius",
    font=("Arial", 11, "bold"),
    bg="#FF5722",
    fg="white",
    width=18,
    height=2,
    command=fahrenheit_to_celsius
)
btn_f_to_c.pack(pady=5)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#607D8B",
    fg="white",
    width=18,
    height=2,
    command=clear
)
btn_clear.pack(pady=5)

# Result label
label_result = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 14, "bold"),
    bg="#E3F2FD",
    fg="#1976D2"
)
label_result.pack(pady=20)

root.mainloop()