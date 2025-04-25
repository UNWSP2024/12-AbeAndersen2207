#UNWSP Programming PythonCos2005DEsp25
#Program_3_Telephone Call Charges
#04.25.25
#Abraham. N. Andersen

import tkinter as tk
from tkinter import messagebox

class CallChargeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Telephone Call Charges")

        self.rate_categories = {
            "Daytime (6:00 A.M. - 5:59 P.M.)": 0.02,
            "Evening (6:00 P.M. - 11:59 P.M.)": 0.12,
            "Off-Peak (Midnight - 5:59 A.M.)": 0.05,
        }

        self.selected_rate = tk.StringVar()
        self.selected_rate.set(list(self.rate_categories.keys())[0])  # Set default

        rate_label = tk.Label(master, text="Select Rate Category:")
        rate_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

        row_num = 1
        for category in self.rate_categories:
            rb = tk.Radiobutton(
                master,
                text=category,
                variable=self.selected_rate,
                value=category,
            )
            rb.grid(row=row_num, column=0, sticky=tk.W, padx=15)
            row_num += 1

        minutes_label = tk.Label(master, text="Enter Call Duration (minutes):")
        minutes_label.grid(row=row_num, column=0, sticky=tk.W, padx=5, pady=5)

        self.minutes_entry = tk.Entry(master)
        self.minutes_entry.grid(row=row_num + 1, column=0, padx=5, pady=5)

        calculate_button = tk.Button(master, text="Calculate Charge", command=self.calculate_charge)
        calculate_button.grid(row=row_num + 2, column=0, pady=10)

    def calculate_charge(self):
        try:
            minutes = float(self.minutes_entry.get())
            if minutes < 0:
                messagebox.showerror("Error", "Please enter a non-negative number of minutes.")
                return
            rate_category = self.selected_rate.get()
            rate_per_minute = self.rate_categories[rate_category]
            charge = minutes * rate_per_minute
            messagebox.showinfo("Call Charge", f"The charge for the call is: ${charge:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the call duration.")

if __name__ == '__main__':
    root = tk.Tk()
    gui = CallChargeGUI(root)
    root.mainloop()