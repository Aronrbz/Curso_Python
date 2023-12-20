# Ejemplo de 'and'
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir.")
else:
    print("No puede conducir.")

# Ejemplo de 'or'
tiene_pasaporte = False
tiene_cedula = True

if tiene_pasaporte or tiene_cedula:
    print("Puede viajar.")
else:
    print("No puede viajar.")

# Ejemplo de 'not'
es_dia_laboral = False

if not es_dia_laboral:
    print("Es fin de semana.")
else:
    print("Es un día laboral.")
    
########################################################################

#Fácil: Supón que una tienda tiene una promoción: si un cliente compra más de 5 artículos o el total de 
#       su compra es mayor a 100 dólares, obtiene un descuento. Escribe una condición que use or para 
#       determinar si se aplica el descuento.

totalProductos = int(input("Ingrese la cantidad de productos comprados: "))
totalMonto = int(input("Ingrese el monto total: "))

if totalProductos > 5 or totalMonto > 100:
    print("Obtuviste un descuento")
else:
    print("No obtuviste un descuento")

#Medio: Imagina que para ingresar a un evento, se debe tener más de 18 años y una entrada válida. 
#       Usa and para escribir una condición que verifique estos requisitos.

edad = int(input("Ingrese su edad: "))
entrada = input("¿Tienes una entrada valida?: ")

if edad > 18 and entrada.lower() == "si":
    print("Puede ingresar al evento.")
else:
    print("No puede ingresar al evento.")

#Difícil: Escribe una condición usando not para verificar si una persona no cumple con alguna de las 
#        siguientes condiciones: tener más de 16 años y menos de 60 años.

edad = int(input("Ingrese su edad: "))

if not (edad > 16 and edad < 60):
    print("Cumple con la condicion.")
else:
    print("No cumple con la condicion.")


#otra forma de desarrollo
    
edad = int(input("Ingrese su edad: "))

if not (16 < edad < 60):
    print("Cumple con la condición.")
else:
    print("No cumple con la condición.")

# En esta versión:

# (16 < edad < 60) verifica si la edad está entre 17 y 59 años (más de 16 y menos de 60).
# not (16 < edad < 60) entonces verifica lo contrario: si la edad no está entre 17 y 59 años. 
# En otras palabras, si la edad es 16 años o menos, o 60 años o más. Este enfoque utiliza la lógica de 
# verificar un rango con una sintaxis concisa, y luego invierte el resultado para encontrar lo que está fuera
# de ese rango.





########################################################################

#mas ejercicios de operador logico con operador ternario

## file para ejecutar pruebas para practicar.

calificacion = int(input("Ingrese su calificación enter 0 y 10: "))
# rango = None

# if calificacion >= 9 and calificacion <= 10:
#     rango = "A"
# elif calificacion >= 8 and calificacion < 9:
#     rango = "B"
# elif calificacion >= 7 and calificacion < 8:
#     rango = "C"
# elif calificacion >= 6 and calificacion < 7:
#     rango = "D"
# elif calificacion >= 0 and calificacion < 6:
#     rango = "F"
# else:
#     rango = "Valor incorrecto"

# print(f"Su rango es: {rango}")


if  9 <= calificacion <= 10:
    print("A")
elif 8 <= calificacion < 9:
    print("B")
elif 7 <= calificacion < 8:
    print("C")
elif 6 <= calificacion < 7:
    print("D")
elif 0 <= calificacion < 6:
    print("F")
else:
    print("Valor incorrecto")

#print(f"Su rango es: {rango}")