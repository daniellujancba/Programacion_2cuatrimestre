""" Partiendo de la base del ejercicio de CLASES, se pide:"""

# ********************************************** CLASE CURSO *********************************************
class Cursos():
    ID_curso = 0,
    Fecha_Inicio = "",
    Titulo = "",
    Descripcion = "",
    Objetivos ="",
    Programa = "",
    Costo = 0,
    Duracio_meses = 0,
    Foto = "",
    Estado = "",
    Curso_categoria = "",
    Curso_clases = []


    def __init__(self,iD_curso,fecha_Inicio,titulo,descripcion,objetivos,programa,costo,duracion_meses,foto,estado,curso_categoria,curso_clases):
        #self.atributo = parametro_enviado

        self.ID_curso = iD_curso 
        self.Fecha_Inicio = fecha_Inicio
        self.Titulo = titulo
        self.Descripcion = descripcion
        self.Objetivos = objetivos
        self.Programa = programa
        self.Costo = costo
        self.Duracio_meses = duracion_meses
        self.Foto = foto
        self.Estado = estado
        self.Curso_categoria = curso_categoria
        self.Curso_clases = curso_clases
    
    def getiD_curso(self): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
        return self.ID_curso
    def getfecha_Inicio(self):
        return self.Fecha_Inicio
    def gettitulo(self):
        return self.Titulo
    def getdescripcion(self):
        return self.Descripcion
    def getobjetivos(self):
        return self.Objetivos
    def getprograma(self):
        return self.Programa
    def getcosto(self):
        return self.Costo
    def getduracion_meses(self):
        return self.Duracio_meses
    def getfoto(self):
        return self.Foto
    def getestado(self):
        return self.Estado
    def getcurso_categoria(self):
        return self.Curso_categoria
    def getcurso_clases(self):
        return self.Curso_clases

    
    def setiD_curso(self,iD_curso):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.ID_curso = iD_curso 
    def setfecha_Inicio(self,fecha_Inicio):
        self.Fecha_Inicio = fecha_Inicio
    def settitulo(self,titulo):
        self.Titulo = titulo
    def setdescripcion(self,descripcion):
        self.Descripcion = descripcion
    def setobjetivos(self,objetivos):
        self.Objetivos = objetivos
    def setprograma(self, programa):
        self.Programa = programa
    def setcosto(self,costo):
        self.Costo = costo
    def setduracion_meses(self,duracion_meses):
        self.Duracio_meses = duracion_meses
    def setfoto(self, foto):
        self.Foto = foto
    def setestado(self,estado):
        self.Estado = estado
    def setcurso_categoria(self,curso_categoria):
        self.Curso_categoria = curso_categoria
    def setcurso_clases(self,curso_clases):
        self.Curso_clases = Curso_clases


    def imprimir_cursos(self):

        if self.Estado == "activo":

            print(f"ID_curso: {self.getiD_curso()}")
            print(f"Fecha_Inicio: {self.getfecha_Inicio()}")
            print(f"Titulo: {self.gettitulo()}")
            print(f"Descripcion: {self.getdescripcion()}")
            print(f"Objetivos: {self.getobjetivos()}")
            print(f"Programa: {self.getprograma()}")
            print(f"Costo: {self.getcosto()}"+" pesos")
            print(f"Duracion: {self.getduracion_meses()}"+" meses")
            print(f"foto: {self.getfoto()}")
            print(f"Categoria: {self.getcurso_categoria()}")
            print(f"Clases del curso: {self.getcurso_clases()}")

        else:
            print("Curso no disponible")  






