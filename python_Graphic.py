        # This code creates a colorful spiral pattern using the turtle module and the colorsys module.
import turtle
import colorsys
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black') # This code sets the background color of the screen to black
t.speed(70)  # The speed of the turtle is set to 70
n = 70 
h = 0
for i in range(360): # The number of iterations is 360
    c = colorsys.hsv_to_rgb(n, 0, 0.8) # this uses for loop to change the hue, 
    # color, angle and radius of the turtle as it draws circles.
    h+= 1/n
    t.color(c)
    t.left(1)
    t.fd(1)
    for j in range(2):# The code uses a nested for loop to draw two circles at each iteration
        t.left(2)
        t.circle(100)


