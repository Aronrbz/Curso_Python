import math #libreria de matematicas. Dependencias

print(round(1.3))
print(round(1.7))
print(round(1.5))
print(abs(-69)) #valor absoluto del numero que nosotros le pasemos, independiente si es positivo o negativo
print(abs(35)) #valor absoluto del numero que nosotros le pasemos, independiente si es positivo o negativo

print(math.ceil(2.1)) #devuelve el numero entero hacia arriba (3)
print(math.floor(4.989898989)) #devuelve el numero entero hacia abajo (4)
print(math.isnan(34)) # veririca que el numero no sea nulo, o no sea un numero. "Is Not A Number" (en este caso es false, porque 23 si es un numero)
## print(math.isnan("A")) error de sintaxys
print(math.pow(3, 4)) #calcula la potencia. Tomadel primero valor, y lo potencia por el segundo valor
print(math.sqrt(16)) #calcula la raiz cuadrada del valor asignado


#ejercicio 1
print(math.factorial(5)) #calcula el factorial de un numero entero

#ejercicio 2
print(math.log(10, 2))  # Logaritmo en base 2 de 10
print(math.log(10))     # Logaritmo natural de 10

#ejercicio 3
print(math.exp(3))