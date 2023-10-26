from usuario import Usuario
from estudiante import Estudiante
from curso import Curso
from profesor import Profesor
import os
from archivo import Archivo
from datetime import date

alumnos = [] #LISTAS A UTILIZAR
profesores = [] #LISTAS A UTILIZAR

alumno1 = Estudiante("Federico", "Alvarado", "email1", "123", "12345", "2023-10-18")
alumno2 = Estudiante("Agustin", "Coronel", "email2", "123", "12345", "2023-10-18")
profesor1 = Profesor("Mercedes", "Valoni", "email3", "123", "Analista Sistemas", "2022")
profesor2 = Profesor("Tomas", "Ponce", "email4", "123", "Analista Sistemas", "2022")

cursos = [
    Curso("Programación I"),
    Curso("Programación II"),
    Curso("Laboratorio I"),
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Matematica"),
    Curso("Estadistica"),
] #LISTAS A UTILIZAR


archivo1 = Archivo("tpi.pdf", date(2023, 10, 15), "PDF", cursos[0])
archivo2 = Archivo("practica1.pdf", date(2023, 10, 20), "PDF", cursos[0])

archivo3 = Archivo("tpii.pdf", date(2023, 10, 16), "PDF", cursos[1])
archivo4 = Archivo("practica2.pdf", date(2023, 10, 21), "PDF", cursos[1])

cursos[0].archivos = [archivo1, archivo2]
cursos[1].archivos = [archivo3, archivo4]

alumnos.append(alumno1)
alumnos.append(alumno2)
profesores.append(profesor1)

def menu_principal():
    print("|--------------------------------------|")
    print("|BIENVENIDO AL CAMPUS VIRTUAL DE LA UTN|")
    print("|--------------------------------------|")    
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
    print("2 - Desmatricularse de un curso")
    print("3 - Ver cursos matriculados")
    print("4 - Volver al menú principal")

def obtener_cursos_ordenados():
    return sorted(cursos, key=lambda x: x.nombre)

