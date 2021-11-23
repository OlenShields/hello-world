import math
temp=0.00001
estimate=1.0
x = float(input("Enter a positive number: "))
def newton(num,estimate):
    estimate=(estimate+num/estimate)/2
    difference =abs(num-estimate**2)
    if difference<= temp:
        return estimate
    else:
        return newton(num,estimate)
print("The functions Estimate: ",newton(x, estimate))
print("Math's estimate: ", math.sqrt(x))

