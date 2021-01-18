from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()

# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column('Pokemon Name', ['Pickachu', 'Squirtle', 'Charamander'], align='l')
table.add_column('Type', ['Electric', 'Water', 'Fire'], align='l')
print(table)