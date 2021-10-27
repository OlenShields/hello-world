#Taking an imput from the user for wage

hWage = float(input("Enter hourly wage: "))

#Taking an imput for the total number of hours at regular pay rate

rHours = float(input("Enter total number of regular hours: "))

#Taking an imput for the total number of hours at overtime rate

otHours = float(input("Enter overtime hours: "))

#Computing the weekly pay based upon the entered variables and given overtime rate

weeklyPay = (hWage * rHours) + (1.5 * hWage * otHours)

#Printing the weekly pay

print (weeklyPay)
