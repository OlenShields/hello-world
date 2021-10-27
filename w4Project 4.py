#project 4

height = float(input('Enter the initial height the ball is dropped from: '))

bounces = int(input('Enter the number of times the ball is allowed to continue bouncing: '))

bounciness = 0.6
distance = height

for i in range(bounces-1):
    height *= bounciness
    distance += 2*height

distance += height*bounciness

print('\nTotal distance traveled is: ' + str(distance) + ' units.')
