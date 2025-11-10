import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")


# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("350x200")
root.configure(bg="#F0F0F0")

# Create title label
title_label = tk.Label(
    root,
    text="Login System",
    font=("Arial", 18, "bold"),
    bg="#F0F0F0"
)
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Username label and entry
label_username = tk.Label(
    root,
    text="Username:",
    font=("Arial", 12),
    bg="#F0F0F0"
)
label_username.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_username = tk.Entry(root, font=("Arial", 12), width=20)
entry_username.grid(row=1, column=1, padx=10, pady=10)

# Password label and entry
label_password = tk.Label(
    root,
    text="Password:",
    font=("Arial", 12),
    bg="#F0F0F0"
)
label_password.grid(row=2, column=0, padx=10, pady=10, sticky="e")

entry_password = tk.Entry(root, font=("Arial", 12), width=20, show="*")
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Login button
login_button = tk.Button(
    root,
    text="Login",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=login
)
login_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()