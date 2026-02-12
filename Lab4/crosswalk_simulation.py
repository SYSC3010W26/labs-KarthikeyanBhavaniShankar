from traffic_lights import TrafficLights
from gpiozero import Button
import time

lights = TrafficLights(17, 27, 22)
button = Button(23)

while True:
    lights.red_on()
    time.sleep(5)

    lights.green_on()

    if button.wait_for_press(timeout=5):
        lights.yellow_on()
        time.sleep(2)
    else:
        lights.yellow_on()
        time.sleep(2)
