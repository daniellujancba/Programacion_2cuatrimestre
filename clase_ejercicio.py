



# ********************************************** CLASE CURSO *********************************************
class Cursos():
    ID_curso = 0,
    Fecha_Inicio = 0,
    Titulo = "",
    Descripcion = "",
    Objetivos ="",
    Programa = "",
    Costo = 0,
    Duracio_meses = 0,
    Foto = "",
    Estado = ""

    def __init__(self,iD_curso,fecha_Inicio,titulo,descripcion,objetivos,programa,costo,duracion_meses,foto,estado):
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


# ********************************************** CLASE CLASES *********************************************
class Clases():
    Nombre_clase = "",
    Fecha_clase = 0,
    Contenido = "",
    Url_drive = ""
    

    def __init__(self,nombre_clase,fecha_clase,contenido,url_drive):
        #self.atributo = parametro_enviado

        self.Nombre_clase = nombre_clase
        self.Fecha_clase = fecha_clase
        self.Contenido = contenido
        self.Url_drive = url_drive
       
    def getnombre_clase(self): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
        return self.Nombre_clase
    def getfecha_clase(self):
        return self.Fecha_clase
    def getcontenido(self):
        return self.Contenido
    def geturl_drive(self):
        return self.Url_drive

    def setnombre_clase(self,nombre_clase):# ESTE METODO ASIGNA UN VALOR A ESTE ATRIBUTO
        self.Nombre_clase = nombre_clase 
    def setfecha_clase(self,fecha_clase):
        self.Fecha_clase = fecha_clase
    def setcontenido(self,contenido):
        self.Contenido = contenido
    def seturl_drive(self,url_drive):
        self.Url_drive = url_drive


# ********************************************** CLASE DOCENTE *********************************************
class Docentes():
    Apellido_docente ="",
    Nombre_docente ="",
    Dni = 0,
    Fecha_nacimiento = 0,
    Direccion_docente = "",
    Localidad = "",
    Codigo_postal = "",
    Provincia = "",
    Celular_docente = 0,
    Email_docente = ""
    

    def __init__(self,apellido_docente,nombre_docente,dni,fecha_nacimiento,direccion_docente,localidad,codigo_postal,provincia,celular_docente,email_docente):
        #self.atributo = parametro_enviado

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
       
    def getapellido_docente(self): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
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
    

# ********************************************** CLASE USUARIOS ********************************************
class Usuarios():
    
    Nombre_usuario ="",
    Apellido_usuario ="",
    Dni_usuario = 0,
    Direccion_usuario = "",
    Fecha_nac_usuario = 0,
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
    
    

    def __init__(self,nombre_usuario,apellido_usuario,dni_usuario,direccion_usuario,fecha_nac_usuario,localidad_usuario,codigo_postal_usuario,provincia_usuario,celular_usuario,email_usuario,clave_acceso_usuario,clave_acceso_usuario_conf,estado_usuario,rol_usuario,validacion_email_usuario):

        
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
       
    def getnombre_usuario(self): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
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


    
    def setnombre_usuario(self,nombre_usuario): # DEVUELVE EL VALOR DE ESTE ATRIBUTO
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



# ********************************************** CLASE CARRITO DE COMPARAS *********************************
class Carrito_de_compras():
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
    Monto_total = 0,
    Nombre_usuario_compra ="",
    Apellido_usuario_compra ="",
    Costo_curso = 0,
    Foto_curso = "",
    Nombre_curso_compra = "",
    Duracion_meses_compras = ""




    def __init__(self,tarjeta_cred_banco,tarjeta_cred_emisor,tarjeta_cred_numero,tarjeta_cred_titular,tarjeta_cred_vencimiento,tarjeta_debito_banco,tarjeta_debito_red,tarjeta_debito_numero,tarjeta_debito_titular,tarjeta_debito_pin,transferencia_banco,transferencia_cbu,transferencia_titular,fecha_compra,confirmacion_compra,monto_total,nombre_usuario_compra,apellido_usuario_compra,costo_curso,foto_curso,nombre_curso_compra,duracion_meses_compras):
        #self.atributo = parametro_enviado

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
        self.Monto_total = monto_total
        self.Nombre_usuario_compra = nombre_usuario_compra
        self.Apellido_usuario_compra = apellido_usuario_compra
        self.Costo_curso = costo_curso
        self.Foto_curso = foto_curso
        self.Nombre_curso_compra = nombre_curso_compra
        self.Duracion_meses_compras = duracion_meses_compras

       
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
    def getmonto_total(self):
        return self.Monto_total
    def getnombre_usuario_compra(self):
        return self.Nombre_usuario_compra
    def getapellido_usuario_compra(self):
        return self.Apellido_usuario_compra
    def getcosto_curso(self):
        return self.Costo_curso
    def getfoto_curso(self):
        return self.Foto_curso
    def getnombre_curso_compra(self):
        return self.Nombre_curso_compra
    def getduracion_meses_compras(self):
        return self.Duracion_meses_compras


    
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
    def setmonto_total(self,monto_total):
        self.Monto_total = monto_total
    def setnombre_usuario_compra(self,nombre_usuario_compra):
        self.Nombre_usuario_compra = nombre_usuario_compra
    def setapellido_usuario_compra(self,apellido_usuario_compra):
        self.Apellido_usuario_compra = apellido_usuario_compra
    def setcosto_curso(self,costo_curso):
        self.Costo_curso = costo_curso
    def setfoto_curso(self,foto_curso):
        self.Foto_curso = foto_curso
    def setnombre_curso_compra(self,nombre_curso_compra):
        self.Nombre_curso_compra = nombre_curso_compra
    def setduracion_meses_compras(self,duracion_meses_compras):
        self.Duracion_meses_compras = duracion_meses_compras


    

    
    