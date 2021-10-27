data = input("Enter any number or press enter with no input to quit: ")
number = float(data)
numbers = 0
theSum = 0
while data != "":
    number = float(data)
    theSum += number
    numbers += 1
    data = input("Enter the next number: ")
print("The sum of the entered numbers is", theSum)
average = theSum / numbers
print("The average of the entered numbers is", average)
