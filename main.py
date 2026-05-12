# ==============================
# main.py
# Simulación de 10 pruebas
# ==============================

from Entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from Reservas import Reserva

print("\n========= SIMULACIONES DEL SISTEMA =========\n")

# ---------------------------------------------------
# SIMULACIÓN 1 - Reserva de sala válida
# ---------------------------------------------------
try:
    cliente1 = Cliente(1, "Maria", "maria@gmail.com")
    servicio1 = ReservaSala(101, "Sala de Juntas", 2, 50000)

    reserva1 = Reserva(cliente1, servicio1, 2)
    reserva1.confirmar()
    reserva1.procesar()

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 2 - Alquiler de equipo válido
# ---------------------------------------------------
try:
    cliente2 = cliente(2, "Carlos", "carlos@gmail.com")
    servicio2 = AlquilerEquipo(102, "VideoBeam", 3, 40000)

    reserva2 = Reserva(cliente2, servicio2, 3)
    reserva2.confirmar()
    reserva2.procesar()

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 3 - Asesoría especializada válida
# ---------------------------------------------------
try:
    cliente3 = cliente(3, "Luisa", "luisa@gmail.com")
    servicio3 = AsesoriaEspecializada(
        103,
        "Asesoría Python",
        4,
        80000,
        "senior"
    )

    reserva3 = Reserva(cliente3, servicio3, 4)
    reserva3.confirmar()
    reserva3.procesar()

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 4 - Cliente inválido
# ---------------------------------------------------
try:
    servicio4 = ReservaSala(104, "Sala VIP", 2, 70000)

    reserva4 = Reserva(None, servicio4, 2)

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 5 - Servicio inexistente
# ---------------------------------------------------
try:
    cliente5 = cliente(5, "Andres", "andres@gmail.com")

    reserva5 = Reserva(cliente5, None, 2)

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 6 - Duración inválida
# ---------------------------------------------------
try:
    cliente6 = cliente(6, "Laura", "laura@gmail.com")
    servicio6 = AlquilerEquipo(106, "Portátil", 1, 60000)

    reserva6 = Reserva(cliente6, servicio6, 0)

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 7 - Procesar sin confirmar
# ---------------------------------------------------
try:
    cliente7 = cliente(7, "Camilo", "camilo@gmail.com")
    servicio7 = ReservaSala(107, "Sala Conferencias", 3, 90000)

    reserva7 = Reserva(cliente7, servicio7, 3)
    reserva7.procesar()

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 8 - Cancelar reserva
# ---------------------------------------------------
try:
    cliente8 = cliente(8, "Valentina", "vale@gmail.com")
    servicio8 = AlquilerEquipo(108, "Micrófono", 2, 25000)

    reserva8 = Reserva(cliente8, servicio8, 2)
    reserva8.cancelar()

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 9 - Cancelar dos veces
# ---------------------------------------------------
try:
    cliente9 = cliente(9, "Felipe", "felipe@gmail.com")
    servicio9 = ReservaSala(109, "Sala Multimedia", 2, 45000)

    reserva9 = Reserva(cliente9, servicio9, 2)

    reserva9.cancelar()
    reserva9.cancelar()

except Exception as e:
    print("Error:", e)

print("\n-----------------------------------\n")

# ---------------------------------------------------
# SIMULACIÓN 10 - Correo inválido
# ---------------------------------------------------
try:
    cliente10 = cliente(10, "Sofia", "correo_invalido")

except Exception as e:
    print("Error:", e)

print("\n========= FIN DE LAS SIMULACIONES =========")
