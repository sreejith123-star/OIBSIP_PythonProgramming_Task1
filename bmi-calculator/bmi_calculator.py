import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt

# ---------------- Functions ---------------- #

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_input = float(height_entry.get())

        # Semester 2 Fix: Auto-convert CM to Meters if user types e.g., 164
        if height_input > 3:
            height = height_input / 100
        else:
            height = height_input

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Please enter positive values!")
            return

        bmi = round(weight / (height ** 2), 2)

        # Classification with color coding
        if bmi < 18.5:
            category, color = "Underweight", "blue"
        elif bmi < 25:
            category, color = "Normal", "green"
        elif bmi < 30:
            category, color = "Overweight", "orange"
        else:
            category, color = "Obese", "red"

        result_label.config(text=f"BMI: {bmi} ({category})", fg=color)
        save_data(bmi)

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

def save_data(bmi):
    file_exists = os.path.isfile("bmi_data.csv")
    with open("bmi_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["BMI"])
        writer.writerow([bmi])

def show_graph():
    if not os.path.isfile("bmi_data.csv"):
        messagebox.showerror("Error", "No history found!")
        return
    
    values = []
    with open("bmi_data.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            values.append(float(row[0]))
    
    plt.figure(figsize=(6,4))
    plt.plot(values, marker='o', color='green')
    plt.title("Your BMI Trend")
    plt.ylabel("BMI Value")
    plt.show()

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Oasis Infobyte - BMI Project")
root.geometry("350x450")

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=15)

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Height (cm or m):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Buttons
tk.Button(root, text="Calculate", command=calculate_bmi, bg="#4CAF50", fg="white", width=15).pack(pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields, width=15).pack(pady=5)
tk.Button(root, text="Show Graph", command=show_graph, width=15).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=20)

root.mainloop()