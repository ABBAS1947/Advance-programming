import tkinter as tk
from tkinter import ttk
import math

def calculate_circle():
    try:
        radius = float(entry_radius.get())
        area = math.pi * (radius ** 2)
        label_circle_result.config(text=f"Area of Circle: {area:.2f} sq units")
    except ValueError:
        label_circle_result.config(text="Please enter a valid number!")

def calculate_square():
    try:
        side = float(entry_square.get())
        area = side ** 2
        label_square_result.config(text=f"Area of Square: {area:.2f} sq units")
    except ValueError:
        label_square_result.config(text="Please enter a valid number!")

def calculate_rectangle():
    try:
        length = float(entry_length.get())
        width = float(entry_width.get())
        area = length * width
        label_rect_result.config(text=f"Area of Rectangle: {area:.2f} sq units")
    except ValueError:
        label_rect_result.config(text="Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("500x400")
root.configure(bg="#F5F5F5")

# Title
title_label = tk.Label(
    root,
    text="Area Calculator",
    font=("Arial", 20, "bold"),
    bg="#F5F5F5",
    fg="#2C3E50"
)
title_label.pack(pady=20)

# Create notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

# Circle Tab
circle_frame = tk.Frame(notebook, bg="#E3F2FD")
notebook.add(circle_frame, text="Circle")

tk.Label(
    circle_frame,
    text="Calculate Circle Area",
    font=("Arial", 14, "bold"),
    bg="#E3F2FD"
).pack(pady=20)

radius_frame = tk.Frame(circle_frame, bg="#E3F2FD")
radius_frame.pack(pady=10)

tk.Label(
    radius_frame,
    text="Enter Radius:",
    font=("Arial", 12),
    bg="#E3F2FD"
).pack(side=tk.LEFT, padx=5)

entry_radius = tk.Entry(radius_frame, font=("Arial", 12), width=15)
entry_radius.pack(side=tk.LEFT, padx=5)

tk.Button(
    circle_frame,
    text="Calculate",
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=15,
    command=calculate_circle
).pack(pady=10)

label_circle_result = tk.Label(
    circle_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#E3F2FD",
    fg="#1976D2"
)
label_circle_result.pack(pady=20)

# Square Tab
square_frame = tk.Frame(notebook, bg="#FFF9C4")
notebook.add(square_frame, text="Square")

tk.Label(
    square_frame,
    text="Calculate Square Area",
    font=("Arial", 14, "bold"),
    bg="#FFF9C4"
).pack(pady=20)

square_input_frame = tk.Frame(square_frame, bg="#FFF9C4")
square_input_frame.pack(pady=10)

tk.Label(
    square_input_frame,
    text="Enter Side:",
    font=("Arial", 12),
    bg="#FFF9C4"
).pack(side=tk.LEFT, padx=5)

entry_square = tk.Entry(square_input_frame, font=("Arial", 12), width=15)
entry_square.pack(side=tk.LEFT, padx=5)

tk.Button(
    square_frame,
    text="Calculate",
    font=("Arial", 11, "bold"),
    bg="#FBC02D",
    fg="white",
    width=15,
    command=calculate_square
).pack(pady=10)

label_square_result = tk.Label(
    square_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#FFF9C4",
    fg="#F57F17"
)
label_square_result.pack(pady=20)

# Rectangle Tab
rect_frame = tk.Frame(notebook, bg="#E8F5E9")
notebook.add(rect_frame, text="Rectangle")

tk.Label(
    rect_frame,
    text="Calculate Rectangle Area",
    font=("Arial", 14, "bold"),
    bg="#E8F5E9"
).pack(pady=20)

length_frame = tk.Frame(rect_frame, bg="#E8F5E9")
length_frame.pack(pady=5)

tk.Label(
    length_frame,
    text="Enter Length:",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack(side=tk.LEFT, padx=5)

entry_length = tk.Entry(length_frame, font=("Arial", 12), width=15)
entry_length.pack(side=tk.LEFT, padx=5)

width_frame = tk.Frame(rect_frame, bg="#E8F5E9")
width_frame.pack(pady=5)

tk.Label(
    width_frame,
    text="Enter Width:",
    font=("Arial", 12),
    bg="#E8F5E9"
).pack(side=tk.LEFT, padx=5)

entry_width = tk.Entry(width_frame, font=("Arial", 12), width=15)
entry_width.pack(side=tk.LEFT, padx=5)

tk.Button(
    rect_frame,
    text="Calculate",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=calculate_rectangle
).pack(pady=10)

label_rect_result = tk.Label(
    rect_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="#E8F5E9",
    fg="#2E7D32"
)
label_rect_result.pack(pady=20)

root.mainloop()