from abc import ABC, abstractmethod
from Entidades import EntidadSistema


class Servicio(EntidadSistema, ABC):
    """
    Clase abstracta base para todos los servicios del sistema.
    Hereda de ABC y EntidadSistema para combinar abstracción e identidad.
    """

    def __init__(self, id_entidad, nombre):
        super().__init__(id_entidad)
        if not nombre:
            raise ValueError("El nombre del servicio no puede estar vacío")
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, impuesto=0.0, descuento=0.0):
        """
        Calcula el costo del servicio con parámetros opcionales.

        :param impuesto: Porcentaje de impuesto como decimal (ej. 0.19 para 19%)
        :param descuento: Porcentaje de descuento como decimal (ej. 0.10 para 10%)
        :return: Costo final como float
        """
        pass

    def __str__(self):
        return f"[ID: {self.id_entidad}] Servicio: {self.nombre}"


# ──────────────────────────────────────────────
# Subclase 1: Reserva de Sala
# ──────────────────────────────────────────────

class ReservaSala(Servicio):
    """
    Servicio de reserva de sala por horas.
    Costo base = horas × costo_por_hora
    """

    def __init__(self, id_entidad, nombre, horas, costo_por_hora):
        super().__init__(id_entidad, nombre)
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        if costo_por_hora <= 0:
            raise ValueError("El costo por hora debe ser mayor a 0")
        self.horas = horas
        self.costo_por_hora = costo_por_hora

    def calcular_costo(self, impuesto=0.0, descuento=0.0):
        base = self.horas * self.costo_por_hora
        return base * (1 + impuesto) * (1 - descuento)

    def __str__(self):
        return (f"{super().__str__()} | Tipo: ReservaSala | "
                f"Horas: {self.horas} | Costo base: ${self.calcular_costo():.2f}")


# ──────────────────────────────────────────────
# Subclase 2: Alquiler de Equipo
# ──────────────────────────────────────────────

class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipo por días.
    Costo base = días × costo_por_dia
    """

    def __init__(self, id_entidad, nombre, dias, costo_por_dia):
        super().__init__(id_entidad, nombre)
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")
        if costo_por_dia <= 0:
            raise ValueError("El costo por día debe ser mayor a 0")
        self.dias = dias
        self.costo_por_dia = costo_por_dia

    def calcular_costo(self, impuesto=0.0, descuento=0.0):
        base = self.dias * self.costo_por_dia
        return base * (1 + impuesto) * (1 - descuento)

    def __str__(self):
        return (f"{super().__str__()} | Tipo: AlquilerEquipo | "
                f"Días: {self.dias} | Costo base: ${self.calcular_costo():.2f}")


# ──────────────────────────────────────────────
# Subclase 3: Asesoría Especializada
# ──────────────────────────────────────────────

class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría con factor multiplicador según nivel del experto.
    Costo base = horas × tarifa_por_hora × factor_nivel
    """

    NIVELES = {
        "junior":      1.0,
        "semi-senior": 1.2,
        "senior":      1.5,
    }

    def __init__(self, id_entidad, nombre, horas, tarifa_por_hora, nivel_experto):
        super().__init__(id_entidad, nombre)
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        if tarifa_por_hora <= 0:
            raise ValueError("La tarifa por hora debe ser mayor a 0")
        if nivel_experto not in self.NIVELES:
            raise ValueError(
                f"Nivel experto inválido. Opciones: {list(self.NIVELES.keys())}"
            )
        self.horas = horas
        self.tarifa_por_hora = tarifa_por_hora
        self.nivel_experto = nivel_experto

    def calcular_costo(self, impuesto=0.0, descuento=0.0):
        base = self.horas * self.tarifa_por_hora * self.NIVELES[self.nivel_experto]
        return base * (1 + impuesto) * (1 - descuento)

    def __str__(self):
        return (f"{super().__str__()} | Tipo: AsesoriaEspecializada | "
                f"Horas: {self.horas} | Nivel: {self.nivel_experto} | "
                f"Costo base: ${self.calcular_costo():.2f}")


# ──────────────────────────────────────────────
# EJEMPLO DE USO
# ──────────────────────────────────────────────

if __name__ == "__main__":
    servicios = [
        ReservaSala("SRV-001", "Sala de reuniones", 3, 50),
        AlquilerEquipo("SRV-002", "Proyector", 2, 30),
        AsesoriaEspecializada("SRV-003", "Consultoría IT", 5, 100, "senior"),
    ]

    for servicio in servicios:
        print(servicio)
        print(f"  Costo base:                  ${servicio.calcular_costo():.2f}")
        print(f"  Con 19% impuesto:            ${servicio.calcular_costo(impuesto=0.19):.2f}")
        print(f"  Con 10% descuento:           ${servicio.calcular_costo(descuento=0.10):.2f}")
        print(f"  Con impuesto y descuento:    ${servicio.calcular_costo(impuesto=0.19, descuento=0.10):.2f}")
        print("-" * 60)
