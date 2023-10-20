import random
import string

class Curso():
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.carrera =  "Tecnicatura Universitaria en Programacion"
        self.__password_matriculacion = self.__generar_password()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def password(self) -> str:
        return self.__password_matriculacion

    @nombre.setter
    def nombre(self, nombre_mat: str):
        self.__nombre = nombre_mat


    def __str__(self) -> str:
        return f"Curso: {self.__nombre} - Carrera: {self.carrera} - Clave de Matriculacion: {self.password}"

    @classmethod
    def __generar_password(cls):
        # Genera una contraseña aleatoria
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))




