#import turtle
#import another_module

#print(another_module.another_variable)
#
# from turtle import Turtle, Screen
# timmy = Turtle() # create an object turtle
# print(timmy) # shows the turtle object created as Timmy and where it is located at in memory
# timmy.shape('turtle') # create turtle shape
# timmy.color('red', 'green') # color turtle red and green
# timmy.forward(100) # move turtle forward 100 paces
#
# my_screen = Screen() # create an object screen
# print(my_screen.canvheight) # print an attribute of the object
# my_screen.exitonclick() # call a method of the object

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align ='l'
print(table.align)
print(table)