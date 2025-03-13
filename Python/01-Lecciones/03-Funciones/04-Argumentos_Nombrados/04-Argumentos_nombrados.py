# Ejercicios
# Fácil   : Define una función mostrar_informacion que tome tres parámetros: nombre, profesion y empresa. Luego, llama a 
#     esta función usando argumentos nombrados, especificando solo nombre y empresa.

def mostrar_informacion(nombre, empresa, profesion="Analista"):
    print(f"Nombre\t\t: {nombre}\nProfesion\t: {profesion}\nEmpresa\t\t: {empresa}")

mostrar_informacion(empresa="Talent", nombre="Aron Bustos")


# Medio   : Escribe una función configurar_alarma que acepte tres parámetros: hora, minutos y sonido, donde sonido tiene 
#     un valor predeterminado. Llama a la función especificando minutos y sonido, omitiendo hora.}

def configurar_alarma(hora=0, minuto=0, sonido="nokia ladrillo"):
    print(f"hora: {hora} Minuto: {minuto} Sonido: {sonido}")

configurar_alarma(sonido="El baile del perro", minuto=40)

# Difícil : Crea una función preparar_bebida que tenga tres parámetros: tipo, azucar y leche, donde azucar y leche son 
#     argumentos opcionales con valores predeterminados. Llama a esta función pasando tipo como argumento posicional y 
#     modificando el valor predeterminado de leche mediante un argumento nombrado.

def preparar_bebidas(tipo, azucar="un kilo", leche="Colun"):
    print(f"tipo: {tipo}, azucar: {azucar}, leche: {leche}")

preparar_bebidas("coca cola", leche="Surlat", azucar="medio kilo")