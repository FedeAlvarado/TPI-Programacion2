from usuario import *
from curso import *


class Estudiante():
    def __init__(self,legajo:int, date_ins:int) -> None:
        self.__legajo = legajo
        self.__date_ins = date_ins
    
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
        pass

    def matriculacion(self, curso:Curso):
        pass
    
