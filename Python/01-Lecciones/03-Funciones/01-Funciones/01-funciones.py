# Ejercicios Prácticos:

# Fácil: Define una función llamada imprimir_mensaje que imprima el mensaje "Aprendiendo Python". 
#     Luego, llama a esta función.

def imprimir_mensaje():
    print("Aprendiendo Python")

imprimir_mensaje()

# Medio: Escribe una función llamada imprimir_cuadrados que imprima los cuadrados de los números 
#     del 1 al 5. Llama a la función para que se ejecute.

def imprimir_cuadrados():
    print("El cuadrado de 1 es: ", 1**2)
    print("El cuadrado de 2 es: ", 2**2)
    print("El cuadrado de 3 es: ", 3**2)
    print("El cuadrado de 4 es: ", 4**2)
    print("El cuadrado de 5 es: ", 5**2)

imprimir_cuadrados()

# Difícil: Crea una función imprimir_tabla que imprima la tabla de multiplicar del 2 (hasta 2x10). 
#     Luego, llama a esta función para que muestre la tabla.

def imprimir_tabla():
    for i in range(1,11):
        multi = 2*i
        print(f"2 x",i,"=", multi )

imprimir_tabla()