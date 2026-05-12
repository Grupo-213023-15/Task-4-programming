from abc import ABC, abstractmethod

# [21] clase abstracta para entidades generales
class EntidadSistema(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad
    
    @abstractmethod
    def mostrar_detalle(self):
        pass
    
# [22] clase cliente con encapsulación de datos personales
class Cliente: # Línea de ejemplo
    def __init__(self, id_entidad, nombre, correo):
        self.id_entidad = id_entidad
        self.nombre = nombre
        self.correo = correo
    
    def obtener_correo(self):
        return self.correo  # <-- Esta línea 22 debe tener 8 espacios (o 2 tabs) a la derecha
