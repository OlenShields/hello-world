side1 = int(input("Input the length of side 1: "))
side2 = int(input("Input the length of side 2: "))
side3 = int(input("Input the length of side 3: "))
if ((side1*side1 + side2*side2 == side3*side3) or
    (side2*side2 + side3*side3 == side1*side1) or
    (side3*side3 + side1*side1 == side2*side2)):
    print("The values entered will produce a right triangle")
else:
    print("The values entered will not produce a right triangle")
