import math
temp = 0.000001
def newton(x, estimate =1):
   difference = abs(x-estimate**2)
   if difference <= temp:
     return estimate
   else :
      return newton(x, (estimate + x / estimate) / 2)
def main():
   while True:
      x = input("Enter a number: ")
      if x == "":
         break
         x = float(x)
      print("The program's estimate is", newton(x))
      print("Python's estimate is ", math.sqrt(x))
if __name__ == "__main__":
   main()

