import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  # You'll need to install pillow: pip install pillow


def submit_form():
    # Get all values
    name = entry_name.get()
    mobile = entry_mobile.get()
    email = entry_email.get()
    address = entry_address.get()
    gender = gender_var.get()
    course = course_var.get()

    # Get languages
    languages = []
    if english_var.get():
        languages.append("English")
    if tagalog_var.get():
        languages.append("Tagalog")
    if hindi_var.get():
        languages.append("Hindi/Urdu")

    # Get communication skill rating
    skill_rating = skill_scale.get()

    # Validation
    if not name or not mobile or not email or not address:
        messagebox.showerror("Error", "Please fill all required fields!")
        return

    if gender == "Select":
        messagebox.showerror("Error", "Please select gender!")
        return

    if not course:
        messagebox.showerror("Error", "Please select a course!")
        return

    if not languages:
        messagebox.showerror("Error", "Please select at least one language!")
        return

    # Create success message
    message = f"Registration Successful!\n\n"
    message += f"Name: {name}\n"
    message += f"Mobile: {mobile}\n"
    message += f"Email: {email}\n"
    message += f"Address: {address}\n"
    message += f"Gender: {gender}\n"
    message += f"Course: {course}\n"
    message += f"Languages: {', '.join(languages)}\n"
    message += f"English Communication Skills: {skill_rating}/100"

    messagebox.showinfo("Success", message)


def clear_form():
    entry_name.delete(0, tk.END)
    entry_mobile.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    gender_var.set("Select")
    course_var.set("")
    english_var.set(False)
    tagalog_var.set(False)
    hindi_var.set(False)
    skill_scale.set(50)


# Create main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x800")
root.configure(bg="#FFFFFF")

# Header with logo background
header_frame = tk.Frame(root, bg="#2C3E50", height=120)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

