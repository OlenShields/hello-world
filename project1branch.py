TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
from tkinter import *
def computeTax():
    gTotal = float(Total.get())
    numDependents = float(Dependants.get())
    taxableIncome = gTotal - STANDARD_DEDUCTION
    taxableIncome = taxableIncome - (DEPENDENT_DEDUCTION * numDependents)
    incomeTax = taxableIncome * TAX_RATE
    myText.set(incomeTax)


calculator = Tk()
myText = StringVar()
calculator.title("Tax Calculator")
calculator.geometry("350x150")
Label(calculator, text="Income").grid(row=0)
Label(calculator, text="Dependents").grid(row=4)
Label(calculator, text="Total tax:").grid(row=8)
result = Entry(calculator, text="", textvariable=myText).grid(
    row=8, column=1)

Total = Entry(calculator)
Dependants = Entry(calculator)

Total.grid(row=0, column=1)
Dependants.grid(row=4, column=1)

b = Button(calculator, text="Compute", command=computeTax)
b.grid(row=6, column=1, columnspan=2, rowspan=2)


mainloop()
