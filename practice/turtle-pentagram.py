import turtle

amity = turtle.Turtle()

amity.color("red")

# circle
for side in range(72):
    amity.forward(10)
    amity.right(5)

# move the starting point of the star
amity.forward(5)

# star
for side in range(5):
    amity.right(72)
    amity.forward(220)
    amity.right(72)