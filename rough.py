import random
x = random.randint(-280, 280)
y = random.randint(-280, 280)

food = Turtle("circle")
food.penup()
food.color("red")
food.goto(x,y)