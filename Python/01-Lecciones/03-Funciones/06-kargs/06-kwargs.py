# Fácil: Define una función imprimir_detalles que use **kwargs para aceptar detalles de un libro como título, 
#     autor y año, e imprima estos detalles en un formato amigable.

# def imprimir_detalles(**kwargs):
#         print(kwargs)

# imprimir_detalles(Titulo="Papelucho", Autor="Marcela Paz", Año="1947")



# Medio: Crea una función calcular_precio que utilice **kwargs para aceptar el precio base de un producto, y opcionalmente, 
#     un descuento en porcentaje. La función debe calcular y mostrar el precio final después del descuento.


#def calcular_precio(**precios):
    # Convertir los argumentos nombrados a enteros
#    precio_base = int(precios["PrecioBase"])
#    descuento = int(precios["DescuentoOpcional"])

#    print("¿Dispone de un descuento?")
#    respuesta = input("Responda con 's' para Sí o 'n' para No: ").lower()

    # Validación de la entrada del usuario
#    while respuesta != 's' and respuesta != 'n':
#        print("Opción no válida. Por favor, ingrese 's' o 'n'.")
#        respuesta = input("Responda con 's' para Sí o 'n' para No: ").lower()

#    if respuesta == 's':  # Aplica el descuento
#        precio_final = int(precio_base - (precio_base * descuento / 100))
#        print(f"El precio con descuento es: ${precio_final}")
#    else:  # No aplica el descuento
#        print(f"No se ha aplicado un descuento. El precio final es: ${precio_base}")

# Llamada a la función
#calcular_precio(PrecioBase="2990", DescuentoOpcional="19")


# Difícil: Escribe una función crear_perfil_usuario que acepte un nombre obligatorio y luego cualquier número de detalles 
#     adicionales sobre el usuario (como email, ciudad, edad) usando **kwargs. La función debe imprimir el perfil completo 
#     del usuario.

#def crear_perfil_usuario(nombre, **kwargs):
#    print(f"Perfil del usuario: {nombre}")

#    for clave in kwargs:
#        print(f"{clave.capitalize()}: {kwargs[clave]}")

# Llamada a la función con argumentos adicionales
#crear_perfil_usuario("Aron Bustos", email="aron.bustos@example.com", ciudad="Santiago", edad="36")
