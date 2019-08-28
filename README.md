# RaspberryPiRFIDUygulamasi
 Raspberry Pi using a card reader application
 
Raspberry Pi kurulumunu burada[](https://github.com/shrgrl/RPi-Kurulumu) anlatmıştım. İlk olarak proje için gerekli olan ayarlamaları yaptım. Bunun için Raspberry Pi’nin ayarlarında SSH, SPI ve kenbi bilgisayarımda kullanabilmek için VNC’yi enable etmem gerekti. 
<td>
 <li>SSH: Ağ üzerinden uzak komut satırı bağlantısı sağlar. SSH arayüzünü güvenlik sebebiyle “pi” kullanıcısının şifresini değiştirmeden aktifleştirmememiz gerekir.</li>
 <li>VNC: Ağ üzerinden uzak masaüstü bağlantısı sağlar.</li> 
 <li>SPI: Donanımsal SPI bağlantısını aktifleştirir. GPIO pinleri aracılığı ile SPI bağlantısına sahip bir cihaz kullanmak istersek (sensör, RFID okuyucu, LCD ekran v.b.) aktifleştirmemiz gerekir.</li>
</td>
<br>Daha sonra gerekli devre elemanlarını ayarladım.  
<br>Gerekli malzemeler:
<td>
 <li>Raspberry Pi</li>
 <li>Breadboard</li>
 <li>RC522 RFID seti</li>
 <li>LED</li>
 <li>220 Ω direnç</li>
 <li>Jumper kablo</li>
</td>
<br>Daha sonra fritsizng ile devre çizimimi yaptım.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img1.jpg)

Ardından çok dikkatli şekilde devremi hazırladım.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img2.jpg)

Devre bağlantımızı tamamladıktan sonra, Python kodumuzun çalışabilmesi için öncelikle gerekli kütüphaneyi yüklememiz gerekli:

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img3.jpg)

Aşağıdaki Python kodunu rfid-read.py isimli bir dosyaya kaydediyoruz.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img4.jpg)

Kodu kaydettikten sonra;

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img5.jpg)

komutu ile çalıştırıyor ve kartımızı okutuyoruz. Böylelikle okuttuğumuz kartın UID’sini öğrenebiliriz.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img6.jpg)

Bana böyle bir id verdi. Bu id’yi bir kenara not ettim. Daha sonra aşağıdaki kodu rc522.py isimli dosyaya kaydettim.

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img7.jpg)

Daha önce kopyaladığım UID’yi, bu kodda yer alan

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img8.jpg)

satırındaki değer ile değiştirdim. Böylece program bizim okutmuş olduğumuz RFID kartını algıladığı zaman bağlamış olduğumuz LED’i yakacak. Farklı bir kart okuttuğumuzda ise LED sönecek:

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img9.jpg)

![](https://github.com/shrgrl/RaspberryPiRFIDUygulamasi/blob/master/images/img10.jpg)



