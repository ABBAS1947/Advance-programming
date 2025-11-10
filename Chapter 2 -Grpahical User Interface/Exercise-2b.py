import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Square Grid Layout")
root.geometry("400x300")

# Create left frame
left_frame = tk.Frame(root, bd=5, relief=tk.RAISED, bg="white")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create right frame
right_frame = tk.Frame(root, bd=5, relief=tk.RAISED, bg="white")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create labels A and B inside left frame
label_a = tk.Label(
    left_frame,
    text="A",
    bg="lightblue",
    font=("Arial", 24, "bold")
)
label_a.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label_b = tk.Label(
    left_frame,
    text="B",
    bg="lightgreen",
    font=("Arial", 24, "bold")
)
label_b.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create labels C and D inside right frame
label_c = tk.Label(
    right_frame,
    text="C",
    bg="lightyellow",
    font=("Arial", 24, "bold")
)
label_c.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

label_d = tk.Label(
    right_frame,
    text="D",
    bg="lightcoral",
    font=("Arial", 24, "bold")
)
label_d.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

root.mainloop()