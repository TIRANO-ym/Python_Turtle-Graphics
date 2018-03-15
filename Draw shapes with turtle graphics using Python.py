import turtle as t
t.shape("turtle")   # Change the cursor to turtle shape

# Triangle
t.color("red")  # Change the ink color to red
for x in range(3):
    t.fd(100)   # = forward
    t.lt(120)   # = left

# Rectangle
t.color("green")    # Change the ink color to green
t.pensize(3)        # Change the line thickness to 3
for x in range(4):
    t.forward(100)  # = fd
    t.left(90)      # = lt

# Circle
t.color("blue")
t.circle(50)        # Radius 50
