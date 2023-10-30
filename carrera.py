class Carrera:
    def __init__(self, nombre: str, cant_anios: int):
        self.__nombre = nombre
        self.__cant_anios = cant_anios
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def anios(self) -> int:
        return self.__cant_anios
    @nombre.setter
    def nombre(self, new_name:str):
        self.__nombre = new_name
    
    def __str__(self) -> str:
        return f'Carrera: {self.nombre}, Duración: {self.cant_anios} años'

    def get_cantidad_materias(self) -> int:
        return 0  