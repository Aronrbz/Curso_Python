# Primera Evaluacion de Programación en Python

# Preguntas Teóricas
# Tipos de Datos y Variables: ¿Cuál es la diferencia entre los tipos de datos int y float en Python?

# R: Los datos INT son numeros enteros, mientras que los Floats son numeros con decimales.

# Operadores: ¿Qué hace el operador ** en Python?

# R: El operador ** es una potencia.

# Strings: Explica brevemente cómo funcionan las secuencias de escape en las cadenas de texto de Python.

# R: Las secuencias de escape son caracteres especiales que se pueden usar en las cadenas de texto de Python
#   para dar formato, saltos de linea, convertir a comentarios, y que facilitan la lectura del codigo o la salda.

# Funciones Matemáticas: Nombra al menos dos funciones de la librería math y describe brevemente para qué se utilizan.

# R: mat.pow(x, y)  : Devuelve x elevado a la potencia y.
#    math.sqrt(x)    : Devuelve la raíz cuadrada de x. 

# Condiciones y Operadores Lógicos: Explica la diferencia entre los operadores == y !=.

# R: El operador == es igual a. mientras que el operador!= es diferente a o distinto de.

# Problemas Prácticos
# Calculadora Básica:
# Escribe un programa que pida al usuario dos números y muestre la suma, resta, multiplicación, y división de esos 
# números.

# R: 
# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("ingrese el segundo número: "))

# suma = num1 + num2
# resta = num1 - num2
# mult = num1 * num2
# div = num1 / num2

# print(f"La suma de {num1} y {num2} es: {suma}")
# print(f"La resta de {num1} y {num2} es: {resta}")
# print(f"La multiplicación de {num1} y {num2} es: {mult}")
# print(f"La división de {num1} y {num2} es: {div}")


# Trabajando con Strings:
# Dada la frase "Hola, mundo", escribe un fragmento de código que imprima la longitud de esta frase y luego la misma 
# frase en mayúsculas.

# Frase = "Hola, mundo"

# print(len(Frase))
# print(Frase.upper())


# Uso de for y range:
# Utiliza un bucle for y la función range para imprimir los números pares del 1 al 10.

# for i in range(11):
#     if i % 2 == 0:
#         print(i)


# Condiciones Anidadas:
# Escribe un programa que solicite la edad del usuario. Si el usuario tiene más de 18 años, imprime "Adulto". Si tiene 
# entre 13 y 18 años, imprime "Adolescente". Si tiene menos de 13, imprime "Niño".

# persona = int(input("Ingrese su edad: "))

# if persona > 18:
#     print("Adulto")
# elif persona < 18 or persona >= 13:
#     print("Adolescente")
# else:
#     print("Niño")

# Loops Anidados:
# Escribe un programa que utilice bucles anidados para imprimir un patrón de asteriscos que forme un cuadrado de 3x3.

# Bucle externo para las filas
# for fila in range(3):
#     # Inicializar una string vacía para la fila actual
#     fila_str = ""
#     # Bucle interno para las columnas
#     for columna in range(3):
#         fila_str += "* "  # Concatenar un asterisco y un espacio
#     # Imprimir la fila completa
#     print(fila_str)