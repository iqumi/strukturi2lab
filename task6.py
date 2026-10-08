import turtle

ORDER = 3
SIDE_LENGTH = 300
SIDES = 3
OUTER_ANGLE = 120


def koch_curve(t: turtle.Turtle, order: int, length: float) -> None:
    if order == 0:
        t.forward(length)
        return

    segment = length / 3
    koch_curve(t, order - 1, segment)
    t.left(60)
    koch_curve(t, order - 1, segment)
    t.right(120)
    koch_curve(t, order - 1, segment)
    t.left(60)
    koch_curve(t, order - 1, segment)


def koch_snowflake(t: turtle.Turtle, order: int, length: float) -> None:
    for _ in range(SIDES):
        koch_curve(t, order, length)
        t.right(OUTER_ANGLE)


def main() -> None:
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)
    t.hideturtle()
    t.color("deep sky blue")
    t.pensize(2)
    t.up()
    t.goto(-SIDE_LENGTH / 2, SIDE_LENGTH / 3)
    t.down()
    koch_snowflake(t, ORDER, SIDE_LENGTH)
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
