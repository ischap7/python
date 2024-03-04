import turtle

bob = turtle.Turtle()
bob.shape("turtle")
bob.penup()

for i in range(12):
    bob.penup()
    bob.forward(50)
    bob.pendown()
    bob.forward(50)
    bob.stamp()
    bob.penup()
    bob.backward(100)
    bob.pendown()
    bob.left(150)
    
   
    
