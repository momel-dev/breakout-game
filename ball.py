from turtle import Turtle


class Ball(Turtle):
    """Represent the ball and control its movement and direction."""

    def __init__(self):
        super().__init__()

        # Configure the ball's appearance and initial position.
        self.hideturtle()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -230)
        self.showturtle()

        # Control the ball's movement speed and direction.
        self.move_speed = 2
        self.x_move = 3
        self.y_move = 3

    def move(self):
        """Move the ball according to its current direction and speed."""
        new_x = self.xcor() + self.x_move * self.move_speed
        new_y = self.ycor() + self.y_move * self.move_speed
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Reverse the ball's horizontal direction."""
        self.x_move *= -1

    def bounce_y(self):
        """Reverse the ball's vertical direction."""
        self.y_move *= -1

    def reset_position(self):
        """Reset the ball's position and direction."""
        self.hideturtle()
        self.goto(0, -230)

        # Reset the direction so the ball always starts moving upward.
        self.x_move = 3
        self.y_move = 3

        self.showturtle()
