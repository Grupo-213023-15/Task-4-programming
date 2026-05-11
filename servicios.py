from abc import ABC, abstractmethod
from Entidades import EntidadSistema

# [cite: 11] Clase abstracta Servicio que hereda de EntidadSistema
class Servicio(ABC, EntidadSistema):
    def __init__(self, id_entidad, nombre):
        super().__init__(id_entidad)
        if not nombre:
            raise ValueError("El nombre del servicio no puede estar vacío")
        self.nombre = nombre

    #  Método abstracto para polimorfismo con parámetro opcional (sobrecarga)
    @abstractmethod
    def calcular_costo(self, descuento=0):
        pass

    def __str__(self):
        return f"Servicio: {self.nombre} (ID: {self.id_entidad})"

# [cite: 11] Servicio especializado 1: Reserva de Sala
class ReservaSala(Servicio):
    def __init__(self, id_entidad, nombre, horas, costo_por_hora):
        super().__init__(id_entidad, nombre)
        self.horas = horas
        self.costo_por_hora = costo_por_hora

    def calcular_costo(self, descuento=0):
        total = self.horas * self.costo_por_hora
        return total - (total * descuento)

# [cite: 11] Servicio especializado 2: Alquiler de Equipo
class AlquilerEquipo(Servicio):
    def __init__(self, id_entidad, nombre, dias, costo_por_dia):
        super().__init__(id_entidad, nombre)
        self.dias = dias
        self.costo_por_dia = costo_por_dia

    def calcular_costo(self, descuento=0):
        total = self.dias * self.costo_por_dia
        return total - (total * descuento)

# [cite: 11] Servicio especializado 3: Asesoría Especializada
class AsesoriaEspecializada(Servicio):
    def __init__(self, id_entidad, nombre, horas, tarifa_por_hora, nivel_experto):
        super().__init__(id_entidad, nombre)
        self.horas = horas
        self.tarifa_por_hora = tarifa_por_hora
        self.nivel_experto = nivel_experto

    def calcular_costo(self, descuento=0):
        # [cite: 11] Implementación de polimorfismo con lógica específica
        factores = {"junior": 1.0, "semi-senior": 1.2, "senior": 1.5}
        factor = factores.get(self.nivel_experto.lower(), 1.0)
        total = self.horas * self.tarifa_por_hora * factor
        return total - (total * descuento)