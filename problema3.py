#PROBLEMA 03
import requests


url = "https://images.unsplash.com/photo-1600804340584-c7db2eacf0bf?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80"
nombre_archivo = "perrito.jpg"

# Realizar una solicitud GET a la URL
response = requests.get(url)

# Guardar la imagen en un archivo local
with open(nombre_archivo, "wb") as archivo:
     archivo.write(response.content)

