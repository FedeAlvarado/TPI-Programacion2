from curso import Curso
from datetime import date

class Archivo:
    def __init__(self, nombre: str, fecha: date, formato: str, curso: Curso):
        self.__nombre = nombre
        self.__fecha = fecha
        self.__formato = formato
        self.__curso = curso

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def formato(self) -> str:
        return self.__formato

    @property
    def curso(self) -> Curso:
        return self.__curso

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Fecha: {self.fecha}, Formato: {self.formato}, Curso: {self.curso.nombre}"


curso_programacion_i = Curso("Programación I")
curso_programacion_ii = Curso("Programación II")

archivo1 = Archivo("tpi.pdf", date(2023, 10, 15), "PDF", curso_programacion_i)
archivo2 = Archivo("practica1.pdf", date(2023, 10, 20), "PDF", curso_programacion_i)

archivo3 = Archivo("tpii.pdf", date(2023, 10, 16), "PDF", curso_programacion_ii)
archivo4 = Archivo("practica2.pdf", date(2023, 10, 21), "PDF", curso_programacion_ii)

curso_programacion_i.archivos = [archivo1, archivo2]
curso_programacion_ii.archivos = [archivo3, archivo4]
