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