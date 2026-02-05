from sense_hat import SenseHat
import time

def get_sensehat():
    sense = SenseHat()
    sense.clear()
    return sense

def alarm(sense, flash_time):
    red = [255, 0, 0]
    off = [0, 0, 0]

    for _ in range(flash_time):
        sense.clear(red)
        time.sleep(1)
        sense.clear(off)
        time.sleep(1)
