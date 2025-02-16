# pylint: disable=invalid-name


"""Ejercicio de sistema de reservación_Reserva"""
import json
import os


class Reserva:
    """Clase que representa la información de una reserva"""
    def __init__(self, reserva_id, cliente_id, hotel_id, habitacion_id):
        self.reserva_id = reserva_id
        self.cliente_id = cliente_id
        self.hotel_id = hotel_id
        self.habitacion_id = habitacion_id

    def guardar_en_archivo(self):
        "Guardar reservaciones de habitación"
        reservas = self.cargar_desde_archivo()
        reservas[self.reserva_id] = self.__dict__
        with open("reservas.json", "w", encoding="utf-8") as archivo:
            json.dump(reservas, archivo, indent=4)

    @staticmethod
    def cargar_desde_archivo():
        "Cargar reservaciones de un hotel"
        if not os.path.exists("reservas.json"):
            return {}
        with open("reservas.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    @staticmethod
    def eliminar_reserva(reserva_id):
        "Eliminar reservaciones de habitación"
        reservas = Reserva.cargar_desde_archivo()
        if reserva_id in reservas:
            del reservas[reserva_id]
            with open("reservas.json", "w", encoding="utf-8") as archivo:
                json.dump(reservas, archivo, indent=4)
