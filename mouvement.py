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


    # FDF je n'ai pas réussi a réguler la vitesse avec la fonction blink ou pulse
    def Avancer(self, capteur_infrarouge, wait=0.1, est_detecter=False):
        while(not est_detecter):
            self.IN1.on()
            self.IN3.on()
            self.ENA.value = 0.3
            self.ENB.value = 0.3
            time.sleep(wait)
            if(capteur_infrarouge.gauche_actif and capteur_infrarouge.droite_actif):
                print("J'arrête")
                est_detecter = True
        time.sleep(0.2)
        self.Initialise()
        self.Tourner_90("right", capteur_infrarouge)
            
    def Est_Sur_Ligne(self, capteur_infrarouge):
        if(not capteur_infrarouge.gauche_actif):
            self.IN1.pulse(fade_in_time=0.2, fade_out_time=0.02)
            return True
        elif(not capteur_infrarouge.droite_actif):
            self.IN3.pulse(fade_in_time=0.2, fade_out_time=0.02)
            return True
        return False
        
    
    def Tourner_90(self, dir, capteur_infrarouge, est_detecter = False,  wait=1):
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
