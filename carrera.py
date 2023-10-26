class Carrera:
    def __init__(self, nombre: str, cant_anios: int):
        self.nombre = nombre
        self.cant_anios = cant_anios

    def __str__(self) -> str:
        return f'Carrera: {self.nombre}, Duración: {self.cant_anios} años'

    def get_cantidad_materias(self) -> int:
        return 0  