import turtle

queen = turtle.Turtle()

queen.speed(30)

for i in range(180):
    queen.forward(100)
    queen.right(30)
    queen.forward(20)
    queen.left(60)
    queen.forward(50)
    queen.right(30)

    queen.penup()
    queen.setposition(0, 0)
    queen.pendown()

    queen.right(2)

turtle.done()
