#Ejercicios para Practicar return

#Fácil: Crea una función doblar_numero que tome un número como parámetro y devuelva el doble de ese número.


#def doblar_numero():
#    resultado = int(input("Ingrese un numero: "))
#    return resultado * 2

#resultado = doblar_numero()
#print(f"El doble del numero es {resultado}")  


#def doblar_numero():
#    numero = int(input("Ingrese un numero: "))
#    return numero, numero * 2  # Retorna ambos valores

#numero_original, resultado_doble = doblar_numero()
#print(f"El doble del número {numero_original} es {resultado_doble}")



#Medio: Escribe una función calcular_area_circulo que reciba el radio de un círculo como parámetro y devuelva el área del círculo. (Usa pi = 3.1416).

#def calcular_area_circulo(radio):  # Nombre corregido
#    area = 3.1416 * radio ** 2
#    return area

#radio_ingresado = float(input("Ingrese el radio del círculo: "))  # Pedimos el radio al usuario
#resultado_area = calcular_area_circulo(radio_ingresado)  # Ahora pasamos el radio como argumento
#print(f"El área del círculo es {resultado_area}")


# Difícil: Define una función obtener_mayor que tome tres números como parámetros y devuelva el mayor de los tres

def obtener_mayor(numero1, numero2, numero3):
    if numero1 >= numero2 and numero1 >= numero3:
        return numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        return numero2
    else:
        return numero3

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
mayor = obtener_mayor(numero1, numero2, numero3)
print(f"El mayor número es {mayor}")