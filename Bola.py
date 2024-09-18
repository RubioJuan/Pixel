import turtle

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Pong Mejorado")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # Desactiva la actualización automática de la pantalla

# Pala de jugador
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370, 0)  # Más separada del centro

# Pala de la computadora
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(370, 0)  # Más separada del centro

# Bola
ball = turtle.Turtle()
ball.speed(1)  # Reduce la velocidad de la animación
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25  # Aumenta la velocidad horizontal
ball.dy = -0.25  # Aumenta la velocidad vertical

# Puntajes
score_a = 0
score_b = 0

# Mostrar puntajes
scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)
scoreboard.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Movimiento de la pala de jugador
paddle_a_up = False
paddle_a_down = False

def paddle_a_up_start():
    global paddle_a_up
    paddle_a_up = True

def paddle_a_up_stop():
    global paddle_a_up
    paddle_a_up = False

def paddle_a_down_start():
    global paddle_a_down
    paddle_a_down = True

def paddle_a_down_stop():
    global paddle_a_down
    paddle_a_down = False

# Teclado
wn.listen()
wn.onkeypress(paddle_a_up_start, "w")
wn.onkeyrelease(paddle_a_up_stop, "w")
wn.onkeypress(paddle_a_down_start, "s")
wn.onkeyrelease(paddle_a_down_stop, "s")

# Movimiento de la pala de la computadora
def paddle_b_move():
    # Asegurarse de que la pala no se mueva fuera de los límites
    if paddle_b.ycor() < ball.ycor() and paddle_b.ycor() < 250:
        y = paddle_b.ycor() + 1
    elif paddle_b.ycor() > ball.ycor() and paddle_b.ycor() > -240:
        y = paddle_b.ycor() - 1
    else:
        y = paddle_b.ycor()
    paddle_b.sety(y)

# Movimiento continuo de la pala del jugador
def move_paddle_a():
    if paddle_a_up and paddle_a.ycor() < 250:
        y = paddle_a.ycor() + 20
        paddle_a.sety(y)
    if paddle_a_down and paddle_a.ycor() > -240:
        y = paddle_a.ycor() - 20
        paddle_a.sety(y)
    wn.ontimer(move_paddle_a, 20)

# Inicia el movimiento continuo
move_paddle_a()

# Bucle principal del juego
game_over = False
while not game_over:
    wn.update()

    # Movimiento de la bola
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Rebote en los bordes superior e inferior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Si la bola toca las barras de juego, se termina
    if ball.xcor() > 390 or ball.xcor() < -390:
        scoreboard.clear()
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Courier", 36, "normal"))
        game_over = True

    # Colisiones con las palas
    if (ball.dx > 0) and (360 > ball.xcor() > 350) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(350)
        ball.dx *= -1

    if (ball.dx < 0) and (-360 < ball.xcor() < -350) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-350)
        ball.dx *= -1

    # Movimiento de la pala de la computadora
    paddle_b_move()