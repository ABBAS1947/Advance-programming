import tkinter as tk
from tkinter import messagebox


def draw_shape():
    shape = shape_var.get()
    canvas.delete("all")  # Clear canvas

    if not shape:
        messagebox.showerror("Error", "Please select a shape!")
        return

    # Get coordinates if extension is implemented
    try:
        x1 = int(entry_x1.get()) if entry_x1.get() else 50
        y1 = int(entry_y1.get()) if entry_y1.get() else 50
        x2 = int(entry_x2.get()) if entry_x2.get() else 250
        y2 = int(entry_y2.get()) if entry_y2.get() else 250
    except ValueError:
        messagebox.showerror("Error", "Please enter valid coordinates!")
        return

    # Draw the selected shape
    if shape == "Oval":
        canvas.create_oval(x1, y1, x2, y2, fill="lightblue", outline="blue", width=3)
    elif shape == "Rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill="lightgreen", outline="green", width=3)
    elif shape == "Square":
        # For square, use the smaller dimension
        size = min(x2 - x1, y2 - y1)
        canvas.create_rectangle(x1, y1, x1 + size, y1 + size, fill="lightyellow", outline="orange", width=3)
    elif shape == "Triangle":
        # Create triangle using polygon
        mid_x = (x1 + x2) / 2
        canvas.create_polygon(mid_x, y1, x1, y2, x2, y2, fill="lightcoral", outline="red", width=3)


def clear_canvas():
    canvas.delete("all")
    shape_var.set("")
    entry_x1.delete(0, tk.END)
    entry_y1.delete(0, tk.END)
    entry_x2.delete(0, tk.END)
    entry_y2.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.title("Shape Drawing Application")
root.geometry("700x600")
root.configure(bg="#F0F0F0")

# Title
title_label = tk.Label(
    root,
    text="Shape Drawing Tool",
    font=("Arial", 20, "bold"),
    bg="#F0F0F0",
    fg="#2C3E50"
)
title_label.pack(pady=10)

# Control frame
control_frame = tk.Frame(root, bg="#E8EAF6", bd=3, relief=tk.RAISED)
control_frame.pack(padx=10, pady=10, fill=tk.X)

# Shape selection
tk.Label(
    control_frame,
    text="Select Shape:",
    font=("Arial", 12, "bold"),
    bg="#E8EAF6"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

shape_var = tk.StringVar()
shapes = ["Oval", "Rectangle", "Square", "Triangle"]

for i, shape in enumerate(shapes):
    rb = tk.Radiobutton(
        control_frame,
        text=shape,
        variable=shape_var,
        value=shape,
        font=("Arial", 11),
        bg="#E8EAF6"
    )
    rb.grid(row=0, column=i + 1, padx=5, pady=10)

# Coordinate inputs (Extension)
coord_frame = tk.LabelFrame(
    control_frame,
    text="Coordinates (Optional - Default: 50,50,250,250)",
    font=("Arial", 10, "bold"),
    bg="#E8EAF6"
)
coord_frame.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

tk.Label(coord_frame, text="X1:", font=("Arial", 10), bg="#E8EAF6").grid(row=0, column=0, padx=5, pady=5)
entry_x1 = tk.Entry(coord_frame, font=("Arial", 10), width=8)
entry_x1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(coord_frame, text="Y1:", font=("Arial", 10), bg="#E8EAF6").grid(row=0, column=2, padx=5, pady=5)
entry_y1 = tk.Entry(coord_frame, font=("Arial", 10), width=8)
entry_y1.grid(row=0, column=3, padx=5, pady=5)

tk.Label(coord_frame, text="X2:", font=("Arial", 10), bg="#E8EAF6").grid(row=0, column=4, padx=5, pady=5)
entry_x2 = tk.Entry(coord_frame, font=("Arial", 10), width=8)
entry_x2.grid(row=0, column=5, padx=5, pady=5)

tk.Label(coord_frame, text="Y2:", font=("Arial", 10), bg="#E8EAF6").grid(row=0, column=6, padx=5, pady=5)
entry_y2 = tk.Entry(coord_frame, font=("Arial", 10), width=8)
entry_y2.grid(row=0, column=7, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(control_frame, bg="#E8EAF6")
button_frame.grid(row=2, column=0, columnspan=5, pady=10)

btn_draw = tk.Button(
    button_frame,
    text="Draw Shape",
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=draw_shape
)
btn_draw.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="#F44336",
    fg="white",
    width=15,
    command=clear_canvas
)
btn_clear.pack(side=tk.LEFT, padx=5)

# Canvas
canvas = tk.Canvas(root, width=650, height=400, bg="white", bd=3, relief=tk.SUNKEN)
canvas.pack(padx=10, pady=10)

root.mainloop()