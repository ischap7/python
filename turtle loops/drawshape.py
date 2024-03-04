import turtle

bob = turtle.Turtle()
bob.shape("turtle")
          
def shape(n):
    for i in range(n):
        bob.forward(100)
        bob.left(360//n)

shape(5)
turtle.done()