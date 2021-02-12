#Problema 1

clave = "contraseña"
password = input("Introducir contraseña:")
if clave == password.lower():
    print("La contraseña ingresada coincide con la guardada")
else:
    print("La contraseña no coincide con la guardada")

#Problema 2

nombre = input("¿Cuál es tu nombre? ")
genero = input("¿Cuál es tu género (M o H)? ")

if (genero == "M" and nombre.lower() < 'm') or (genero == "H" and nombre.lower() > 'n'):
    grupo = "A"
else:
    grupo = "B"
print("Tu grupo es:" + grupo)