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