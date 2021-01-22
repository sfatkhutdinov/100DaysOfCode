from turtle import Screen
from paddle import Paddle

# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')

# TODO 2: Create and move a paddle
paddle_r = Paddle('right')
paddle_l = Paddle('left')
screen.listen()
screen.onkey(paddle_r.move_up, 'Up')
screen.onkey(paddle_r.move_down, 'Down')
screen.onkey(paddle_l.move_up, 'w')
screen.onkey(paddle_l.move_down, 's')

# TODO 3: Create another paddle
# TODO 4: Create the ball and make it move
# TODO 5: Detect collision with wall and bounce
# TODO 6: Detect collision with paddle
# TODO 7: Detect when paddle misses
# TODO 8: Keep score
screen.exitonclick()
