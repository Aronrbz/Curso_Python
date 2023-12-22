# Ejercicios para ti:

# Fácil: Escribe un bucle while que comience con x = 0 e imprima x mientras x sea menor a 5.

# x = 0
# while x < 5:
#     print(x)
#     x += 1



# Medio: Utiliza un bucle while para crear un pequeño programa que pida al usuario que ingrese números hasta que 
#         escriba "stop". Imprime cada número ingresado.


# numeros = ""
# while numeros.lower() != "stop":
#     numeros = input("Ingresa cualquier número. Escribe 'stop' para salir: ")
#     print(numeros)

# Difícil: Haz un bucle while que sume números del 1 al 10 (inclusive). Utiliza una variable para llevar la cuenta 
#         # de la suma y otra para llevar la cuenta del número actual. Imprime la suma total después de salir del 
#           bucle.


numero = 0
while numero <= 10 :
    print(numero)
    numero += 1
    suma = numero + numero
    print ("suma parcial", numero)
print ("suma final", suma)