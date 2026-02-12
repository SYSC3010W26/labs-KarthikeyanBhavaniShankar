from gpiozero import LED

class TrafficLights:

    def __init__(self, red_pin, yellow_pin, green_pin):
        self.red = LED(red_pin)
        self.yellow = LED(yellow_pin)
        self.green = LED(green_pin)

    def red_on(self):
        self.red.on()
        self.yellow.off()
        self.green.off()

    def yellow_on(self):
        self.red.off()
        self.yellow.on()
        self.green.off()

    def green_on(self):
        self.red.off()
        self.yellow.off()
        self.green.on()
