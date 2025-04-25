#UNWSP Programming PythonCos2005DEsp25
#Program_2_Joe's Automotive Services
#04.25.25
#Abraham. N. Andersen

import tkinter as tk

class AutomotiveServiceGUI:
    def __init__(self, master):
        self.master = master
        master.title("Joe's Automotive Services")

        self.services = {
            "Oil Change": 30.00,
            "Lube Job": 20.00,
            "Radiator Flush": 40.00,
            "Transmission Fluid": 100.00,
            "Inspection": 35.00,
            "Muffler Replacement": 200.00,
            "Tire Rotation": 20.00,
        }

        self.checkbox_vars = {}
        row_num = 0
        for service, price in self.services.items():
            var = tk.BooleanVar()
            tk.Checkbutton(master, text=f"{service} - ${price:.2f}", variable=var).grid(row=row_num, column=0, sticky=tk.W)
            self.checkbox_vars[service] = var
            row_num += 1

        self.calculate_button = tk.Button(master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=row_num, column=0, pady=10)

        self.total_label = tk.Label(master, text="Total Charges: $0.00", font=("Arial", 12, "bold"))
        self.total_label.grid(row=row_num + 1, column=0, sticky=tk.W)

    def calculate_total(self):
        total = 0.0
        for service, var in self.checkbox_vars.items():
            if var.get():
                total += self.services[service]
        self.total_label.config(text=f"Total Charges: ${total:.2f}")

if __name__ == '__main__':
    root = tk.Tk()
    gui = AutomotiveServiceGUI(root)
    root.mainloop()