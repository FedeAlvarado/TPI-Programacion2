from abc import ABC

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, password):
        self.__name = nombre
        self.__surname = apellido
        self.__email = email
        self.__password = password

    @property
    def password(self):
        return self.__password
    
    @property
    def name(self):
        return self.__name
    
    @property
    def surname(self):
        return self.__surname
    
    @property
    def email(self):
        return self.__email
    
    @password.setter
    def password(self,new_pass):
        self.__password  = new_pass

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @surname.setter
    def surname(self, surname):
        self.__surname= surname

    def validar_credenciales(self, email:str, password: str) -> bool:
        return self.__email == email and self.__password == password
    
    def __str__(self) -> str:
        return f'Email: {self.email} Contraseña: {self.password}'
    

    