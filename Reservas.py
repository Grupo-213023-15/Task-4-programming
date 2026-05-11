from excepciones import *
from datetime import datetime


class Reserva:
    def __init__(self, cliente, servicio, duracion):
        try:
            if cliente is None:
                raise ClienteInvalidoError("El cliente no puede ser nulo")

            if servicio is None:
                raise ServicioNoDisponibleError("El servicio no existe")

            if duracion <= 0:
                raise DuracionInvalidaError("Duración inválida")

            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion
            self.estado = "pendiente"
            self.fecha = datetime.now()

        except Exception as e:
            self.registrar_error(e)
            raise  # re-lanza la excepción

    # -----------------------------
    # Confirmar reserva
    # -----------------------------
    def confirmar(self):
        try:
            if self.estado != "pendiente":
                raise EstadoInvalidoError("Solo reservas pendientes pueden confirmarse")

            self.estado = "confirmada"
            print("✅ Reserva confirmada")

        except Exception as e:
            self.registrar_error(e)

    # -----------------------------
    # Cancelar reserva
    # -----------------------------
    def cancelar(self):
        try:
            if self.estado == "cancelada":
                raise EstadoInvalidoError("La reserva ya está cancelada")

            self.estado = "cancelada"
            print("❌ Reserva cancelada")

        except Exception as e:
            self.registrar_error(e)

    # -----------------------------
    # Procesar reserva
    # -----------------------------
    def procesar(self):
        try:
            if self.estado != "confirmada":
                raise EstadoInvalidoError("Debe confirmarse antes de procesar")

            costo = self.servicio.calcular_costo(self.duracion)
            print(f"💰 Costo total: {costo}")

        except Exception as e:
            self.registrar_error(e)

        else:
            print("✔ Procesamiento exitoso")

        finally:
            print("🔚 Fin del proceso de reserva")

    # -----------------------------
    # LOGS (MUY IMPORTANTE)
    # -----------------------------
    def registrar_error(self, error):
        with open("logs.txt", "a") as archivo:
            archivo.write(f"[ERROR] {datetime.now()} - {str(error)}\n")
