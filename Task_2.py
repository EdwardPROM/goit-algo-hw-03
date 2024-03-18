import turtle
import argparse

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    parser = argparse.ArgumentParser(description="Visualize Koch snowflake fractal.")
    parser.add_argument("order", type=int, help="Level of recursion for Koch snowflake")
    args = parser.parse_args()

    order = args.order
    size = 400

    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch Snowflake (Order {order})")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size/2, 150)
    t.pendown()
    t.color("blue")

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()
