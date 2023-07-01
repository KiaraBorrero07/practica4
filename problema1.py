#PROBLEMA 01
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        return float(data['bpi']['USD']['rate'].replace(',', ''))
    except requests.RequestException:
        return None

def main():
    # Para solicitar la cantidad de bitcoins al usuario
    while True:
        try:
            n = float(input("Ingrese la cantidad de bitcoins que posee: "))
            break
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")

    # Para obtener el precio actual de bitcoin
    bitcoin_price = get_bitcoin_price()

    if bitcoin_price is None:
        print("Error al obtener el precio de bitcoin. Por favor, inténtelo de nuevo más tarde.")
        return

    # Calculo del costo actual en USD
    cost_in_usd = n * bitcoin_price

    # Para mostrar el resultado del costo actual de bitcoins en USD
    print(f"El costo actual de {n:,} Bitcoins es: ${cost_in_usd:,.4f}")

if __name__ == '__main__':
    main()
