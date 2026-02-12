sense = SenseHat()
sense.clear()

while True:
choice = input("Enter T for Temperature, H for Humidity, P for Pressure: ")
choice = choice.upper()

if choice == "T":
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
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

    message = f"T:{temperature:.1f}C P:{pressure:.1f} H:{humidity:.1f}%"
    sense.show_message(message, scroll_speed=0.07)
else:
    sense.show_message("Invalid Choice",
                       text_colour=[255,255,0])

    time.sleep(1
