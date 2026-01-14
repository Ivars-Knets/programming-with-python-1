import turtle

luz = turtle.Turtle()
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]

# get in a better position on screen
luz.penup()
luz.width(5)
luz.back(100)
luz.pendown()

for i in range(len(rainbow)):
    rainbow_color = rainbow[i]
    arch_move = 10 + i
    half_circumference = 0
    
    luz.color(rainbow_color)
    luz.left(90)
    for side in range(37):
        half_circumference += arch_move
        luz.forward(arch_move)
        luz.right(5)
        
    luz.penup()
    luz.left(95)
    # c = 2*r*pi = d*pi  => d = c/pi
    luz.back((2*half_circumference) / 3.1)
    luz.pendown()
    
