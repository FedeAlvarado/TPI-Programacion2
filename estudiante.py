from usuario import *
from curso import *


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, password, legajo, date_ins):
        super().__init__(nombre, apellido, email, password)
        self.__legajo = legajo
        self.__date_ins = date_ins
        self.mi_cursos = []  

    @property
    def legajo(self) -> str:
        return self.__legajo
    @property
    def date_ins(self) -> int:
        return self.__date_ins
    
    @legajo.setter
    def legajo(self, legajo: int):
        self.__legajo = legajo

    @date_ins.setter
    def date_ins(self, date) -> int:
        self.__date_ins = date
    
    def __str__(self) -> str:
        return f'Legajo: {self.legajo} Fecha de Inscripción: {self.date_ins}'

    def matriculacion(self, curso:Curso):
        pass
    
