from usuario import Usuario
from estudiante import Estudiante
from curso import Curso
from profesor import Profesor
from curso import obtener_cursos_ordenados

alumnos = []
profesores = []

alumno1 = Estudiante("nombre1", "apellido1", "email1", "123", "12345", "2023-10-18")
alumno2 = Estudiante("nombre2", "apellido2", "email2", "123", "12345", "2023-10-18")
profesor1 = Profesor("nombre_profesor1", "apellido_profesor1", "email", "123", "Matemáticas")

alumnos.append(alumno1)
alumnos.append(alumno2)
profesores.append(profesor1)

def menu_principal():
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver cursos")
    print("4 - Salir")

def menu_profesor():
    print("1 - Dictar curso")
    print("2 - Ver curso")
    print("3 - Volver al menú principal")

def menu_alumno():
    print("1 - Matricularse a un curso")
    print("2 - Ver curso")
    print("3 - Volver al menú principal")

while True:
    menu_principal()
    opt = input("Ingrese una opción: ")
    if opt == "1":
        email = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        alumno_encontrado = None
        for alumno in alumnos:
            if isinstance(alumno, Estudiante) and alumno.validar_credenciales(email, password):
                alumno_encontrado = alumno
                break
        if alumno_encontrado:
            print(f"Bienvenido, {alumno_encontrado.name} {alumno_encontrado.surname} (alumno).")

            while True:
                menu_alumno()
                opt_alumno = input("Ingrese una opción de estudiante: ")

                if opt_alumno == "1":
                    #  matricularse en un curso
                    pass
                elif opt_alumno == "2":
                    # ver cursos
                    pass
                elif opt_alumno == "3":
                    break  # volver al menú principal

        else:
            print("Error: Correo electrónico o contraseña incorrectos.")

    elif opt == "2":
        email = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        profe_encontrado = None
        for profesor in profesores:
            if isinstance(profesor, Profesor )  and profesor.validar_credenciales(email, password):
                profesor_encontrado = profesor
                break
        if profesor_encontrado:
            print(f"Bienvenido, {profesor_encontrado.name} {profesor_encontrado.surname} (profesor).")

            while True:
                menu_profesor()
                opt_profesor = input("Ingrese una opción de profesor: ")

                if opt_profesor == "1":
                    # dictar un curso
                    pass
                elif opt_profesor == "2":
                    #  ver cursos que el profesor está dictando
                    pass
                elif opt_profesor == "3":
                    break  # volver al menú principal

        else:
            print("Error: Correo electrónico o contraseña incorrectos.")
    elif opt == "3":
         cursos_ordenados = obtener_cursos_ordenados()
         for curso in cursos_ordenados:
            print(curso)
    elif opt == "4":
        print("Saludos!.")
        break

