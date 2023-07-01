#PROBLEMA 02
import random
from pyfiglet import Figlet

# Para obtener la lista de fuentes disponibles
figlet = Figlet()
fuentes_disponibles = figlet.getFonts()

# Para solicitar al usuario el nombre de la fuente o para seleccionar aleatoriamente una fuente si no se proporciona una
fuente_seleccionada = input("Ingrese el nombre de la fuente (dejar en blanco para seleccionar aleatoriamente): ")
if not fuente_seleccionada:
    fuente_seleccionada = random.choice(fuentes_disponibles)

# Para solicitar al usuario el texto que se desea imprimir
texto_imprimir = input("Ingrese el texto a imprimir: ")

# Para configurar la selección de la fuente
figlet.setFont(font=fuente_seleccionada)

# Para imprimir el texto 
print(figlet.renderText(texto_imprimir))