""" Crear cuatro listas:
1. Con los nombres de su familia.
2. Con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).
3. Con los nombres de ciudades que hayan visitado.
4. Con las fechas y nombres de eventos importantes de su vida."""

nombreFamilia = ["Roberto","Juanita","India","Raul","Amelio","Marta"]

tempDelMesJulioMin2023cba = [3,12,10,13,9,8,10,9,9,9,11,5,2,-3,-2,1,3,3,4,3,9,9,4,3,3,1,1,3,5,7]

ciudadesVisitadas = ["Salta","La Rioja","Capital Federal","Posadas","San Salvador","Carlos Paz"]

eventosImportantes = [["29/04/1972","día en que nací"],["29/04/1973","cumplí mi primer año"],["29/04/1990","cumplí 18 años"],["13/12/1997","vi a queensryche"]]

# 1. Ordenar alfabéticamente la lista de los nombres de familia.
nombreFamilia.sort()
print(nombreFamilia)

# 2. Ordenar ascendentemente la lista de temperaturas.
tempDelMesJulioMin2023cba.sort()
print(tempDelMesJulioMin2023cba)

# 3. Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.
tempDelMesAgostomin2023cba = [11,11,5,3,7,5,4,2,-1,8,4,4,4,10,3]
tempDelMesJulioMin2023cba.extend(tempDelMesAgostomin2023cba)
print(tempDelMesJulioMin2023cba)

# 4. Quitar de la lista de los nombres de familia, a tus abuelos.

i = "si"
while i == "si":
    i=str(input("desea borrar un nombre de la familia: "))
    if i == "si":
        abuelos = str(input("ingrese el nombre a borrar;"))
        nombreFamilia.remove(abuelos)
        i = "si"
    else:
        break
print("los familiares restantes son: ")
print(nombreFamilia)

# Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.

c = "si"
while c == "si":
    c=str(input("desea borrar una ciudad poco linda: "))
    if c == "si":
        ciudad = str(input("ingrese el nombre a borrar;"))
        ciudadesVisitadas.remove(ciudad)
        c = "si"
    else:
        break
print("las ciudades restantes son: ")
print(ciudadesVisitadas)

# 6. Mostrar todas las listas.

print(nombreFamilia)

print(tempDelMesJulioMin2023cba)

print(tempDelMesJulioMin2023cba)

print(nombreFamilia)

print(ciudadesVisitadas)





