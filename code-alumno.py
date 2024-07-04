import csv
import os
import platform

filename = 'Alumnos.csv'


def menu():
    print("=" * 30)
    print("\n1.- Ingresar Alumno.")
    print("2.- Eliminar Alumno.")
    print("3.- Ver Listado del Curso.")
    print("4.- Salir y guardar.\n")
    print("=" * 30)
    opcion = input("\nSeleccione una opción: ")
    return int(opcion)

def rut_existe(rut):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == rut:
                return True
            
def ingresar_alumno():
    alumnos = filename
    rut = input("\nIngrese el rut del alumno: ")
    
    if rut_existe(rut):
        print("\nEl RUT ingresado ya existe. Intente con otro RUT.")
        return
    nombre = input("\nIngrese el Nombre del Alumno: ")
    nota = input("\nIngrese la nota del alumno: ")

    file_exists = os.path.isfile(alumnos)

    with open(alumnos, mode='a',newline='') as file:
        writer = csv.writer(file)
        if not file_exists or os.stat(alumnos).st_size == 0:
             writer.writerow(['Rut','Nombre','Nota'])
        writer.writerow([rut, nombre, nota])

    
    print(f"\nAlumno ingresado exitosamente en {alumnos}")

def eliminar_alumno():
    rut = input("\nIngrese el RUT del alumno que desea eliminar: ")
    if not rut_existe(rut):
        print("\nEl RUT ingresado no existe. Intete con otro RUT.")
        return
    
    with open(filename, mode='r')as file:
        rows = list(csv.reader(file))
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != rut:
                writer.writerow(row)
    print(f"\nAlumno con RUT {rut} eliminado exitosamente.")


def ver_listado():
    if os.path.isfile(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(', '.join(row))

while True:
    opcion = menu()
    if opcion == 1:
        ingresar_alumno()
    elif opcion == 2:
        eliminar_alumno()
    elif opcion == 3:
        ver_listado()
    elif opcion == 4:
        print("\nSaliendo y guardando...")
        break
    else: 
        print("\nOpción errónea. Intente de nuevo.")