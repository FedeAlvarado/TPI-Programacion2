import random
import string

class Curso:
    def __init__(self, materia, carrera):
        self.materia = materia
        self.carrera = carrera
        self.__password_matriculacion = self.generar_password()

    @property
    def materia(self) -> str:
        return self.__materia

    @property
    def carrera(self) -> str:
        return self.__carrera

    @property
    def password(self) -> str:
        return self.__password_matriculacion

    @materia.setter
    def materia(self, materia: str):
        self.__materia = materia

    @carrera.setter
    def carrera(self, carrera: str):
        self.__carrera = carrera

    def __str__(self) -> str:
        return f'Materia: {self.materia} Carrera: {self.carrera}'

    @classmethod
    def generar_password(cls):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(8))
    
cursos = [
        Curso("InglesI", "Tecnicatura Universitaria en Programación"),
        Curso("InglesII", "Tecnicatura Universitaria en Programación"),
        Curso("Laboratorio I", "Tecnicatura Universitaria en Programación"),
        Curso("Laboratorio II", "Tecnicatura Universitaria en Programación"),
        Curso("Programación I", "Tecnicatura Universitaria en Programación"),
        Curso("Programación II", "Tecnicatura Universitaria en Programación")
        ]

# Ordenar la lista de cursos alfabéticamente por materia
cursos_ordenados = sorted(cursos, key=lambda curso: curso.materia)

def obtener_cursos_ordenados():
    return cursos_ordenados

