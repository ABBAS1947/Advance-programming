import tkinter as tk
from tkinter import ttk


def update_greeting():
    name = entry_name.get()
    color = color_var.get()

    if name:
        greeting = f"Hello, {name}! Welcome!"
        label_display.config(text=greeting, fg=color)
    else:
        label_display.config(text="Please enter your name!", fg="red")


# Create main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("500x400")

# InputFrame
input_frame = tk.Frame(root, bg="#E3F2FD", bd=5, relief=tk.RAISED)
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Title label in blue
title_label = tk.Label(
    input_frame,
    text="Greeting Application",
    font=("Arial", 18, "bold"),
    fg="blue",
    bg="#E3F2FD"
)
title_label.pack(pady=20)

# Entry field for name
name_frame = tk.Frame(input_frame, bg="#E3F2FD")
name_frame.pack(pady=10)

label_name = tk.Label(
    name_frame,
    text="Enter Your Name:",
    font=("Arial", 12),
    bg="#E3F2FD"
)
label_name.pack(side=tk.LEFT, padx=5)

entry_name = tk.Entry(name_frame, font=("Arial", 12), width=20)
entry_name.pack(side=tk.LEFT, padx=5)

# Color dropdown
color_frame = tk.Frame(input_frame, bg="#E3F2FD")
color_frame.pack(pady=10)

label_color = tk.Label(
    color_frame,
    text="Select Color:",
    font=("Arial", 12),
    bg="#E3F2FD"
)
label_color.pack(side=tk.LEFT, padx=5)

color_var = tk.StringVar()
color_var.set("black")
color_dropdown = ttk.Combobox(
    color_frame,
    textvariable=color_var,
    values=["black", "red", "blue", "green", "purple", "orange"],
    font=("Arial", 11),
    width=18,
    state="readonly"
)
color_dropdown.pack(side=tk.LEFT, padx=5)

# Update button
btn_update = tk.Button(
    input_frame,
    text="Update Greeting",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=20,
    command=update_greeting
)
btn_update.pack(pady=20)

# DisplayFrame
display_frame = tk.Frame(root, bg="#FFF9C4", bd=5, relief=tk.SUNKEN)
display_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Display label
label_display = tk.Label(
    display_frame,
    text="",
    font=("Arial", 16, "bold"),
    bg="#FFF9C4",
    wraplength=400
)
label_display.pack(expand=True)

root.mainloop()