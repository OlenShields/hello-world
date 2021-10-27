#project 6

iterationNum = int(input("Enter the number of iterations: "));

piNum = 0;
iterationCount = 1;
for i in range(0,iterationNum + 1):
    piNum = piNum + (pow(-1,i) * 4.0)/(2 * i + 1)
print("The approximate value of pi is ", piNum)
