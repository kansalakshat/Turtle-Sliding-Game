import turtle
import random
import time

screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")


aura = turtle.Turtle()
aura.hideturtle()
aura.color("#0CB4DE")
aura.pensize(4)
aura.speed(0)
aura.penup()
aura.goto(-250, -250)
aura.pendown()
for i in range(4):
    aura.forward(500)
    aura.left(90)
aura.left(90)
aura.forward(125)
aura.right(90)
aura.forward(500)
aura.left(90)
aura.forward(125)
aura.left(90)
aura.forward(500)
aura.right(90)
aura.forward(125)
aura.right(90)
aura.forward(500)
for i in range(2):
    aura.left(90)
    aura.forward(125)
aura.left(90)
aura.forward(500)
aura.right(90)
aura.forward(125)
aura.right(90)
aura.forward(500)
aura.left(90)
aura.forward(125)
aura.left(90)
aura.forward(500)

timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.color("white")
timer_turtle.penup()
timer_turtle.goto(0, 285)

start_time = time.time()
running = True

def update_timer():
    if running:
        elapsed = int(time.time() - start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        timer_turtle.clear()
        timer_turtle.write(f"Time: {minutes:02}:{seconds:02}",
                           align="center", font=("Arial", 16, "bold"))
        screen.ontimer(update_timer, 1000)

moves = 0
moves_turtle = turtle.Turtle()
moves_turtle.hideturtle()
moves_turtle.penup()
moves_turtle.color("white")
moves_turtle.goto(-200, 285)

def movewriter():
    moves_turtle.clear()
    moves_turtle.write(f"Moves: {moves}", align="left", font=("Arial", 16, "bold"))

screen.addshape("images/1.gif")
i1 = turtle.Turtle()
i1.shape("images/1.gif")
i1.speed(0)
i1.penup()
i1.goto(-190,190)

screen.addshape("images/2.gif")
i2 = turtle.Turtle()
i2.shape("images/2.gif")
i2.speed(0)
i2.penup()
i2.goto(-63,190)

screen.addshape("images/3.gif")
i3 = turtle.Turtle()
i3.speed(0)
i3.shape("images/3.gif")
i3.penup()
i3.goto(63,190)

screen.addshape("images/4.gif")
i4 = turtle.Turtle()
i4.shape("images/4.gif")
i4.speed(0)
i4.penup()
i4.goto(190,190)

screen.addshape("images/5.gif")
i5 = turtle.Turtle()
i5.shape("images/5.gif")
i5.speed(0)
i5.penup()
i5.goto(-190,62)

screen.addshape("images/6.gif")
i6 = turtle.Turtle()
i6.shape("images/6.gif")
i6.speed(0)
i6.penup()
i6.goto(-62,62)

screen.addshape("images/7.gif")
i7 = turtle.Turtle()
i7.shape("images/7.gif")
i7.speed(0)
i7.penup()
i7.goto(62,62)

screen.addshape("images/8.gif")
i8 = turtle.Turtle()
i8.shape("images/8.gif")
i8.speed(0)
i8.penup()
i8.goto(190,62)

screen.addshape("images/9.gif")
i9 = turtle.Turtle()
i9.shape("images/9.gif")
i9.speed(0)
i9.penup()
i9.goto(-188,-62)

screen.addshape("images/10.gif")
i10 = turtle.Turtle()
i10.shape("images/10.gif")
i10.speed(0)
i10.penup()
i10.goto(-63,-62)

screen.addshape("images/11.gif")
i11 = turtle.Turtle()
i11.shape("images/11.gif")
i11.speed(0)
i11.penup()
i11.goto(63,-62)

screen.addshape("images/12.gif")
i12 = turtle.Turtle()
i12.shape("images/12.gif")
i12.speed(0)
i12.penup()
i12.goto(188,-62)

screen.addshape("images/13.gif")
i13 = turtle.Turtle()
i13.shape("images/13.gif")
i13.speed(0)
i13.penup()
i13.goto(-188,-188)

screen.addshape("images/14.gif")
i14 = turtle.Turtle()
i14.shape("images/14.gif")
i14.speed(0)
i14.penup()
i14.goto(-62,-188)

screen.addshape("images/15.gif")
i15 = turtle.Turtle()
i15.shape("images/15.gif")
i15.speed(0)
i15.penup()
i15.goto(62,-188)

screen.addshape("images/blank.gif")
ib = turtle.Turtle()
ib.shape("images/blank.gif")
ib.speed(0)
ib.penup()
ib.goto(190,-188)

turtles = [i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15]
places = [(-190,190),(-63,190),(63,190),(190,190),(-190,62),(-62,62),(62,62),(190,62),
          (-188,-62),(-63,-62),(63,-62),(188,-62),(-188,-188),(-62,-188),(62,-188)]

def win():
    global running
    count = 0
    for i in range(0, 15):
        if turtles[i].pos() == places[i]:
            count += 1
    if count == 15:
        running = False
        elapsed = int(time.time() - start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        timer_turtle.clear()
        timer_turtle.write(f"Finished in {minutes:02}:{seconds:02}",
                           align="center", font=("Arial", 16, "bold"))
        screen.addshape("images/win.gif")
        iw = turtle.Turtle()
        iw.shape("images/win.gif")


def swap1(x,y):
    global moves
    if i1.distance(ib)<=130:
        p1=i1.pos()
        pb=ib.pos()
        i1.goto(pb)
        ib.goto(p1)
        moves += 1
        movewriter()
        win()

def swap2(x,y):
    global moves
    if i2.distance(ib)<=130:
        p2=i2.pos()
        pb=ib.pos()
        i2.goto(pb)
        ib.goto(p2)
        moves += 1
        movewriter()
        win()

def swap3(x,y):
    global moves
    if i3.distance(ib)<=130:
        p3=i3.pos()
        pb=ib.pos()
        i3.goto(pb)
        ib.goto(p3)
        moves += 1
        movewriter()
        win()

def swap4(x,y):
    global moves
    if i4.distance(ib)<=130:
        p4=i4.pos()
        pb=ib.pos()
        i4.goto(pb)
        ib.goto(p4)
        moves += 1
        movewriter()
        win()

def swap5(x,y):
    global moves
    if i5.distance(ib)<=130:
        p5=i5.pos()
        pb=ib.pos()
        i5.goto(pb)
        ib.goto(p5)
        moves += 1
        movewriter()
        win()

def swap6(x,y):
    global moves
    if i6.distance(ib)<=130:
        p6=i6.pos()
        pb=ib.pos()
        i6.goto(pb)
        ib.goto(p6)
        moves += 1
        movewriter()
        win()

def swap7(x,y):
    global moves
    if i7.distance(ib)<=130:
        p7=i7.pos()
        pb=ib.pos()
        i7.goto(pb)
        ib.goto(p7)
        moves += 1
        movewriter()
        win()

def swap8(x,y):
    global moves
    if i8.distance(ib)<=130:
        p8=i8.pos()
        pb=ib.pos()
        i8.goto(pb)
        ib.goto(p8)
        moves += 1
        movewriter()
        win()

def swap9(x,y):
    global moves
    if i9.distance(ib)<=130:
        p9=i9.pos()
        pb=ib.pos()
        i9.goto(pb)
        ib.goto(p9)
        moves += 1
        movewriter()
        win()

def swap10(x,y):
    global moves
    if i10.distance(ib)<=130:
        p10=i10.pos()
        pb=ib.pos()
        i10.goto(pb)
        ib.goto(p10)
        moves += 1
        movewriter()
        win()

def swap11(x,y):
    global moves
    if i11.distance(ib)<=130:
        p11=i11.pos()
        pb=ib.pos()
        i11.goto(pb)
        ib.goto(p11)
        moves += 1
        movewriter()
        win()

def swap12(x,y):
    global moves
    if i12.distance(ib)<=130:
        p12=i12.pos()
        pb=ib.pos()
        i12.goto(pb)
        ib.goto(p12)
        moves += 1
        movewriter()
        win()

def swap13(x,y):
    global moves
    if i13.distance(ib)<=130:
        p13=i13.pos()
        pb=ib.pos()
        i13.goto(pb)
        ib.goto(p13)
        moves += 1
        movewriter()
        win()

def swap14(x,y):
    global moves
    if i14.distance(ib)<=130:
        p14=i14.pos()
        pb=ib.pos()
        i14.goto(pb)
        ib.goto(p14)
        moves += 1
        movewriter()
        win()

def swap15(x,y):
    global moves
    if i15.distance(ib)<=130:
        p15=i15.pos()
        pb=ib.pos()
        i15.goto(pb)
        ib.goto(p15)
        moves += 1
        movewriter()
        win()


i1.onclick(swap1)
i2.onclick(swap2)
i3.onclick(swap3)
i4.onclick(swap4)
i5.onclick(swap5)
i6.onclick(swap6)
i7.onclick(swap7)
i8.onclick(swap8)
i9.onclick(swap9)
i10.onclick(swap10)
i11.onclick(swap11)
i12.onclick(swap12)
i13.onclick(swap13)
i14.onclick(swap14)
i15.onclick(swap15)

swap = [swap1,swap2,swap3,swap4,swap5,swap6,swap7,swap8,
        swap9,swap10,swap11,swap12,swap13,swap14,swap15]

for i in swap:
    idx=0
    for i in range(0,15):
        p,q=random.choice(turtles).pos()
        b = random.choice(swap)(p,q)
        idx+=1
    if idx==15:
        flag=True

moves = 0
movewriter()
update_timer()
turtle.done()