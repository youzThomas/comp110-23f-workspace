"""EX05 - Turtle Project."""

__author__ = "730679279"

from turtle import Turtle, colormode, done


def draw_house(a_turtle: Turtle, start_x: float, start_y: float) -> None:
    """Draw a house."""
    a_turtle.penup()
    a_turtle.goto(start_x, start_y)
    a_turtle.pendown()
    a_turtle.color("orange")
    a_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        a_turtle.forward(200)
        a_turtle.left(90)
        i = i + 1
    
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(start_x + 50.0, start_y)
    a_turtle.pendown()
    a_turtle.color("brown")
    a_turtle.begin_fill()
    
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(70)
    a_turtle.left(90)
    a_turtle.forward(50)
    a_turtle.left(90)
    a_turtle.forward(70)

    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(start_x + 170, start_y + 170)
    a_turtle.pendown()
    a_turtle.color("blue")
    a_turtle.right(90)
    a_turtle.begin_fill()

    j: int = 0
    while (j < 4):
        a_turtle.forward(60)
        a_turtle.left(90)
        j = j + 1

    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.goto(start_x, start_y + 200.0)
    a_turtle.pendown()
    a_turtle.color("brown")
    a_turtle.begin_fill()
    a_turtle.right(120)
    a_turtle.forward(200)
    a_turtle.right(120)
    a_turtle.forward(200)

    a_turtle.end_fill()


def draw_tree(paint: Turtle, x: float, y: float) -> None:
    """Draw four trees in a line."""
    i: int = 0
    while (i < 4):
        paint.penup()
        paint.goto(x, y)
        paint.pendown()
        colormode(255)
        paint.color(79, 54, 20)
        paint.begin_fill()
        paint.forward(60)
        paint.left(90)
        paint.forward(150)
        paint.left(90)
        paint.forward(60)
        paint.left(90)
        paint.forward(150)
        paint.end_fill()
        paint.left(90)
        paint.left(60)
        paint.penup()
        paint.goto(x - 30, y + 150)
        paint.pendown()
        paint.color("lightgreen")
        paint.begin_fill()
        paint.forward(120)
        paint.right(120)
        paint.forward(120)
        paint.right(120)
        paint.forward(120)
        paint.end_fill()
        paint.right(180)
        paint.penup()
        paint.goto(x - 30, y + 100)
        paint.pendown()
        paint.color("lightgreen")
        paint.begin_fill()
        paint.left(60)
        paint.forward(120)
        paint.right(120)
        paint.forward(120)
        paint.right(120)
        paint.forward(120)
        paint.end_fill()
        paint.right(180)
        x = x + 150
        i = i + 1


def draw_sun(painter: Turtle, x: float, y: float, radius: float) -> None:
    """Draw a sun at the top-right of the canva."""
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

    painter.color(235, 112, 46)
    painter.begin_fill()
    painter.circle(radius)
    painter.end_fill()


def draw_cloud(t: Turtle, x: float, y: float) -> None:
    """Draw a cloud."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("lightblue")
    t.begin_fill()
    t.setheading(90)
    t.circle(-5, 180)
    t.setheading(90)
    t.circle(-10, 180)
    t.setheading(90)
    t.circle(-5, 180)
    t.setheading(0)
    t.circle(-10, 180)
    t.setheading(-90)
    t.circle(-5, 180)
    t.setheading(-90)
    t.circle(-5, 180)
    t.setheading(-90)
    t.circle(-10, 180)
    t.setheading(0)
    t.circle(10, -150)
    t.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    display: Turtle = Turtle()

    draw_house(display, 10, -100)
    display.left(60)
    draw_tree(display, -700, -50)
    draw_tree(display, -700, -400)
    draw_sun(display, 600, 250, 100)
    draw_cloud(display, -700, 400)
    draw_cloud(display, -560, 410)
    draw_cloud(display, -500, 380)
    draw_cloud(display, -400, 300)
    draw_cloud(display, -320, 380)
    
    done()


if __name__ == "__main__":
    main()