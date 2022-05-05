import gpiozero
import time

class Mouvement:
    def __init__(self):
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)  # moteur G
        self.ENA = gpiozero.PWDOutputDevice(13)

        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14) # mouteur
        self.ENB = gpiozero.PWDOutputDevice(18)

    def forward(self, time=0):
        self.IN1.on()
        self.ENA.on()
        time.sleep(5)
        self.IN1.off()
        self.ENA.off()     

    def turn90(self, dir):
        pass
