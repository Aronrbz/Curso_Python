# Inicializamos la variable del resultado con un valor que no interfiera con la primera operación
ultimo_resultado = 0
primera_vez = True

while True:
    # Solicitar el primer número o el resultado para seguir operando
    if primera_vez:
        num1 = input("Ingresa el primer número o 'salir' para terminar: ")
        primera_vez = False
    else:
        num1 = input("Ingresa el siguiente número o 'salir' para terminar: ")

    # Verificar si el usuario quiere salir
    if num1.lower() == "salir":
        break

    num1 = float(num1)  # Convertir el número a flotante

    # Si es la primera vez, usamos el número ingresado, de lo contrario, usamos el último resultado
    if primera_vez:
        ultimo_resultado = num1

    # Solicitar la operación
    operacion = input("Ingresa la operación (suma, resta, multi, div) o 'salir': ").lower()

    # Verificar si el usuario quiere salir
    if operacion == "salir":
        break

    # Solicitar el segundo número
    num2 = float(input("Ingresa el segundo número: "))

    # Realizar la operación
    if operacion == "suma":
        ultimo_resultado += num2
    elif operacion == "resta":
        ultimo_resultado -= num2
    elif operacion == "multi":
        ultimo_resultado *= num2
    elif operacion == "div":
        ultimo_resultado /= num2
    else:
        print("Operación no válida")

    # Mostrar el resultado
    print("El resultado es:", ultimo_resultado)

# Fin del programa
print("Calculadora finalizada.")
