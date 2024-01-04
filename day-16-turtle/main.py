
# import another_module
# from turtle import Turtle, Screen
# import prettytable
# print(another_module.another_variable)
# # import turtle
# # timmy=turtle.Turtle()
#
#
# timmy=Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electrico"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.align = "l"
print(table)
