# programa muy basico que permite realizar operaciones matematicas entre dos numeros

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

# Transformamos el digito numerico, a valor de numero. Si no anteponemos la sigla "int" antes de input, el numero
# ingresado se tomara como texto y no como un numero, por ende, el programa va a concatenar (juntar) los numeros en lugar de sumarlos.
# por ejemplo: 10 + 20 = 1020 /// pero si anteponemos la sigra int antes de input, el resultado cambiria: 10 + 20 = 30


suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2

mensaje = f"""Para los numeros {num1} y {num2},
el resultado de la suma es: {suma},
el resultado de la resta es: {resta},
el resultado de la multiplicacion es: {mult},
el resultado de la division es: {div}"""

print(mensaje)
