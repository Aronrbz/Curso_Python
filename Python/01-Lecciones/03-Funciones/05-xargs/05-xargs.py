# Ejercicios

# Fácil: Escribe una función mostrar_mensajes que use *args para aceptar varios mensajes como argumentos y los imprima 
# uno tras otro.

# def mostrar_mensajes(*mensajes):
#     for mensaje in mensajes:
#         print(mensaje)

# mostrar_mensajes('Hola', 'este es', 'el curso de python', 'para principiantes')

# Medio: Define una función multiplicar_numeros que utilice *args para recibir varios números y calcule el producto de 
# todos ellos. Imprime el resultado.

# def multiplicar_numeros(*numeros):
#     producto = 1 #al ser multiplicacion, producto no puede valer 0, de lo contrario el resultado siempre sera 0
#     for numero in numeros:
#         producto *= numero
#     print(producto)

# multiplicar_numeros(2,5,6)

# Difícil: Crea una función min_max que utilice *args para tomar varios números y luego imprima el menor y el mayor de 
# esos números.

# def min_max(*numeros):
#    vmin = vmax = numeros[0] # Asignamos el primer valor de numeros directamente, asumiendo que *numeros no está vacío.
#     for numero in numeros:
#         if numero < vmin:
#             vmin = numero
#         if numero > vmax:
#             vmax = numero
#     print(f"Min: {vmin}, Max: {vmax}")

# min_max(5, 8, 7)