import random
import string

class Curso():
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
        self.__password_matriculacion = self.generar_password()

    @property
    def nombre(self) -> str:
        return self.__nombre
    @property
    def password(self) -> str:
        return self.__password_matriculacion
    
    @nombre.setter
    def nombre(self, nombre_mat: str):
        self.__nombre = nombre_mat

    def __str__(self) -> str:
        return f"Clave:{self.__password_matriculacion} "
        
    @classmethod
    def generar_password() -> str:
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod
    
    #no se si anda este generador de contraseñas

cursito = Curso("Ingles")
print(cursito)
print(cursito)
