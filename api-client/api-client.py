# Fetch remote data
import requests
import sys

usage = "Usage: python api-client.py <symbol> [currency]" \
"\nExample: python api-client.py BTC USD" \
"\n         python api-client.py ETH EUR\n" \
"\n  symbol: Cryptocurrency symbol (e.g., BTC, ETH)" \
"\n  currency: Optional. Currency to convert to (default: USD)"

if (len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']):
    print(usage)
    sys.exit(1)

symbol = sys.argv[1]
currency = len(sys.argv) > 2 and sys.argv[2] or "USD"
url = f"https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms={currency}"


def fetch_data(url):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        sys.exit(1)
    return response.json()

jsonData = fetch_data(url)
price = jsonData.get(currency)
print(f"The current price of {symbol.upper()} is: {price} {currency}")
