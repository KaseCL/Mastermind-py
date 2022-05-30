import turtle
from turtle import color, done
turtle.screensize(canvwidth=1920, canvheight=1080, bg='#d8d4d4')
import random
turtle.tracer(1,0)
turtle.speed(0)

#Colores
r = '#ff0000' #rojo
y = '#ffff66' #amarillo
v = '#33ff33' #verde
a = '#3333ff' #azul
o = '#cc9933' #naranjo
p = '#cc33cc' #rosa
w = '#ffffff' #blanco
n = '#000000' #negro
g = '#999999' #gris

#Clave secreta
c1 = random.randint(1,6)
c2 = random.randint(1,6)
c3 = random.randint(1,6)
c4 = random.randint(1,6)
c5 = random.randint(1,6)

#Colores disponibles para elegir
def colores(x3,y3,z3):
    turtle.penup()
    turtle.goto(x3,y3)
    turtle.pendown()
    turtle.color(z3)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color(n)
    turtle.circle(15)  
    turtle.penup()
    turtle.goto(-190,-180)
    turtle.pendown()
    turtle.forward(175)
#Coordenadas Colores y su ciclo
x3 = -215
y3 = 100
for i in range (1,7):
    if i == 1:
        colores(x3,y3,r)
    elif i ==2:
        colores(x3,y3,y)
    elif i ==3:
        colores(x3,y3,v)
    elif i ==4:
        colores(x3,y3,a)
    elif i ==5:
        colores(x3,y3,o)
    elif i ==6:
        colores(x3,y3,p)
    y3 = y3 - 35

#Coordenadas planilla del juego
x1 = -175
y1 = 150
def plantilla_juego(x1,y1):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.color(g)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color(n)
    turtle.circle(15)
plantilla_juego(x1,y1)

#Ciclo planilla de juego
for i in range (1,11):
    for i in range (1,6):
        plantilla_juego(x1,y1)
        x1 = x1 + 35
    x1 = -175
    y1 = y1 - 35

#Coordenadas circulos pequeños
x2 = 0
y2 = 160
z2 = g
def colores_acertados(x2,y2,z2):
    #Plantilla del juego (circulos pequeños grises)
    turtle.penup()
    turtle.goto(x2,y2)
    turtle.pendown()
    turtle.color(z2)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.color(n)
    turtle.circle(5)

#Ciclo circulos pequeños
for i in range (1,11):
    for i in range (1,6):
        colores_acertados(x2,y2,z2)
        x2 = x2 + 15
    x2 = 0
    y2 = y2 - 35

#Funcion input jugador
def ingresa_secuencia_jugador():
    global jc1,jc2,jc3,jc4,jc5
    print('----------------------')
    print('1 = Rojo ')
    print('2 = Amarillo')
    print('3 = Verde ')
    print('4 = Azul')
    print('5 = Naranjo')
    print('6 = Rosado')
    print('----------------------')
    jc1 = int(input('Ingrese su color para la casilla 1:'))
    while jc1 > 6 or 1 > jc1:
        print('Ingrese un valor valido')
        jc1 = int(input('Ingrese su color para la casilla 1:'))
    jc2 = int(input('Ingrese su color para la casilla 2:'))
    while jc2 > 6 or 1 > jc2:
        print('Ingrese un valor valido')
        jc2 = int(input('Ingrese su color para la casilla 2:'))
    jc3 = int(input('Ingrese su color para la casilla 3:'))
    while jc3 > 6 or 1 > jc3:
        print('Ingrese un valor valido')
        jc3 = int(input('Ingrese su color para la casilla 3:'))
    jc4 = int(input('Ingrese su color para la casilla 4:'))
    while jc4 > 6 or 1 > jc4:
        print('Ingrese un valor valido')
        jc4 = int(input('Ingrese su color para la casilla 4:'))
    jc5 = int(input('Ingrese su color para la casilla 5:'))
    while jc5 > 6 or 1 > jc5:
        print('Ingrese un valor valido')
        jc5 = int(input('Ingrese su color para la casilla 5:'))

