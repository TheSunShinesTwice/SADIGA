import tkinter as tk
from tkinter import simpledialog
from datetime import datetime, timedelta
import re

# Define algorithms for all buttons
def button_1_algorithm(input_date):
    input_date = datetime.strptime(input_date, "%d-%m-%Y")
    learning_dates = [input_date + timedelta(days=d) for d in [1, 7, 16, 35, 80, 100]]
    applying_dates = [input_date + timedelta(days=d) for d in [4, 10, 20, 45, 60, 85, 110, 150]]
    return learning_dates, applying_dates

def button_2_algorithm(input_date):
    input_date = datetime.strptime(input_date, "%d-%m-%Y")
    learning_dates = [input_date + timedelta(days=d) for d in [1, 5, 9, 14, 21, 30, 50, 75, 95, 100, 150]]
    applying_dates = [input_date + timedelta(days=d) for d in [3, 7, 10, 40, 65, 80, 130]]
    return learning_dates, applying_dates

def button_3_algorithm(input_date):
    input_date = datetime.strptime(input_date, "%d-%m-%Y")
    learning_dates = [input_date + timedelta(days=d) for d in [1, 5, 9, 14, 21, 30, 50, 75, 95, 100, 150]]
    applying_dates = [input_date + timedelta(days=d) for d in [3, 10, 40, 80, 130]]
    return learning_dates, applying_dates

def button_4_algorithm(input_date):
    input_date = datetime.strptime(input_date, "%d-%m-%Y")
    learning_dates = [input_date + timedelta(days=d) for d in [1, 5, 14, 45, 90, 100, 150]]
    applying_dates = [input_date + timedelta(days=d) for d in [3, 7, 10, 21, 30, 50, 60, 85, 125, 160]]
    return learning_dates, applying_dates

def button_5_algorithm(input_date):
    input_date = datetime.strptime(input_date, "%d-%m-%Y")
    learning_dates = [input_date + timedelta(days=d) for d in [3, 7, 15, 50, 80, 150]]
    applying_dates = [input_date + timedelta(days=d) for d in [5, 30, 60, 100]]
    return learning_dates, applying_dates

def validate_date(date_str):
    pattern = r'^\d{2}-\d{2}-\d{4}$'
    return re.match(pattern, date_str) is not None

def get_input_date_and_topic():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    input_date = simpledialog.askstring("Input Date", "Enter the date (DD-MM-YYYY):")

    if input_date and not validate_date(input_date):
        tk.messagebox.showerror("Error", "Please enter the date in DD-MM-YYYY format.")
        return

    if input_date:
        topic_window = tk.Tk()
        topic_window.title("Select Topic")

        def handle_button_click(button_algorithm):
            learning_dates, applying_dates = button_algorithm(input_date)
            output_text = "Learning Dates:\n"
            for date in learning_dates:
                output_text += date.strftime("%d-%m-%Y") + "\n"
            output_text += "\nApplying Dates:\n"
            for date in applying_dates:
                output_text += date.strftime("%d-%m-%Y") + "\n"
            output_label.config(text=output_text)

        button_labels = [
            ("Moderate Topics/Physics/Physical Chemistry", button_1_algorithm),
            ("Most Advanced Topics/Organic Chemistry", button_2_algorithm),
            ("Inorganic Chemistry/Advanced Theoretical Topics", button_3_algorithm),
            ("Mathematics", button_4_algorithm),
            ("Light topics/English/Coaching", button_5_algorithm)
        ]

        for label, algorithm in button_labels:
            btn = tk.Button(topic_window, text=label, command=lambda a=algorithm: handle_button_click(a))
            btn.pack()

        output_label = tk.Label(topic_window, text="")
        output_label.pack()

        topic_window.mainloop()

get_input_date_and_topic()
