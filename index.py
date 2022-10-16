from tkinter import mainloop
import turtle

scr = turtle.Screen()
scr.setup(width=800, height=600)

scr.title("Pong")
scr.bgcolor("black")

p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("white")
p1.penup()
p1.goto(-350, 0)
p1.shapesize(stretch_wid=5, stretch_len=1)

p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("white")
p2.penup()
p2.goto(350, 0)
p2.shapesize(stretch_wid=5, stretch_len=1)

pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.penup()
pelota.goto(0,0)
pelota.color("white")
pelota.dx = 5
pelota.dy = 5

linea = turtle.Turtle()
linea.color("white")
linea.goto(0, -400)
linea.goto(0, 400)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
#hideturtle sirve para esconder la flecha
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0          Player 2: 0", align="center", font=("Arial", 20, "normal"))

marcador_a = 0
marcador_b = 0

def p1_up():
    y = p1.ycor()
    p1.sety(y + 20)

def p1_down():
    y = p1.ycor()
    p1.sety(y - 20)

def p2_up():
    y = p2.ycor()
    p2.sety(y + 20)

def p2_down():
    y = p2.ycor()
    p2.sety(y - 20)


scr.listen()
scr.onkeypress(p1_up, "w")
scr.onkeypress(p1_down, "s")
scr.onkeypress(p2_up, "Up")
scr.onkeypress(p2_down, "Down")

while True:
    scr.update()
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    if(pelota.ycor() > 290):
        pelota.dy *= -1
    if(pelota.ycor() < -290):
        pelota.dy *= -1

    if(pelota.xcor() > 390):
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador_a += 1
        pen.clear()
        pen.write("Player 1: {}           Player 2: {}".format(marcador_a, marcador_b), align="center", font=("Arial", 20, "normal"))
    if(pelota.xcor() < -390):
        pelota.goto(0,0)
        pelota.dx *= -1
        marcador_b += 1
        pen.clear()
        pen.write("Player 1: {}          Player 2: {}".format(marcador_a, marcador_b), align="center", font=("Arial", 20, "normal"))
    """ Si las coordenadas x de pelota estan entre las
    cord de la paleta
    segundo if dice si las cord y es menor al lado sup
    de la paleta, el otro if lo mismo pero con la parte inf """

    if(pelota.xcor() > 340) and (pelota.xcor() < 350) and (pelota.ycor() < p2.ycor()+50) and (pelota.ycor() > p2.ycor()-50):
        pelota.dx *= -1

    if(pelota.xcor() < -340) and (pelota.xcor() > -350) and (pelota.ycor() < p1.ycor()+50) and (pelota.ycor() > p1.ycor()-50):
        pelota.dx *= -1

turtle.mainloop()

