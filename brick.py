import random
from turtle import Turtle

# Colors used to give the bricks a random appearance.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Brick(Turtle):
    """Represent a colored brick in the Breakout game."""

    def __init__(self, position):
        super().__init__()

        # Configure the brick's appearance.
        self.hideturtle()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()

        # Place the brick at its assigned position.
        self.goto(position)
        self.showturtle()
