# RaspberryPiRFIDUygulamasi
 
Raspberry Pi kurulumunu burada[](https://github.com/shrgrl/RPi-Kurulumu) anlatmıştım. İlk olarak proje için gerekli olan ayarlamaları yaptım. Bunun için Raspberry Pi’nin ayarlarında SSH, SPI ve kenbi bilgisayarımda kullanabilmek için VNC’yi enable etmem gerekti. 
<td>
 <li>SSH: Ağ üzerinden uzak komut satırı bağlantısı sağlar. SSH arayüzünü güvenlik sebebiyle “pi” kullanıcısının şifresini değiştirmeden aktifleştirmememiz gerekir.</li>
 <li>VNC: Ağ üzerinden uzak masaüstü bağlantısı sağlar.</li> 
 <li>SPI: Donanımsal SPI bağlantısını aktifleştirir. GPIO pinleri aracılığı ile SPI bağlantısına sahip bir cihaz kullanmak istersek (sensör, RFID okuyucu, LCD ekran v.b.) aktifleştirmemiz gerekir.</li>
</td>
<br>Daha sonra gerekli devre elemanlarını ayarladım:<br><br>
<td>
 <li>Raspberry Pi</li>
 <li>Breadboard</li>
 <li>RC522 RFID seti</li>
 <li>LED</li>
 <li>220 Ω direnç</li>
 <li>Jumper kablo</li>
</td>

<br>Daha sonra fritzing ile devre çizimimi yaptım.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img1.jpg)

Ardından çok dikkatli şekilde devremi hazırladım.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img2.jpg)

Devre bağlantımızı tamamladıktan sonra, Python kodumuzun çalışabilmesi için öncelikle gerekli kütüphaneyi yüklememiz gerekli:

```python
sudo pip install pi-rc522
```

Aşağıdaki Python kodunu rfid-read.py isimli bir dosyaya kaydediyoruz.

```python
from pirc522 import RFID
import signal
import time

rdr = RFID()
util = rdr.util()
util.debug = True
print("Kart bekleniyor...")
rdr.wait_for_tag()
(error, data) = rdr.request()

if not error:
 print("Kart Algilandi!")
 (error, uid) = rdr.anticoll()
 if not error:
 kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
 print(kart_uid)
```

Kodu kaydettikten sonra;

```python
python rfid-read.py
```

komutu ile çalıştırıyor ve kartımızı okutuyoruz. Böylelikle okuttuğumuz kartın UID’sini öğrenebiliriz.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img6.jpg)

Bana böyle bir id verdi. Bu id’yi bir kenara not ettim. Daha sonra aşağıdaki kodu rc522.py isimli dosyaya kaydettim.

```python
from pirc522 import RFID
import signal
import time
import RPi.GPIO as GPIO 

ledpin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)
rdr = RFID()
util = rdr.util()
util.debug = True

while True:
 rdr.wait_for_tag()
 (error, data) = rdr.request()
 if not error:
 print("\nKart Algilandi!")
 (error, uid) = rdr.anticoll()
 if not error:
 # Print UID
 kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
 print(kart_uid)
 if kart_uid == "xxxxxxxxxxxxxxxx":
 print("LED Yandi!")
 GPIO.output(ledpin, True) 
 else: 
 print("LED Sondu!")
 GPIO.output(ledpin, False)
```

Daha önce kopyaladığım UID’yi, bu kodda yer alan

```python
if kart_uid == "xxxxxxxxxxxxxxxx":
```

satırındaki değer ile değiştirdim. Böylece program bizim okutmuş olduğumuz RFID kartını algıladığı zaman bağlamış olduğumuz LED’i yakacak. Farklı bir kart okuttuğumuzda ise LED sönecek:

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img9.jpg)

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img10.jpg)



