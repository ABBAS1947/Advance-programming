import tkinter as tk
from tkinter import messagebox, simpledialog


class Student:
    def __init__(self, code, name, cw1, cw2, cw3, exam):
        self.code = code
        self.name = name
        self.cw1 = int(cw1)
        self.cw2 = int(cw2)
        self.cw3 = int(cw3)
        self.exam = int(exam)

    def total_cw(self):
        return self.cw1 + self.cw2 + self.cw3

    def total(self):
        return self.total_cw() + self.exam

    def percentage(self):
        return (self.total() / 160) * 100

    def grade(self):
        p = self.percentage()
        if p >= 70:
            return 'A'
        elif p >= 60:
            return 'B'
        elif p >= 50:
            return 'C'
        elif p >= 40:
            return 'D'
        else:
            return 'F'


class StudentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("700x500")
        self.students = []
        self.filename = "resources/studentMarks.txt"

        self.load_students()
        self.create_widgets()

    def load_students(self):
        try:
            file = open(self.filename, 'r')
            lines = file.readlines()
            file.close()

            num_students = int(lines[0].strip())
            for i in range(1, num_students + 1):
                parts = lines[i].strip().split(',')
                student = Student(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                self.students.append(student)
        except:
            messagebox.showerror("Error", "Cannot find studentMarks.txt file!")

    def save_students(self):
        file = open(self.filename, 'w')
        file.write(str(len(self.students)) + "\n")
        for student in self.students:
            line = f"{student.code},{student.name},{student.cw1},{student.cw2},{student.cw3},{student.exam}\n"
            file.write(line)
        file.close()

    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="Student Manager", font=("Arial", 20, "bold"), bg="blue", fg="white")
        title_label.pack(fill=tk.X, pady=10)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        btn1 = tk.Button(button_frame, text="View All Students", command=self.view_all, width=20, height=2)
        btn1.grid(row=0, column=0, padx=5, pady=5)

        btn2 = tk.Button(button_frame, text="View Individual Student", command=self.view_individual, width=20, height=2)
        btn2.grid(row=0, column=1, padx=5, pady=5)

        btn3 = tk.Button(button_frame, text="Highest Score", command=self.show_highest, width=20, height=2)
        btn3.grid(row=1, column=0, padx=5, pady=5)

        btn4 = tk.Button(button_frame, text="Lowest Score", command=self.show_lowest, width=20, height=2)
        btn4.grid(row=1, column=1, padx=5, pady=5)

        btn5 = tk.Button(button_frame, text="Sort Records", command=self.sort_records, width=20, height=2)
        btn5.grid(row=2, column=0, padx=5, pady=5)

        btn6 = tk.Button(button_frame, text="Add Student", command=self.add_student, width=20, height=2)
        btn6.grid(row=2, column=1, padx=5, pady=5)

        btn7 = tk.Button(button_frame, text="Delete Student", command=self.delete_student, width=20, height=2)
        btn7.grid(row=3, column=0, padx=5, pady=5)

        btn8 = tk.Button(button_frame, text="Update Student", command=self.update_student, width=20, height=2)
        btn8.grid(row=3, column=1, padx=5, pady=5)

        # Display area
        self.text_box = tk.Text(self.root, height=15, width=80)
        self.text_box.pack(padx=10, pady=10)

    def display_text(self, text):
        self.text_box.delete('1.0', tk.END)
        self.text_box.insert('1.0', text)

    def format_student(self, student):
        text = f"Student Name: {student.name}\n"
        text += f"Student Number: {student.code}\n"
        text += f"Total Coursework: {student.total_cw()}/60\n"
        text += f"Exam Mark: {student.exam}/100\n"
        text += f"Overall Percentage: {student.percentage():.2f}%\n"
        text += f"Grade: {student.grade()}\n"
        text += "-" * 50 + "\n"
        return text

    def view_all(self):
        if len(self.students) == 0:
            self.display_text("No students found!")
            return

        output = "ALL STUDENT RECORDS\n"
        output += "=" * 50 + "\n\n"

        for student in self.students:
            output += self.format_student(student)

        total_percentage = 0
        for student in self.students:
            total_percentage += student.percentage()

        average = total_percentage / len(self.students)

        output += f"\nTotal Students: {len(self.students)}\n"
        output += f"Average Percentage: {average:.2f}%\n"

        self.display_text(output)

    def view_individual(self):
        if len(self.students) == 0:
            messagebox.showwarning("Warning", "No students found!")
            return

        # Create new window
        window = tk.Toplevel(self.root)
        window.title("Select Student")
        window.geometry("300x400")

        tk.Label(window, text="Select a student:", font=("Arial", 12)).pack(pady=10)

        listbox = tk.Listbox(window, height=15, width=40)
        listbox.pack(padx=10, pady=10)

        for i in range(len(self.students)):
            student = self.students[i]
            listbox.insert(tk.END, f"{i + 1}. {student.name}")

        def show_selected():
            selection = listbox.curselection()
            if len(selection) > 0:
                index = selection[0]
                output = "INDIVIDUAL STUDENT RECORD\n"
                output += "=" * 50 + "\n\n"
                output += self.format_student(self.students[index])
                self.display_text(output)
                window.destroy()

        tk.Button(window, text="View", command=show_selected, width=15).pack(pady=10)

    def show_highest(self):
        if len(self.students) == 0:
            messagebox.showwarning("Warning", "No students found!")
            return

        highest_student = self.students[0]
        for student in self.students:
            if student.total() > highest_student.total():
                highest_student = student

        output = "STUDENT WITH HIGHEST SCORE\n"
        output += "=" * 50 + "\n\n"
        output += self.format_student(highest_student)

        self.display_text(output)

    def show_lowest(self):
        if len(self.students) == 0:
            messagebox.showwarning("Warning", "No students found!")
            return

        lowest_student = self.students[0]
        for student in self.students:
            if student.total() < lowest_student.total():
                lowest_student = student

        output = "STUDENT WITH LOWEST SCORE\n"
        output += "=" * 50 + "\n\n"
        output += self.format_student(lowest_student)

        self.display_text(output)

    def sort_records(self):
        if len(self.students) == 0:
            messagebox.showwarning("Warning", "No students found!")
            return

        window = tk.Toplevel(self.root)
        window.title("Sort Records")
        window.geometry("250x150")

        tk.Label(window, text="Choose sort order:", font=("Arial", 12)).pack(pady=20)

        def sort_ascending():
            for i in range(len(self.students)):
                for j in range(i + 1, len(self.students)):
                    if self.students[i].total() > self.students[j].total():
                        temp = self.students[i]
                        self.students[i] = self.students[j]
                        self.students[j] = temp
            window.destroy()
            self.view_all()

        def sort_descending():
            for i in range(len(self.students)):
                for j in range(i + 1, len(self.students)):
                    if self.students[i].total() < self.students[j].total():
                        temp = self.students[i]
                        self.students[i] = self.students[j]
                        self.students[j] = temp
            window.destroy()
            self.view_all()

        tk.Button(window, text="Ascending", command=sort_ascending, width=15).pack(pady=5)
        tk.Button(window, text="Descending", command=sort_descending, width=15).pack(pady=5)

    def add_student(self):
        code = simpledialog.askstring("Input", "Enter student code (1000-9999):")
        if code is None:
            return

        name = simpledialog.askstring("Input", "Enter student name:")
        if name is None:
            return

        cw1 = simpledialog.askstring("Input", "Enter coursework 1 mark (0-20):")
        if cw1 is None:
            return

        cw2 = simpledialog.askstring("Input", "Enter coursework 2 mark (0-20):")
        if cw2 is None:
            return

        cw3 = simpledialog.askstring("Input", "Enter coursework 3 mark (0-20):")
        if cw3 is None:
            return

        exam = simpledialog.askstring("Input", "Enter exam mark (0-100):")
        if exam is None:
            return

        try:
            code_num = int(code)
            cw1_num = int(cw1)
            cw2_num = int(cw2)
            cw3_num = int(cw3)
            exam_num = int(exam)

            if code_num < 1000 or code_num > 9999:
                messagebox.showerror("Error", "Code must be between 1000 and 9999!")
                return

            if cw1_num < 0 or cw1_num > 20 or cw2_num < 0 or cw2_num > 20 or cw3_num < 0 or cw3_num > 20:
                messagebox.showerror("Error", "Coursework marks must be between 0 and 20!")
                return

            if exam_num < 0 or exam_num > 100:
                messagebox.showerror("Error", "Exam mark must be between 0 and 100!")
                return

            new_student = Student(code, name, cw1, cw2, cw3, exam)
            self.students.append(new_student)
            self.save_students()

            messagebox.showinfo("Success", f"Student {name} added successfully!")
        except:
            messagebox.showerror("Error", "Please enter valid numbers!")

    def delete_student(self):
        if len(self.students) == 0:
            messagebox.showwarning("Warning", "No students found!")
            return

        window = tk.Toplevel(self.root)
        window.title("Delete Student")
        window.geometry("300x400")

        tk.Label(window, text="Select student to delete:", font=("Arial", 12)).pack(pady=10)

        listbox = tk.Listbox(window, height=15, width=40)
        listbox.pack(padx=10, pady=10)

        for i in range(len(self.students)):
            student = self.students[i]
            listbox.insert(tk.END, f"{student.name} ({student.code})")

        def delete_selected():
            selection = listbox.curselection()
            if len(selection) > 0:
                index = selection[0]
                student_name = self.students[index].name

                answer = messagebox.askyesno("Confirm", f"Delete {student_name}?")
                if answer:
                    del self.students[index]
                    self.save_students()
                    messagebox.showinfo("Success", "Student deleted!")
                    window.destroy()

        tk.Button(window, text="Delete", command=delete_selected, width=15).pack(pady=10)

    def update_student(self):
        if len(self.students) == 0:
            messagebox.showwarning("Warning", "No students found!")
            return

        window = tk.Toplevel(self.root)
        window.title("Update Student")
        window.geometry("300x400")

        tk.Label(window, text="Select student to update:", font=("Arial", 12)).pack(pady=10)

        listbox = tk.Listbox(window, height=15, width=40)
        listbox.pack(padx=10, pady=10)

        for i in range(len(self.students)):
            student = self.students[i]
            listbox.insert(tk.END, f"{student.name} ({student.code})")

        def update_selected():
            selection = listbox.curselection()
            if len(selection) > 0:
                index = selection[0]
                student = self.students[index]
                window.destroy()

                name = simpledialog.askstring("Update", f"Enter new name (current: {student.name}):")
                if name:
                    student.name = name

                cw1 = simpledialog.askstring("Update", f"Enter coursework 1 (current: {student.cw1}):")
                if cw1:
                    student.cw1 = int(cw1)

                cw2 = simpledialog.askstring("Update", f"Enter coursework 2 (current: {student.cw2}):")
                if cw2:
                    student.cw2 = int(cw2)

                cw3 = simpledialog.askstring("Update", f"Enter coursework 3 (current: {student.cw3}):")
                if cw3:
                    student.cw3 = int(cw3)

                exam = simpledialog.askstring("Update", f"Enter exam mark (current: {student.exam}):")
                if exam:
                    student.exam = int(exam)

                self.save_students()
                messagebox.showinfo("Success", "Student updated!")

        tk.Button(window, text="Update", command=update_selected, width=15).pack(pady=10)


# Main program
root = tk.Tk()
app = StudentManager(root)
root.mainloop()