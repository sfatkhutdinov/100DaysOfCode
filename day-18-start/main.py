from turtle import Turtle, Screen
import random

tim = Turtle()

def change_color(turtle):
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R, G, B)

def draw_shape(turtle, sides):
    change_color(turtle)
    for _ in range(sides):
        tim.forward(100)
        tim.right(360 / sides)
    
def draw_to_some_shape(turtle, sides):
    for i in range(3,sides + 1):
        draw_shape(turtle, i)


def random_walk(turtle, iterations=200, size=10, speed=0, step_size=30):
    angle = [i for i in range(360)]
    for _ in range(iterations):
        turtle.speed(speed)
        turtle.pensize(size)
        change_color(turtle)
        turtle.forward(step_size)
        turtle.setheading(random.choice(angle))
    
def spirograph(turtle, angle=72, speed=0, circle_size=100):
    adjusted_angle = 360 / angle   
    turtle.speed(0) 
    for _ in range(angle):
        turtle.circle(circle_size)
        change_color(turtle)
        current_heading = turtle.heading()
        new_heading = current_heading + adjusted_angle
        turtle.setheading(new_heading)



screen = Screen()
screen.exitonclick()