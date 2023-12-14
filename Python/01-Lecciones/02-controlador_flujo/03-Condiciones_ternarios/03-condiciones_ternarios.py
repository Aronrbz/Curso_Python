#edad = 19

#edad = int(input("Ingrese su edad: "))

#mensajes = "Es mayor de edad" if edad > 17  else "Es menor de edad"

# if edad > 17:
#     mensajes = "Es mayor de edad"
# else:
#     mensajes = "Es menor de edad"

#print(mensajes)

#Ejercicio 1

temperatura = int(input("Ingresa la temperatura: ")) 
estado_agua = "Gas" if temperatura > 100 else "liquido"
print(estado_agua)


#Ejercicio 2

miNumero = int(input("Ingresa un numero: "))
parImpar = "es par" if miNumero % 2 == 0 else "es impar"
print(parImpar)

#Ejercicio 3

es_estudiante = input("¿Eres estudiante (si/no)? ")
precio_entrada = 5 if es_estudiante.lower() == 'si' else 10
print(f"El precio de la entrada es: {precio_entrada} dólares")
