
from flask import Flask, render_template
import BlynkLib
import os
import random
import time

app = Flask(__name__)

BLYNK_AUTH = os.getenv("BLYNK_AUTH")
blynk = BlynkLib.Blynk(BLYNK_AUTH)

latest_moisture = 50

@app.route("/")
def home():
    global latest_moisture

    latest_moisture = random.randint(25, 85)

    if latest_moisture < 40:
        status = "Plant needs water"
    else:
        status = "Soil moisture is good"

    blynk.run()
    blynk.virtual_write(0, latest_moisture)

    return render_template(
        "index.html",
        moisture=latest_moisture,
        status=status
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)