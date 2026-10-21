from turtle import Turtle


class Scoreboard(Turtle):
    """Track and display the player's score and remaining lives."""

    def __init__(self):
        super().__init__()

        # Initialize the player's score and available lives.
        self.score = 0
        self.lives = 3

        # Configure the scoreboard without drawing lines.
        self.color("white")
        self.penup()
        self.hideturtle()

        # Display the initial score and lives.
        self.show_score()

    def increase_score(self):
        """Increase the score by one point and refresh the display."""
        self.score += 1
        self.show_score()

    def reset_score(self):
        """Reset the score to zero and refresh the display."""
        self.score = 0
        self.show_score()

    def lose_lives(self):
        """Remove one life and refresh the display."""
        self.lives -= 1
        self.show_score()

    def show_score(self):
        """Display the current score and remaining lives."""
        self.clear()
        self.goto(-350, 260)
        self.write(
            f"Score: {self.score}   |   Lives: {self.lives}",
            align="left",
            font=("Arial", 16, "normal"),
        )