#Transformar colores de numeros a hexadecimal
def transformador_de_colores(jc1,jc2,jc3,jc4,jc5):
    global ct1,ct2,ct3,ct4,ct5
    ct1 = 0
    ct2 = 0
    ct3 = 0
    ct4 = 0 
    ct5 = 0
    if jc1 == 1:
        ct1 = r
    elif jc1 == 2:
        ct1 = y
    elif jc1 == 3:
        ct1 = v
    elif jc1 == 4:
        ct1 = a
    elif jc1 == 5:
        ct1 = o
    elif jc1 == 6:
        ct1 = p

    if jc2 == 1:
        ct2 = r
    elif jc2 == 2:
        ct2 = y
    elif jc2 == 3:
        ct2 = v
    elif jc2 == 4:
        ct2 = a
    elif jc2 == 5:
        ct2 = o
    elif jc2 == 6:
        ct2 = p

    if jc3 == 1:
        ct3 = r
    elif jc3 == 2:
        ct3 = y
    elif jc3 == 3:
        ct3 = v
    elif jc3 == 4:
        ct3 = a
    elif jc3 == 5:
        ct3 = o
    elif jc3 == 6:
        ct3 = p

    if jc4 == 1:
        ct4 = r
    elif jc4 == 2:
        ct4 = y
    elif jc4 == 3:
        ct4 = v
    elif jc4 == 4:
        ct4 = a
    elif jc4 == 5:
        ct4 = o
    elif jc4 == 6:
        ct4 = p

    if jc5 == 1:
        ct5 = r
    elif jc5 == 2:
        ct5 = y
    elif jc5 == 3:
        ct5 = v
    elif jc5 == 4:
        ct5 = a
    elif jc5 == 5:
        ct5 = o
    elif jc5 == 6:
        ct5 = p


def comprobar_colores_acertados(jc1,jc2,jc3,jc4,jc5,c1,c2,c3,c4,c5):
    global negras,blancas
    negras = 0
    blancas = 0
    if jc1 == c1:
        negras += 1
        jc1 = True
        c1 = True
    if jc2 == c2:
        negras += 1
        jc2 = True
        c2 = True
    if jc3 == c3:
        negras += 1
        jc3 = True
        c3 = True
    if jc4 == c4:
        negras += 1
        jc4 = True
        c4 = True
    if jc5 == c5:
        negras += 1
        jc5 = True
        c5 = True
    
    if jc1 != True:
        if jc1 == c2:
            blancas += 1
            c2 = True
        elif jc1 == c3:
            blancas += 1
            c3 = True
        elif jc1 == c4:
            blancas += 1
            c4 = True
        elif jc1 == c5:
            blancas += 1
            c5 = True

    if jc2 != True:
        if jc2 == c1:
            blancas += 1
            c1 = True
        elif jc2 == c3:
            blancas += 1
            c3 = True
        elif jc2 == c4:
            blancas += 1
            c4 = True
        elif jc2 == c5:
            blancas += 1
            c5 = True

    if jc3 != True:
        if jc3 == c1:
            blancas += 1
            c1 = True
        elif jc3 == c2:
            blancas += 1
            c2 = True
        elif jc3 == c4:
            blancas += 1
            c4 = True
        elif jc3 == c5:
            blancas += 1
            c5 = True

    if jc4 != True:
        if jc4 == c1:
            blancas += 1
            c1 = True
        elif jc4 == c2:
            blancas += 1
            c2 = True
        elif jc4 == c3:
            blancas += 1
            c3 = True
        elif jc4 == c5:
            blancas += 1
            c5 = True

    if jc5 != True:
        if jc5 == c1:
            blancas += 1
            c1 = True
        elif jc5 == c2:
            blancas += 1
            c2 = True
        elif jc5 == c3:
            blancas += 1
            c3 = True
        elif jc5 == c4:
            blancas += 1
            c4 = True
    
