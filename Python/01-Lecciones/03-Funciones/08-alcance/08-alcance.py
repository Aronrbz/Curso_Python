#Ejercicios de Práctica

#Fácil: Crea una función mostrar_nombre que defina una variable nombre dentro de la función e imprima su valor. Luego, intenta imprimir nombre fuera 
#de la función y observa qué sucede.

# def mostrar_nombre():
#     nombre = "Aaron"
#     print(nombre)

# mostrar_nombre()
# print(nombre)
#ocurre un error porque nombre esta dentro de una funcion y no es variable local, por ende esta fuera del alcance. 


#Medio: Escribe una función contar_llamadas que incremente una variable llamadas cada vez que la función es llamada. Usa una variable global 
#para mantener el conteo.

# llamadas = 0

# def contar_llamadas():
#     global llamadas
#     llamadas += 1
#     print(llamadas)

# contar_llamadas()
# contar_llamadas()
# contar_llamadas()


#Difícil: Define una variable mensaje_global fuera de una función. Dentro de la función, modifica el valor de la variable sin usar global, 
#y luego imprime su valor dentro y fuera de la función. ¿El valor se modificó realmente?

# mensaje_global = "saludo global"

# def modificar_variable():
#     mensaje_global = "saludo funcion"


# print(mensaje_global)
# modificar_variable()
# print(mensaje_global)

# respuesta: el valor no se modifico
