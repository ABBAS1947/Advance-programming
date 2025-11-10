import tkinter as tk
import random

# we will start off with functions first.
def displayMenu():
    global level_frame, quiz_frame
    level_frame.pack()
    quiz_frame.pack_forget()
    result_frame.pack_forget()

def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)

def decideOperation():
    return random.choice(['+', '-'])

def start_quiz(level_choice):
    global level
    level = level_choice
    global question_num, score
    question_num = 0
    score = 0
    level_frame.pack_forget()
    quiz_frame.pack()
    next_question()

def next_question():
    global num1, num2, op, correct_answer, question_num
    if question_num == 10:
        displayResults()
        return

    question_num += 1
    num1 = randomInt(level)
    num2 = randomInt(level)
    op = decideOperation()
    correct_answer = num1 + num2 if op == '+' else num1 - num2
    feedback_label.config(text="")
    question_label.config(text=f"Question {question_num}:  {num1} {op} {num2} = ?")
    answer_entry.delete(0, tk.END)

def isCorrect(user_answer):
    global correct_answer, score
    try:
        user_answer = int(user_answer)
    except ValueError:
        feedback_label.config(text="Please enter a number.", fg="red")
        return

    if user_answer == correct_answer:
        feedback_label.config(text="Correct!", fg="green")
        score += 10
        window.after(1000, next_question)
    else:
        feedback_label.config(text="Incorrect. Try again!", fg="red")
        submit_btn.config(command=lambda: second_attempt())

def second_attempt():
    global score
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        feedback_label.config(text="Please enter a number.", fg="red")
        return

    if user_answer == correct_answer:
        feedback_label.config(text="Correct on second try!", fg="green")
        score += 5
    else:
        feedback_label.config(text=f"Wrong again! Correct answer: {correct_answer}", fg="red")
    window.after(1000, next_question)

def displayResults():
    quiz_frame.pack_forget()
    result_frame.pack()
    score_label.config(text=f"Your Final Score: {score}/100")
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    else:
        grade = "F"
    grade_label.config(text=f"Your Rank: {grade}")

# and this is the tkinter gui setup
window = tk.Tk()
window.title("Arithmetic Quiz")
window.geometry("400x300")
window.config(bg="#f2f2f2")


level_frame = tk.Frame(window, bg="#f2f2f2")
tk.Label(level_frame, text="Select Difficulty Level", font=("Arial", 16), bg="#f2f2f2").pack(pady=15)
tk.Button(level_frame, text="Easy (1-digit)", width=20, command=lambda: start_quiz(1)).pack(pady=5)
tk.Button(level_frame, text="Moderate (2-digit)", width=20, command=lambda: start_quiz(2)).pack(pady=5)
tk.Button(level_frame, text="Advanced (4-digit)", width=20, command=lambda: start_quiz(3)).pack(pady=5)

# well this is the frame for the quiz after level selection.
quiz_frame = tk.Frame(window, bg="#f2f2f2")
question_label = tk.Label(quiz_frame, text="", font=("Arial", 14), bg="#f2f2f2")
question_label.pack(pady=10)
answer_entry = tk.Entry(quiz_frame, font=("Arial", 14))
answer_entry.pack(pady=5)
submit_btn = tk.Button(quiz_frame, text="Submit", command=lambda: isCorrect(answer_entry.get()))
submit_btn.pack(pady=5)
feedback_label = tk.Label(quiz_frame, text="", font=("Arial", 12), bg="#f2f2f2")
feedback_label.pack(pady=10)

# and this is the result frame.
result_frame = tk.Frame(window, bg="#f2f2f2")
score_label = tk.Label(result_frame, text="", font=("Arial", 16), bg="#f2f2f2")
score_label.pack(pady=10)
grade_label = tk.Label(result_frame, text="", font=("Arial", 14), bg="#f2f2f2")
grade_label.pack(pady=10)
tk.Button(result_frame, text="Play Again", command=displayMenu).pack(pady=5)
tk.Button(result_frame, text="Exit", command=window.destroy).pack(pady=5)

displayMenu()
window.mainloop()
