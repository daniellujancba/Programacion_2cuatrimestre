"""Ejercicios Estructuras Condicionales:
Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea correspondiente:"""

# 1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo
numero = int(input("Ingrese un Numero:"))
if numero == 10:
    print("Usted a ganado!!!")
else:
    print("Siga Participando")

# 2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco, seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

numero = int(input("Ingrese un Numero:"))
if numero < 10:
    print("Falto un Poco Seguí Participando")
elif numero > 10:
    print("¡Te pasaste, a seguir intentando!")
else:
    print("Usted a Ganado!!!")

# 3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia = str(input("Ingrese un dia de la semana: "))

if dia == "lunes":
    print("Tenga un buen comienzo de semana!!!")
elif dia == "viernes":
    print("Es viernes y el cuerpo lo sabe!!!")
elif dia == "sabado":
    print("Comienza el descanso del fin de semana!!!")
elif dia == "domingo":
    print("Lindo dia para un asadito familiar!!!")
else:
    print("Aun falta para los dias lindos")

# 4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.

vocal = str(input("Ingrese una letra: "))

if vocal == "a":
    print("Es Una Vocal")
elif vocal == "e":
    print("Es Una Vocal")
elif vocal == "i":
    print("Es Una Vocal")
elif vocal == "o":
    print("Es Una Vocal")
elif vocal == "u":
    print("Es Una Vocal")
else:
    print("Esta letra no es una Vocal")