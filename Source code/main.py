import tkinter as tk
from tkinter import messagebox
import math

# ------------------------
# FUNCTIONS
# ------------------------

def add():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_var.set(f"Result: {a + b}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

def subtract():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_var.set(f"Result: {a - b}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

def multiply():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_var.set(f"Result: {a * b}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

def divide():
    try:
        a = float(entry1.get())
        b = float(entry2.get())

        if b == 0:
            messagebox.showerror("Error", "Cannot divide by zero")
            return

        result_var.set(f"Result: {a / b}")
    except:
        messagebox.showerror("Error", "Enter valid numbers")

# ------------------------
# ADVANCED MATH
# ------------------------

def cube_root():
    try:
        num = float(entry1.get())

        if num >= 0:
            result = num ** (1/3)
        else:
            result = -((-num) ** (1/3))

        result_var.set(f"Cube Root: {result:.4f}")

    except:
        messagebox.showerror("Error", "Enter a valid number")

def square_root():
    try:
        num = float(entry1.get())

        if num < 0:
            messagebox.showerror("Error", "Negative number not allowed")
            return

        result = math.sqrt(num)
        result_var.set(f"Square Root: {result:.4f}")

    except:
        messagebox.showerror("Error", "Enter a valid number")

def power():
    try:
        base = float(entry1.get())
        exponent = float(entry2.get())

        result = base ** exponent
        result_var.set(f"Power Result: {result}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

def average():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())

        avg = (a + b + c) / 3
        result_var.set(f"Average: {avg:.2f}")

    except:
        messagebox.showerror("Error", "Enter valid numbers")

# ------------------------
# TEMPERATURE CONVERTER
# ------------------------

def c_to_f():
    try:
        c = float(entry1.get())
        f = (c * 9/5) + 32
        result_var.set(f"Fahrenheit: {f:.2f}°F")
    except:
        messagebox.showerror("Error", "Enter valid Celsius value")

def f_to_c():
    try:
        f = float(entry1.get())
        c = (f - 32) * 5/9
        result_var.set(f"Celsius: {c:.2f}°C")
    except:
        messagebox.showerror("Error", "Enter valid Fahrenheit value")

def c_to_k():
    try:
        c = float(entry1.get())
        k = c + 273.15
        result_var.set(f"Kelvin: {k:.2f}K")
    except:
        messagebox.showerror("Error", "Enter valid Celsius value")

def k_to_c():
    try:
        k = float(entry1.get())

        if k < 0:
            messagebox.showerror("Error", "Kelvin cannot be negative")
            return

        c = k - 273.15
        result_var.set(f"Celsius: {c:.2f}°C")
    except:
        messagebox.showerror("Error", "Enter valid Kelvin value")

# ------------------------
# CLEAR
# ------------------------

def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_var.set("Result will appear here")

# ------------------------
# GUI
# ------------------------

root = tk.Tk()
root.title("Python Smart Calculator")
root.geometry("900x700")
root.state("zoomed")   # fullscreen/maximized
root.resizable(True, True)

title = tk.Label(
    root,
    text="Python Smart Calculator",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

tk.Label(root, text="Number 1").pack()
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

tk.Label(root, text="Number 2").pack()
entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

tk.Label(root, text="Number 3 (Average Only)").pack()
entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=15)

# ------------------------
# BUTTONS
# ------------------------

tk.Button(frame, text="Add", width=12, command=add).grid(row=0, column=0, padx=5, pady=5)
tk.Button(frame, text="Subtract", width=12, command=subtract).grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="Multiply", width=12, command=multiply).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame, text="Divide", width=12, command=divide).grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame, text="Cube Root", width=12, command=cube_root).grid(row=2, column=0, padx=5, pady=5)
tk.Button(frame, text="Square Root", width=12, command=square_root).grid(row=2, column=1, padx=5, pady=5)

tk.Button(frame, text="Power", width=12, command=power).grid(row=3, column=0, padx=5, pady=5)
tk.Button(frame, text="Average", width=12, command=average).grid(row=3, column=1, padx=5, pady=5)

tk.Button(frame, text="C → F", width=12, command=c_to_f).grid(row=4, column=0, padx=5, pady=5)
tk.Button(frame, text="F → C", width=12, command=f_to_c).grid(row=4, column=1, padx=5, pady=5)

tk.Button(frame, text="C → K", width=12, command=c_to_k).grid(row=5, column=0, padx=5, pady=5)
tk.Button(frame, text="K → C", width=12, command=k_to_c).grid(row=5, column=1, padx=5, pady=5)

# ------------------------
# CLEAR BUTTON
# ------------------------

tk.Button(root, text="Clear", width=25, command=clear_fields).pack(pady=10)

# ------------------------
# RESULT LABEL
# ------------------------

result_var = tk.StringVar()
result_var.set("Result will appear here")

result_label = tk.Label(
    root,
    textvariable=result_var,
    font=("Arial", 14, "bold")
)
result_label.pack(pady=20)

# ------------------------
# FOOTER
# ------------------------

footer = tk.Label(
    root,
    text="Developer Ammar - Smart Calculator",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=10)

root.mainloop()