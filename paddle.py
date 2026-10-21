from turtle import Turtle


class Paddle(Turtle):
    """Represent the player's paddle and handle its horizontal movement."""

    def __init__(self, position):
        super().__init__()

        # Configure the paddle's appearance and position.
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(position)
        self.showturtle()

    def go_right(self):
        """Move the paddle right without crossing the screen boundary."""
        new_x = self.xcor() + 40

        # Keep the paddle within the right edge of the play area.
        if new_x <= 330:
            self.goto(new_x, self.ycor())

    def go_left(self):
        """Move the paddle left without crossing the screen boundary."""
        new_x = self.xcor() - 40

        # Keep the paddle within the left edge of the play area.
        if new_x >= -330:
            self.goto(new_x, self.ycor())
