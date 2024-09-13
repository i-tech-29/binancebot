from binance.client import Client
import time

# Binance API anahtarlarınız
api_key = 'API_KEYINIZ'
api_secret = 'SECRET_KEYINIZ'

# Binance Client'ı oluşturma
client = Client(api_key, api_secret)

# Basit bir alım satım stratejisi
def check_market_and_trade(symbol, buy_threshold, sell_threshold):
    # Piyasa fiyatını al
    price = float(client.get_symbol_ticker(symbol=symbol)['price'])
    print(f"{symbol} fiyatı: {price}")

    # Alım-Satım koşulları
    if price < buy_threshold:
        print("Alım yapılıyor...")
        order = client.order_market_buy(symbol=symbol, quantity=0.001)
        print(order)
    elif price > sell_threshold:
        print("Satış yapılıyor...")
        order = client.order_market_sell(symbol=symbol, quantity=0.001)
        print(order)

# Ana döngü
while True:
    try:
        check_market_and_trade('BTCUSDT', buy_threshold=25000, sell_threshold=30000)
        time.sleep(60)  # 1 dakika bekle
    except Exception as e:
        print(f"Hata: {e}")
        time.sleep(60)
