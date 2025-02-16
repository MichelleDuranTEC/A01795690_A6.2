# pylint: disable=invalid-name


"""Ejercicio de sistema de reservación_Cliente"""
import json
import os


class Cliente:
    """Clase que representa a un cliente de un hotel"""
    def __init__(self, cliente_id, nombre, correo):
        self.cliente_id = cliente_id
        self.nombre = nombre
        self.correo = correo

    def guardar_en_archivo(self):
        "Guardar clientes de un hotel"
        clientes = self.cargar_desde_archivo()
        clientes[self.cliente_id] = self.__dict__
        with open("clientes.json", "w", encoding="utf-8") as archivo:
            json.dump(clientes, archivo, indent=4)

    @staticmethod
    def cargar_desde_archivo():
        "Cargar clientes de un hotel"
        if not os.path.exists("clientes.json"):
            return {}
        with open("clientes.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    @staticmethod
    def eliminar_cliente(cliente_id):
        "Eliminar clientes de un hotel"
        clientes = Cliente.cargar_desde_archivo()
        if cliente_id in clientes:
            del clientes[cliente_id]
            with open("clientes.json", "w", encoding="utf-8") as archivo:
                json.dump(clientes, archivo, indent=4)

    def modificar_cliente(self, nombre=None, correo=None):
        "Modificar información clientes de un hotel"
        if nombre:
            self.nombre = nombre
        if correo:
            self.correo = correo
        self.guardar_en_archivo()
