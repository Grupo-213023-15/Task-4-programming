import logging

# configuración para que los errores se guarden en 'errores.log'
logging.basicConfig(
    filename='errores.log',
    level=logging.error,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_error(mensaje):
    logging.error(mensaje)