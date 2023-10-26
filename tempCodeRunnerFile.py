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
                                # Aquí puedes agregar el código para mostrar los archivos del curso
                                # Puedes acceder a los archivos asociados al curso usando curso_seleccionado.archivos
                                for archivo in curso_seleccionado.archivos:
                                    print(archivo)
                            else:
                                print("Opción no válida. Intente de nuevo.")
                        except ValueError:
                            print("Ingrese un número válido para seleccionar un curso.")