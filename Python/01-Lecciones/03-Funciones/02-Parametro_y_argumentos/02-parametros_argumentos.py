# # Ejercicios
# # Fácil: Escribe una función describir_persona que tome un nombre y una edad (como parámetros posicionales) 
# #     y los imprima.

# def describir_persona(nombre, edad):
#     print(f"Nombre: {nombre}, Edad: {edad}")

# describir_persona("Alice", 30)

# # Medio: Crea una función crear_perfil que tome un nombre y luego un número variable de argumentos (*args) 
# #     representando los intereses de la persona. La función debe imprimir el nombre y los intereses.

# def crear_perfil(nombre, *intereses):
#     print(f"Nombre: {nombre}")
#     print("Intereses:")
#     for interes in intereses:
#         print(f"- {interes}")

# crear_perfil("Alice", "Leer", "Programar", "Caminar")



# # Difícil: Desarrolla una función configurar_perfil que tome un nombre y luego varios argumentos con palabras  
# #     clave (**kwargs) para detalles adicionales como 'ocupación', 'ciudad', etc. La función debe imprimir todos  
# #     los detalles del perfil.


# def configurar_perfil(nombre, **detalles):
#     print(f"Perfil de {nombre}:")
#     for clave, valor in detalles.items():
#         print(f"{clave.capitalize()}: {valor}")

# configurar_perfil("Bob", ocupacion="Desarrollador", ciudad="Ciudad Gótica", edad=35)

