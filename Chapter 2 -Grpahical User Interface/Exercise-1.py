import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Welcome")

# Set default window size
root.geometry("400x200")

# Disable resizing
root.resizable(False, False)

# Add background color
root.configure(bg="#E8F4F8")

# Create welcome label with custom font
welcome_label = tk.Label(
    root,
    text="Welcome to My Application!",
    font=("Arial", 20, "bold"),
    bg="#E8F4F8",
    fg="#2C3E50"
)
welcome_label.pack(expand=True)

root.mainloop()