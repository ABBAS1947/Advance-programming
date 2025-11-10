import tkinter as tk
from tkinter import ttk, messagebox


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
root.geometry("450x720")
root.configure(bg="#E8E8E8")

# Header Frame (Dark blue/gray)
header_frame = tk.Frame(root, bg="#3D4B5C", height=100)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

header_label = tk.Label(
    header_frame,
    text="BATH SPA | RAK CAMPUS\nUNIVERSITY",
    font=("Arial", 12, "bold"),
    bg="#3D4B5C",
    fg="white",
    justify=tk.LEFT
)
header_label.pack(pady=20, padx=20, anchor="w")

# Main content frame (Light gray background)
content_frame = tk.Frame(root, bg="#E8E8E8")
content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)

# Title
title_label = tk.Label(
    content_frame,
    text="Student Management System",
    font=("Arial", 16, "bold"),
    bg="#E8E8E8",
    fg="#000000"
)
title_label.pack(pady=(5, 0))

subtitle_label = tk.Label(
    content_frame,
    text="New Student Registration",
    font=("Arial", 10),
    bg="#E8E8E8",
    fg="#000000"
)
subtitle_label.pack(pady=(0, 15))

# Form frame
form_frame = tk.Frame(content_frame, bg="#E8E8E8")
form_frame.pack()

# Student Name
tk.Label(
    form_frame,
    text="Student Name",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=0, column=0, sticky="w", pady=6)

entry_name = tk.Entry(form_frame, font=("Arial", 9), width=35, bg="#B8B8B8", relief=tk.FLAT, bd=0)
entry_name.grid(row=0, column=1, pady=6, ipady=3)

# Mobile Number
tk.Label(
    form_frame,
    text="Mobile Number",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=1, column=0, sticky="w", pady=6)

entry_mobile = tk.Entry(form_frame, font=("Arial", 9), width=35, bg="#B8B8B8", relief=tk.FLAT, bd=0)
entry_mobile.grid(row=1, column=1, pady=6, ipady=3)

# Email Id
tk.Label(
    form_frame,
    text="Email Id",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=2, column=0, sticky="w", pady=6)

entry_email = tk.Entry(form_frame, font=("Arial", 9), width=35, bg="#B8B8B8", relief=tk.FLAT, bd=0)
entry_email.grid(row=2, column=1, pady=6, ipady=3)

# Home Address
tk.Label(
    form_frame,
    text="Home Address",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=3, column=0, sticky="w", pady=6)

entry_address = tk.Entry(form_frame, font=("Arial", 9), width=35, bg="#B8B8B8", relief=tk.FLAT, bd=0)
entry_address.grid(row=3, column=1, pady=6, ipady=3)

# Gender
tk.Label(
    form_frame,
    text="Gender",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=4, column=0, sticky="w", pady=6)

gender_var = tk.StringVar()
gender_var.set("Select")

# Custom style for combobox to match the image
style = ttk.Style()
style.theme_use('clam')
style.configure('Custom.TCombobox',
                fieldbackground="#B8B8B8",
                background="#B8B8B8",
                borderwidth=0,
                relief="flat")

gender_dropdown = ttk.Combobox(
    form_frame,
    textvariable=gender_var,
    values=["Select", "Male", "Female", "Other"],
    font=("Arial", 9),
    width=33,
    state="readonly",
    style='Custom.TCombobox'
)
gender_dropdown.grid(row=4, column=1, pady=6, ipady=3)

# Course Enrolled
tk.Label(
    form_frame,
    text="Course Enrolled",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=5, column=0, sticky="nw", pady=6)

course_var = tk.StringVar()
course_frame = tk.Frame(form_frame, bg="#E8E8E8")
course_frame.grid(row=5, column=1, sticky="w", pady=6)

tk.Radiobutton(
    course_frame,
    text="BSc CC",
    variable=course_var,
    value="BSc CC",
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(anchor="w")

tk.Radiobutton(
    course_frame,
    text="BSc CY",
    variable=course_var,
    value="BSc CY",
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(anchor="w")

tk.Radiobutton(
    course_frame,
    text="BSc PSY",
    variable=course_var,
    value="BSc PSY",
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(anchor="w")

tk.Radiobutton(
    course_frame,
    text="BA & BM",
    variable=course_var,
    value="BA & BM",
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(anchor="w")

# Languages known
tk.Label(
    form_frame,
    text="Languages known",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).grid(row=6, column=0, sticky="nw", pady=6)

lang_frame = tk.Frame(form_frame, bg="#E8E8E8")
lang_frame.grid(row=6, column=1, sticky="w", pady=6)

english_var = tk.BooleanVar()
tagalog_var = tk.BooleanVar()
hindi_var = tk.BooleanVar()

lang_row1 = tk.Frame(lang_frame, bg="#E8E8E8")
lang_row1.pack(anchor="w")

tk.Checkbutton(
    lang_row1,
    text="English",
    variable=english_var,
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(side=tk.LEFT)

tk.Checkbutton(
    lang_row1,
    text="Tagalog",
    variable=tagalog_var,
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(side=tk.LEFT)

tk.Checkbutton(
    lang_frame,
    text="Hindi/Urdu",
    variable=hindi_var,
    font=("Arial", 9),
    bg="#E8E8E8",
    activebackground="#E8E8E8"
).pack(anchor="w")

# Rate your English communication skills
tk.Label(
    content_frame,
    text="Rate your English communication skills",
    font=("Arial", 9),
    bg="#E8E8E8",
    fg="#000000"
).pack(pady=(15, 5))

skill_scale = tk.Scale(
    content_frame,
    from_=0,
    to=100,
    orient=tk.HORIZONTAL,
    length=350,
    bg="#E8E8E8",
    fg="#000000",
    troughcolor="#D0D0D0",
    activebackground="#4A90E2",
    highlightthickness=0,
    showvalue=0,
    sliderrelief=tk.FLAT
)
skill_scale.set(50)
skill_scale.pack()

# Buttons
button_frame = tk.Frame(content_frame, bg="#E8E8E8")
button_frame.pack(pady=20)

btn_submit = tk.Button(
    button_frame,
    text="Submit",
    font=("Arial", 10, "bold"),
    bg="#3D4B5C",
    fg="white",
    width=18,
    height=2,
    command=submit_form,
    relief=tk.FLAT,
    bd=0
)
btn_submit.pack(side=tk.LEFT, padx=10)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 10, "bold"),
    bg="#3D4B5C",
    fg="white",
    width=18,
    height=2,
    command=clear_form,
    relief=tk.FLAT,
    bd=0
)
btn_clear.pack(side=tk.LEFT, padx=10)

root.mainloop()