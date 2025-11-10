import tkinter as tk
from tkinter import messagebox
import random


class GuessWordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Word Game")
        self.root.geometry("600x500")
        self.root.configure(bg="#E1F5FE")

        # Word list
        self.words = [
            "PYTHON", "JAVASCRIPT", "PROGRAMMING", "COMPUTER", "ALGORITHM",
            "DATABASE", "INTERNET", "DEVELOPER", "SOFTWARE", "HARDWARE",
            "NETWORK", "SECURITY", "FUNCTION", "VARIABLE", "INTERFACE"
        ]

        self.score = 0
        self.current_word = ""
        self.shuffled_word = ""
        self.words_played = 0
        self.max_words = 10

        self.create_widgets()
        self.new_word()

    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="🎮 Guess the Word Game 🎮",
            font=("Arial", 24, "bold"),
            bg="#E1F5FE",
            fg="#0277BD"
        )
        title_label.pack(pady=20)

        # Score display
        self.score_label = tk.Label(
            self.root,
            text=f"Score: {self.score} | Words: {self.words_played}/{self.max_words}",
            font=("Arial", 14, "bold"),
            bg="#E1F5FE",
            fg="#01579B"
        )
        self.score_label.pack(pady=10)

        # Instructions
        inst_label = tk.Label(
            self.root,
            text="Unscramble the letters to form the correct word!",
            font=("Arial", 12),
            bg="#E1F5FE",
            fg="#0277BD"
        )
        inst_label.pack(pady=5)

        # Shuffled word display
        word_frame = tk.Frame(self.root, bg="#B3E5FC", bd=5, relief=tk.RAISED)
        word_frame.pack(pady=20, padx=20, fill=tk.X)

        self.shuffled_label = tk.Label(
            word_frame,
            text="",
            font=("Arial", 28, "bold"),
            bg="#B3E5FC",
            fg="#01579B"
        )
        self.shuffled_label.pack(pady=20)

        # Input frame
        input_frame = tk.Frame(self.root, bg="#E1F5FE")
        input_frame.pack(pady=20)

        tk.Label(
            input_frame,
            text="Your Answer:",
            font=("Arial", 12, "bold"),
            bg="#E1F5FE"
        ).pack(side=tk.LEFT, padx=5)

        self.entry_answer = tk.Entry(input_frame, font=("Arial", 14), width=20)
        self.entry_answer.pack(side=tk.LEFT, padx=5)
        self.entry_answer.bind('<Return>', lambda e: self.check_answer())

        # Buttons
        button_frame = tk.Frame(self.root, bg="#E1F5FE")
        button_frame.pack(pady=20)

        btn_submit = tk.Button(
            button_frame,
            text="Submit",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            width=12,
            command=self.check_answer
        )
        btn_submit.pack(side=tk.LEFT, padx=5)

        btn_skip = tk.Button(
            button_frame,
            text="Skip",
            font=("Arial", 12, "bold"),
            bg="#FF9800",
            fg="white",
            width=12,
            command=self.skip_word
        )
        btn_skip.pack(side=tk.LEFT, padx=5)

        btn_hint = tk.Button(
            button_frame,
            text="Hint",
            font=("Arial", 12, "bold"),
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.show_hint
        )
        btn_hint.pack(side=tk.LEFT, padx=5)

        # Result label
        self.result_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            bg="#E1F5FE"
        )
        self.result_label.pack(pady=10)

    def shuffle_word(self, word):
        word_list = list(word)
        random.shuffle(word_list)
        shuffled = ''.join(word_list)

        # Make sure shuffled word is different from original
        while shuffled == word and len(word) > 1:
            random.shuffle(word_list)
            shuffled = ''.join(word_list)

        return shuffled

    def new_word(self):
        if self.words_played >= self.max_words:
            self.end_game()
            return

        self.current_word = random.choice(self.words)
        self.shuffled_word = self.shuffle_word(self.current_word)
        self.shuffled_label.config(text=self.shuffled_word)
        self.entry_answer.delete(0, tk.END)
        self.result_label.config(text="")

    def check_answer(self):
        user_answer = self.entry_answer.get().upper().strip()

        if not user_answer:
            messagebox.showwarning("Warning", "Please enter an answer!")
            return

        if user_answer == self.current_word:
            self.score += 10
            self.words_played += 1
            self.result_label.config(text="✓ Correct! +10 points", fg="green")
            self.score_label.config(text=f"Score: {self.score} | Words: {self.words_played}/{self.max_words}")
            self.root.after(1500, self.new_word)
        else:
            self.result_label.config(text=f"✗ Wrong! The answer was: {self.current_word}", fg="red")
            self.words_played += 1
            self.score_label.config(text=f"Score: {self.score} | Words: {self.words_played}/{self.max_words}")
            self.root.after(2000, self.new_word)

    def skip_word(self):
        self.result_label.config(text=f"Skipped! The answer was: {self.current_word}", fg="orange")
        self.words_played += 1
        self.score_label.config(text=f"Score: {self.score} | Words: {self.words_played}/{self.max_words}")
        self.root.after(1500, self.new_word)

    def show_hint(self):
        hint = self.current_word[0] + "_" * (len(self.current_word) - 2) + self.current_word[-1]
        self.result_label.config(text=f"Hint: {hint}", fg="blue")

    def end_game(self):
        percentage = (self.score / (self.max_words * 10)) * 100

        message = f"Game Over!\n\n"
        message += f"Final Score: {self.score}/{self.max_words * 10}\n"
        message += f"Percentage: {percentage:.1f}%\n\n"

        if percentage >= 80:
            message += "Excellent! 🌟"
        elif percentage >= 60:
            message += "Good Job! 👍"
        elif percentage >= 40:
            message += "Not Bad! 😊"
        else:
            message += "Keep Practicing! 💪"

        result = messagebox.askyesno("Game Over", message + "\n\nPlay Again?")

        if result:
            self.score = 0
            self.words_played = 0
            self.score_label.config(text=f"Score: {self.score} | Words: {self.words_played}/{self.max_words}")
            self.new_word()
        else:
            self.root.destroy()


# Create main window
root = tk.Tk()
app = GuessWordGame(root)
root.mainloop()