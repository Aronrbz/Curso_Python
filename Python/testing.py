#Fácil: Supón que una tienda tiene una promoción: si un cliente compra más de 5 artículos o el total de 
#       su compra es mayor a 100 dólares, obtiene un descuento. Escribe una condición que use or para 
#       determinar si se aplica el descuento.

# totalProductos = int(input("Ingrese la cantidad de productos comprados: "))
# totalMonto = int(input("Ingrese el monto total: "))

# if totalProductos > 5 or totalMonto > 100:
#     print("Obtuviste un descuento")
# else:
#     print("No obtuviste un descuento")

#Medio: Imagina que para ingresar a un evento, se debe tener más de 18 años y una entrada válida. 
#       Usa and para escribir una condición que verifique estos requisitos.

# edad = int(input("Ingrese su edad: "))
# entrada = input("¿Tienes una entrada valida?: ")

# if edad > 18 and entrada.lower() == "si":
#     print("Puede ingresar al evento.")
# else:
#     print("No puede ingresar al evento.")

#Difícil: Escribe una condición usando not para verificar si una persona no cumple con alguna de las 
#        siguientes condiciones: tener más de 16 años y menos de 60 años.

# edad = int(input("Ingrese su edad: "))

# if not (edad > 16 and edad < 60):
#     print("Cumple con la condicion.")
# else:
#     print("No cumple con la condicion.")


#otra forma de desarrollo
    
# edad = int(input("Ingrese su edad: "))

# if not (16 < edad < 60):
#     print("Cumple con la condición.")
# else:
#     print("No cumple con la condición.")

