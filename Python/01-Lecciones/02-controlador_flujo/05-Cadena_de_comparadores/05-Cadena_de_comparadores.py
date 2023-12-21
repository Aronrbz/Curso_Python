# calificacion = int(input("Ingrese su calificación enter 0 y 10: "))

# if  9 <= calificacion <= 10:
#     print("A")
# elif 8 <= calificacion < 9:
#     print("B")
# elif 7 <= calificacion < 8:
#     print("C")
# elif 6 <= calificacion < 7:
#     print("D")
# elif 0 <= calificacion < 6:
#     print("F")
# else:
#     print("Valor incorrecto")


# Ejercicios para ti:

# Fácil: Verifica si una variable edad está entre 13 y 19 (adolescente).

# 1ra forma
# edad = int(input("Ingrese su edad: "))
# edad = "es adolecente" if 13 <= edad <= 19 else "no es adolecente"
# print(edad)

# 2da forma
# edad = int(input("Ingrese su edad: "))
# if edad >= 13 and edad <= 19:
#     print("Es adolecente") 
# else:
#     print("No es adolecente")


# Medio: Dada una variable temperatura, verifica si está por debajo del punto de congelación (0 grados Celsius)
#         o por encima del punto de ebullición del agua (100 grados Celsius).

# temperatura = int(input("Ingrese su temperatura: "))
# temperatura = "es por debajo del punto de congelación" if 0 >= temperatura < 100 else "por encima del punto de ebullición del agua"
# print(temperatura)  

# # 2da forma

# if 0 >= temperatura < 100:
#     print("Es por debajo del punto de congelación")
# else:
#     print("Por encima del punto de ebullición del agua")

# temperatura = int(input("Ingrese su temperatura: "))
# print("Fuera del rango de agua líquida" if temperatura < 0 or temperatura > 100 else "Dentro del rango de agua líquida")



# Difícil: Considera tres variables a, b y c. Comprueba si a es menor que b y si b es igual a c.

# a = int(input("Ingrese su primer número: "))
# b = int(input("Ingrese su segundo número: "))
# c = int(input("Ingrese su tercer número: "))

# if a < b and b == c:
#     print("a es menor que b y b es igual a c")
# elif b < a and b == c:
#     print("b es menor que a y b es igual a c")
# elif a < b and b != c:
#     print("a es menor que b y b no es igual a c")
# elif b < a and b!= c:
#     print("b es menor que a y b no es igual a c")
# else:
#     print("a es mayor que b y b no es igual a c")


# # 2da forma
# a = int(input("Ingrese su primer número: "))
# b = int(input("Ingrese su segundo número: "))
# c = int(input("Ingrese su tercer número: "))
# if a < b and b == c:
#     print("a es menor que b y b es igual a c")
# else:
#     print("La condición no se cumple")


# Estos ejercicios te ayudarán a entender cómo utilizar las cadenas de comparadores en diferentes situaciones.