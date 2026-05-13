from abc import ABC, abstractmethod


class EntidadSistema(ABC):
    """
    Clase base abstracta para todas las entidades del sistema.
    Proporciona un identificador único y comportamiento común.
    """

    def __init__(self, id_entidad):
        if not id_entidad:
            raise ValueError("El id_entidad no puede estar vacío")
        self._id_entidad = id_entidad

    @property
    def id_entidad(self):
        return self._id_entidad

    @abstractmethod
    def __str__(self):
        pass
