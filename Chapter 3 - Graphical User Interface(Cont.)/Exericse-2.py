import tkinter as tk
from tkinter import messagebox


def make_coffee():
    coffee_type = coffee_var.get()


    options = []
    if sugar_var.get():
        options.append("Sugar")
    if milk_var.get():
        options.append("Milk")
    if cream_var.get():
        options.append("Cream")
    if vanilla_var.get():
        options.append("Vanilla")

    if not coffee_type:
        messagebox.showerror("Error", "Please select a coffee type!")
        return


    prices = {
        "Espresso": 3.00,
        "Cappuccino": 4.50,
        "Latte": 4.00,
        "Americano": 3.50,
        "Mocha": 5.00
    }

    total_price = prices[coffee_type]
    total_price += len(options) * 0.50
    message = f"Order Summary:\n\n"
    message += f"Coffee Type: {coffee_type}\n"
    if options:
        message += f"Add-ons: {', '.join(options)}\n"
    else:
        message += f"Add-ons: None\n"
    message += f"\nTotal Price: ${total_price:.2f}"

    messagebox.showinfo("Order Confirmed", message)


def reset_order():
    coffee_var.set("")
    sugar_var.set(False)
    milk_var.set(False)
    cream_var.set(False)
    vanilla_var.set(False)



root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("450x550")
root.configure(bg="#6D4C41")


title_label = tk.Label(
    root,
    text="Coffee Vending Machine",
    font=("Arial", 20, "bold"),
    bg="#6D4C41",
    fg="white"
)
title_label.pack(pady=20)


coffee_frame = tk.LabelFrame(
    root,
    text="Select Coffee Type",
    font=("Arial", 12, "bold"),
    bg="#BCAAA4",
    fg="#3E2723",
    bd=3
)
coffee_frame.pack(padx=20, pady=10, fill=tk.BOTH)

coffee_var = tk.StringVar()

coffees = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"]
for coffee in coffees:
    rb = tk.Radiobutton(
        coffee_frame,
        text=coffee,
        variable=coffee_var,
        value=coffee,
        font=("Arial", 11),
        bg="#BCAAA4",
        activebackground="#A1887F"
    )
    rb.pack(anchor=tk.W, padx=20, pady=5)


options_frame = tk.LabelFrame(
    root,
    text="Select Add-ons",
    font=("Arial", 12, "bold"),
    bg="#BCAAA4",
    fg="#3E2723",
    bd=3
)
options_frame.pack(padx=20, pady=10, fill=tk.BOTH)

sugar_var = tk.BooleanVar()
milk_var = tk.BooleanVar()
cream_var = tk.BooleanVar()
vanilla_var = tk.BooleanVar()

cb_sugar = tk.Checkbutton(
    options_frame,
    text="Sugar (+$0.50)",
    variable=sugar_var,
    font=("Arial", 11),
    bg="#BCAAA4",
    activebackground="#A1887F"
)
cb_sugar.pack(anchor=tk.W, padx=20, pady=5)

cb_milk = tk.Checkbutton(
    options_frame,
    text="Milk (+$0.50)",
    variable=milk_var,
    font=("Arial", 11),
    bg="#BCAAA4",
    activebackground="#A1887F"
)
cb_milk.pack(anchor=tk.W, padx=20, pady=5)

cb_cream = tk.Checkbutton(
    options_frame,
    text="Cream (+$0.50)",
    variable=cream_var,
    font=("Arial", 11),
    bg="#BCAAA4",
    activebackground="#A1887F"
)
cb_cream.pack(anchor=tk.W, padx=20, pady=5)

cb_vanilla = tk.Checkbutton(
    options_frame,
    text="Vanilla (+$0.50)",
    variable=vanilla_var,
    font=("Arial", 11),
    bg="#BCAAA4",
    activebackground="#A1887F"
)
cb_vanilla.pack(anchor=tk.W, padx=20, pady=5)


button_frame = tk.Frame(root, bg="#6D4C41")
button_frame.pack(pady=20)

btn_order = tk.Button(
    button_frame,
    text="Make Coffee",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=15,
    command=make_coffee
)
btn_order.pack(side=tk.LEFT, padx=5)

btn_reset = tk.Button(
    button_frame,
    text="Reset",
    font=("Arial", 12, "bold"),
    bg="#F44336",
    fg="white",
    width=15,
    command=reset_order
)
btn_reset.pack(side=tk.LEFT, padx=5)

root.mainloop()