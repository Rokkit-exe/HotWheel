import gpiozero
import time

class Mouvement:
    def __init__(self):
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)  # moteur G
        self.ENA = gpiozero.PWMOutputDevice(13)

        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14) # mouteur
        self.ENB = gpiozero.PWMOutputDevice(18)

    def forward(self, wait=0):
        self.IN1.on()
        self.IN3.on()
        self.ENA.on()
        self.ENB.on()
        time.sleep(wait)
        self.initialise()   

    def turn90(self, dir):
        pass

    def initialise(self):
        self.ENA.off()
        self.ENB.off()
        self.IN1.off()
        self.IN2.off()
        self.IN3.off()
        self.IN4.off()
