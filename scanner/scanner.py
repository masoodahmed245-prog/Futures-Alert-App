import time
import requests

COINS = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "SOLUSDT",
    "XRPUSDT",
]

BINANCE_URL = "https://fapi.binance.com/fapi/v1/ticker/price"


def get_price(symbol):
    response = requests.get(
        BINANCE_URL,
        params={"symbol": symbol},
        timeout=10
    )
    response.raise_for_status()
    return float(response.json()["price"])


def main():
    print("🚀 Futures Alert Scanner")
    print("● SCANNER ONLINE")
    print("Monitoring Binance Futures prices...\n")

    while True:
        for coin in COINS:
            try:
                price = get_price(coin)
                print(f"{coin}: {price}")
            except Exception as error:
                print(f"{coin}: ERROR - {error}")

        print("-" * 40)
        time.sleep(10)


if __name__ == "__main__":
    main()