# Load and display BSU logo image
try:
    logo_image = Image.open("bsu_logo.png")   lace with your image filename
    logo_image = logo_image.resize((200, 80), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(header_frame, image=logo_photo, bg="#2C3E50")
    logo_label.image = logo_photo  # Keep a reference
    logo_label.pack(pady=20, padx=20, anchor="w")
except:
    # Fallback to text if image not found
    logo_label = tk.Label(
        header_frame,
        text="BATH SPA | RAK\nUNIVERSITY     CAMPUS",
        font=("Arial", 14, "bold"),
        bg="#2C3E50",
        fg="white",
        justify=tk.LEFT
    )
    logo_label.pack(pady=20, padx=20, anchor="w")

# Title section
title_frame = tk.Frame(root, bg="#FFFFFF")
title_frame.pack(pady=15)

title_label = tk.Label(
    title_frame,
    text="Student Management System",
    font=("Arial", 18, "bold"),
    bg="#FFFFFF",
    fg="#2C3E50"
)
title_label.pack()

subtitle_label = tk.Label(
    title_frame,
    text="New Student Registration",
    font=("Arial", 11),
    bg="#FFFFFF",
    fg="#2C3E50"
)
subtitle_label.pack()

# Form frame
form_frame = tk.Frame(root, bg="#FFFFFF")
form_frame.pack(padx=50, pady=10)

# Student Name
tk.Label(
    form_frame,
    text="Student Name",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=0, column=0, sticky="e", pady=8, padx=(0, 10))

entry_name = tk.Entry(form_frame, font=("Arial", 10), width=30, bg="#BDBDBD", relief=tk.FLAT)
entry_name.grid(row=0, column=1, pady=8)

# Mobile Number
tk.Label(
    form_frame,
    text="Mobile Number",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=1, column=0, sticky="e", pady=8, padx=(0, 10))

entry_mobile = tk.Entry(form_frame, font=("Arial", 10), width=30, bg="#BDBDBD", relief=tk.FLAT)
entry_mobile.grid(row=1, column=1, pady=8)

# Email Id
tk.Label(
    form_frame,
    text="Email Id",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=2, column=0, sticky="e", pady=8, padx=(0, 10))

entry_email = tk.Entry(form_frame, font=("Arial", 10), width=30, bg="#BDBDBD", relief=tk.FLAT)
entry_email.grid(row=2, column=1, pady=8)

# Home Address
tk.Label(
    form_frame,
    text="Home Address",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=3, column=0, sticky="e", pady=8, padx=(0, 10))

entry_address = tk.Entry(form_frame, font=("Arial", 10), width=30, bg="#BDBDBD", relief=tk.FLAT)
entry_address.grid(row=3, column=1, pady=8)

# Gender
tk.Label(
    form_frame,
    text="Gender",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=4, column=0, sticky="e", pady=8, padx=(0, 10))

gender_var = tk.StringVar()
gender_var.set("Select")
gender_dropdown = ttk.Combobox(
    form_frame,
    textvariable=gender_var,
    values=["Select", "Male", "Female", "Other"],
    font=("Arial", 10),
    width=28,
    state="readonly"
)
gender_dropdown.grid(row=4, column=1, pady=8)

# Course Enrolled
tk.Label(
    form_frame,
    text="Course Enrolled",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=5, column=0, sticky="ne", pady=8, padx=(0, 10))

course_var = tk.StringVar()
course_frame = tk.Frame(form_frame, bg="#FFFFFF")
course_frame.grid(row=5, column=1, sticky="w", pady=8)

tk.Radiobutton(
    course_frame,
    text="BSc CC",
    variable=course_var,
    value="BSc CC",
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(anchor="w", pady=2)

tk.Radiobutton(
    course_frame,
    text="BSc CY",
    variable=course_var,
    value="BSc CY",
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(anchor="w", pady=2)

tk.Radiobutton(
    course_frame,
    text="BSc PSY",
    variable=course_var,
    value="BSc PSY",
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(anchor="w", pady=2)

tk.Radiobutton(
    course_frame,
    text="BA & BM",
    variable=course_var,
    value="BA & BM",
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(anchor="w", pady=2)

# Languages known
tk.Label(
    form_frame,
    text="Languages known",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).grid(row=6, column=0, sticky="ne", pady=8, padx=(0, 10))

lang_frame = tk.Frame(form_frame, bg="#FFFFFF")
lang_frame.grid(row=6, column=1, sticky="w", pady=8)

english_var = tk.BooleanVar()
tagalog_var = tk.BooleanVar()
hindi_var = tk.BooleanVar()

lang_row1 = tk.Frame(lang_frame, bg="#FFFFFF")
lang_row1.pack(anchor="w")

tk.Checkbutton(
    lang_row1,
    text="English",
    variable=english_var,
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(side=tk.LEFT)

tk.Checkbutton(
    lang_row1,
    text="Tagalog",
    variable=tagalog_var,
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(side=tk.LEFT, padx=(10, 0))

tk.Checkbutton(
    lang_frame,
    text="Hindi/Urdu",
    variable=hindi_var,
    font=("Arial", 9),
    bg="#FFFFFF"
).pack(anchor="w", pady=2)

# Rate your English communication skills - AT THE BOTTOM
rating_frame = tk.Frame(root, bg="#FFFFFF")
rating_frame.pack(pady=15, padx=50)

tk.Label(
    rating_frame,
    text="Rate your English communication skills",
    font=("Arial", 10),
    bg="#FFFFFF",
    fg="#5F5F5F"
).pack(anchor="w")

skill_scale = tk.Scale(
    rating_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=380,
    bg="#FFFFFF",
    fg="#2C3E50",
    troughcolor="#E0E0E0",
    activebackground="#1E88E5",
    highlightthickness=0,
    showvalue=0
)
skill_scale.set(50)
skill_scale.pack(pady=5)

# Buttons - AT THE BOTTOM
button_frame = tk.Frame(root, bg="#FFFFFF")
button_frame.pack(pady=20)

btn_submit = tk.Button(
    button_frame,
    text="Submit",
    font=("Arial", 12, "bold"),
    bg="#2C3E50",
    fg="white",
    width=15,
    height=2,
    command=submit_form,
    relief=tk.FLAT
)
btn_submit.pack(side=tk.LEFT, padx=15)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#2C3E50",
    fg="white",
    width=15,
    height=2,
    command=clear_form,
    relief=tk.FLAT
)
btn_clear.pack(side=tk.LEFT, padx=15)

root.mainloop()