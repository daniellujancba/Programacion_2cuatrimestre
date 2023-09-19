# Que la clase Docente, sea herencia de la clase Usuario.

class Usuarios():
    Id_usuario  = 0
    Nombre_usuario ="",
    Apellido_usuario ="",
    Dni_usuario = 0,
    Direccion_usuario = "",
    Fecha_nac_usuario = "",
    Localidad_usuario = "",
    Codigo_postal_usuario = "",
    Provincia_usuario = "",
    Celular_usuario = 0,
    Email_usuario = "",
    Clave_acceso_usuario = "",
    Clave_acceso_usuario_conf = "",
    Estado_usuario = "",
    Rol_usuario = "",
    Validacion_email_usuario = ""
    
    

    def __init__(self,id_usuario,nombre_usuario,apellido_usuario,dni_usuario,direccion_usuario,fecha_nac_usuario,localidad_usuario,codigo_postal_usuario,provincia_usuario,celular_usuario,email_usuario,clave_acceso_usuario,clave_acceso_usuario_conf,estado_usuario,rol_usuario,validacion_email_usuario):

        self.Id_usuario = id_usuario
        self.Nombre_usuario = nombre_usuario
        self.Apellido_usuario = apellido_usuario
        self.Dni_usuario = dni_usuario
        self.Direccion_usuario = direccion_usuario
        self.Fecha_nac_usuario = fecha_nac_usuario
        self.Localidad_usuario = localidad_usuario
        self.Codigo_postal_usuario = codigo_postal_usuario
        self.Provincia_usuario = provincia_usuario
        self.Celular_usuario = celular_usuario
        self.Email_usuario = email_usuario
        self.Clave_acceso_usuario = clave_acceso_usuario
        self.Clave_acceso_usuario_conf = clave_acceso_usuario_conf
        self.Estado_usuario = estado_usuario
        self.Rol_usuario = rol_usuario
        self.Validacion_email_usuario = validacion_email_usuario
       
    def getid_usuario(self):
        return self.Id_usuario
    def getnombre_usuario(self):
        return self.Nombre_usuario
    def getapellido_usuario(self):
        return self.Apellido_usuario
    def getdni_usuario(self):
        return self.Dni_usuario
    def getdireccion_usuario(self):
        return self.Direccion_usuario
    def getfecha_nac_usuario(self): 
        return self.Fecha_nac_usuario
    def getlocalidad_usuario(self):
        return self.Localidad_usuario
    def getcodigo_postal_usuario(self):
        return self.Codigo_postal_usuario
    def getprovincia_usuario(self):
        return self.Provincia_usuario
    def getcelular_usuario(self): 
        return self.Celular_usuario
    def getemail_usuario(self):
        return self.Email_usuario
    def getclave_acceso_usuario(self): 
        return self.Clave_acceso_usuario
    def getclave_acceso_usuario_conf(self):
        return self.Clave_acceso_usuario_conf
    def getestado_usuario(self):
        return self.Estado_usuario
    def getrol_usuario(self):
        return self.Rol_usuario
    def getvalidacion_email_usuario(self):
        return self.Validacion_email_usuario


    def setid_usuario(self,id_usuario):
        self.Id_usuario = id_usuario
    def setnombre_usuario(self,nombre_usuario):
        self.Nombre_usuario = nombre_usuario
    def setapellido_usuario(self,apellido_usuario):
        self.Apellido_usuario = apellido_usuario
    def setdni_usuario(self,dni_usuario):
        self.Dni_usuario = dni_usuario
    def setdireccion_usuario(self,direccion_usuario):
        self.Direccion_usuario = direccion_usuario
    def setfecha_nac_usuario(self,fecha_nac_usuario): 
        self.Fecha_nac_usuario = fecha_nac_usuario
    def setlocalidad_usuario(self,localidad_usuario):
        self.Localidad_usuario = localidad_usuario
    def setcodigo_postal_usuario(self,codigo_postal_usuario):
        self.Codigo_postal_usuario = codigo_postal_usuario
    def setprovincia_usuario(self,provincia_usuario):
        self.Provincia_usuario = provincia_usuario
    def setcelular_usuario(self,celular_usuario): 
        self.Celular_usuario = celular_usuario
    def setemail_usuario(self,email_usuario):
        self.Email_usuario = email_usuario
    def setclave_acceso_usuario(self,clave_acceso_usuario): 
        self.Clave_acceso_usuario = clave_acceso_usuario
    def setclave_acceso_usuario_conf(self,clave_acceso_usuario_conf):
        self.Clave_acceso_usuario_conf = clave_acceso_usuario_conf
    def setestado_usuario(self,estado_usuario):
        self.Estado_usuario = estado_usuario
    def setrol_usuario(self,rol_usuario):
        self.Rol_usuario = rol_usuario
    def setvalidacion_email_usuario(self,validacion_email_usuario):
        self.Validacion_email_usuario = validacion_email_usuario


    def imprimir_usuario(self):

        print(f"Nombre: {self.getnombre_usuario()}")
        print(f"Apellido: {self.getapellido_usuario()}")
        print(f"DNI: {self.getdni_usuario()}")
        print(f"Direccion: {self.getdireccion_usuario()}")
        print(f"Fecha nacimiento: {self.getfecha_nac_usuario()}")
        print(f"Localidad: {self.getlocalidad_usuario()}")
        print(f"codigo postal: {self.getcodigo_postal_usuario()}")
        print(f"Provincia: {self.getprovincia_usuario()}")
        print(f"celular: {self.getcelular_usuario()}")
        print(f"email: {self.getemail_usuario()}")
        print(f"rol: {self.getrol_usuario()}")


class Docente(Usuarios):
    pass


usuario1 = Usuarios(1,"carlos","luna",22774118,"alcorta 35","14/05/1975","la granja","5086","cordoba",351246789,"lacasa@gmail.com","1234","1234","activo","docente","validado")
usuario2 = Usuarios(1,"ezequiel","unla",22774118,"alcorta 35","14/05/1975","la granja","5086","cordoba",351246789,"lacasa2@gmail.com","4321","4321","activo","estudiante","validado")


docente1 = Docente(1,"carlos","luna",22774118,"alcorta 35","14/05/1975","la granja","5086","cordoba",351246789,"lacasa@gmail.com","1234","1234","activo","docente","validado")

docente1.imprimir_usuario()
