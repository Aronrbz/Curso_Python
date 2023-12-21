# for numero in range(5):
#     print(numero, numero * 'hola mundo ')


# buscar = 3
# for numero in range(5):
#     print(numero)
#     if numero == buscar:
#         print("encontrado", buscar)
#         break #detiene el bucle para que no se ejecute la siguiente instrucción o iteracion.

# buscar = 10
# for numero in range(5):
#     #print(numero) #al desmarcar este print, mostrara el listado de 0 a 4 y al final mostrara el else.
#     if numero == buscar:
#         print("encontrado", buscar)
#         break 
# else:
#     print("no encontrado")

# for char in "ultimate python":
#     print(char)
# itera un string

########################################################################

# Ejercicios para ti:

# Fácil: Crea una lista de tres colores. Usa un bucle for para imprimir cada color de la lista.

# colores = "rojo", "azul", "amarillo"

# for color in colores:
#     print(color)

# # Medio: Usa un bucle for con range() para imprimir todos los números del 1 al 10.

# for numero in range(1, 11):
#     print(numero)

# # Difícil: Dada una lista de números, usa un bucle for para sumar todos los números de la lista. 
# #   Imprime el total al final.

# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total = 0

# for numero in lista_numeros:
#     total += numero
# print (total)

##############################################

# for i in range(1, 11):  # Bucle externo para las tablas del 1 al 10
#     print(i)
#     for j in range(1, 11):  # Bucle interno para cada multiplicación
#         resultado = i * j
#         print(i, "x", j, "=",resultado)


