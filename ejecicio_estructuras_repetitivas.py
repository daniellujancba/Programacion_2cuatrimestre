"""Ejercicios Estructuras Repetitivas:
Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea correspondiente:"""

# 1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar hasta que se ingrese -1.
suma = 0
a = True
while a == True:
    numero = int(input("Ingrese un numero: "))
    if numero != -1:
        suma = suma + numero
        a = True
    else:
        break
print("La suma es: ",suma)

# 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
mayores = 0
menores = 0
iguales = 0

a = int(input("Ingrese la cantidad de numeros a evaluar: "))
b = 0
c = True
d = 0

while c == True:
    if not a == b:
        numero = int(input("Ingrese un numero: "))
        b = b + 1
        if numero > 0:
            mayores = mayores + 1
            c == True
        elif numero < 0:
            menores = menores + 1
            c == True
        else:
            d = d + 1
            c == True
    else:
        break

print("La cantidad de numeros mayores a cero es: ",mayores)
print("La cantidad de numeros menores a cero es: ",menores)
print("La cantidad de numeros iguales a cero es: ",d)


# 3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un cero.

c = 1
while c!= 0:
    letra = str(input("Ingrese una letra:"))
    if letra == "a":
        print("es una vocal")
        consulta = str(input("Desea ingresar otra letra: "))
        if consulta == "si":
            c = 1
        else:
            c = 0
    elif letra == "e":
        print("es una vocal")
        consulta = str(input("Desea ingresar otra letra: "))
        if consulta == "si":
            c = 1
        else:
            c = 0
    elif letra == "i":
        print("es una vocal")
        consulta = str(input("Desea ingresar otra letra: "))
        if consulta == "si":
            c = 1
        else:
            c = 0
    elif letra == "o":
        print("es una vocal")
        consulta = str(input("Desea ingresar otra letra: "))
        if consulta == "si":
            c = 1
        else:
            c = 0
    elif letra == "u":
        print("es una vocal")
        consulta = str(input("Desea ingresar otra letra: "))
        if consulta == "si":
            c = 1
        else:
            c = 0
    else:
        print("no es una vocal")
        consulta = str(input("Desea ingresar otra letra: "))
        if consulta == "si":
            c = 1
        else:
            c = 0

# 4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos.
c = 1
suma = 0
a = 0

while c!=0:
    a = a + 1
    numero = int(input("ingrese un numero por favor: "))
    if numero != 0:
        suma = suma + numero
        media = suma / a
        c = 1
    else:
        c = 0

print("la suma de los numeros es: ",suma)
print("la media de los numeros es: ",media)