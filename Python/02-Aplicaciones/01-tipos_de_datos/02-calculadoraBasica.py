# Importamos la librería math para funciones matemáticas adicionales
import math

# Solicitamos al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Realizamos las operaciones básicas
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2  # Asumimos que el usuario no va a ingresar un cero aquí para simplificar

# Utilizamos algunas funciones de la librería math
potencia = math.pow(num1, num2)  # num1 elevado a num2
raiz_cuadrada_num1 = math.sqrt(num1)  # Raíz cuadrada de num1
raiz_cuadrada_num2 = math.sqrt(num2)  # Raíz cuadrada de num2

# Mostramos los resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {mult}")
print(f"La división de {num1} y {num2} es: {div}")
print(f"La potencia de {num1} elevado a {num2} es: {potencia}")
print(f"La raíz cuadrada de {num1} es: {raiz_cuadrada_num1}")
print(f"La raíz cuadrada de {num2} es: {raiz_cuadrada_num2}")
