import turtle


a=turtle.Turtle()
a.getscreen().bgcolor ("cyan")
a.penup()


a.goto(-200,100)
a.pendown()


a.speed(3000)
def star(turtle,size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
            turtle.forward (size)
            star (turtle,size/3)
            turtle.left(216)
            turtle.end_fill()
            import turtle
            col=('red','yellow','green','cyan','blue','white')
            t=turtle.Turtle()
            screen=turtle.Screen()
            screen.bgcolor('black')
            t.speed(3000)
            for i in range(100):
                t.color(col[i%6])
                t.forward(i*4)
                t.left(150)
                t.width(2)

star(a,360)
turtle.done()