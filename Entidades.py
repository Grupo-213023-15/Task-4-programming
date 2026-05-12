from abc import ABC, abstractmethod

# [21] clase abstracta para entidades generales
class entidadsistema(ABC):
    def __init__(self, id_entidad):
        self.id_entidad = id_entidad
    
    @abstractmethod
    def mostrar_detalle(self):
        pass
    
# [22] clase cliente con encapsulación de datos personales
class cliente(entidadsistema):
    def __init__(self, id_entidad, nombre, correo):
        super().__init__(id_entidad)
        self.__nombre = nombre #atributo privado
        self.__correo = self.__validar_correo(correo)
        
    def __validar_correo(self, correo):
        if "@" not in correo:
            raise ValueError("correo inválido")
    return correo

    def mostrar_detalle(self):
        return f"cliente: {self.__nombre} (id: {self.id__entidad})"
