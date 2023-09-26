import turtle
import turtle

 
s = turtle.Screen()
t = turtle.Turtle()
s.title("Ethiopian orginal Flag")
s.setup(width=700, height=600)
 
# Title on the window
 
pen = turtle.Turtle()
pen.speed(0)
pen.color("green") # this will show the color of green 
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("An ancient Ethiopian Flag", align="center",font=("Arial", 24, "normal"))
 
t.up()
t.goto(-100, -100)
t.down()
# blue strip
t.color("red") # this will show the color of red
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.end_fill()
 
# Move for next color
t.up()
t.goto(100, -50)
t.down()
# white strip
t.color("yellow")  # this will show the color of yellow
t.begin_fill()
t.left(90)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.end_fill()
 
# Move for next color
t.up()
t.goto(100, 0)
t.down()
# red strip
t.color("green") # this will show the color of green 
t.begin_fill()
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.left(90)
t.forward(50)
t.left(90)
t.forward(200)
t.end_fill()