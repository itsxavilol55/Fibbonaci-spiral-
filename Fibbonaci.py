from turtle import *
import colorsys

# Configuración de la pantalla
bgcolor("black")
speed(0.1)

# Variables para la secuencia de Fibonacci
fib_num1 = 0
fib_num2 = 1
fib_num3 = 1
# Configuración del color
hue = 0
color_step = 1/20
# Bucle principal para dibujar la espiral de Fibonacci
for i in range(20):  # se puede cambiar 20 por una variable o constante que represente el número de iteraciones que se desea
    # Configuración del color para cada iteración
    color(colorsys.hsv_to_rgb(hue, 0.7, 1))
    hue += color_step
    # Dibujar un cuadrado y un arco de círculo para cada número de Fibonacci
    for j in range(4):
        forward(fib_num3 * 10)
        left(90)
    circle(fib_num3 * 10, 90)
    # Actualizar la secuencia de Fibonacci
    fib_num3 = fib_num1 + fib_num2
    fib_num1 = fib_num2
    fib_num2 = fib_num3
done()
