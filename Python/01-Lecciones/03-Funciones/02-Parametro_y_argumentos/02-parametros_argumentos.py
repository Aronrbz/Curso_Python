# Ejercicios:

# Fácil: Escribe una función sumar que tome dos parámetros, num1 y num2, y que imprima la suma de estos números.


#opcion 1
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

def sumar(num1, num2):
    print(num1 + num2)

sumar(num1, num2)

#opcion 2
def sumar(num1, num2):
    print(num1 + num2)

sumar(8, 3)


# Medio: Crea una función saludar_persona que tome un parámetro nombre y otro hora_del_dia 
#     (por ejemplo, "mañana", "tarde", "noche") y que imprima un saludo apropiado, como "Buenos días, Juan".

def saludar_persona(nombre, hora_del_dia):
    if hora_del_dia == "mañana":
        print("Buenos días", nombre)
    elif hora_del_dia == "tarde":
        print("Buenas tardes", nombre)
    else:
        print("Buenas Noches", nombre)

# ## Aca, podemos ir cambiando los argumentos, y estos contestaran a la hora del dia que escribamos
saludar_persona("Carlos", "noche")

# Difícil: Haz una función imprimir_informacion que tome tres parámetros: nombre, edad y ciudad, y que imprima 
#     una oración con esta información, como "Soy Ana, tengo 25 años y vengo de Madrid".

def imprimir_informacion(nombre, edad, ciudad):
    print(f"Soy {nombre}, tengo {edad} años y vengo de {ciudad}.")

imprimir_informacion("Ana", 25, "Madrid")