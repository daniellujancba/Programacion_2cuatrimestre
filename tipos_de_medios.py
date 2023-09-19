from enum import Enum

class Tipos_Medio_Contacto (Enum):

    WhatsApp = 1
    Correo_electrónico = 2
    Call_center = 3
    Referido_interno = 4

print(Tipos_Medio_Contacto.WhatsApp.value)
print(Tipos_Medio_Contacto.Correo_electrónico.value)
print(Tipos_Medio_Contacto.Call_center.value)
print(Tipos_Medio_Contacto.Referido_interno.value)