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
        self.Initialise()


    
    def Avancer(self):
        print('avancer')
        self.IN1.on()
        self.IN3.on()
        self.ENA.value = 0.5
        self.ENB.value = 0.5
            
                     
    def main(self, est_detecter=False):
        while (not est_detecter):
            self.Avancer()
            
            if(self.capteur_infrarouge.gauche_actif and self.capteur_infrarouge.droite_actif):
                print("J'arrête")
                est_detecter = True
            if(self.capteur_infrarouge.gauche_actif and not self.capteur_infrarouge.droite_actif):
                self.Correction("gauche")
            if(not self.capteur_infrarouge.gauche_actif and self.capteur_infrarouge.droite_actif):
                self.Correction("droite")
            

    def Correction(self, dir):
        if(dir == "gauche"):
            print("correction gauche")
            #while(capteur_infrarouge.gauche_actif):
            #self.IN1.off()
            self.ENA.value = 0.2
            self.ENB.value = 0.8
                #self.IN2.on()
        elif(dir == "droite"):
            print("correction droite")
            #while(capteur_infrarouge.droite_actif):  
            #self.IN3.off()
            self.ENA.value = 0.8
            self.ENB.value = 0.2
            #self.IN4.on()
            
        
    
    def Tourner(self, dir, capteur_infrarouge, est_detecter = False,  wait=0.78):
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
