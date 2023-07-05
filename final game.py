import pgzrun
from random import randint
#this line will import the pgzrun file
#This line will make it possible to run the current file with all the pygame commands
score = 0
basketball = Actor("bball.jpg")
#The Actor() function goes into the image folder and retrieves the name of the file inside the parentheses.You can change "Basketball" to the name of your item.
def draw():
    screen.clear()
#this will clear the screen
    basketball.draw()
#.draw will draw the icon on the screen.
#line will make it possible to run the current file with all the pygame commands
def place_icon():
    basketball.x = randint(10,800) 
    basketball.y = randint(10,600)
#This piece of code will place the icon 300 pixels along the x axis and 200 pixels along the y axis.After defining the function,you have to call it:
def on_mouse_down(pos):#pos is the position of the cursor
    global score#changing the score everywhere
    if basketball.collidepoint(pos):
        print("Nice Shot")
        place_icon()
        score +=1
        print(score)
    else:print("Miss")
    # on_mouse_down() is a function that runs everytime you click the mouse
pgzrun.go()  
    
    
    
    