# ********************************************** CLASE CLASES *********************************************
class Clases():
    Id_clase = 0,
    Nombre_clase = "",
    Fecha_clase = "",
    Contenido = "",
    Url_drive = "",
    Clase_docente = ""
    

    def __init__(self,id_clase,nombre_clase,fecha_clase,contenido,url_drive,clase_docente):
        #self.atributo = parametro_enviado

        self.Id_clase = id_clase
        self.Nombre_clase = nombre_clase
        self.Fecha_clase = fecha_clase
        self.Contenido = contenido
        self.Url_drive = url_drive
        self.Clase_docente = clase_docente
       
    def getid_clase(self): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
        return self.Id_clase
    def getnombre_clase(self): 
        return self.Nombre_clase
    def getfecha_clase(self):
        return self.Fecha_clase
    def getcontenido(self):
        return self.Contenido
    def geturl_drive(self):
        return self.Url_drive
    def getclase_docente(self):
        return self.Clase_docente

    def setid_clase(self,id_clase):
        return self.Id_clase
    def setnombre_clase(self,nombre_clase):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.Nombre_clase = nombre_clase 
    def setfecha_clase(self,fecha_clase):
        self.Fecha_clase = fecha_clase
    def setcontenido(self,contenido):
        self.Contenido = contenido
    def seturl_drive(self,url_drive):
        self.Url_drive = url_drive
    def setclase_docente(self,clase_docente):
        self.Clase_docente = clase_docente


    def imprimir_clases(self):

        print(f"ID_curso: {self.getid_clase()}")
        print(f"Fecha_Inicio: {self.getnombre_clase()}")
        print(f"Titulo: {self.getfecha_clase()}")
        print(f"Descripcion: {self.getcontenido()}")
        print(f"Objetivos: {self.geturl_drive()}")
        print(f"Docente: {self.getclase_docente()}")
        



# ********************************************** CLASE DOCENTE *********************************************
class Docentes():
    Id_docente = 0
    Apellido_docente ="",
    Nombre_docente ="",
    Dni = 0,
    Fecha_nacimiento = "",
    Direccion_docente = "",
    Localidad = "",
    Codigo_postal = "",
    Provincia = "",
    Celular_docente = 0,
    Email_docente = ""
    

    def __init__(self,id_docente,apellido_docente,nombre_docente,dni,fecha_nacimiento,direccion_docente,localidad,codigo_postal,provincia,celular_docente,email_docente):
        #self.atributo = parametro_enviado
        self.Id_docente = id_docente
        self.Apellido_docente = apellido_docente
        self.Nombre_docente = nombre_docente
        self.Dni = dni
        self.Fecha_nacimiento = fecha_nacimiento
        self.Direccion_docente = direccion_docente
        self.Localidad = localidad
        self.Codigo_postal = codigo_postal
        self.Provincia = provincia
        self.Celular_docente = celular_docente
        self.Email_docente = email_docente
       
    
    def getid_docente(self): 
        return self.Id_docente
    def getapellido_docente(self): 
        return self.Apellido_docente
    def getnombre_docente(self):
        return self.Nombre_docente
    def getdni(self):
        return self.Dni
    def getfecha_nacimiento(self):
        return self.Fecha_nacimiento
    def getdireccion_docente(self): 
        return self.Direccion_docente
    def getlocalidad(self):
        return self.Localidad
    def getcodigo_postal(self):
        return self.Codigo_postal
    def getprovincia(self):
        return self.Provincia
    def getcelular_docente(self): 
        return self.Celular_docente
    def getemail_docente(self):
        return self.Email_docente

    def setid_docente(self,id_docente):
        self.Id_docente = id_docente
    def setapellido_docente(self,apellido_docente):
        self.Apellido_docente = apellido_docente
    def setnombre_docente(self,nombre_docente):
        self.Nombre_docente = nombre_docente
    def setdni(self,dni):
        self.Dni = dni
    def setfecha_nacimiento(self,fecha_nacimiento):
        self.Fecha_nacimiento = fecha_nacimiento
    def setdireccion_docente(self,direccion_docente): 
        self.Direccion_docente = direccion_docente
    def setlocalidad(self,localidad):
        self.Localidad = localidad
    def setcodigo_postal(self,codigo_postal):
        self.Codigo_postal = codigo_postal
    def setprovincia(self,provincia):
        self.Provincia = provincia
    def setcelular_docente(self,celular_docente): 
        self.Celular_docente = celular_docente
    def setemail_docente(self,email_docente):
        self.Email_docente = email_docente


    def imprimir_docentes(self):

        print(f"Nombre: {self.getnombre_docente()}")
        print(f"Apellido: {self.getapellido_docente()}")
        print(f"celular: {self.getcelular_docente()}")
        print(f"email: {self.getemail_docente()}")

