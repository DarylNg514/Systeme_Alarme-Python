
from gpiozero import LED, Button as GpioButton
from time import sleep
from tkinter import*
import threading
from flask import Flask, request
import requests

app = Flask(__name__)
machine_ip = "10.1.10.121"

endpoint = f"http://{machine_ip}:8000/receive_zones_data"

class SystemAlarm :

    systemStatus = 0
    EtatZone1="OFF"
    EtatZone2="OFF"
    EtatZone3="OFF"
    EtatZone4="OFF"
    
    def __init__(self,root):
		
                self.sega = LED(8)
                self.segb = LED(9)
                self.segc = LED(10)
                self.segd = LED(11)
                self.sege = LED(12)
                self.segf = LED(13)
                self.segg = LED(17)
                self.segdp = LED(20)
                self.lamp = LED(16)
                self.btn1 = GpioButton(27)
                self.btn2 = GpioButton(22)
                self.btn3 = GpioButton(5)
                self.btn4 = GpioButton(6)	
                self.btn5 = GpioButton(19)

                self.tk=root
                self.lbltitle = Label(self.tk,text="Alarms")
                self.lbltitle.grid(row=0,column=0, columnspan=2)
                self.lblzone1 = Label(self.tk,text="Z1",background="white")
                self.lblzone1.grid(row=1,column=0)
                self.lblzone2 = Label(self.tk,text="Z2",background="white")
                self.lblzone2.grid(row=1,column=1)
                self.lblzone3 = Label(self.tk,text="Z3",background="white")
                self.lblzone3.grid(row=2,column=0)
                self.lblzone4 = Label(self.tk,text="Z4",background="white")
                self.lblzone4.grid(row=2,column=1)
                self.lblStatus = Label(self.tk,text="Status")
                self.lblStatus.grid(row=3,column=0, columnspan=2)
                self.lbloN = Label(self.tk,text="ON",background="white")
                self.lbloN.grid(row=4,column=0)
                self.lbloFF = Label(self.tk,text="OFF",background="white")
                self.lbloFF.grid(row=4,column=1)
                self.btnAct=Button(self.tk,text="Activate",command=lambda:self.activate())
                self.btnAct.grid(row=5,column=0)
                self.btnDes=Button(self.tk,text="DeActivate",command=lambda:self.deactivate())
                self.btnDes.grid(row=5,column=1)
                self.btnRes=Button(self.tk,text="Reset",command=lambda:self.Reset())
                self.btnRes.grid(row=6,column=0,columnspan=2)

                self.show0()
                # Définissez les actions des boutons GPIO ici
                self.btn1.when_pressed = lambda: self.activate() if self.systemStatus == 0 else self.deactivate()
                self.btn2.when_pressed = lambda: self.Z1() if self.systemStatus == 1 else None
                self.btn3.when_pressed = lambda: self.Z2() if self.systemStatus == 1 else None
                self.btn4.when_pressed = lambda: self.Z3() if self.systemStatus == 1 else None
                self.btn5.when_pressed = lambda: self.Z4() if self.systemStatus == 1 else None

              

                self.tk.mainloop()
                

    def activate(self):
        self.lbloN.config(background="red")
        self.lbloFF.config(background="white")
        if self.systemStatus == 0:
            self.cout_up()
            # Lancer la fonction cliniot dans un autre thread
            thread2 = threading.Thread(target=self.cliniot)
            thread2.start()

    def deactivate(self):
        self.lbloFF.config(background="red")
        self.lbloN.config(background="white")
        self.lblzone1.config(background="white")
        self.lblzone2.config(background="white")
        self.lblzone3.config(background="white")
        self.lblzone4.config(background="white")
        self.EtatZone1="OFF"
        self.EtatZone2="OFF"
        self.EtatZone3="OFF"
        self.EtatZone4="OFF"
        if self.systemStatus == 1:
            self.cout_down()


    def show0(self):
    #0
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.on()
        self.segdp.on()
    

    def show1(self):

        #1
        self.sega.on()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.on()
        self.segg.on()
        self.segdp.on()


    def show2(self):

        #2
        self.sega.off()
        self.segb.off()
        self.segc.on()
        self.segd.off()
        self.sege.off()
        self.segf.on()
        self.segg.off()
        self.segdp.on()  
        

    def show3(self):

        #3
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.on()
        self.segf.on()
        self.segg.off()
        self.segdp.on() 


    def show4(self):

        #4
        self.sega.on()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.off()
        self.segg.off()
        self.segdp.on() 


    def show5(self):
        #5
        self.sega.off()
        self.segb.on()
        self.segc.off()
        self.segd.off()
        self.sege.on()
        self.segf.off()
        self.segg.off()
        self.segdp.on()  
    

    def show6(self):
        #6
        self.sega.off()
        self.segb.on()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.off()
        self.segdp.on() 


    def show7(self):
        #7
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.on()
        self.segg.on()
        self.segdp.on()     



    def show8(self):
        #8
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.off()
        self.sege.off()
        self.segf.off()
        self.segg.off()
        self.segdp.on()  


    def show9(self):
        #9
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.on()
        self.segf.off()
        self.segg.off()
        self.segdp.on()    



    def showA(self):
        #A
        self.sega.off()
        self.segb.off()
        self.segc.off()
        self.segd.on()
        self.sege.off()
        self.segf.off()
        self.segg.off()
        
    def lampON(self):
        self.lamp.off()
        
        
        
    def lampOFF(self):
        self.lamp.on()
        
        
    def showpoint(self):
        self.segdp.off()
        
    def showNopoint(self):
        self.segdp.on()
        
    def cliniot(self):
        # Fonction de clignotement encapsulée dans un thread
        def cliniot_thread():
            while self.systemStatus == 1:
                self.showpoint()
                sleep(0.5)
                self.showNopoint()
                sleep(0.5)
        
        thread = threading.Thread(target=cliniot_thread)
        thread.start()
    

    def cout_up(self):
        #0
        self.show0()
        sleep(1)

        #1
        self.show1()    
        sleep(1)

        #2
        self.show2() 
        sleep(1)

        #3
        self.show3()  
        sleep(1)
            
        #4
        self.show4()
        sleep(1)

        #5
        self.show5()
        sleep(1)

        #6
        self.show6() 
        sleep(1)

        #7
        self.show7() 
        sleep(1)


        #8
        self.show8()  
        sleep(1)


        #9
        self.show9()
        sleep(1)

        #0
        self.showA()
        self.systemStatus = 1



    def cout_down(self):

        #9
        self.show9    
        sleep(1)

        #8
        self.show8()  
        sleep(1)

        #7
        self.show7()   
        sleep(1)

        #6
        self.show6()  
        sleep(1)

        #5
        self.show5() 
        sleep(1)

        #4
        self.show4()  
        sleep(1)

        #3
        self.show3()    
        sleep(1)

        #2
        self.show2()  
        sleep(1)

        #1
        self.show1()    
        sleep(1)
        
        #0
        self.show0()
        sleep(1)

        self.show0()
        self.systemStatus = 0
    def Reset(self):
        self.systemStatus = 0
        self.lbloFF.config(background="white")
        self.lbloN.config(background="white")
        self.lblzone1.config(background="white")
        self.lblzone2.config(background="white")
        self.lblzone3.config(background="white")
        self.lblzone4.config(background="white")
        self.EtatZone1="OFF"
        self.EtatZone2="OFF"
        self.EtatZone3="OFF"
        self.EtatZone4="OFF"
        self.showA()


    def Z1(self):
        self.lblzone1.config(background="red")
        self.lblzone2.config(background="white")
        self.lblzone3.config(background="white")
        self.lblzone4.config(background="white")
        self.show1()
        self.EtatZone1="ON"
        self.EtatZone2="OFF"
        self.EtatZone3="OFF"
        self.EtatZone4="OFF"
        self.send_data(self.EtatZone1,self.EtatZone2,self.EtatZone3,self.EtatZone4)

    def Z2(self):
        self.lblzone1.config(background="white")
        self.lblzone2.config(background="red")
        self.lblzone3.config(background="white")
        self.lblzone4.config(background="white")
        self.show2()
        self.EtatZone2="ON"
        self.EtatZone1="OFF"
        self.EtatZone3="OFF"
        self.EtatZone4="OFF"
        self.send_data(self.EtatZone1,self.EtatZone2,self.EtatZone3,self.EtatZone4)

    def Z3(self):
        self.lblzone1.config(background="white")
        self.lblzone2.config(background="white")
        self.lblzone3.config(background="red")
        self.lblzone4.config(background="white")
        self.show3()
        self.EtatZone3="ON"
        self.EtatZone2="OFF"
        self.EtatZone1="OFF"
        self.EtatZone4="OFF"
        self.send_data(self.EtatZone1,self.EtatZone2,self.EtatZone3,self.EtatZone4)

    def Z4(self):
        self.lblzone1.config(background="white")
        self.lblzone2.config(background="white")
        self.lblzone3.config(background="white")
        self.lblzone4.config(background="red")
        self.show4()
        self.EtatZone4="ON"
        self.EtatZone2="OFF"
        self.EtatZone3="OFF"
        self.EtatZone1="OFF"
        self.send_data(self.EtatZone1,self.EtatZone2,self.EtatZone3,self.EtatZone4)

    def send_data(self,Zone1,Zone2,Zone3,Zone4):
        machine_ip = "10.1.10.121"

        endpoint = f"http://{machine_ip}:8000/receive_zones_data"

        zones_data = {
            "Zone1": Zone1,
            "Zone2": Zone2,
            "Zone3": Zone3,
            "Zone4": Zone4
        }

        try:
            response = requests.post(endpoint, json=zones_data)
            response.raise_for_status()
            print("Donnees envoyees avec succes e la machine.")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'envoi des donnees e la machine : {e}")
 

    
r=Tk()
sys = SystemAlarm(r)


