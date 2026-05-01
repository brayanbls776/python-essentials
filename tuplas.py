#necesitas un programa para calcular los promedios de tus alumnos;
#el programa pide el nombre del alumno seguido de su calificación;
#los nombres son ingresados en cualquier orden;
#el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso Fundamentos de Python)
#una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
registro = {}
while True:
    nombre = input("Ingrese el nombre del alumno (o deje vacío para finalizar): ")
    if nombre == "":
        break
    calificacion = float(input("Ingrese la calificación de {}: ".format(nombre)))
    # Aquí puedes almacenar los nombres y calificaciones en una lista o diccionario para calcular los promedios después 
    registro[nombre] = calificacion

# Calcular los promedios
for nombre, calificacion in registro.items():
    print("El promedio de {} es: {}".format(nombre, calificacion))

    