# ********************************************** CLASE USUARIOS ********************************************
class Usuarios():
    Id_Usuario = 0
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
    
    

    def __init__(self,id_Usuario,nombre_usuario,apellido_usuario,dni_usuario,direccion_usuario,fecha_nac_usuario,localidad_usuario,codigo_postal_usuario,provincia_usuario,celular_usuario,email_usuario,clave_acceso_usuario,clave_acceso_usuario_conf,estado_usuario,rol_usuario,validacion_email_usuario):

        self.Id_Usuario = id_Usuario
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
       
    def getid_Usuario(self): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
        return self.Id_Usuario
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


    def setid_Usuario(self,id_Usuario): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
        self.Id_Usuario = id_Usuario
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
    def getcelular_usuario(self,celular_usuario): 
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

# ********************************************** CLASE CARRITO DE COMPARAS *********************************

class Carrito_de_compras():
    Id_Carrito_Compra = 0,
    Carrito_usuario = "",
    Carrito_foto = "",
    Carrito_curso = "",
    Carrito_descripcion = "",
    Carrito_precio = 0,
    Carrito_total = 0
    Carrito_formapago = "",
    Compras_cursos = []
    
    
    def __init__(self,id_Carrito_Compra,carrito_usuario,carrito_foto,carrito_curso,carrito_descripcion,carrito_precio,carrito_total,carrito_formapago,compras_cursos):
        #self.atributo = parametro_enviado
        self.Id_Carrito_Compra = id_Carrito_Compra
        self.Carrito_usuario = carrito_usuario
        self.Carrito_foto = carrito_foto
        self.Carrito_curso = carrito_curso
        self.Carrito_descripcion = carrito_descripcion
        self.Carrito_precio = carrito_precio
        self.Carrito_total = carrito_total
        self.Carrito_formapago = carrito_formapago
        self.Compras_cursos = compras_cursos
        

    def getid_Carrito_Compra(self): 
        return self.Id_Carrito_Compra   
    def getcarrito_usuario(self): 
        return self.Carrito_usuario
    def getcarrito_foto(self):
        return self.Carrito_foto
    def getcarrito_curso(self): 
        return self.Carrito_curso
    def getcarrito_descripcion(self):
        return self.Carrito_descripcion
    def getcarrito_precio(self): 
        return self.Carrito_precio  
    def getcarrito_total(self):
        return self.Carrito_total
    def getcarrito_formapago(self):
        return self.Carrito_formapago
    def getcompras_cursos(self):
        return self.Compras_cursos
    
    
    def setid_Carrito_Compra(self,id_Carrito_Compra): 
        self.Id_Carrito_Compra = id_Carrito_Compra
    def setcarrito_usuario(self,carrito_usuario): 
        self.Carrito_usuario = carrito_usuario
    def setcarrito_foto(self,carrito_foto):
        self.Carrito_foto = carrito_foto
    def setcarrito_curso(self,carrito_curso): 
        self.Carrito_curso = carrito_curso
    def setcarrito_descripcion(self,carrito_descripcion):
        self.Carrito_descripcion = carrito_descripcion
    def setcarrito_precio(self,carrito_precio): 
        self.Carrito_precio = carrito_precio  
    def setcarrito_total(self,carrito_total):
        self.Carrito_total = carrito_total
    def setcarrito_formapago(self,carrito_formapago):
        self.Carrito_formapago = carrito_formapago
    def setcompras_cursos(self,compras_cursos):
        self.Compras_cursos = compras_cursos
    

    def agregar_curso(self):
        continuar = True

        while continuar == True:
            consulta = str(input("desae agregar un curso: "))
            if consulta == "si":
                curso_elegido = str(input("nombre del curso: "))
                if curso_elegido == getcarrito_curso():
                    self.Compras_cursos.append(getcarrito_curso)
                    #self.Carrito_total += carrito_curso.getcarrito_precio()
                    continuar = True
                else:
                    print("no esta ese curso")
            else:
                break

            # sin resolver aun
            #self.Carrito_total += getcarrito_precio

    def imprimir_carrito(self):

        print(f"cursos seleccionados: {self.getcompras_cursos()}")


# ********************************************** CLASE MEDIOS DE PAGO *********************************

