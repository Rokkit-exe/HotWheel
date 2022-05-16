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
        self.Initialise()


    
    def Avancer(self, capteur_infrarouge, est_detecter=False):
        self.Initialise()
        while(not est_detecter):
            self.IN1.on()
            self.IN3.on()
            self.ENA.value = 0.3
            self.ENB.value = 0.3
            if(capteur_infrarouge.gauche_actif and capteur_infrarouge.droite_actif):
                print("J'arrête")
                est_detecter = True
            elif(capteur_infrarouge.gauche_actif or capteur_infrarouge.droite_actif):
                self.Est_Sur_Ligne(capteur_infrarouge)
            
    def Est_Sur_Ligne(self, capteur_infrarouge):
        if(capteur_infrarouge.gauche_actif):
            print("Je rentre correction gauche")
            self.ENA.value = 0
            self.ENB.value = 1
        elif(capteur_infrarouge.droite_actif):
            print("Je rentre correction droite")
            self.ENA.value = 1
            self.ENB.value = 0
        
    
    def Tourner_90(self, dir, capteur_infrarouge, est_detecter = False,  wait=0.78):
        while(not est_detecter):
            if (dir == "left"):
                self.IN2.on()
                self.IN3.on()
                self.ENA.value = 0.4
                self.ENB.value = 0.4
            elif (dir == "right"):
                self.IN1.on()
                self.IN4.on()
                self.ENA.value = 0.4
                self.ENB.value = 0.4
            time.sleep(wait)
            if(dir == "left"):
                if(capteur_infrarouge.gauche_actif):
                    print("IR gauche activé")
                    est_detecter=True
            elif(dir == "right"):
                if(capteur_infrarouge.droite_actif):
                    print("IR droite activé")
                    est_detecter = True

    def Wiggle(self):
        self.turn90("right", 0.5)
        self.turn90("left", 0.5)
        self.turn90("right", 1)
        self.turn90("right", 1)
        self.turn90("left", 0.5)
        self.turn90("left", 0.5)

    def Initialise(self):
        self.ENA.off()
        self.ENB.off()
        self.IN1.off()
        self.IN2.off()
        self.IN3.off()
        self.IN4.off()
