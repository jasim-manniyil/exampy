import turtle

# Create a turtle object
square_turtle = turtle.Turtle()
square_turtle.pencolor("blue")
square_turtle.fillcolor("red")

# Function to draw a square
def draw_square(size):
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)

# Set the size of the square
square_size = 100

# Draw the square
draw_square(square_size)

# Finish drawing
turtle.done()
