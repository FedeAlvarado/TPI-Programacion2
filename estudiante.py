from usuario import Usuario
from curso import Curso
from datetime import *

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, password, legajo):
        super().__init__(nombre, apellido, email, password)
        self.__legajo = legajo
        self.__date_ins = date.today()
        self.__mis_cursos = []

    @property
    def legajo(self) -> str:
        return self.__legajo

    @property
    def date_ins(self) -> int:
        return self.__date_ins

    @property
    def mis_cursos(self):
        return self.__mis_cursos

    def __str__(self) -> str:
        return f'Legajo: {self.legajo} Fecha de Inscripción: {self.date_ins}'

    def matricular_curso(self, curso: Curso):
        self.__mis_cursos.append(curso)

    def desmatricular_curso(self, curso: Curso):
        if curso in self.__mis_cursos:
            self.__mis_cursos.remove(curso)

    @legajo.setter
    def legajo(self, legajo: int):
        self.__legajo = legajo

    @date_ins.setter
    def date_ins(self, date) -> int:
        self.__date_ins = date

    def __str__(self) -> str:
        return f'Legajo: {self.legajo} Fecha de Inscripción: {self.date_ins}'

