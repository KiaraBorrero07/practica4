#PROBLEMA 04
import os

def crear_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"
    with open(nombre_archivo, "w") as archivo:
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")

    print(f"Tabla de multiplicar del {numero} guardada en el archivo {nombre_archivo}.")

def mostrar_tabla_multiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"
    if not os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} no existe.")
        return

    with open(nombre_archivo, "r") as archivo:
        tabla = archivo.read()

    print(f"Tabla de multiplicar del {numero}:\n")
    print(tabla)

def mostrar_linea_tabla(numero, linea):
    if numero < 1 or numero > 10 or linea < 1 or linea > 10:
        print("Los números deben estar entre 1 y 10.")
        return

    nombre_archivo = f"tabla-{numero}.txt"
    if not os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} no existe.")
        return

    with open(nombre_archivo, "r") as archivo:
        lineas = archivo.readlines()

    if linea > len(lineas):
        print(f"El archivo {nombre_archivo} no tiene una línea {linea}.")
        return

    linea_deseada = lineas[linea - 1]
    print(f"Línea {linea} de la tabla de multiplicar del {numero}:")
    print(linea_deseada)

def mostrar_menu():
    print("----- MENU -----")
    print("1. Crear tabla de multiplicar")
    print("2. Mostrar tabla de multiplicar completa")
    print("3. Mostrar línea de la tabla de multiplicar")
    print("4. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            crear_tabla_multiplicar(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla_multiplicar(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea (1-10): "))
            mostrar_linea_tabla(numero, linea)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

ejecutar_programa()
