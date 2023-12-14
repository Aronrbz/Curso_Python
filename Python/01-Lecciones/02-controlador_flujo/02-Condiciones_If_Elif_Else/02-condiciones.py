edad = int(input("Ingrese su edad: "))

if edad > 65:
    print("Puedes entrar al cine con un super descuento")

elif edad > 55:
    print("Puedes entrar al cine con un descuento")

elif edad > 17:
    print("Puedes entrar al cine")

else:
    print("No puedes entrar a la discoteca")
    print("vaya a jugar")

print("Listo")

#Ejercicio 1
temp = int(input("Ingrese temperatura: "))

if temp > 25:
    print("Hace calor")
else:
    print("Hace frío")

#Ejercicio 2
puntos = int(input("su puntuacion fue: "))

if puntos >= 1001:
    print("¡Nuevo récord!")
elif puntos > 500 :
    print("Buena puntuación")
else:
    print("Sigue intentando")

#Ejercicio 3
numero_secreto = 9
numero_adivinado = int(input("adivine el numero secreto: "))

if numero_adivinado == numero_secreto:
    print("¡Adivinaste el numero secreto!")
else:
    print("Intenta de nuevo")