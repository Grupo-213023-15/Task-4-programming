from abc import ABC, abstractmethod
from Entidades import EntidadSistema

# EntidadSistema va PRIMERO para evitar el error de MRO
class Servicio(EntidadSistema, ABC): 
    def __init__(self, id_entidad, nombre):
        super().__init__(id_entidad)
        self.nombre = nombre

    @abstractmethod
    def mostrar_detalle(self):
        pass

class ReservaSala(Servicio):
    def mostrar_detalle(self):
        return f"Sala reservada: {self.nombre}"

class AlquilerEquipo(Servicio):
    def mostrar_detalle(self):
        return f"Equipo alquilado: {self.nombre}"

class AsesoriaEspecializada(Servicio):
    def mostrar_detalle(self):
        return f"Asesoría técnica: {self.nombre}"