#Circulos pequeños negro,blanco y gris
def colores_acertados_comprobados(x2,y2,z2):
    turtle.penup()
    turtle.goto(x2,y2)
    turtle.pendown()
    turtle.color(z2)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.color(n)
    turtle.circle(5) 

#Coordenadas circulos pequeños y su ciclo correspondiente
y2 = 160
def repetir_colores_acertados_comprobados(negras,blancas,y2):
    x2 = 0
    for i in range (1,6):
        if i == 1:
            if negras > 0:
                z2 = n
                negras -= 1
            elif blancas > 0:
                z2 = w
                blancas -= 1
            else:
                z2 = g
            colores_acertados_comprobados(x2,y2,z2)
        elif i == 2:
            if negras > 0:
                z2 = n
                negras -= 1
            elif blancas > 0:
                z2 = w
                blancas -= 1
            else:
                z2 = g
            colores_acertados_comprobados(x2,y2,z2)
        elif i == 3:
            if negras > 0:
                z2 = n
                negras -= 1
            elif blancas > 0:
                z2 = w
                blancas -= 1
            else:
                z2 = g
            colores_acertados_comprobados(x2,y2,z2)
        elif i == 4:
            if negras > 0:
                z2 = n
                negras -= 1
            elif blancas > 0:
                z2 = w
                blancas -= 1
            else:
                z2 = g
            colores_acertados_comprobados(x2,y2,z2)
        elif i == 5:
            if negras > 0:
                z2 = n
                negras -= 1
            elif blancas > 0:
                z2 = w
                blancas -= 1
            else:
                z2 = g
            colores_acertados_comprobados(x2,y2,z2)
        x2 = x2 + 15

#Circulos de colores respecto al input del jugador
x1 = -175
y1 = 150
def colores_jugador(x1,y1,z1):
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.color(z1)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()
    turtle.color(n)
    turtle.circle(15)

intentos = 0
#Ciclo de los input del jugador
def repetir_colores_jugador(intentos,y2):
    x1 = -175
    y1 = 150
    while intentos < 10:
        turtle.penup()
        turtle.forward(2000)
        print('----------------------')
        print(c1,c2,c3,c4,c5)
        ingresa_secuencia_jugador()
        transformador_de_colores(jc1,jc2,jc3,jc4,jc5)
        for i in range (1,6):
            if i == 1:
                colores_jugador(x1,y1,ct1)
            elif i == 2:
                colores_jugador(x1,y1,ct2)
            elif i == 3:
                colores_jugador(x1,y1,ct3)
            elif i == 4:
                colores_jugador(x1,y1,ct4)
            elif i == 5:
                colores_jugador(x1,y1,ct5)
            x1 = x1 + 35
        x1 = -175
        y1 = y1 - 35
        comprobar_colores_acertados(jc1,jc2,jc3,jc4,jc5,c1,c2,c3,c4,c5)
        print('----------------------')
        print('Negras:',negras)
        print('Blancas:',blancas)
        print('----------------------')
        contador = 1
        for i in range (contador):
            repetir_colores_acertados_comprobados(negras,blancas,y2)
            y2 = y2 - 35
            contador += 1
        if negras == 5:
            intentos = 10
            print('Haz ganado')
            print('Combinacion ganadora:',jc1,jc2,jc3,jc4,jc5)
            x1 = -175
            y1 = -225
            transformador_de_colores(c1,c2,c3,c4,c5)
            for i in range (1,6):
                if i == 1:
                    colores_jugador(x1,y1,ct1)
                elif i == 2:
                    colores_jugador(x1,y1,ct2)
                elif i == 3:
                    colores_jugador(x1,y1,ct3)
                elif i == 4:
                    colores_jugador(x1,y1,ct4)
                elif i == 5:
                    colores_jugador(x1,y1,ct5)
                x1 = x1 + 35
                turtle.penup()
                turtle.forward(2000)
        intentos += 1 
repetir_colores_jugador(intentos,y2)

turtle.update()
done()
