# x = input("")

    #int()
    #str()
    #float()
    #bool() ---- Truthy - True - cualquier parametro que le pasemos lo evalua como true
    #            Falsy  - False - a exceptuando : un string vacio -"", -0 ,none
    # solo con esos 3 excepciones bool evalua false

print(bool(""))
print(bool("0"))
print(bool(None))
print(bool(" "))
print(bool(0))


#ejercicio 1
numero = int("123")
print(numero + 77)

#ejercicio 2
pi = 3.14159
print("El valor de pi es aproximadamente " + str(pi))

#ejercicio 3
valorVacio = ""
print(not bool(valorVacio))