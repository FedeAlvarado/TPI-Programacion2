from usuario import Usuario
from estudiante import Estudiante
from curso import Curso
from profesor import Profesor

alumnos = []
profesores = []

alumno1 = Estudiante("nombre1", "apellido1", "email1", "123", "12345", "2023-10-18")
alumno2 = Estudiante("nombre2", "apellido2", "email2", "123", "12345", "2023-10-18")
profesor1 = Profesor("nombre_profesor1", "apellido_profesor1", "email", "123", "Matemáticas")
cursos = [
    Curso("Programación I", "Tecnicatura Universitaria en Programación"),
    Curso("Programación II", "Tecnicatura Universitaria en Programación"),
    Curso("Laboratorio II", "Tecnicatura Universitaria en Programación"),
    Curso("InglesI", "Tecnicatura Universitaria en Programación"),
    Curso("InglesII", "Tecnicatura Universitaria en Programación")
]
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

def obtener_cursos_ordenados():
    return cursos_ordenados

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

                cursos_ordenados = sorted(cursos, key=lambda x: x.nombre)

                if opt_alumno == "1":
                    print("Cursos disponibles:")
                    for i, curso in enumerate(cursos_ordenados, start=1):
                        print(f"{i}. {curso.nombre}")
                    curso_seleccionado = None
                    while curso_seleccionado is None:
                        try:
                            opcion = int(input("Seleccione el número del curso: "))
                            if 1 <= opcion <= len(cursos_ordenados):
                                curso_seleccionado = cursos_ordenados[opcion - 1]

                                if curso_seleccionado not in alumno_encontrado.mi_cursos:  # Verificar si ya está matriculado
                                    password_matriculacion = input(f"Ingrese la contraseña de matriculación para '{curso_seleccionado.nombre}': ")
                                    if password_matriculacion == curso_seleccionado.password:
                                        alumno_encontrado.mi_cursos.append(curso_seleccionado)  # Agregar el curso a mi_cursos
                                        print(f"Te has matriculado en el curso {curso_seleccionado.nombre}.")
                                    else:
                                        print("Contraseña de matriculación incorrecta. Intente de nuevo.")
                                else:
                                    print("Ya estás matriculado en este curso.")
                            else:
                                print("Opción no válida. Intente de nuevo.")
                        except ValueError:
                            print("Ingrese un número válido.")

                elif opt_alumno == "2":
                    if isinstance(alumno_encontrado, Estudiante):
                     print("Cursos disponibles para matricularse:")
                    cursos_ordenados = sorted(cursos, key=lambda x: x.nombre)
                    for i, curso in enumerate(cursos_ordenados, start=1):
                        print(f"{i} {curso.nombre}")
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

