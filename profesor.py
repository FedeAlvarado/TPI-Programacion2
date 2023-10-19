from usuario import Usuario
from curso import Curso
class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, password, materia):
        super().__init__(nombre, apellido, email, password)
        self.__materia = materia

    
    @property
    def titulo(self) -> str:
        return self.__titulo
    @property
    def anio_ingreso(self) -> int:
        return self.__anio_ingreso
    
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
    
    @anio_ingreso.setter
    def anio_ingreso(self, anio: str):
        self.__anio_ingreso = anio
    
    def dictar_curso(curso:Curso):
        pass
    
    def __str__(self) -> str:
        pass