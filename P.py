import turtle

t = turtle.Turtle()

# Configuración inicial (puedes ajustar estos valores)
t.speed(3)
t.pensize(2)
t.pencolor("light blue")

# Levantar la pluma y posicionar para el inicio de la "A"
t.penup()
t.goto(-350, 150)  # Ajusta estas coordenadas para la posición inicial de la "A"
t.pendown()

# Dibujar el lado izquierdo de la "A"
t.left(75)         # Inclinación para el lado izquierdo
t.forward(150)

# Dibujar el lado derecho de la "A"
t.right(150)        # Cambia la dirección para el lado derecho (150 = 75 + 75)
t.forward(150)


# Levantar la pluma y posicionar para la barra transversal
t.penup()
t.goto(-340, 200)   # Ajusta estas coordenadas para la barra transversal
t.pendown()


# Dibujar la barra transversal
t.setheading(0)
t.left(180)        # Ajusta el ángulo para que sea horizontal (180 - 75)
t.forward(-50)


# --- Dibujo de la letra "L" ---
# Calculamos aproximadamente dónde terminó la "A" horizontalmente
# El lado derecho de la "A" termina aproximadamente en X = -200 + 150 * cos(75 grados)
# cos(75) es aproximadamente 0.2588
# X final de la "A" ≈ -200 + 38.8 = -161.2
# Vamos a darle un pequeño espacio, por ejemplo -150 para el inicio de la L

t.penup()
t.goto(-450, 100)  # Ajustamos la coordenada X para que esté a la derecha de la "A"
                    # Mantenemos la misma altura inicial (Y = 150)
# Levanta la pluma de la tortuga (no dibuja al moverse)
t.goto(-265, 300)           # Mueve la tortuga a la coordenada (-130 en X, 150 en Y) sin dibujar
t.pendown()                  # Baja la pluma de la tortuga (comienza a dibujar al moverse)
t.setheading(270)            # Establece la orientación de la tortuga a 270 grados (hacia abajo/sur)
t.forward(150)               # Mueve la tortuga hacia adelante 150 píxeles en la dirección actual (abajo), dibujando una línea vertical
t.setheading(0)              # Establece la orientación de la tortuga a 0 grados (hacia la derecha/este)
t.forward(80)                # Mueve la tortuga hacia adelante 75 píxeles en la dirección actual (derecha), dibujando una línea horizontal
                    
                
# --- Dibujo de la letra "F" ---
# La "L" terminó aproximadamente en X = -130 + 75 = -55
# Vamos a empezar la "F" un poco más a la derecha, por ejemplo en X = -40
t.penup()
t.goto(-180, 300)  # Misma altura inicial que la "A" y la "L"
t.pendown()
t.setheading(270)  # Apuntar hacia abajo para la línea vertical
t.forward(150)

# Dibujar la barra superior de la "F"
t.penup()
t.goto(-180, 300)  # Volver al inicio de la línea vertical
t.pendown()
t.setheading(0)    # Apuntar hacia la derecha
t.forward(60)      # Longitud de la barra superior

# Dibujar la barra del medio de la "F"
t.penup()
t.goto(-180, 240)   # Aproximadamente la mitad de la línea vertical
t.pendown()
t.setheading(0)
t.forward(60)      # Longitud de la barra del medio


# --- Dibujo de la letra "R" ---
# La "F" terminó aproximadamente en X = -170 + 60 = -110
# Vamos a empezar la "R" un poco más a la derecha, por ejemplo en X = -100
t.penup()
t.goto(-110, 300)  # Misma altura inicial
t.pendown()
t.setheading(270)  # Línea vertical
t.forward(150)

# Dibujar la curva superior de la "R" (aproximación con un círculo)
t.penup()
t.goto(-110, 300)  # Volver al inicio de la línea vertical
t.pendown()
t.setheading(0)    # Apuntar hacia la derecha para iniciar el semicírculo
t.circle(-35, 180) # Dibuja un semicírculo (radio negativo para la dirección)

# Dibujar la pierna de la "R"
t.penup()
t.goto(-100, 230)   # Aproximadamente la mitad de la línea vertical
t.pendown()
t.setheading(-60)  # Ángulo para la pierna
t.forward(90)
#***********************************************************************
# --- Dibujo de la letra "E" ---
# La "L" terminó aproximadamente en X = -130 + 75 = -55
# Vamos a empezar la "F" un poco más a la derecha, por ejemplo en X = -40
t.penup()
t.goto(-50, 300)  # Misma altura inicial que la "A" y la "L"
t.pendown()
t.setheading(270)  # Apuntar hacia abajo para la línea vertical
t.forward(150)

# Dibujar la barra superior de la "E"
t.penup()
t.goto(-50, 300)  # Volver al inicio de la línea vertical
t.pendown()
t.setheading(0)    # Apuntar hacia la derecha
t.forward(60)      # Longitud de la barra superior

# Dibujar la barra del medio de la "E"
t.penup()
t.goto(-50, 230)   # Aproximadamente la mitad de la línea vertical
t.pendown()
t.setheading(0)
t.forward(60)      # Longitud de la barra del medio

# Dibujar la barra del medio de la "E"
t.penup()
t.goto(-50, 150)   # Aproximadamente la mitad de la línea vertical
t.pendown()
t.setheading(0)
t.forward(60)      # Longitud de la barra del medio

# --- Dibujo de la letra "D" ---
# La "E" terminó aproximadamente en X = -20 + 60 = 40
# Vamos a empezar la "D" un poco más a la derecha, por ejemplo en X = 50
t.penup()
t.goto(40, 300)  # Misma altura inicial
t.pendown()
t.setheading(270)  # Línea vertical
t.forward(150)

# Dibujar la curva de la "D" (aproximación con un círculo)
t.penup()
t.goto(40, 300)  # Volver al inicio de la línea vertical superior
t.pendown()
t.setheading(0)    # Apuntar hacia la derecha para iniciar el semicírculo
t.circle(-75, 180) # Dibuja un semicírculo


# --- Dibujo de la letra "O" ---
# La "D" terminó aproximadamente en X = 50 - 75 = -25
# Vamos a empezar la "O" un poco más a la derecha, por ejemplo en X = 60
t.penup()
t.goto(210, 300)  # Misma altura inicial
t.pendown()
t.circle(75)      # Dibuja un círculo completo

# Mantener la ventana abierta
turtle.done()




