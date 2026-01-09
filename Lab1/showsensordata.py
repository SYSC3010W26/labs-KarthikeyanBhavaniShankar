from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

while True:
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()

    message = f"T:{temperature:.1f}C P:{pressure:.1f} H:{humidity:.1f}%"
    sense.show_message(message, scroll_speed=0.07)

    time.sleep(1)
