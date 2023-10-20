from usuario import Usuario
from curso import Curso
class Profesor(Usuario):
    def __init__(self, nombre:str, apellido:str, email:str, password:str, titulo:str, anio:str):
        super().__init__(nombre, apellido, email, password)
        self.__titulo = titulo
        self.__anio_egreso = anio
        self.__mis_cursos = []

    
    @property
    def titulo(self) -> str:
        return self.__titulo
    @property
    def anio_ingreso(self) -> int:
        return self.__anio_egreso
        
    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo
    
    @anio_ingreso.setter
    def anio_ingreso(self, anio: str):
        self.__anio_ingreso = anio
    
    @property
    def dicto_curso(self):
        return self.__mis_cursos
    @dicto_curso.setter
    def dicto_curso(self, curso):
        self.__mis_cursos = curso
    
    def dictar_curso(self, curso:Curso):
        self.dicto_curso.append(curso)
    
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}"