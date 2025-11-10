import tkinter as tk
import time
import random

sentences = [
    "Object Oriented Programming using Python",
    "Full stack software developer.",
    "Python is a fun programming language.",
    "Thabani Jason Moyo."
]

sentence = random.choice(sentences)

root = tk.Tk()
root.title("Kinetic Input Proficiency Evaluator")
root.geometry("1920x1080")

start_time = 0

def start_test():
    global start_time
    start_time = time.time()
    text_entry.delete(0, tk.END)
    result_label.config(text="Typing started...")

def finish_test():
    if start_time == 0:
        result_label.config(text="Click 'Start' first!")
        return
    end_time = time.time()
    total_time = end_time - start_time
    typed_text = text_entry.get()
    words = len(typed_text.split())
    wpm = words / (total_time / 60)
    correct = 0
    for i, c in enumerate(typed_text):
        if i < len(sentence) and c == sentence[i]:
            correct += 1
    accuracy = (correct / len(sentence)) * 100
    result_label.config(text=f"WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%")

label = tk.Label(root, text="Type the following sentence:", font=("Arial", 14))
label.pack(pady=10)
sentence_label = tk.Label(root, text=sentence, wraplength=600, font=("Arial", 12))
sentence_label.pack(pady=10)

text_entry = tk.Entry(root, width=80, font=("Arial", 12))
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Start", command=start_test, width=10).pack(side="left", padx=10)
tk.Button(button_frame, text="Finish", command=finish_test, width=10).pack(side="left", padx=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
