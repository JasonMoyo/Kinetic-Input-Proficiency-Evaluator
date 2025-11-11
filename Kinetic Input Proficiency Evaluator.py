import tkinter as tk
from tkinter import messagebox
import time
import random
import os

sentences = [
    "Object Oriented Programming using Python",
    "Full stack software developer.",
    "Python is a fun programming language.",
    "Thabani Jason Moyo."
]

sentence = random.choice(sentences)
start_time = 0
user_name = ""
txt_file = "typing_history.txt"

if not os.path.exists(txt_file):
    with open(txt_file, "w") as f:
        f.write("==== TYPING HISTORY RECORDS ====\n\n")

root = tk.Tk()
root.title("Kinetic Input Proficiency Evaluator")
root.geometry("1920x1080")
root.configure(bg="#EAF0F1")

login_frame = tk.Frame(root, bg="#EAF0F1")
login_frame.pack(expand=True)

tk.Label(login_frame, text="Welcome to Kinetic Input Proficiency Evaluator",
         font=("Arial", 18, "bold"), bg="#EAF0F1", fg="#2C3E50").pack(pady=20)
tk.Label(login_frame, text="Enter your name to begin:", font=("Arial", 12),
         bg="#EAF0F1").pack(pady=10)
name_entry = tk.Entry(login_frame, width=30, font=("Arial", 12))
name_entry.pack(pady=5)

def start_login():
    global user_name
    user_name = name_entry.get().strip()
    if user_name == "":
        messagebox.showwarning("Input Required", "Please enter your name to start.")
    else:
        login_frame.pack_forget()
        show_typing_test()

tk.Button(login_frame, text="Continue", command=start_login,
          bg="#2ECC71", fg="white", font=("Arial", 12), width=15).pack(pady=20)

def show_typing_test():
    global text_entry, result_label, sentence_label, start_time

    test_frame = tk.Frame(root, bg="#EAF0F1")
    test_frame.pack(expand=True, fill="both")

    tk.Label(test_frame, text=f"Welcome, {user_name}!",
             font=("Arial", 14, "bold"), bg="#EAF0F1", fg="#1B4F72").pack(pady=10)
    tk.Label(test_frame, text="Type the following sentence:",
             font=("Arial", 12, "bold"), bg="#EAF0F1").pack(pady=5)

    global sentence
    sentence_label = tk.Label(test_frame, text=sentence, wraplength=700,
                              font=("Arial", 12), bg="white", fg="#2C3E50",
                              padx=10, pady=10, relief="solid")
    sentence_label.pack(pady=10)

    text_entry = tk.Entry(test_frame, width=70, font=("Arial", 12))
    text_entry.pack(pady=10, ipady=5)

    button_frame = tk.Frame(test_frame, bg="#EAF0F1")
    button_frame.pack(pady=10)

    tk.Button(button_frame, text="Start", command=start_test, width=12,
              bg="#3498DB", fg="white", font=("Arial", 11)).pack(side="left", padx=10)
    tk.Button(button_frame, text="Finish", command=finish_test, width=12,
              bg="#E67E22", fg="white", font=("Arial", 11)).pack(side="left", padx=10)
    tk.Button(button_frame, text="Reset", command=reset_test, width=12,
              bg="#9B59B6", fg="white", font=("Arial", 11)).pack(side="left", padx=10)
    tk.Button(button_frame, text="View History", command=view_history, width=12,
              bg="#16A085", fg="white", font=("Arial", 11)).pack(side="left", padx=10)

    result_label = tk.Label(test_frame, text="", font=("Arial", 12, "bold"),
                            bg="#EAF0F1", fg="#2C3E50")
    result_label.pack(pady=20)

def start_test():
    global start_time
    start_time = time.time()
    text_entry.delete(0, tk.END)
    result_label.config(text="Typing started... Start typing now!")

def finish_test():
    global start_time
    if start_time == 0:
        result_label.config(text="Please click 'Start' first!")
        return

    end_time = time.time()
    total_time = end_time - start_time
    typed_text = text_entry.get().strip()

    if typed_text == "":
        messagebox.showwarning("No Input", "You haven't typed anything yet!")
        return

    words = len(typed_text.split())
    wpm = words / (total_time / 60)
    correct = sum(1 for i, c in enumerate(typed_text) if i < len(sentence) and c == sentence[i])
    accuracy = (correct / len(sentence)) * 100

    result = f"WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%"
    result_label.config(text=result)
    messagebox.showinfo("Typing Test Result",
                        f"User: {user_name}\nTime: {total_time:.2f} sec\n\n{result}")

    with open(txt_file, "a") as f:
        f.write(f"Name: {user_name} | WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}% | Time: {total_time:.2f}s\n")

def reset_test():
    global start_time, sentence
    start_time = 0
    sentence = random.choice(sentences)
    sentence_label.config(text=sentence)
    text_entry.delete(0, tk.END)
    result_label.config(text="New sentence loaded! Click Start to try again.")

def view_history():
    if not os.path.exists(txt_file):
        messagebox.showinfo("No Data", "No history found yet!")
        return

    history_window = tk.Toplevel(root)
    history_window.title("Typing History")
    history_window.geometry("600x400")
    history_window.configure(bg="#F8F9F9")

    tk.Label(history_window, text="Typing History (All Users)",
             font=("Arial", 13, "bold"), bg="#F8F9F9", fg="#2C3E50").pack(pady=10)

    text_box = tk.Text(history_window, wrap="word", font=("Arial", 11))
    text_box.pack(padx=20, pady=10, fill="both", expand=True)

    with open(txt_file, "r") as f:
        data = f.read()

    text_box.insert("1.0", data)
    text_box.config(state="disabled")

root.mainloop()
