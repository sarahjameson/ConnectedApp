import BlynkLib
import os
import time

BLYNK_AUTH = os.getenv("BLYNK_AUTH")

blynk = BlynkLib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()

    print("Connected to Blynk")
    blynk.virtual_write(0, 50)

    time.sleep(2)