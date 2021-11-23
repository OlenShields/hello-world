def drawCircle (turtle, centerpoint, radius):
    circumference = 2 * 3.14 * (radius/120)
    print ("The circumference moved is"), circumference
    turtle.up()
    (x,y) = centerpoint[-1]
    turtle.turn(3)
    turtle.move(120)
    turtle.down()
    from turtlegraphics import Turtle
    turtle=Turtle()
    drawCircle(turtle, [(20,20)], 20)
