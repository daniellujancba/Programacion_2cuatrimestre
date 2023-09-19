
# Generar una clase de Medios de Contacto que contenga:
# Id_MedioContacto
# Fecha
# Email
# Telefono
# Direccion
# Nombre

class Medios_de_contacto():

    Id_MedioContacto = 0,
    Fecha = "",
    Email = "",
    Telefono = "",
    Direccion = "",
    Nombre = ""

    def __init__(self,id_MedioContacto,fecha,email,telefono,direccion,nombre):

        self.Id_MedioContacto = id_MedioContacto
        self.Fecha = fecha
        self.Email = email
        self.Telefono = telefono
        self.Direccion = direccion
        self.Nombre = nombre

    def getid_MedioContacto(self): 
        return self.Id_MedioContacto  
    def getfecha(self): 
        return self.Fecha
    def getemail(self):
        self.Email = email
    def gettelefono(self): 
        return self.Telefono
    def getdireccion(self):
        return self.Direccion
    def getnombre(self): 
        return self.Nombre

    def setid_MedioContacto(self,id_MedioContacto): 
        self.Id_MedioContacto = id_MedioContacto  
    def setfecha(self,fecha): 
        self.Fecha = fecha
    def setemail(self,email):
        self.Email = email
    def settelefono(self,telefono): 
        self.Telefono = telefono
    def setdireccion(self,direccion):
        self.Direccion = direccion
    def setnombre(self,nombre): 
        self.Nombre = nombre


    def imprimir_Medios_de_Contacto(self):

        print(f"ID_curso: {self.getid_MedioContacto()}")
        print(f"Fecha_Inicio: {self.getfecha()}")
        print(f"Titulo: {self.getemail()}")
        print(f"Descripcion: {self.gettelefono()}")
        print(f"Objetivos: {self.getdireccion()}")
        print(f"Docente: {self.getnombre()}")