class Medios_de_pago():
    Id_Medios_Pago = 0,
    Tarjeta_cred_Banco = "",
    Tarjeta_cred_Emisor = "",
    Tarjeta_cred_numero = 0,
    Tarjeta_cred_titular = "",
    Tarjeta_cred_vencimiento = "",
    Tarjeta_debito_Banco = "",
    Tarjeta_debito_red = "",
    Tarjeta_debito_numero = 0,
    Tarjeta_debito_titular = "",
    Tarjeta_debito_pin = "",
    Transferencia_banco = "",
    Transferencia_cbu = 0,
    Transferencia_titular = "",
    Fecha_compra = "",
    Confirmacion_compra = "",
    Monto_Total = 0,
    Nombre_usuario_compra ="",
    Apellido_usuario_compra ="",
    




    def __init__(self,id_Medios_Pago,tarjeta_cred_banco,tarjeta_cred_emisor,tarjeta_cred_numero,tarjeta_cred_titular,tarjeta_cred_vencimiento,tarjeta_debito_banco,tarjeta_debito_red,tarjeta_debito_numero,tarjeta_debito_titular,tarjeta_debito_pin,transferencia_banco,transferencia_cbu,transferencia_titular,fecha_compra,confirmacion_compra,monto_Total,nombre_usuario_compra,apellido_usuario_compra,costo_curso,foto_curso,nombre_curso_compra,duracion_meses_compras):
        #self.atributo = parametro_enviado
        self.Id_Medios_Pago = id_Medios_Pago
        self.Tarjeta_cred_banco = tarjeta_cred_banco
        self.Tarjeta_cred_emisor = tarjeta_cred_emisor
        self.Tarjeta_cred_numero = tarjeta_cred_numero
        self.Tarjeta_cred_titular = tarjeta_cred_titular
        self.Tarjeta_cred_vencimiento = tarjeta_cred_vencimiento
        self.Tarjeta_debito_banco = tarjeta_debito_banco
        self.Tarjeta_debito_red = tarjeta_debito_red
        self.Tarjeta_debito_numero = tarjeta_debito_numero
        self.Tarjeta_debito_titular = tarjeta_debito_titular
        self.Tarjeta_debito_pin = tarjeta_debito_pin
        self.Transferencia_banco = transferencia_banco
        self.Transferencia_cbu = transferencia_cbu
        self.Transferencia_titular = transferencia_titular
        self.Fecha_compra = fecha_compra
        self.Confirmacion_compra = confirmacion_compra
        self.Monto_Total = monto_Total
        self.Nombre_usuario_compra = nombre_usuario_compra
        self.Apellido_usuario_compra = apellido_usuario_compra

        def getid_Medios_Pago(self): 
            return self.id_Medios_Pago
        def gettarjeta_cred_banco(self): 
            return self.Tarjeta_cred_banco
        def gettarjeta_cred_emisor(self):
            return self.Tarjeta_cred_emisor
        def gettarjeta_cred_numero(self): 
            return self.Tarjeta_cred_numero
        def gettarjeta_cred_titular(self):
            return self.Tarjeta_cred_titular
        def gettarjeta_cred_vencimiento(self): 
            return self.Tarjeta_cred_vencimiento  
        def gettarjeta_debito_banco(self):
            return self.Tarjeta_debito_banco
        def gettarjeta_debito_red(self):
            return self.Tarjeta_debito_red
        def gettarjeta_debito_numero(self):
            return self.Tarjeta_debito_numero
        def gettarjeta_debito_titular(self):
            return self.Tarjeta_debito_titular
        def gettarjeta_debito_pin(self):
            return self.Tarjeta_debito_pin
        def gettransferencia_banco(self):
            return self.Transferencia_banco
        def gettransferencia_cbu(self):
            return self.Transferencia_cbu
        def gettransferencia_titular(self):
            return self.Transferencia_titular
        def getfecha_compra(self):
            return self.Fecha_compra
        def getconfirmacion_compra(self):
            return self.Confirmacion_compra
        def getmonto_Total(self):
            return self.Monto_Total
        def getnombre_usuario_compra(self):
            return self.Nombre_usuario_compra
        def getapellido_usuario_compra(self):
            return self.Apellido_usuario_compra
        
        
        def setid_Medios_Pago(self,id_Medios_Pago): 
            self.Id_Medios_Pago = id_Medios_Pago
        def settarjeta_cred_banco(self,tarjeta_cred_banco): 
            self.Tarjeta_cred_banco = tarjeta_cred_banco
        def settarjeta_cred_emisor(self,tarjeta_cred_emisor):
            self.Tarjeta_cred_emisor = tarjeta_cred_emisor
        def settarjeta_cred_numero(self,tarjeta_cred_numero): 
            self.Tarjeta_cred_numero = tarjeta_cred_numero
        def settarjeta_cred_titular(self,tarjeta_cred_titular):
            self.Tarjeta_cred_titular = tarjeta_cred_titular
        def settarjeta_cred_vencimiento(self,tarjeta_cred_vencimiento): 
            self.Tarjeta_cred_vencimiento = tarjeta_cred_vencimiento  
        def settarjeta_debito_banco(self,tarjeta_debito_banco):
            self.Tarjeta_debito_banco = tarjeta_debito_banco
        def settarjeta_debito_red(self,tarjeta_debito_red):
            self.Tarjeta_debito_red = tarjeta_debito_red
        def settarjeta_debito_numero(self,tarjeta_debito_numero):
            self.Tarjeta_debito_numero = tarjeta_debito_numero
        def settarjeta_debito_titular(self,tarjeta_debito_titular):
            self.Tarjeta_debito_titular = tarjeta_debito_titular
        def settarjeta_debito_pin(self,tarjeta_debito_pin):
            self.Tarjeta_debito_pin = tarjeta_debito_pin
        def settransferencia_banco(self,transferencia_banco):
            self.Transferencia_banco = transferencia_banco
        def settransferencia_cbu(self,transferencia_cbu):
            self.Transferencia_cbu = transferencia_cbu
        def settransferencia_titular(self,transferencia_titular):
            self.Transferencia_titular = transferencia_titular
        def setfecha_compra(self,fecha_compra):
            self.Fecha_compra = fecha_compra
        def setconfirmacion_compra(self,confirmacion_compra):
            self.Confirmacion_compra = confirmacion_compra
        def setmonto_Total(self,monto_Total):
            self.Monto_Total = monto_Total
        def setnombre_usuario_compra(self,nombre_usuario_compra):
            self.Nombre_usuario_compra = nombre_usuario_compra
        def setapellido_usuario_compra(self,apellido_usuario_compra):
            self.Apellido_usuario_compra = apellido_usuario_compra
        

