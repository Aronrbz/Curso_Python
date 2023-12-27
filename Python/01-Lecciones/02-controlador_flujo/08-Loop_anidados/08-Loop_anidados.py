#for dentro de un for
# for i in range(3):  # Bucle externo
#     for j in range(3):  # Bucle interno
#         print(f"({i}, {j})")


#Combinación de while / for:
# i = 0
# while i < 3:  # Bucle externo
#     for j in range(3):  # Bucle interno
#         print(f"({i}, {j})")
#     i += 1

#Este código hace algo similar al anterior, pero usando un bucle while como externo.

#Combinación de while / while:  
# i = 0
# while i < 3:
#     j = 0
#     while j < 3:
#         print(f"({i}, {j})")
#         j += 1
#     i += 1

#Este código imprimirá pares de números, similar al ejemplo anterior, pero utilizando dos bucles while.
    
#Combinación de for / while:

# for i in range(3):
#     j = 0
#     while j < 3:
#         print(f"({i}, {j})")
#         j += 1

#Aquí, el bucle externo for itera sobre i, y dentro de este, un bucle while itera sobre j.


################## Ejercicios ###############################
# Fácil: Dada una lista de listas (por ejemplo, [[1, 2], [3, 4], [5, 6]]), usa bucles anidados para imprimir cada 
#     número individual.

# lista_de_listas = ((1, 2), (3, 4),  (5, 6))

# for i in lista_de_listas:
#     print(i)
#     for j in i:
#         print(j)

# Medio: Crea una tabla de multiplicar del 1 al 3 utilizando bucles anidados. Es decir, tu código debería imprimir 
#     el producto de cada par de números entre 1 y 3.

# i = 1
# while i <= 3:
#     j = 1
#     print(f"Tabla del {i}")
#     while j <= 10:
#         resultado = i * j
#         print(i, "x" ,j ,"=" , resultado)
#         j += 1
#     i += 1


# Difícil: Considera una lista de palabras. Usa un bucle anidado para imprimir cada letra de cada palabra en líneas 
#     separadas.

# lista_de_palabras = ("hola", "mundo", "python")

# for palabra in lista_de_palabras:
#     print("desgloce de la palabra", palabra)
#     for letra in palabra:
#         print(letra)