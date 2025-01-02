import tkinter as tk
import os
import random

class QASystem:
    def __init__(self, root, directory="question_set"):
        self.root = root
        self.root.title("Q&A System")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        self.qa_pairs = self.load_questions_and_answers(directory)
        self.question_order = list(self.qa_pairs.keys())
        random.shuffle(self.question_order)
        self.current_question_index = 0

        self.create_widgets()

    def load_questions_and_answers(self, directory):
        """Load questions and answers from files in the specified directory."""
        qa_pairs = {}
        for file in os.listdir(directory):
            if file.endswith("question.txt"):
                question_id = file[:-12]  # Remove "question.txt"
                answer_file = f"{question_id}answer.txt"
                if os.path.exists(os.path.join(directory, answer_file)):
                    with open(os.path.join(directory, file), "r", encoding='utf-8', errors='replace') as qf:
                        question = qf.read().strip()
                    with open(os.path.join(directory, answer_file), "r",  encoding='utf-8', errors='replace') as af:
                        answer = af.read().strip()
                    qa_pairs[question_id] = (question, answer)
        return qa_pairs

    def create_widgets(self):
        header_label = tk.Label(self.root, text="Welcome to the Q&A System", font=("Verdana", 18, "bold"), bg="#121212", fg="#ffffff")
        header_label.pack(pady=10)

        frame = tk.Frame(self.root, bg="#121212")
        frame.pack(pady=20)

        self.create_question_area(frame)
        self.create_answer_area(frame)
        self.create_controls(frame)

    def create_question_area(self, frame):
        question_frame = tk.Frame(frame, bg="#121212")
        question_frame.grid(row=0, column=0, columnspan=2, pady=10)

        question_scroll = tk.Scrollbar(question_frame, orient=tk.VERTICAL)
        self.question_text = tk.Text(question_frame, wrap=tk.WORD, font=("Verdana", 14), height=8, width=60, yscrollcommand=question_scroll.set, bg="#1e1e1e", fg="#ffffff", state=tk.DISABLED)
        question_scroll.config(command=self.question_text.yview)
        question_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.question_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_answer_area(self, frame):
        answer_frame = tk.Frame(frame, bg="#121212")
        answer_frame.grid(row=3, column=0, columnspan=2, pady=10)

        answer_scroll = tk.Scrollbar(answer_frame, orient=tk.VERTICAL)
        self.answer_text = tk.Text(answer_frame, wrap=tk.WORD, font=("Verdana", 14), height=8, width=60, yscrollcommand=answer_scroll.set, bg="#1e1e1e", fg="#76c7c0", state=tk.DISABLED)
        answer_scroll.config(command=self.answer_text.yview)
        answer_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.answer_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_controls(self, frame):
        self.user_answer_entry = tk.Entry(frame, width=50, font=("Verdana", 14), bg="#1e1e1e", fg="#ffffff", insertbackground="#ffffff")
        self.user_answer_entry.grid(row=1, column=0, columnspan=2, pady=10)

        check_answer_button = tk.Button(frame, text="Submit Answer", command=self.check_answer, font=("Verdana", 14), bg="#4caf50", fg="white", width=15)
        check_answer_button.grid(row=2, column=0, pady=10, padx=5)

        next_question_button = tk.Button(frame, text="Next Question", command=self.show_next_question, font=("Verdana", 14), bg="#2196f3", fg="white", width=15)
        next_question_button.grid(row=2, column=1, pady=10, padx=5)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, font=("Verdana", 14), bg="#f44336", fg="white", width=20)
        exit_button.pack(pady=10)

    def show_next_question(self):
        """Display the next question."""
        if not self.qa_pairs:
            self.display_message(self.question_text, "No questions available.")
            self.display_message(self.answer_text, "")
            return

        if self.current_question_index >= len(self.question_order):
            self.display_message(self.question_text, "No more questions.")
            self.display_message(self.answer_text, "")
            return

        question_id = self.question_order[self.current_question_index]
        self.current_question_index += 1

        self.display_message(self.question_text, self.qa_pairs[question_id][0])
        self.user_answer_entry.delete(0, tk.END)
        self.display_message(self.answer_text, "")

    def check_answer(self):
        """Check the user's answer and display the correct answer."""
        if self.current_question_index == 0 or self.current_question_index > len(self.question_order):
            self.display_message(self.answer_text, "Please load a question first.")
            return

        question_id = self.question_order[self.current_question_index - 1]
        correct_answer = self.qa_pairs[question_id][1]
        self.display_message(self.answer_text, f"{correct_answer}")

    def display_message(self, widget, message):
        widget.config(state=tk.NORMAL)
        widget.delete("1.0", tk.END)
        widget.insert(tk.END, message)
        widget.config(state=tk.DISABLED)

