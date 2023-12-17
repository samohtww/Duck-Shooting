from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
from playsound import playsound
from math import *

breedte = 1700
lengte = 300
resolutie = "1700x300"

# Gemaakt door Thom Lamens en Matthew Unterberger, voor vragen schroom niet om een berichtje te sturen.


# TO-DO (voeg iest toe als je iets gedaan wilt hebben):
# 1. Functionerend maken van Easy Ducks (mogen erg dicht bij elkaar)
# 2. Eventuele verdere verbeteringen en of opschoning (niet perse noodzakelijk)


# De tkinter mainloop die ervoor zorgt dat er verschillende frames in beeld komen
# Door de "change" functie aan te roepen verwijdert hij het huidige scherm en geeft het gekozen scherm weer.
class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = Difficulty_selector(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()

# Dit is het scherm wat de dificulty verandert, momenteel maakt hij een globale varriable die vervolgens in het game scherm gebruikt wordt voor verdere handelingen
# Handig zou zijn als dit niet via een globale variable gaat, maar dat moet nog verandert worden
class Difficulty_selector(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        master.title("Difficulty selector")
        master.geometry("300x200")
        self.status = Label(self)
        self.status.pack()
        lbl = Label(self, text='How many lanes?')
        lbl.pack()
        self.lane_amount = Entry(self)
        self.lane_amount.pack()
        lbl = Label(self, text='Enter difficulty')
        lbl.pack()
        btn = Button(self, text="Easy", command=self.Easy)
        btn.pack()
        btn = Button(self, text="Medium", command=self.Medium)
        btn.pack()
        btn = Button(self, text="Hard", command=self.Hard)
        btn.pack()

    def Easy(self, event=None):
        global number
        number = 1
        global Amount_of_lanes
        enrty_value = self.lane_amount.get()                        # Entry veld voor lanes, atm moet het een even getal zijn voor image generatie.
        try:                                                        # Als het geen getal is of er is niks ingevuld is maakt hij er automatisch 2 van.
            Amount_of_lanes = int(enrty_value)
        except:
            Amount_of_lanes = 2
        self.master.change(Game)

    def Medium(self, event=None):
        global number
        number = 2
        global Amount_of_lanes
        enrty_value = self.lane_amount.get()
        try:
            Amount_of_lanes = int(enrty_value)
        except:
            Amount_of_lanes = 2
        self.master.change(Game)

    def Hard(self, event=None):
        global number
        number = 3
        global Amount_of_lanes
        enrty_value = self.lane_amount.get()
        try:
            Amount_of_lanes = int(enrty_value)
        except:
            Amount_of_lanes = 2
        self.master.change(Game)


# Het daad werkelijke Game scherm met in de __init__: De difficulty verwerking, de keuze van de afbeeldingen en de parameters: lanes, rounds en pressed.
# Lanes gaat over de hoeveel heid banen die in gebruik zijn, rounds gaat over de hoeveelheid pijlen er per ronde geschoten worden en
# pressed gaat over hoevaak er nieuwe eendjes gegenereerd zijn, dit is voor de check_coordinates zodat hij weet dat er genoeg coordinate gegenereerd zijn.
class Game(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        master.title("Main application")
        master.geometry(resolutie)
        self.canvas = Canvas(master, width=breedte, height=lengte, background="black")
        
        if number == 1:
            imageB = "Images/Duck_easy_blue.png"
            imageR = "Images/Duck_easy_red.png"
            imageW = "Images/Duck_wrong_hard.png"
            self.breedte_image = 100
        elif number == 2:
            imageB = "Images/Duck_medium_blue.png"
            imageR = "Images/Duck_medium_red.png"
            imageW = "Images/Duck_wrong_hard.png"
            self.breedte_image = 50
        elif number == 3:
            imageB = "Images/Duck_blue_hard.png"
            imageR = "Images/Duck_red_hard.png"
            imageW = "Images/Duck_wrong_hard.png"
            self.breedte_image = 40

        self.img0 = ImageTk.PhotoImage(Image.open(imageB))
        self.img1 = ImageTk.PhotoImage(Image.open(imageR))
        self.imageW = ImageTk.PhotoImage(Image.open(imageW))

        self.rounds = 3
        self.lanes = Amount_of_lanes                                              # Door het aantal images dat momenteel in de loop staan moet dit een even getal zijn anders genereerd
        self.pressed = 0                                                          # hij 1 (of meerdere) image(s) niet en kan je niet de vorigen images zien.
        self.background = "Black"                                                 
        
        self.Wrong = 0

        self.image_list = []
        for i in range(self.lanes):                                 # Indien er meerdere afbeeldingen gebruikt willen worden moeten deze hier in de loop gezet worden, 
            self.image_list.append(self.img0)                       # anders zullen deze niet gegenereerd worden.
            self.image_list.append(self.img1)

        self.coordinates_list = []
        self.image_coordinates = []
        self.Wrong_list = []

        self.canvas.pack()
        self.master.bind("<Left>", self.Update_image)
        self.master.bind("<Up>", self.Show_previous_imgages)
        self.master.bind("<Right>", self.Auto_run)
        self.master.bind("<Down>", self.Update_color)

    def Update_color(self, event=None):
        if self.background == "Black":
            self.canvas.configure(background="Gray")
            self.background = "Gray"
        elif self.background == "Gray":
            self.canvas.configure(background="Black")
            self.background = "Black"  
    
    
    # Het automatisch laten runnen van de applicatie, momenteel geregeld door verschillende functies die de applicatie een aantal seconden laat wachten.
    # Het is geprobeerd om dit in de functie zelf toe te passen, alleen verschenen er toen geen eendjes op het scherm;
    # De coordinaten werden wel gegenereerd maar het canvas liet de plaatjes niet zien.
    def Auto_run(self, event=None):
        for i in range(3):
            for j in range(2):
                playsound('Sounds/Ping.mp3')
                self.Wait1()
            
            self.Wait5()
            self.Update_image()
            self.Wait10()
            self.canvas.delete('all')
            self.Wait2()
        self.Show_previous_imgages()

    def Wait1(self):
        var = IntVar()
        self.master.after(800, var.set, 1)
        self.master.wait_variable(var)
        
    def Wait2(self):
        var = IntVar()
        self.master.after(2000, var.set, 1)
        self.master.wait_variable(var)

    def Wait5(self):
        var = IntVar()
        self.master.after(5000, var.set, 1)
        self.master.wait_variable(var)

    def Wait10(self):
        var = IntVar()
        self.master.after(10000, var.set, 1)
        self.master.wait_variable(var)


    # Hier worden de coordinaten berekent, deze worden vervolgens gechekt op dat de coordinaten niet in de buurt van elkaar zijn om vervolgens in een lijst geappend te worden.
    # De coordinaten worden overigens via de random functie gegenereerd, de random functie heeft verschillende parameters die ervoor zorgen dat de coordinaten binnen het scherm vallen.
    def Get_coordinates(self, event=None):
        self.lane_number = 0
        for i in range(self.lanes):
            self.lane_number += 1
            x = random.randint(((breedte-self.breedte_image)//self.lanes)*(i)+10,(((breedte-self.breedte_image)//self.lanes)*(i+1)-10))
            y = random.randint(0,(lengte-self.breedte_image))
        
            self.coordinates_list.append([x,y])
            self.Check_coordinates()
            self.Check_doubles()

            self.No_shoot(i)

    # Kijkt op basis van een kans of er een decoy eend moet worden gegenereerd, momenteel is de kan 1 op 5 dat dit gebeurt.
    def No_shoot(self, i):
        if random.randint(0,100) < 50:
            x = random.randint(((breedte-self.breedte_image)//self.lanes)*(i)+10,(((breedte-self.breedte_image)//self.lanes)*(i+1)-10))
            y = random.randint(0,(lengte-self.breedte_image))

            self.Wrong = 1
            self.coordinates_list.append([x,y])
            self.Check_coordinates()
            self.Wrong = 0
        
        else: 
            self.Wrong_list.append([0,4000])                                                                 # Dit is zo omdat bij het genereren van de plaatjes hij over een lijst heen moet loopen die voldoende gevuld is.

    # Het checken van coordinaten gebaseerd op de euclidean disctance (de hemelsbreedte afstand tussen de punten).
    def Check_coordinates(self):
        for i in range(len(self.coordinates_list)-1):
            if sqrt(((self.coordinates_list[i][0]-self.coordinates_list[-1][0])**2)+((self.coordinates_list[i][1]-self.coordinates_list[-1][1])**2)) < self.breedte_image:
                self.coordinates_list = self.coordinates_list[:-1]
                self.New_coordinates_calculation()
        self.Update_lists()

    # Voegt de juiste coordinaten in de juiste lijst voor verder gebruik
    def Update_lists(self):
        if self.Wrong == 0:
            self.image_coordinates.append(self.coordinates_list[-1])
            self.Check_doubles()
        elif self.Wrong == 1:
            self.Wrong_list.append(self.coordinates_list[-1])
            self.Check_doubles()

    # Controleerd of de laatste en de op 1 na laatste hetzelfde zijn, en halen deze weg als het zo is.
    def Check_doubles(self):
        try:
            if self.image_coordinates[-2] == self.image_coordinates[-1]:
                self.image_coordinates = self.image_coordinates[:-1]
        except IndexError:
            pass
        
        try:
            if self.Wrong_list[-1] != [0,4000]:
                if self.Wrong_list[-2] == self.Wrong_list[-1]:
                    self.Wrong_list = self.Wrong_list[:-1]
        except IndexError:
            pass

    # Als hij binnen de euclidean disctance zit wordt doormiddel van deze functie een nieuw coordinaat gegenereerd.
    # De functie houd rekening met in welke lane het coordinaat moet komen.
    def New_coordinates_calculation(self):
        x = random.randint(((breedte-self.breedte_image)//self.lanes)*(self.lane_number-1),(((breedte-self.breedte_image)//self.lanes)*self.lane_number))
        y = random.randint(0,(lengte-self.breedte_image))

        self.coordinates_list.append([x,y])
        self.Check_coordinates()

    # Deze functie checked of er genoeg coordinaten gegenereerd zijn om alles goed weer te kunnen geven.
    # Om deze scalable te maken wordt er gekeken naar de aantal lanes en hoeveel er op de update_image knop wordt geklikt.
             

    # De functie die de daadwerkelijke plaatjes plaatst op het canvas en het canvas opschoont van vorige eendjes. 
    # De x en y coordinaten worden uit de lijst van lijsten gehaald om vervolgens omgezet te worden naar een xy coordinaat.
    # Handig om even te kijken of het via sets kan (misschien sneller gezien het waarschijnlijk een lagere groteO heeft),
    # GroteO is de complexiteit van algorithmes.
    def Update_image(self, event=None):
        self.canvas.delete('all')
        self.pressed += 1
        self.Get_coordinates()
        
        self.canvas.configure(background="black")
        self.background = "Black"

        # print(self.coordinates_list)
        print(self.Wrong_list)
        print(self.image_coordinates)

        x = 0
        for j in range(self.lanes):
            x -= 1
            self.canvas.create_image(self.image_coordinates[x][0],self.image_coordinates[x][1],anchor=NW,image=self.image_list[j])
            self.canvas.create_image(self.Wrong_list[x][0],self.Wrong_list[x][1],anchor=NW,image=self.imageW)
        

    # Deze functie laat doormiddel van een loop de voorgaande plaatjes zien, momenteel staat de "rounds" op 3 (gezien er 3 pijlen per ronden geschoten worden).
    # Daarnaast wordt er ook rekening gehouden met de hoeveelheid lanes in de 2de loop.
    def Show_previous_imgages(self, event=None):
        x = 0
        for i in range(self.rounds):
            for j in range(self.lanes):
                x -= 1
                self.canvas.create_image(self.image_coordinates[x][0],self.image_coordinates[x][1],anchor=NW,image=self.image_list[j])
                self.canvas.create_image(self.Wrong_list[x][0],self.Wrong_list[x][1],anchor=NW,image=self.imageW)
        
        self.coordinates_list.clear()                               # Resetten van de lijsten zodat hij niet te veel opslaat, indien dit niet gedaan wordt kan hij uiteindelijk geen nieuwe coordinaten meer vinden en genereren
        self.image_coordinates.clear()
        self.Wrong_list.clear()
        self.pressed = 0


if __name__=="__main__":
    app=MainApp()
    app.mainloop()