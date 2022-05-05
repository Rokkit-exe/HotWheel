import gpiozero
import time

class Mouvement:
    def __init__(self):
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)  # moteur G
        self.ENA = gpiozero.PWMOutputDevice(13)

        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14) # moteur D
        self.ENB = gpiozero.PWMOutputDevice(18)
        self.initialise()

    def forward(self, speed=25, wait=2):
        fade_in = speed / 1000
        fade_out = (100 - speed) / 1000
        print(fade_out)
        self.IN1.on()
        self.IN3.on()
        #self.ENA.on()
        #self.ENB.on()
        self.ENA.pulse(fade_in_time=fade_in, fade_out_time=fade_out)
        self.ENB.pulse(fade_in_time=fade_in, fade_out_time=fade_out)
        time.sleep(wait)
        self.initialise()   

    def turn90(self, dir, wait=1, condition=False):
        #while not condition:
            if (dir == "left"):
                self.IN2.on()
                self.IN3.on()
                self.ENA.on()
                self.ENB.on()
            elif (dir == "right"):
                self.IN1.on()
                self.IN4.on()
                self.ENA.on()
                self.ENB.on()
            time.sleep(wait)
            condition = True
            self.initialise()

    def wiggle(self):
        self.turn90("right", 0.5)
        self.turn90("left", 0.5)
        self.turn90("right", 1)
        self.turn90("right", 1)
        self.turn90("left", 0.5)
        self.turn90("left", 0.5)

    def initialise(self):
        self.ENA.off()
        self.ENB.off()
        self.IN1.off()
        self.IN2.off()
        self.IN3.off()
        self.IN4.off()