# Que la clase Docente, sea herencia de la clase Usuario.

class Docente(Usuarios):
    pass


# Generar una clase nueva que sea compra y contenga:
    # Id_Compra
    # Id_Carrito_Compra
    # Id_Medios_Pago
    # Id_Usuario
    # Fecha
    # Monto_Total


class Compra(Carrito_de_compras,Medios_de_pago,Usuarios):
    Id_Compra = 0

    def __init__(self,id_Compra,id_Carrito_Compra,id_Medios_Pago,id_Usuario,fecha_compra,monto_Total):
        Carrito_de_compras.__init__(self,id_Carrito_Compra,carrito_usuario,carrito_foto,carrito_curso,carrito_descripcion,carrito_precio,carrito_total,carrito_formapago,compras_cursos)

        Medios_de_pago.__init__(self,id_Medios_Pago,tarjeta_cred_banco,tarjeta_cred_emisor,tarjeta_cred_numero,tarjeta_cred_titular,tarjeta_cred_vencimiento,tarjeta_debito_banco,tarjeta_debito_red,tarjeta_debito_numero,tarjeta_debito_titular,tarjeta_debito_pin,transferencia_banco,transferencia_cbu,transferencia_titular,fecha_compra,confirmacion_compra,monto_Total,nombre_usuario_compra,apellido_usuario_compra,costo_curso,foto_curso,nombre_curso_compra,duracion_meses_compras)

        Usuarios.__init__(self,id_Usuario,nombre_usuario,apellido_usuario,dni_usuario,direccion_usuario,fecha_nac_usuario,localidad_usuario,codigo_postal_usuario,provincia_usuario,celular_usuario,email_usuario,clave_acceso_usuario,clave_acceso_usuario_conf,estado_usuario,rol_usuario,validacion_email_usuario)

        self.Id_Compra = id_Compra




