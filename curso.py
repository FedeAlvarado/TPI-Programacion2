import random
import string

class Curso():
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.__password_matriculacion = self.generar_password()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def carrera(self) -> str:
        return self.__carrera

    @property
    def password(self) -> str:
        return self.__password_matriculacion

    @nombre.setter
    def nombre(self, nombre_mat: str):
        self.__nombre = nombre_mat

    @carrera.setter
    def carrera(self, carrera: str):
        self.__carrera = carrera

    def __str__(self) -> str:
        return f"Curso: {self.__nombre} - Carrera: {self.__carrera}"

    @classmethod
    def generar_password(cls):
        # Genera una contraseña aleatoria
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))




