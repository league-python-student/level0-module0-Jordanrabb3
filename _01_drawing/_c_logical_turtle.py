import random
import turtle

# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

# ====================== DO NOT EDIT THE CODE ABOVE ===========================

def screenClicked(x, y):
    print('You pressed: x=' + str(x) + ', y=' + str(y))
    
    # 6. Call the turtle .penup() method
    jordan.penup()
    # 7. Move the turtle to a new location using .goto(x, y)
    jordan.goto(x=100, y=100)
def turtleClicked(x, y):
    print('turtle clicked!')
    
    # 8. Make a for loop to run the next instructions 3 times
    for i in range(3):
        # 9. Make the turtle spin 360 degrees using the .right() method
        jordan.right(360)
        # 10. Use the .color() method and getRandomColor() function to change
        # the color of the turtle,
        # myTurtle.color(getRandomColor())
        jordan.color(getRandomColor())

if __name__ == '__main__':
    window = turtle.Screen()
    window.setup(width=0.75, height=0.8, startx=0, starty=0)
    
    # 1. Make a new turtle
    jordan = turtle.Turtle()
    # 2. Make your turtle's shape 'turtle', .shape('turtle')
    jordan.shape('turtle')
    # 3. Set your turtle's color using .color('green') and .pencolor('blue')
    jordan.color('pink')
    # 4. Set and new width, length, and outline of our turtle
    #    myTurtle.turtlesize(stretch_wid=10, stretch_len=10, outline=4)
    jordan.turtlesize(stretch_wid=2, stretch_len=2, outline=4)
    # 5. Uncomment the following line and replace 'myTurtle' with your turtle
    #myTurtle.onclick(turtleClicked)
    jordan.onclick(turtleClicked)
# ===================== DO NOT EDIT THE CODE BELOW ============================
    window.onclick(screenClicked)
    turtle.done()
