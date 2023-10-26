import random
import string

class Curso():
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.carrera = "Tecnicatura Universitaria en Programacion"
        self.__password_matriculacion = self.__generar_password()
        self.prox_cod = 0
        self.contrasenia_matriculacion = ""
        self.archivos = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def password(self) -> str:
        return self.__password_matriculacion

    @nombre.setter
    def nombre(self, nombre_mat: str):
        self.__nombre = nombre_mat

    def nuevo_archivo(self, archivo):
        pass

    def __str__(self) -> str:
        return f"Curso: {self.__nombre} - Carrera: {self.carrera} - Clave de Matriculación: {self.password}"

    @classmethod
    def __generar_password(cls):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))





