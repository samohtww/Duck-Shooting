from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
from playsound import playsound
from math import *

breedte = 1700
lengte = 300
resolutie = "1700x300"

# De tkinter mainloop die ervoor zorgt dat er verschillende frames in beeld komen
# Door de change functie aan te roepen verwijdert hij het huidige scherm en maakt hij een nieuwe
class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = Difficulty_selector(self)
        self.frame.pack()

    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack()

# Dit is het scherm wat de dificulty verandert momenteel maakt hij een nummer globaal die vervolgens in het game scherm gebruikt wordt voor verdere handelingen
# Handig zou zijn als dit niet via een globale variable gaat in de toekomst maar dat moet nog verandert worden
class Difficulty_selector(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)

        master.title("Difficulty selector")
        master.geometry("300x200")
        self.status = Label(self)
        self.status.pack()
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
        self.master.change(Game)

    def Medium(self, event=None):
        global number
        number = 2
        self.master.change(Game)

    def Hard(self, event=None):
        global number
        number = 3
        self.master.change(Game)


# Het daad werkelijke Game scherm met in de __init__ de difficulty verwerking voor de keuze van de afbeeldingen
class Game(Frame):
    def __init__(self, master=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        master.title("Main application")
        master.geometry(resolutie)
        self.canvas = Canvas(master, width=breedte, height=lengte, background="black")
        
        if number == 1:
            self.imageB = "Images/Duck_easy_blue.png"
            self.imageR = "Images/Duck_easy_red.png"
            self.breedte_image = 200
        elif number == 2:
            self.imageB = "Images/Duck_medium_blue.png"
            self.imageR = "Images/Duck_medium_red.png"
            self.breedte_image = 100
        elif number == 3:
            self.imageB = "Images/Duck_blue_hard.png"
            self.imageR = "Images/Duck_red_hard.png"
            self.breedte_image = 40

        self.img0 = ImageTk.PhotoImage(Image.open(self.imageB))
        self.img1 = ImageTk.PhotoImage(Image.open(self.imageR))
        self.rounds = 25
        self.lanes = 2
        self.pressed = 0

        self.image_list = []
        self.image_list.append(self.img0)
        self.image_list.append(self.img1)

        self.coordinates_list = [[0,0]]

        self.canvas.pack()
        self.master.bind("<Left>", self.Update_image)
        self.master.bind("<Up>", self.Show_previous_imgages)
        self.master.bind("<Right>", self.Auto_run)

# Het automatisch laten runnen van de applicatie, momenteel geregeld door verschillende functies die de applicatie een aantal seconden laat wachten
# Het is geprobeerd om dit in de functie zelf toe te passen alleen verschenen er toen geen eendjes op het scherm, de coordinaten werden wel gegenereerd maar het canvas liet de plaatjes niet zien.
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


# Hier worden de coordinaten berekent, deze worden vervolgens gechekt op dat de coordinaten niet in de buurt van elkaar zijn om vervolgens in een lijst geappend te worden
# De coordinaten worden overigens via de random functie gegenereerd, de random functie heeft verschillende parameters die ervoor zorgen dat de coordinaten binnen het scherm vallen
    def Get_coordinates(self, event=None):
        while self.Check_corodinate_quantitiy() == False:
            x = random.randint(0, breedte-self.breedte_image)
            # x = random.randint(((breedte-self.breedte_image)//self.lanes)*(i-1),(((breedte-self.breedte_image)//self.lanes)*i))
            y = random.randint(0,(lengte-self.breedte_image))
            
            self.coordinates_list.append([x,y])
            print(self.coordinates_list)
            self.Check_coordinates()
            

# Het checken van coordinaten gebaseerd op de eucidean disctance (de hemelsbreedte afstand tussen de punten)
    def Check_coordinates(self):
        for i in range(len(self.coordinates_list)-1):
            if sqrt(((self.coordinates_list[i][0]-self.coordinates_list[-1][0])**2)+((self.coordinates_list[i][1]-self.coordinates_list[-1][1])**2)) < self.breedte_image:
                self.coordinates_list = self.coordinates_list[:-1]

    def Check_corodinate_quantitiy(self):
        if (len(self.coordinates_list)-1) > (self.lanes*self.pressed):
            return True
        else:
            return False   

# De functie die de daadwerkelijke plaatjes plaatst op het canvas en het canvas opschoont van vorige eendjes. 
# De losse x en y coordinaten worden uit de lijsten gehaald om vervolgens samen gevoegd te worden tot 1 x en y coordinaat  
    def Update_image(self, event=None):
        self.canvas.delete('all')
        self.pressed += 1
        self.Get_coordinates()
        
        x = 0
        for j in range(self.lanes):
            x -= 1
            self.canvas.create_image(self.coordinates_list[x][0],self.coordinates_list[x][1],anchor=NW,image=self.image_list[j])
        

# Deze functie laat doormiddel van een loop de voorgaande plaatjes zien, momenteel staat de "rounds" op 3 (gezien er 3 pijlen per ronden geschoten worden)
# Daarnaast wordt er ook rekening gehouden met de hoeveelheid lanes in de 2de for loop
    def Show_previous_imgages(self, event=None):
        x = 0
        for i in range(self.rounds):
            for j in range(self.lanes):
                x -= 1
                self.canvas.create_image(self.coordinates_list[x][0],self.coordinates_list[x][1],anchor=NW,image=self.image_list[j])


if __name__=="__main__":
    app=MainApp()
    app.mainloop()