while True:
    menu_principal()
    opt = input("Ingrese una opción: ")

    if opt == "1":
        print("|--------------------------------------|")
        print("|-----------CAMPUS DEL ALUMNO----------|")
        print("|--------------------------------------|")        
        email = input("Ingrese su correo electrónico: ")
        password = input("Ingrese su contraseña: ")
        alumno_encontrado = None
        for alumno in alumnos:
            if isinstance(alumno, Estudiante) and alumno.validar_credenciales(email, password):
                alumno_encontrado = alumno
                break
        if alumno_encontrado:
            os.system('cls')
            print(f"BIENVENIDO AL CAMPUS, {alumno_encontrado.name} {alumno_encontrado.surname}.")

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
                                
                                if curso_seleccionado in alumno_encontrado.mis_cursos:
                                    print("Ya estás matriculado en este curso.")
                                else:
                                    alumno_encontrado.mis_cursos.append(curso_seleccionado)
                                    print(f"Te has matriculado en el curso {curso_seleccionado.nombre}.")
                                    input("\nPresione una tecla para volver al menú: ")
                                    os.system('cls')
                            else:
                                print("Opción no válida. Intente de nuevo.")
                        except ValueError:
                            print("Ingrese un número válido.")



                elif opt_alumno == "2":
                    print("Cursos matriculados:")
                    for i, curso in enumerate(alumno_encontrado.mis_cursos, start=1):
                        print(f"{i}. {curso.nombre}")
                    curso_seleccionado = None
                    while curso_seleccionado is None:
                        try:
                            opcion = int(input("Seleccione el número del curso a desmatricular: "))
                            if 1 <= opcion <= len(alumno_encontrado.mis_cursos):
                                curso_seleccionado = alumno_encontrado.mis_cursos[opcion - 1]
                                alumno_encontrado.desmatricular_curso(curso_seleccionado)
                                print(f"Te has desmatriculado del curso {curso_seleccionado.nombre}.")
                            else:
                                print("Opción no válida. Intente de nuevo.")
                        except ValueError:
                            print("Ingrese un número válido.")

                elif opt_alumno == "3":
                    cursos_inscriptos = alumno_encontrado.mis_cursos
                    if not cursos_inscriptos:
                        print("No estás inscrito en ningún curso.")
                    else:
                        for i, curso in enumerate(cursos_inscriptos, start=1):
                            print(f"{i}. {curso.nombre}")

                        opcion_curso = input("Seleccione el número del curso para ver los archivos: ")
                        try:
                            opcion_curso = int(opcion_curso)
                            if 1 <= opcion_curso <= len(cursos_inscriptos):
                                curso_seleccionado = cursos_inscriptos[opcion_curso - 1]
                                print(f"Archivos para el curso '{curso_seleccionado.nombre}':")
                                for archivo in curso_seleccionado.archivos:
                                    print(archivo)
                            else:
                                print("Opción no válida. Intente de nuevo.")
                        except ValueError:
                            print("Ingrese un número válido para seleccionar un curso.")


                elif opt_alumno == "4":
                    break  # volver al menú principal

                else:
                    print("Error: Correo electrónico o contraseña incorrectos.")


    elif opt == "2":
            print("|--------------------------------------|")
            print("|----------CAMPUS DEL PROFESOR---------|")
            print("|--------------------------------------|") 
            email = input("Ingrese su correo electrónico: ")
            password = input("Ingrese su contraseña: ")
            profesor_encontrado = None
            for profesor in profesores:
                if isinstance(profesor, Profesor )  and profesor.validar_credenciales(email, password):
                    profesor_encontrado = profesor
                    break
            if profesor_encontrado:
                os.system('cls')
                print(f"BIENVENIDO AL CAMPUS, {profesor_encontrado.name} {profesor_encontrado.surname}.")
                
                while True:
                    menu_profesor()
                    opt_profesor = input("Ingrese una opción de profesor: ")
                    cursos_ordenados = sorted(cursos, key=lambda x: x.nombre)
                    if opt_profesor == "1":
                        print("Cursos disponibles:")
                        for i, curso in enumerate(cursos_ordenados, start=1):
                            print(f"{i}. {curso.nombre}")
                        curso_seleccionado = None
                        while curso_seleccionado is None:
                            try:
                                opcion = int(input("Seleccione el número del curso que desea dictar: "))
                                os.system('cls')
                                if 1 <= opcion <= len(cursos_ordenados):
                                    curso_seleccionado = cursos_ordenados[opcion - 1]

                                    if curso_seleccionado not in profesor_encontrado.dicto_curso:  
                                            profesor_encontrado.dicto_curso.append(curso_seleccionado)  
                                            print(f"Te has subscripto para dictar el curso {curso_seleccionado.nombre}.")
                                            print(f"La contraseña de este curso es: {curso_seleccionado.password}")
                                            print("Anotela para compartirla con sus alumnos el primer dia de clases!!")
                                            input("\nPresione una tecla para volver al menu: ")
                                            os.system('cls')
                                    else:
                                        print("ATENCION!!\nYa estás dictando este curso.")
                                else:
                                    print("Opción no válida. Intente de nuevo.")
                            except ValueError:
                                print("Ingrese un número válido para poder continuar")
                        pass
                    elif opt_profesor == "2":

                        cursos_dictados = profesor_encontrado.dicto_curso
                        if not cursos_dictados:
                             print("Todavia no se anoto en el dictado de ningun curso")
                        else:     
                            for i, curso in enumerate(cursos_dictados, start=1):
                                print(f"{i}. {curso.nombre}")
                        curso_seleccionado = None
                        while curso_seleccionado is None:
                            try:
                                opcion = int(input("Seleccione el número del curso que desea averiguar la informacion: "))
                                if 1 <= opcion <= len(cursos_dictados):
                                    curso_seleccionado = cursos_dictados[opcion - 1]
                                    print(f"Nombre del curso: {curso_seleccionado.nombre}")
                                    print(f"Contraseña del curso: {curso_seleccionado.password}")
                                    input("\nPresione una tecla para volver al menu: ")
                                    os.system('cls')
                            except ValueError:
                                print("Ingrese un número válido para poder continuar")                       
                    elif opt_profesor == "3":
                        break 
            else:
                print("Error: Correo electrónico o contraseña incorrectos.")
    elif opt == "3":
            cursos_ordenados = sorted(cursos, key=lambda x: x.nombre)
            cursos_ordenados = obtener_cursos_ordenados()
            print("A continuacion se detallan los cursos que dicta la UTN: \n")            
            for curso in cursos_ordenados:
                print(f"{curso.nombre}  ----- {curso.carrera}")
            input("\nPresione una tecla para continuar: ")
            os.system('cls')
                
    elif opt == "4":
            print("Saludos!.")
            break
    elif  opt < "1" or opt > "4":
        os.system('cls')
        print("OPCION INVALIDA, INGRESE UN NUMERO DEFINIDO EN EL MENU \n")

