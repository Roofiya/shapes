import turtle

#turtle.forward(15)
#turtle.right(25)
#turtle.done()

t = turtle.Turtle()
turtle.pencolor()

r = 50
t.circle(r)

# radius for smallest circle
r = 10
# number of circles
n = 10
# loop for printing tangent circles
for i in range(1, n + 1, 1):
    t.circle(r * i)
turtle.done()