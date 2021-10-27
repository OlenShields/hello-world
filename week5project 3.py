import random
import math

smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
while True:
    count += 1
    myNumber = (smaller + larger) // 2
    print('%d %d' % (smaller, larger))
    print('Your number is %d' % myNumber)
    choice = input('Enter equal, higher, or lower: ')
    if choice == 'equal':
        print("I got it in %d tries!" % count)
        break
    elif math.log(larger - smaller):
        print("I'm out of guesses after", count, "tries")
        break
    elif choice == 'larger':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1
