#project 5

#importing math

import math


#creating a function

def prediction():
    sp = int(input("Enter the initial number of organism: "))

    g = float(input("Enter the rate of growth: "))

    while(g<1):
        


        g = float(input("Enter the rate of growth: "))

    r = int(input("Enter the number of hours to achieve the entered rate of growth: "))

    t = int(input("Enter the number of hours which the poplation grows: "))

    tp=sp

    hours = 1

    while (hours < t):

        tp *= g

        hours += r
    print("The total population is " + str(int(tp)))
    
#calling the created function
    
prediction()
