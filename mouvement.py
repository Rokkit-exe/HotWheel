from gpiozero import OutputDevice
import time

class Mouvement:
    def __init__(self):
        self.IN1 = OutputDevice.DigitalOutputDevice(6)
        self.IN2 = OutputDevice.DigitalOutputDevice(5)  # moteur G
        self.ENA = OutputDevice.PWDOutputDevice(13)

        self.IN3 = OutputDevice.DigitalOutputDevice(15)
        self.IN4 = OutputDevice.DigitalOutputDevice(14) # mouteur
        self.ENB = OutputDevice.PWDOutputDevice(18)

    def forward(self, time=0):
        self.IN1.on()
        self.ENA.on()
        time.sleep(5)
        self.IN1.off()
        self.ENA.off()     

    def turn90(self, dir):
        pass
