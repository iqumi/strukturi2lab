import random
import turtle

SEED = 11
DEPTH = 8
LEFT_X = -480
RIGHT_X = 480
BOTTOM_Y = -300
SKY_COLOR = "light sky blue"

Point = tuple[float, float]

LAYERS = (
    {"color": "slate gray", "base": 40, "peak": 130, "roughness": 0.22},
    {"color": "dim gray", "base": 0, "peak": 100, "roughness": 0.2},
    {"color": "dark olive green", "base": -80, "peak": 60, "roughness": 0.18},
    {"color": "dark green", "base": -170, "peak": -40, "roughness": 0.16},
)


def midpoint_displacement(left: Point, right: Point, depth: int,
                          roughness: float) -> list[Point]:
    if depth == 0:
        return [left]

    width = right[0] - left[0]
    mid_x = (left[0] + right[0]) / 2
    mid_y = (left[1] + right[1]) / 2
    mid_y += random.uniform(-1, 1) * roughness * width
    middle = (mid_x, mid_y)

    left_part = midpoint_displacement(left, middle, depth - 1, roughness)
    right_part = midpoint_displacement(middle, right, depth - 1, roughness)
    return left_part + right_part


def build_ridge(base: float, peak: float, roughness: float) -> list[Point]:
    left = (LEFT_X, base)
    top = (random.uniform(LEFT_X / 2, RIGHT_X / 2), peak)
    right = (RIGHT_X, base)
    return (midpoint_displacement(left, top, DEPTH, roughness)
            + midpoint_displacement(top, right, DEPTH, roughness)
            + [right])


def draw_polygon(t: turtle.Turtle, ridge: list[Point], color: str) -> None:
    t.color(color)
    t.up()
    t.goto(LEFT_X, BOTTOM_Y)
    t.down()
    t.begin_fill()
    for point in ridge:
        t.goto(point)
    t.goto(RIGHT_X, BOTTOM_Y)
    t.goto(LEFT_X, BOTTOM_Y)
    t.end_fill()


def main() -> None:
    random.seed(SEED)
    screen = turtle.Screen()
    screen.setup(1000, 700)
    screen.bgcolor(SKY_COLOR)
    screen.tracer(0)
    t = turtle.Turtle()
    t.hideturtle()

    for layer in LAYERS:
        ridge = build_ridge(layer["base"], layer["peak"], layer["roughness"])
        draw_polygon(t, ridge, layer["color"])

    screen.update()
    screen.exitonclick()


if __name__ == "__main__":
    main()
