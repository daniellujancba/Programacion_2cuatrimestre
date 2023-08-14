#Ejercicios Tuplas:
#Crear tres tuplas con datos random.
tupla_1 = ("Roberto","Roca 358","La Calera","Cordoba",75,7368943)
tupla_2 = ("Alberto","Gral Paz 2136","La Carlota","Cordoba",81,4596123)
tupla_3 = ("Susana","Tarija 427","Carlos Paz","Cordoba",67,10887546)

#Crear una lista que las contenga y mostrarla.
listaDeTuplas = []

# camino 1: insertar todas las tuplas a la lista

i = "si"
while i== "si":
    i = str(input("desea ingresar todas la tuplas a una lista?: "))
    if i == "si":
        listaDeTuplas.append(tupla_1)
        listaDeTuplas.append(tupla_2)
        listaDeTuplas.append(tupla_3)
    else:
        break

print(listaDeTuplas)


# camino 2: elegir las tuplas a insertar
i = "si"
while i == "si":
    i = str(input("desea ingresar a la lista una tupla?: "))
    if i == "si":
        nombre = str(input("Ingrese el nombre de la tupla: "))
        if nombre == "tupla_1":
            listaDeTuplas.append(tupla_1)
        elif nombre == "tupla_2":
            listaDeTuplas.append(tupla_2)
        elif nombre == "tupla_3":
            listaDeTuplas.append(tupla_3)
        else:
            print("ingrese un nombre valido")

    else:
        break


print(listaDeTuplas)

