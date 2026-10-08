import random
import turtle

TRUNK_LENGTH = 90 # длина ствола
MIN_BRANCH_LENGTH = 5 # мин. длина веток
LEAF_LENGTH = 30 # длина листьев
MIN_ANGLE = 15 # для случайного угла
MAX_ANGLE = 45 # для случайного угла
MIN_STEP = 6 # для случайной длины
MAX_STEP = 12 # для случайной длины
BRANCH_COLOR = "saddle brown"
LEAF_COLORS = ("pink", "light pink", "pale violet red")


def set_style(t: turtle.Turtle, branch_len: int) -> None:
    t.pensize(max(1, branch_len // 7))
    if branch_len <= LEAF_LENGTH:
        t.color(random.choice(LEAF_COLORS))
    else:
        t.color(BRANCH_COLOR)


def tree(branch_len: int, t: turtle.Turtle) -> None:
    if branch_len <= MIN_BRANCH_LENGTH:
        return

    right_angle = random.randint(MIN_ANGLE, MAX_ANGLE)
    left_angle = random.randint(MIN_ANGLE, MAX_ANGLE)
    step = random.randint(MIN_STEP, MAX_STEP)

    set_style(t, branch_len)
    t.forward(branch_len)
    t.right(right_angle)
    tree(branch_len - step, t)
    t.left(right_angle + left_angle)
    tree(branch_len - step, t)
    t.right(left_angle)
    set_style(t, branch_len)
    t.backward(branch_len)


def main() -> None:
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.tracer(0)
    t.hideturtle()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    tree(TRUNK_LENGTH, t)
    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
