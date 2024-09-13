Kripto para alım satım botu yazmak oldukça kapsamlı bir iş, ancak temel seviyede bir **Python** botu yazabilir ve nasıl çalıştığını açıklayabilirim. Bu tür bir bot genellikle bir borsanın API'sini kullanarak işlem yapar, alım-satım stratejileri uygular ve riskleri yönetir. Temel adımları şu şekilde özetleyebiliriz:

### 1. Borsa API'si:
İlk adım olarak, bir kripto para borsası seçmemiz gerekiyor. Örneğin:
- **Binance**
- **Coinbase**
- **Kraken**

Bu borsaların API'lerini kullanarak işlem gerçekleştirebiliriz. Örneğin, **Binance API**'siyle bir bot yazabiliriz.

### 2. API Anahtarlarının Alınması:
Botu kullanabilmek için API anahtarlarına ihtiyacınız olacak. Borsaların API sayfasından anahtarları oluşturabilirsiniz. Bu anahtarlar botun borsada işlem yapmasına izin verir:
- **API Key:** Erişim izni
- **Secret Key:** Güvenli bağlantı

### 3. Python Botunun Yazılması:

İlk olarak, Binance API'yi kullanarak basit bir bot yazalım. Bu bot, piyasa verilerini alıp belirli bir koşul sağlandığında alım veya satım yapabilir.

#### Gereksinimler:
- Python 3.x
- `binance` Python kütüphanesi

#### Adımlar:
1. Python ortamını hazırlayın.
2. Gerekli kütüphaneyi kurun:
   ```bash
   pip install python-binance
   ```

3. Aşağıdaki gibi bir bot kodu oluşturun:

```python
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
```

### 4. Kodun Çalışma Mantığı:
- `check_market_and_trade` fonksiyonu, piyasadan belirli bir kripto paranın fiyatını alır (örneğin `BTCUSDT` yani Bitcoin/USDT çifti).
- Eğer fiyat belirlediğiniz bir **alım sınırının** altına düşerse, alım yapar.
- Eğer fiyat **satış sınırının** üstüne çıkarsa, satış yapar.
- Bot 1 dakika aralıklarla piyasa fiyatını kontrol eder.

### 5. Botun Kullanımı:
1. Binance API'inden aldığınız `api_key` ve `api_secret` değerlerini kodun içine yerleştirin.
2. Alım ve satım eşiklerini (`buy_threshold`, `sell_threshold`) kendi stratejinize göre ayarlayın.
3. Botu çalıştırmak için komut satırından şu komutu kullanın:
   ```bash
   python bot.py
   ```

### Önemli Notlar:
- Bu bot çok basit bir stratejiye dayanmaktadır. Gerçek ticarette daha karmaşık ve güvenli stratejiler geliştirilmesi gerekir.
- API anahtarlarınızı ve diğer bilgilerinizi güvenli bir şekilde sakladığınızdan emin olun.
- Alım satım işlemleri gerçek para içerdiği için riskleri göz önünde bulundurun.

Bu şekilde bir başlangıç yapabilirsiniz. Botu daha fazla özelleştirmek isterseniz, farklı stratejiler ve risk yönetimi ekleyebiliriz.
