Excepciones personalizadas 


class ErrorReserva(Exception):
    """Excepción base para reservas"""
    pass


class ClienteInvalidoError(ErrorReserva):
    pass


class ServicioNoDisponibleError(ErrorReserva):
    pass


class DuracionInvalidaError(ErrorReserva):
    pass


class EstadoInvalidoError(ErrorReserva):
    pass
