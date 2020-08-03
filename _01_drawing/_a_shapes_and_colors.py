import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')
    
    # This code makes a new Turtle. Pick a new name for the turtle
    jordan = turtle.Turtle()
    jordan.shape('turtle')
    jordan.turtlesize(stretch_wid=2, stretch_len=2, outline=2)
    # Makejordan.turtlesize(stretch_wid=7, stretch_len=7, outline=7)jordan.turtlesize(stretch_wid=7, stretch_len=7, outline=7) your turtle's shape 'turtle', .shape('turtle')
    jordan.speed(4)
    # Set your turtle's speed using .speed(2)
    jordan.color('pink')
    # Set your turtle's color using .color('green') and .pencolor('blue')
    jordan.pencolor('black')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    jordan.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    jordan.right(80)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(8):
        jordan.forward(60)
        jordan.right(90)
        jordan.forward(60)
        jordan.left(180)
        jordan.backward(80)
        # Move your turtle to a new place on the screen using .goto(x, y)
    jordan.circle(radius=100, extent=300, steps=600)# x=0 and y=0 is the center of the screen
    
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    
# ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
