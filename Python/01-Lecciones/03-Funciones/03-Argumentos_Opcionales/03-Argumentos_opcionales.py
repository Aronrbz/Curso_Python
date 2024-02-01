# Ejercicios
# Fácil: Define una función crear_correo que tome un argumento opcional dominio con el valor predeterminado 
#       "ejemplo.com" y un argumento requerido nombre_usuario, y que imprima el correo electrónico completo.

def crear_correo(nombre_usuario, dominio="ejemplo.com"):
    if dominio != "ejemplo.com":
        print(f"{nombre_usuario}@{dominio}.com")
    else:
        print(f"{nombre_usuario}@{dominio}")

crear_correo("jdoe", "gmail")


# Medio: Crea una función imprimir_detalle_pedido que tome un argumento requerido producto y dos argumentos opcionales: 
#     cantidad con valor predeterminado 1 y precio con valor predeterminado 10. La función debe imprimir un resumen del 
#     pedido.

def detalle_pedido (producto, cantidad=1, precio=10):
    print(f"Su Resumen de pedido: \nProducto\t:{producto}\nCantidad\t:{cantidad}\nPrecio\t\t:{precio}")

detalle_pedido("Tomates", 2, 2500)



# Difícil: Escribe una función generar_despedida que tome un argumento requerido nombre y un argumento opcional formal 
#     con valor predeterminado False. Si formal es True, la función debe imprimir: 
#     "Le deseamos un buen día, Sr./Sra. [nombre]". Si es False, simplemente debe decir "Adiós, [nombre]".

def generar_despedida(nombre, formal=False):
    if formal == True:
        print(f"Le deseamos un buen día, Sr./Sra. {nombre}")
    else:
        print(f"Adiós, {nombre}")

generar_despedida("Juan", False)