import gpiozero
import time

class Mouvement:
    def __init__(self, capteur_infrarouge):
        self.IN1 = gpiozero.DigitalOutputDevice(6)
        self.IN2 = gpiozero.DigitalOutputDevice(5)  # moteur G
        self.ENA = gpiozero.PWMOutputDevice(13)

        self.IN3 = gpiozero.DigitalOutputDevice(15)
        self.IN4 = gpiozero.DigitalOutputDevice(14) # moteur D
        self.ENB = gpiozero.PWMOutputDevice(18)
        
        self.capteur_infrarouge = capteur_infrarouge
        self.Initialiser()

            
    def Avancer(self, est_detecter=False):
        time.sleep(0.5)
        while (not est_detecter):
            self.Initialiser()
            self.IN1.on()
            self.IN3.on()
            self.ENA.value = 0.3
            self.ENB.value = 0.3
            time.sleep(0.01)
            
            if(self.capteur_infrarouge.doit_arreter):
                time.sleep(0.18)
                est_detecter = True
                self.capteur_infrarouge.doit_arreter = False
            else:
                if(self.capteur_infrarouge.gauche_actif):
                    self.Correction("gauche")
                if(self.capteur_infrarouge.droite_actif):
                    self.Correction("droite")

    def Correction(self, dir, wait=0.1):
        if (dir == "gauche"):
            self.IN2.on()
            self.IN3.on()
            self.ENA.value = 0.38
            self.ENB.value = 0.38
        elif (dir == "droite"):
            self.IN1.on()
            self.IN4.on()
            self.ENA.value = 0.38
            self.ENB.value = 0.38
        time.sleep(wait)
    
    def Tourner(self, dir, est_detecter = False,  wait=1):
        time.sleep(wait)
        self.Initialiser()
        if(dir != None):
            
            while(not est_detecter):
                if (dir == "left"):
                    self.IN2.on()
                    self.IN3.on()
                    self.ENA.value = 0.37
                    self.ENB.value = 0.37
                    if(self.capteur_infrarouge.gauche_actif):
                        est_detecter=True
                        self.Initialiser()
                elif (dir == "right"):
                    self.IN1.on()
                    self.IN4.on()
                    self.ENA.value = 0.37
                    self.ENB.value = 0.37
            
                    if(self.capteur_infrarouge.droite_actif):
                        est_detecter=True
                        self.Initialiser()
            
            

    def Initialiser(self):
        self.ENA.off()
        self.ENB.off()
        self.IN1.off()
        self.IN2.off()
        self.IN3.off()
        self.IN4.off()
