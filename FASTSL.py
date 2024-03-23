import tkinter as tk

class ServiceLevelCalculatorWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Service Level Calculator")
        self.geometry("300x200")
        self.configure(bg="gray")
        self.create_widgets()

    def create_widgets(self):
        self.grid = tk.Frame(self, bg="gray", padx=10, pady=10)
        self.grid.pack(expand=True, fill="both")

        self.add_entry("Total Calls:", 0)
        self.add_entry("Total Answered Calls:", 1)
        self.add_entry("Answered Calls within 30s:", 2)
        self.add_entry("Abandoned Calls (after 5s):", 3)

        self.calculateButton = tk.Button(self.grid, text="Calculate", command=self.on_calculate_button_clicked)
        self.calculateButton.grid(row=4, column=0, columnspan=2, pady=5)

        self.serviceLevelLabel = tk.Label(self.grid, text="", fg="black", bg="gray")
        self.serviceLevelLabel.grid(row=5, column=0, columnspan=2, pady=5)

    def add_entry(self, labelText, row):
        label = tk.Label(self.grid, text=labelText, fg="white", bg="gray", anchor="w")
        label.grid(row=row, column=0, padx=5, pady=5, sticky="w")

        entry = tk.Entry(self.grid)
        entry.grid(row=row, column=1, padx=5, pady=5)
        entry.config(width=20)

    def on_calculate_button_clicked(self):
        try:
            totalCalls = int(self.grid.grid_slaves(row=0, column=1)[0].get())
            totalAnsweredCalls = int(self.grid.grid_slaves(row=1, column=1)[0].get())
            answeredCalls30s = int(self.grid.grid_slaves(row=2, column=1)[0].get())
            abandonedCalls5s = int(self.grid.grid_slaves(row=3, column=1)[0].get())

            if totalAnsweredCalls + abandonedCalls5s == 0:
                raise ValueError("Total answered calls and abandoned calls cannot be zero.")

            serviceLevel = (answeredCalls30s / (totalAnsweredCalls + abandonedCalls5s)) * 100.0

            serviceLevelText = "Service Level: {:.2f}%".format(serviceLevel)
            self.serviceLevelLabel.config(text=serviceLevelText)

            # Set text color to red if service level is below 85%
            if serviceLevel < 85:
                self.serviceLevelLabel.config(fg="red")
            else:
                self.serviceLevelLabel.config(fg="black")

        except ValueError as e:
            self.serviceLevelLabel.config(text="Error: " + str(e), fg="black")

win = ServiceLevelCalculatorWindow()
win.mainloop()
