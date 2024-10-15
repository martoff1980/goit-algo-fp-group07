import turtle


def squaretree(x, y, order, size, angle=0, alpha=45, beta=45):
    if order < 0:
        return

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(angle)
    turtle.fd(size)
    turtle.left(90)
    x1, y1 = turtle.xcor(), turtle.ycor()

    squaretree(x1, y1, order-1, size/2**0.5, angle+alpha)
    squaretree(x1, y1, order-1, size/2**0.5, angle-beta)


def draw_squaretree(order, size=50):
    window = turtle.Screen()
    window.bgcolor("black")

    turtle.color("red")
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-size / 4, size/4)
    turtle.pendown()

    squaretree(-size / 4, size/4, order, size, 90, 60, 20)

    window.mainloop()


level_recursion = int(input("Введіть рівень рекурсії:"))
draw_squaretree(level_recursion)
