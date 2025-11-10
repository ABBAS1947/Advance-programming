import tkinter as tk
from tkinter import font
import random


class JokeTeller:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa Joke Teller")
        self.root.geometry("600x400")
        self.root.configure(bg="#2C3E50")

        self.jokes = self.load_jokes()
        self.current_joke = None
        self.showing_punchline = False

        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        text_font = font.Font(family="Helvetica", size=12)
        button_font = font.Font(family="Helvetica", size=11)

        self.title_label = tk.Label(root, text="Alexa Joke Teller",
                                    font=title_font, bg="#2C3E50", fg="#ECF0F1")
        self.title_label.pack(pady=20)

        self.input_frame = tk.Frame(root, bg="#2C3E50")
        self.input_frame.pack(pady=10)

        self.input_entry = tk.Entry(self.input_frame, font=text_font, width=30)
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.bind('<Return>', lambda e: self.process_input())

        self.submit_btn = tk.Button(self.input_frame, text="Send", font=button_font,
                                    command=self.process_input, bg="#3498DB", fg="white")
        self.submit_btn.pack(side=tk.LEFT)

        self.joke_text = tk.Text(root, font=text_font, height=8, width=50,
                                 wrap=tk.WORD, bg="#34495E", fg="#ECF0F1",
                                 state=tk.DISABLED, relief=tk.FLAT)
        self.joke_text.pack(pady=20, padx=20)

        self.action_btn = tk.Button(root, text="Show Punchline", font=button_font,
                                    command=self.show_punchline, bg="#27AE60",
                                    fg="white", state=tk.DISABLED, width=20)
        self.action_btn.pack(pady=10)

        self.quit_btn = tk.Button(root, text="Quit", font=button_font,
                                  command=root.quit, bg="#E74C3C", fg="white", width=20)
        self.quit_btn.pack(pady=5)

        self.display_message("Type 'Alexa tell me a Joke' to get started!")
        self.input_entry.focus()

    def load_jokes(self):
        try:
            with open('resources/randomJokes.txt', 'r') as file:
                jokes = []
                for line in file:
                    line = line.strip()
                    if '?' in line:
                        parts = line.split('?', 1)
                        setup = parts[0] + '?'
                        punchline = parts[1]
                        jokes.append((setup, punchline))
                return jokes
        except FileNotFoundError:
            return [("Why did the chicken cross the road?", "To get to the other side."),
                    ("What happens if you boil a clown?", "You get a laughing stock.")]

    def display_message(self, message):
        self.joke_text.config(state=tk.NORMAL)
        self.joke_text.delete(1.0, tk.END)
        self.joke_text.insert(tk.END, message)
        self.joke_text.config(state=tk.DISABLED)

    def process_input(self):
        user_input = self.input_entry.get().strip().lower()
        self.input_entry.delete(0, tk.END)

        if "alexa tell me a joke" in user_input:
            self.tell_joke()
        else:
            self.display_message("Please say 'Alexa tell me a Joke' to hear a joke!")

    def tell_joke(self):
        if self.jokes:
            self.current_joke = random.choice(self.jokes)
            self.display_message(self.current_joke[0])
            self.showing_punchline = False
            self.action_btn.config(state=tk.NORMAL)

    def show_punchline(self):
        if self.current_joke and not self.showing_punchline:
            self.display_message(f"{self.current_joke[0]}\n\n{self.current_joke[1]}")
            self.showing_punchline = True
            self.action_btn.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    app = JokeTeller(root)
    root.mainloop()