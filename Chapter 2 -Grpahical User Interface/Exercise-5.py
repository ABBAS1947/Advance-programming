import tkinter as tk
from tkinter import messagebox


def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "add":
            result = num1 + num2
            label_result.config(text=f"Result: {result}")
        elif operation == "subtract":
            result = num1 - num2
            label_result.config(text=f"Result: {result}")
        elif operation == "multiply":
            result = num1 * num2
            label_result.config(text=f"Result: {result}")
        elif operation == "divide":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero!")
            else:
                result = num1 / num2
                label_result.config(text=f"Result: {result}")
        elif operation == "modulo":
            result = num1 % num2
            label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")


# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x450")
root.configure(bg="#F5F5F5")

# Title
title_label = tk.Label(
    root,
    text="Simple Calculator",
    font=("Arial", 20, "bold"),
    bg="#F5F5F5",
    fg="#2C3E50"
)
title_label.pack(pady=20)

# Number 1
frame_num1 = tk.Frame(root, bg="#F5F5F5")
frame_num1.pack(pady=10)
label_num1 = tk.Label(frame_num1, text="Number 1:", font=("Arial", 12), bg="#F5F5F5")
label_num1.pack(side=tk.LEFT, padx=5)
entry_num1 = tk.Entry(frame_num1, font=("Arial", 12), width=20)
entry_num1.pack(side=tk.LEFT, padx=5)

# Number 2
frame_num2 = tk.Frame(root, bg="#F5F5F5")
frame_num2.pack(pady=10)
label_num2 = tk.Label(frame_num2, text="Number 2:", font=("Arial", 12), bg="#F5F5F5")
label_num2.pack(side=tk.LEFT, padx=5)
entry_num2 = tk.Entry(frame_num2, font=("Arial", 12), width=20)
entry_num2.pack(side=tk.LEFT, padx=5)

# Operation buttons
button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.pack(pady=20)

btn_add = tk.Button(button_frame, text="+", font=("Arial", 14, "bold"),
                    bg="#4CAF50", fg="white", width=5, height=2,
                    command=lambda: calculate("add"))
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_subtract = tk.Button(button_frame, text="-", font=("Arial", 14, "bold"),
                         bg="#2196F3", fg="white", width=5, height=2,
                         command=lambda: calculate("subtract"))
btn_subtract.grid(row=0, column=1, padx=5, pady=5)

btn_multiply = tk.Button(button_frame, text="×", font=("Arial", 14, "bold"),
                         bg="#FF9800", fg="white", width=5, height=2,
                         command=lambda: calculate("multiply"))
btn_multiply.grid(row=0, column=2, padx=5, pady=5)

btn_divide = tk.Button(button_frame, text="÷", font=("Arial", 14, "bold"),
                       bg="#9C27B0", fg="white", width=5, height=2,
                       command=lambda: calculate("divide"))
btn_divide.grid(row=1, column=0, padx=5, pady=5)

btn_modulo = tk.Button(button_frame, text="%", font=("Arial", 14, "bold"),
                       bg="#F44336", fg="white", width=5, height=2,
                       command=lambda: calculate("modulo"))
btn_modulo.grid(row=1, column=1, padx=5, pady=5)

btn_clear = tk.Button(button_frame, text="Clear", font=("Arial", 14, "bold"),
                      bg="#607D8B", fg="white", width=5, height=2,
                      command=clear)
btn_clear.grid(row=1, column=2, padx=5, pady=5)

# Result label
label_result = tk.Label(
    root,
    text="Result: ",
    font=("Arial", 16, "bold"),
    bg="#F5F5F5",
    fg="#2C3E50"
)
label_result.pack(pady=20)

root.mainloop()