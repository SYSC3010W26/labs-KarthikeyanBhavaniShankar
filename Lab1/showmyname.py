from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

name = "Karthikeyan Bhavani Shankar"

while True:
    sense.show_message(name, scroll_speed=0.08, text_colour=[0, 255, 0])
    time.sleep(0.5)
