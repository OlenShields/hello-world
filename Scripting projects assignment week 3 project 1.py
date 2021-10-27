# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
               
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))   

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents

#using round to output 2 decimals of precison at most
incomeTax = round(taxableIncome * TAX_RATE, 2)
         
# Display the income tax
print("The income tax is $" + str(incomeTax))
