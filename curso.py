import random
import string
from archivo import Archivo

class Curso():
    __prox_cod = int(0) 
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__password_matriculacion = self.__generar_password()
        self.__codigo = self.__prox_cod + 1
        self.__archivos = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def password(self) -> str:
        return self.__password_matriculacion
    @property
    def cod(self) -> int:
        return self.__codigo
    @property
    def archivos(self):
        return self.__archivos
    @property
    def cantidad_archivos(self) -> int:
        return len(self.archivos)
    
    @nombre.setter
    def nombre(self, nombre_mat: str):
        self.__nombre = nombre_mat
    @archivos.setter
    def archivos(self,new_arc):
        self.__archivos = new_arc

    def nuevo_archivo(self, archivo: Archivo):
        self.__archivos.append(archivo)

    def __str__(self) -> str:
        return f"Curso: {self.__nombre} - Carrera: {self.carrera} - Clave de Matriculación: {self.password} - Cantidad de archivos:{self.cantidad_archivos}"

    @classmethod
    def __generar_password(cls):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))





