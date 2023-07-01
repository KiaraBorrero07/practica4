#PROBLEMA 06
import sqlite3
import requests
from datetime import datetime

# Para obtener los datos de precio de Bitcoin desde la API de CoinDesk
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()

# Para extraer los precios de Bitcoin en USD, GBP y EUR
precio_usd = data["bpi"]["USD"]["rate_float"]
precio_gbp = data["bpi"]["GBP"]["rate_float"]
precio_eur = data["bpi"]["EUR"]["rate_float"]

# Para crear una conexión a la base de datos
conexion = sqlite3.connect('cryptos.db')
cursor = conexion.cursor()

# Para crear la tabla "bitcoin"
cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  moneda TEXT,
                  precio REAL,
                  fecha TEXT)''')

# Para insertar los datos en la tabla "bitcoin"
fecha_actual = datetime.now().strftime("%Y-%m-%d")
cursor.execute("INSERT INTO bitcoin (moneda, precio, fecha) VALUES (?, ?, ?)", ("USD", precio_usd, fecha_actual))
cursor.execute("INSERT INTO bitcoin (moneda, precio, fecha) VALUES (?, ?, ?)", ("GBP", precio_gbp, fecha_actual))
cursor.execute("INSERT INTO bitcoin (moneda, precio, fecha) VALUES (?, ?, ?)", ("EUR", precio_eur, fecha_actual))

# Para guardar los cambios y cerrar la conexión a la base de datos
conexion.commit()
conexion.close()

print("Los datos de Bitcoin se han almacenado en la tabla 'bitcoin' de la base de datos 'cryptos.db'.")
