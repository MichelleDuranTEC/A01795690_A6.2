# pylint: disable=invalid-name


"""Ejercicio de sistema de reservación_Tests"""
import unittest

# Ignorar errores de importación en pylint
from hotel import Hotel  # pylint: disable=import-error
from cliente import Cliente  # pylint: disable=import-error
from reserva import Reserva  # pylint: disable=import-error

class TestSistema(unittest.TestCase):
    """Clase para pruebas unitarias"""
    def setUp(self):
        self.hotel = Hotel("H001", "Hotel Central", "CDMX", {"101": True, "102": True})
        self.cliente = Cliente("C001", "Michelle Duran", "michelle@example.com")
        self.reserva = Reserva("R001", "C001", "H001", "101")
    def test_crear_hotel(self):
        "Crear hotel"
        self.hotel.guardar_en_archivo()
        hoteles = Hotel.cargar_desde_archivo()
        self.assertIn("H001", hoteles)
    def test_eliminar_hotel(self):
        "Eliminar hotel"
        self.hotel.guardar_en_archivo()
        Hotel.eliminar_hotel("H001")
        hoteles = Hotel.cargar_desde_archivo()
        self.assertNotIn("H001", hoteles)
    def test_modificar_hotel(self):
        "Modificar información del hotel"
        self.hotel.guardar_en_archivo()
        self.hotel.modificar_hotel(nombre="Hotel Modificado", ubicacion="Nueva Ubicación")
        hoteles = Hotel.cargar_desde_archivo()
        self.assertEqual(hoteles["H001"]["nombre"], "Hotel Modificado")
        self.assertEqual(hoteles["H001"]["ubicacion"], "Nueva Ubicación")
    def test_crear_cliente(self):
        "Crear cliente"
        self.cliente.guardar_en_archivo()
        clientes = Cliente.cargar_desde_archivo()
        self.assertIn("C001", clientes)
    def test_eliminar_cliente(self):
        "Eliminar cliente"
        self.cliente.guardar_en_archivo()
        Cliente.eliminar_cliente("C001")
        clientes = Cliente.cargar_desde_archivo()
        self.assertNotIn("C001", clientes)
    def test_modificar_cliente(self):
        "Modificar información del cliente"
        self.cliente.guardar_en_archivo()
        self.cliente.modificar_cliente(nombre="Nuevo Nombre", correo="nuevo@example.com")
        clientes = Cliente.cargar_desde_archivo()
        self.assertEqual(clientes["C001"]["nombre"], "Nuevo Nombre")
        self.assertEqual(clientes["C001"]["correo"], "nuevo@example.com")
    def test_reservar_habitacion(self):
        "Reservar habitación"
        resultado = self.hotel.reservar_habitacion("101")
        self.assertTrue(resultado)
        self.assertFalse(self.hotel.habitaciones["101"])
    def test_eliminar_reserva(self):
        "Eliminar reserva"
        self.reserva.guardar_en_archivo()
        Reserva.eliminar_reserva("R001")
        reservas = Reserva.cargar_desde_archivo()
        self.assertNotIn("R001", reservas)

if __name__ == "__main__":
    unittest.main()
