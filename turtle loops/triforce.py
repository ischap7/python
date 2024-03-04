import turtle

bob = turtle.Turtle()
bob.shape("turtle")

length = int(input("Enter side length:"))


for _ in range(3):
    bob.forward(length)
    bob.left(120)

bob.forward(length//2)
bob.left(120)

for _ in range(3):
    bob.forward(length//2)
    bob.right(120)

turtle.done()
