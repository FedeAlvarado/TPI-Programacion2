from datetime import date

class Archivo:
    def __init__(self, nombre: str,formato: str):
        self.__nombre = nombre
        self.__fecha = date.today()
        self.__formato = formato
        

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def formato(self) -> str:
        return self.__formato


    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Fecha: {self.fecha}, Formato: {self.formato}"


# curso_programacion_i = Curso("Programación I")
# curso_programacion_ii = Curso("Programación II")

# archivo1 = Archivo("tpi.pdf", "PDF", curso_programacion_i)
# archivo2 = Archivo("practica1.pdf","PDF", curso_programacion_i)

# archivo3 = Archivo("tpii.pdf","PDF", curso_programacion_ii)
# archivo4 = Archivo("practica2.pdf","PDF", curso_programacion_ii)

# curso_programacion_i.archivos = [archivo1, archivo2]
# curso_programacion_ii.archivos = [archivo3, archivo4]
