#Ejercicio Diccionarios:
#Crear el siguiente diccionario:
#las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.

nucleoFamiliar = {23445896:"carlos",45896771:"analia",52864999:"carlota",11258741:"julian"}


#Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)

i = "si"

while i == "si":
    i = str(input("desea ingresar un valor al diccionario: "))
    if i == "si":
        a = int(input("Ingrese el DNI como clave: "))
        b = str(input("ingrese el Nombre como valor: "))

        nucleoFamiliar.update({a:b})
    else:
        break

print(nucleoFamiliar)

#Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.
import random
letras_1 = ["a","b","c","d","e","f","g","h"]
letras_2 = ["i","j","k","l","m","n","o","p"]
letras_3 = ["q","r","s","t","u","v","w","x"]
letras_4 = ["y","z","A","B","C","D","E","F"]
i = "si"
diccionarioTelefonos = {}


while i == "si":
    i = str(input("desea generar una clave para su numero de telefono: "))
    if i == "si":
        telefono = int(input("Ingrese su numero de telefono: "))
        a = str(random.randrange(0,10))
        b = str(random.randrange(0,10))
        c = str(random.randrange(0,10))
        d = str(random.randrange(0,10))
        e = str(random.choice(letras_1))
        f = str(random.choice(letras_2))
        g = str(random.choice(letras_3))
        h = str(random.choice(letras_4))
        clave = a+b+c+d+e+f+g+h
        diccionarioTelefonos.update({clave:telefono})
    else:
        break

print("La clave generada para su telefono es: ")
print(diccionarioTelefonos)



