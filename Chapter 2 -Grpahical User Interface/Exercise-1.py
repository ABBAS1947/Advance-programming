import tkinter as tk

root = tk.Tk()
root.title("Welcome")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#E8F4F8")


welcome_label = tk.Label(
    root,
    text="Welcome to My Application!",
    font=("Arial", 20, "bold"),
    bg="#E8F4F8",
    fg="#2C3E50"
)
welcome_label.pack(expand=True)

root.mainloop()