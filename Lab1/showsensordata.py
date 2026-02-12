from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

choice = input("Which sensor to display: (t)emperature,(p)ressure, or (h)umidity: ")
choice = choice.upper()

if choice == "T":
    temperature = sense.get_temperature()
    sense.show_message(f"T:{temperature:.1f}C",
                       text_colour=[255,0,0])

elif choice == "H":
    humidity = sense.get_humidity()
    sense.show_message(f"H:{humidity:.1f}%",
                       text_colour=[0,0,255])

elif choice == "P":
    pressure = sense.get_pressure()
    sense.show_message(f"P:{pressure:.1f}hPa",
                       text_colour=[0,255,0])

else:
    sense.show_message("Invalid Choice",
                       text_colour=[255,255,0])

    time.sleep(1)
