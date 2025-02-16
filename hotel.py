# pylint: disable=invalid-name


"""Ejercicio de sistema de reservación_Hotel"""
import json
import os


class Hotel:
    """Clase que representa la información de un hotel"""

    def __init__(self, hotel_id, nombre, ubicacion, habitaciones):
        self.hotel_id = hotel_id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = habitaciones  # Dict {room_id: disponible}

    def guardar_en_archivo(self):
        "Guardar hoteles de archivo. Se puede mostrar información del hotel"
        hoteles = self.cargar_desde_archivo()
        hoteles[self.hotel_id] = self.__dict__
        with open("hoteles.json", "w", encoding="utf-8") as archivo:
            json.dump(hoteles, archivo, indent=4)

    @staticmethod
    def cargar_desde_archivo():
        "Crear un hotel. Cargar hoteles de archivo"
        if not os.path.exists("hoteles.json"):
            return {}
        with open("hoteles.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    @staticmethod
    def eliminar_hotel(hotel_id):
        "Eliminar un hotel"
        hoteles = Hotel.cargar_desde_archivo()
        if hotel_id in hoteles:
            del hoteles[hotel_id]
            with open("hoteles.json", "w", encoding="utf-8") as archivo:
                json.dump(hoteles, archivo, indent=4)

    def modificar_hotel(self, nombre=None, ubicacion=None):
        "Modificar información del hotel"
        if nombre:
            self.nombre = nombre
        if ubicacion:
            self.ubicacion = ubicacion
        self.guardar_en_archivo()

    def reservar_habitacion(self, habitacion_id):
        "Reservar una habitación"
        if self.habitaciones.get(habitacion_id, False):
            self.habitaciones[habitacion_id] = False
            self.guardar_en_archivo()
            return True
        return False

    def cancelar_reserva(self, habitacion_id):
        "Cancelar una reserva"
        if habitacion_id in self.habitaciones:
            self.habitaciones[habitacion_id] = True
            self.guardar_en_archivo()
            return True
        return False
