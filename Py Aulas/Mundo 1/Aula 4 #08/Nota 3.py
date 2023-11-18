import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(3)

# Use a loop to draw the square
for i in range(7):
    t.forward(20)
    t.right(300)

# Keep the window open until the user closes it
turtle.mainloop()