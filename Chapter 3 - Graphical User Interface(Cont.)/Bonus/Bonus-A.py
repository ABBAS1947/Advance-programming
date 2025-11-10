import tkinter as tk
from tkinter import messagebox, scrolledtext


class BurgerShackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Burger Shack Ordering System")
        self.root.geometry("650x700")
        self.root.configure(bg="#FFF3E0")


        self.burger_prices = {"Beef Burger": 8.99, "Chicken Burger": 7.99, "Veggie Burger": 6.99}
        self.topping_prices = {"Cheese": 1.50, "Bacon": 2.00, "Avocado": 1.75, "Egg": 1.25}
        self.condiment_prices = {"Ketchup": 0.25, "Mayonnaise": 0.25, "BBQ Sauce": 0.50, "Mustard": 0.25}
        self.side_prices = {"Fries": 3.50, "Onion Rings": 4.00, "Salad": 3.00, "Soda": 2.50, "Milkshake": 4.50}

        self.create_widgets()

    def create_widgets(self):

        title_label = tk.Label(
            self.root,
            text="🍔 Burger Shack 🍔",
            font=("Arial", 24, "bold"),
            bg="#FFF3E0",
            fg="#BF360C"
        )
        title_label.pack(pady=15)


        main_frame = tk.Frame(self.root, bg="#FFF3E0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10)


        burger_frame = tk.LabelFrame(
            main_frame,
            text="Select Your Burger",
            font=("Arial", 12, "bold"),
            bg="#FFCCBC",
            fg="#BF360C"
        )
        burger_frame.pack(fill=tk.X, padx=10, pady=5)

        self.burger_var = tk.StringVar()
        for burger, price in self.burger_prices.items():
            rb = tk.Radiobutton(
                burger_frame,
                text=f"{burger} - ${price:.2f}",
                variable=self.burger_var,
                value=burger,
                font=("Arial", 11),
                bg="#FFCCBC"
            )
            rb.pack(anchor=tk.W, padx=20, pady=3)


        topping_frame = tk.LabelFrame(
            main_frame,
            text="Select Toppings",
            font=("Arial", 12, "bold"),
            bg="#FFE0B2",
            fg="#E65100"
        )
        topping_frame.pack(fill=tk.X, padx=10, pady=5)

        self.topping_vars = {}
        for topping, price in self.topping_prices.items():
            var = tk.BooleanVar()
            self.topping_vars[topping] = var
            cb = tk.Checkbutton(
                topping_frame,
                text=f"{topping} - ${price:.2f}",
                variable=var,
                font=("Arial", 10),
                bg="#FFE0B2"
            )
            cb.pack(anchor=tk.W, padx=20, pady=2)


        condiment_frame = tk.LabelFrame(
            main_frame,
            text="Select Condiments",
            font=("Arial", 12, "bold"),
            bg="#FFF9C4",
            fg="#F57F17"
        )
        condiment_frame.pack(fill=tk.X, padx=10, pady=5)

        self.condiment_vars = {}
        for condiment, price in self.condiment_prices.items():
            var = tk.BooleanVar()
            self.condiment_vars[condiment] = var
            cb = tk.Checkbutton(
                condiment_frame,
                text=f"{condiment} - ${price:.2f}",
                variable=var,
                font=("Arial", 10),
                bg="#FFF9C4"
            )
            cb.pack(anchor=tk.W, padx=20, pady=2)


        side_frame = tk.LabelFrame(
            main_frame,
            text="Select Sides & Drinks",
            font=("Arial", 12, "bold"),
            bg="#C8E6C9",
            fg="#2E7D32"
        )
        side_frame.pack(fill=tk.X, padx=10, pady=5)

        self.side_vars = {}
        for side, price in self.side_prices.items():
            var = tk.BooleanVar()
            self.side_vars[side] = var
            cb = tk.Checkbutton(
                side_frame,
                text=f"{side} - ${price:.2f}",
                variable=var,
                font=("Arial", 10),
                bg="#C8E6C9"
            )
            cb.pack(anchor=tk.W, padx=20, pady=2)


        button_frame = tk.Frame(self.root, bg="#FFF3E0")
        button_frame.pack(pady=10)

        btn_order = tk.Button(
            button_frame,
            text="Place Order",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15,
            command=self.place_order
        )
        btn_order.pack(side=tk.LEFT, padx=5)

        btn_reset = tk.Button(
            button_frame,
            text="Reset",
            font=("Arial", 12, "bold"),
            bg="#F44336",
            fg="white",
            width=15,
            command=self.reset_order
        )
        btn_reset.pack(side=tk.LEFT, padx=5)

    def calculate_total(self):
        total = 0
        order_items = []


        burger = self.burger_var.get()
        if burger:
            total += self.burger_prices[burger]
            order_items.append(f"{burger}: ${self.burger_prices[burger]:.2f}")


        for topping, var in self.topping_vars.items():
            if var.get():
                total += self.topping_prices[topping]
                order_items.append(f"  + {topping}: ${self.topping_prices[topping]:.2f}")


        for condiment, var in self.condiment_vars.items():
            if var.get():
                total += self.condiment_prices[condiment]
                order_items.append(f"  + {condiment}: ${self.condiment_prices[condiment]:.2f}")


        for side, var in self.side_vars.items():
            if var.get():
                total += self.side_prices[side]
                order_items.append(f"{side}: ${self.side_prices[side]:.2f}")

        return total, order_items

    def place_order(self):
        if not self.burger_var.get():
            messagebox.showerror("Error", "Please select a burger!")
            return

        total, order_items = self.calculate_total()


        payment_window = tk.Toplevel(self.root)
        payment_window.title("Payment")
        payment_window.geometry("400x450")
        payment_window.configure(bg="#E8F5E9")


        tk.Label(
            payment_window,
            text="Order Summary",
            font=("Arial", 16, "bold"),
            bg="#E8F5E9",
            fg="#2E7D32"
        ).pack(pady=10)

        order_text = scrolledtext.ScrolledText(
            payment_window,
            width=40,
            height=10,
            font=("Arial", 10),
            bg="white"
        )
        order_text.pack(padx=20, pady=10)

        for item in order_items:
            order_text.insert(tk.END, item + "\n")
        order_text.insert(tk.END, f"\n{'=' * 35}\n")
        order_text.insert(tk.END, f"Total: ${total:.2f}\n")
        order_text.config(state=tk.DISABLED)


        payment_frame = tk.Frame(payment_window, bg="#E8F5E9")
        payment_frame.pack(pady=10)

        tk.Label(
            payment_frame,
            text="Amount Paid: $",
            font=("Arial", 12),
            bg="#E8F5E9"
        ).pack(side=tk.LEFT, padx=5)

        entry_payment = tk.Entry(payment_frame, font=("Arial", 12), width=10)
        entry_payment.pack(side=tk.LEFT, padx=5)

        result_label = tk.Label(
            payment_window,
            text="",
            font=("Arial", 11, "bold"),
            bg="#E8F5E9",
            fg="#1B5E20"
        )
        result_label.pack(pady=10)

        def process_payment():
            try:
                paid = float(entry_payment.get())
                if paid < total:
                    result_label.config(text=f"Insufficient! Need ${total - paid:.2f} more", fg="red")
                else:
                    change = paid - total
                    result_label.config(text=f"Payment Successful!\nChange: ${change:.2f}", fg="green")
                    messagebox.showinfo("Success", f"Order completed!\nChange: ${change:.2f}")
                    payment_window.destroy()
                    self.reset_order()
            except ValueError:
                result_label.config(text="Invalid amount!", fg="red")

        tk.Button(
            payment_window,
            text="Pay",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=15,
            command=process_payment
        ).pack(pady=10)

    def reset_order(self):
        self.burger_var.set("")
        for var in self.topping_vars.values():
            var.set(False)
        for var in self.condiment_vars.values():
            var.set(False)
        for var in self.side_vars.values():
            var.set(False)



root = tk.Tk()
app = BurgerShackApp(root)
root.mainloop()