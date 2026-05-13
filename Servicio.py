from abc import ABC, abstractmethod
from Entidades import EntidadSistema


class Servicio(ABC, EntidadSistema):
    def __init__(self, id_entidad, nombre):
        super().__init__(id_entidad)          # EntidadSistema recibe el id
        if not nombre:
            raise ValueError("El nombre del servicio no puede estar vacío")
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        """
        Parámetros opcionales:
          descuento : porcentaje de descuento  (ej. 0.10 = 10 %)
          impuesto  : porcentaje de impuesto   (ej. 0.19 = 19 %)
        Retorna el costo final aplicando descuento primero, luego impuesto.
        """
        pass

    def _aplicar_modificadores(self, costo_base, descuento=0.0, impuesto=0.0):
        """Lógica compartida: descuento → impuesto."""
        if not (0.0 <= descuento <= 1.0):
            raise ValueError("El descuento debe estar entre 0.0 y 1.0")
        if not (0.0 <= impuesto <= 1.0):
            raise ValueError("El impuesto debe estar entre 0.0 y 1.0")
        costo = costo_base * (1 - descuento)
        costo = costo * (1 + impuesto)
        return round(costo, 2)

    def __str__(self):
        return f"[ID: {self.id_entidad}] Servicio: {self.nombre}"


class ReservaSala(Servicio):
    def __init__(self, id_entidad, nombre, horas, costo_por_hora):
        super().__init__(id_entidad, nombre)
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        if costo_por_hora <= 0:
            raise ValueError("El costo por hora debe ser mayor a 0")
        self.horas = horas
        self.costo_por_hora = costo_por_hora

    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        base = self.horas * self.costo_por_hora
        return self._aplicar_modificadores(base, descuento, impuesto)

    def __str__(self):
        return (f"{super().__str__()} | Tipo: ReservaSala | "
                f"Horas: {self.horas} | Costo base: {self.calcular_costo()}")


class AlquilerEquipo(Servicio):
    def __init__(self, id_entidad, nombre, dias, costo_por_dia):
        super().__init__(id_entidad, nombre)
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")
        if costo_por_dia <= 0:
            raise ValueError("El costo por día debe ser mayor a 0")
        self.dias = dias
        self.costo_por_dia = costo_por_dia

    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        base = self.dias * self.costo_por_dia
        return self._aplicar_modificadores(base, descuento, impuesto)

    def __str__(self):
        return (f"{super().__str__()} | Tipo: AlquilerEquipo | "
                f"Días: {self.dias} | Costo base: {self.calcular_costo()}")


class AsesoriaEspecializada(Servicio):
    _FACTORES = {
        "junior": 1.0,
        "semi-senior": 1.2,
        "senior": 1.5,
    }

    def __init__(self, id_entidad, nombre, horas, tarifa_por_hora, nivel_experto):
        super().__init__(id_entidad, nombre)
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        if tarifa_por_hora <= 0:
            raise ValueError("La tarifa por hora debe ser mayor a 0")
        if nivel_experto not in self._FACTORES:
            raise ValueError(f"Nivel experto inválido. Opciones: {list(self._FACTORES)}")
        self.horas = horas
        self.tarifa_por_hora = tarifa_por_hora
        self.nivel_experto = nivel_experto

    def calcular_costo(self, descuento=0.0, impuesto=0.0):
        base = self.horas * self.tarifa_por_hora * self._FACTORES[self.nivel_experto]
        return self._aplicar_modificadores(base, descuento, impuesto)

    def __str__(self):
        return (f"{super().__str__()} | Tipo: AsesoriaEspecializada | "
                f"Horas: {self.horas} | Nivel: {self.nivel_experto} | "
                f"Costo base: {self.calcular_costo()}")


# =========================
# EJEMPLO DE USO (PRUEBA)
# =========================
if __name__ == "__main__":
    servicios = [
        ReservaSala("SRV-001", "Sala de reuniones", 3, 50),
        AlquilerEquipo("SRV-002", "Proyector", 2, 30),
        AsesoriaEspecializada("SRV-003", "Consultoría IT", 5, 100, "senior"),
    ]

    for servicio in servicios:
        print(servicio)
        print(f"  Sin modificadores  : {servicio.calcular_costo()}")
        print(f"  Con 10% descuento  : {servicio.calcular_costo(descuento=0.10)}")
        print(f"  Con 19% impuesto   : {servicio.calcular_costo(impuesto=0.19)}")
        print(f"  Descuento+impuesto : {servicio.calcular_costo(descuento=0.10, impuesto=0.19)}")
        print("-" * 60)
