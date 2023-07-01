#PROBLEMA 05
import csv

# Ingreso de datos de precios de Bitcoin
datos_bitcoin = [
    ["Fecha", "Precio"],
    ["2023-06-28", 30335],
    ["2023-06-29", 30452],
    ["2023-06-30", 30406]
]

# Para almacenar los datos de Bitcoin en archivo de texto (txt)
with open("bitcoindatos.txt", "w") as archivo_txt:
    for fila in datos_bitcoin:
        archivo_txt.write(",".join(str(dato) for dato in fila) + "\n")
    print("Datos de Bitcoin almacenados en bitcoindatos.txt")

# Para almacenar los datos de Bitcoin en archivo CSV
with open("bitcoindatos.csv", "w", newline="") as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos_bitcoin)
    print("Datos de Bitcoin almacenados en bitcoindatos.csv")
