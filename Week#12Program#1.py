#UNWSP Programming PythonCos2005DEsp25
#Program_1_Gas Mileage Calculator
#04.25.25
#Abraham. N. Andersen

import tkinter as tk
from tkinter import ttk

def calculate_mpg():
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())
        if gallons > 0:
            mpg = miles / gallons
            result_label.config(text=f"Miles Per Gallon (MPG): {mpg:.2f}")
        else:
            result_label.config(text="Gallons must be greater than zero.")
    except ValueError:
        result_label.config(text="Enter numbers.")
window = tk.Tk()
window.title("Gas Mileage Calculator")
gallons_label = ttk.Label(window, text="Gallons of Gas:")
gallons_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
gallons_entry = ttk.Entry(window)
gallons_entry.grid(row=0, column=1, padx=5, pady=5)
miles_label = ttk.Label(window, text="Miles on Full Tank:")
miles_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
miles_entry = ttk.Entry(window)
miles_entry.grid(row=1, column=1, padx=5, pady=5)
calculate_button = ttk.Button(window, text="Calculate MPG", command=calculate_mpg)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
result_label = ttk.Label(window, text="Miles Per Gallon (MPG): ")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()