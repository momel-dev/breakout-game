from tkinter import messagebox
from turtle import Screen

from ball import Ball
from brick import Brick
from paddle import Paddle
from scoreboard import Scoreboard

# Configure the game window.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")

# Disable automatic screen updates for smoother rendering.
screen.tracer(0)

# Initialize the game objects.
scoreboard = Scoreboard()
paddle = Paddle((0, -250))
ball = Ball()

# Store the bricks that are currently active in the game.
brick_list = []


def create_brick_list():
    """Create a grid of bricks for the current stage."""
    for row in range(5):
        for col in range(7):
            # Calculate each brick's position in the grid.
            x = col * 100 - 300
            y = 200 - row * 40
            brick_list.append(Brick((x, y)))


# Create the initial set of bricks.
create_brick_list()

# Enable keyboard controls for the paddle.
screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")


def check_brick_collision():
    """Remove hit bricks, update the score, and bounce the ball."""
    # Iterate over a copy because bricks are removed from the original list.
    for brick in brick_list.copy():
        # Check whether the ball is close enough to a brick to count as a hit.
        if (
                abs(ball.xcor() - brick.xcor()) < 50
                and abs(ball.ycor() - brick.ycor()) < 20
        ):
            # Hide the hit brick and remove it from the active brick list.
            brick.hideturtle()
            brick_list.remove(brick)

            # Award a point and reverse the ball's vertical direction.
            scoreboard.increase_score()
            ball.bounce_y()
            break


def game_loop():
    """Update the game state and schedule the next frame."""
    # Refresh the screen and move the ball.
    screen.update()
    ball.move()

    # Bounce the ball off the left and right walls.
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    # Bounce the ball off the top wall.
    if ball.ycor() > 290:
        ball.bounce_y()

    # Bounce the ball when it hits the paddle while moving downward.
    if (
            paddle.xcor() - 70 < ball.xcor() < paddle.xcor() + 70
            and -260 < ball.ycor() <= -230
            and ball.y_move < 0
    ):
        ball.bounce_y()

    # Reset the ball and remove a life when it falls below the screen.
    if ball.ycor() < -300:
        ball.reset_position()
        ball.move_speed = 2
        scoreboard.lose_lives()

        # End the game when the player runs out of lives.
        if scoreboard.lives == 0:
            messagebox.showinfo("Game Over", "You lose the game!")
            return

    # Check whether the ball has hit any active brick.
    check_brick_collision()

    # Start a new stage when all bricks have been destroyed.
    if not brick_list:
        create_brick_list()
        ball.reset_position()

        # Increase the ball's speed to make the next stage more challenging.
        ball.move_speed += 0.1

        # Notify the player that the stage has been completed.
        # scoreboard.show_stage_complete_message()
        messagebox.showinfo("Stage Complete", "You completed the stage!")

    # Schedule the next game update after 10 milliseconds.
    screen.ontimer(game_loop, 10)


# Start the game loop.
game_loop()

# Keep the Turtle window open and responsive to user input.
screen.mainloop()
