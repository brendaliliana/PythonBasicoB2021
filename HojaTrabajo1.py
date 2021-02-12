#Problema 1

altura = int(input("Introducir altura del triángulo:"))
for h in range(altura):
    print("*"*(h+1))

#Problema 2

numero = int(input("Ingrese un número entero:"))
def primo(numero):
    conteo=0
    resultado = True
    for n in range(1,numero + 1):
        if (numero%n==0):
            conteo+=1
        if(conteo>2):
            resultado = False 
            break 
    return resultado
if(primo (numero)==True):
    print("El número es primo ")
else :
    print("El número no es primo")