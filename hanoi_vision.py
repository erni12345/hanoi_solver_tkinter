'''
Le module hanoi_vision permet d'afficher un état du jeu de hanoi[tour0[],tour1[],tour2[]]
à l'aide d'une fenetre Tkinter
Ce module importe tkinter et time
'''
import tkinter as tk
import time
import random
from tkinter.constants import HORIZONTAL
class Visualisation_hanoi:
    '''
    Classe Visualisation_hanoi
    Pour construire une telle classe faire l'appel:
    v=Visualisation_hanoi(h) avec h un état du jeu de hanoi sous la forme d'une liste de 3 listes
    Par exemple, à l'initialisation:
        h=[[5,4,3,2,1],[],[]]
        v=Visualisation_hanoi(h)
    '''
    def __init__(self,hanoi=[]):
        self.visu=tk.Tk()
        self.visu.title("Les tours de Hanoï")
        self.visu.geometry("800x800")
        self.monCanvas = tk.Canvas(self.visu, width=800, height=600, bg='white')
        self.monCanvas.pack()
        self.monCanvas.create_rectangle(130,500,140,100,fill="black")
        self.monCanvas.create_rectangle(400,500,410,100,fill="black")
        self.monCanvas.create_rectangle(660,500,670,100,fill="black")
        self.monCanvas.create_rectangle(15,500,255,520,fill="black")
        self.monCanvas.create_rectangle(285,500,525,520,fill="black")
        self.monCanvas.create_rectangle(545,500,785,520,fill="black")
        self.w = tk.Scale(self.visu, from_=0, to_=10, orient=HORIZONTAL, label="Vitesse")
        self.w.pack()

        for i in range(len(hanoi)):
            centre=[135,405,665]
            for j in range(len(hanoi[i])):
                self.monCanvas.create_rectangle(centre[i]-10-10*hanoi[i][j],498-20*j,centre[i]+10+10*hanoi[i][j],502-20*j-20,fill="red")
        self.visu.update()
    def mise_a_jour(self,hanoi):
        '''
        La fonction mise_a_jour(hanoi) met à jour la fenetre tkinter créée lors de l'initialisation
        En cours de partie on peut l'utiliser ainsi si v est l'instance de la classe 
            hanoi=[[5,1] ,[3],[2,1]]
            v.mise_a_jour(hanoi)
        '''
        time.sleep(int(self.w.get())/10)
        self.monCanvas.delete("all")
        self.monCanvas.create_rectangle(130,500,140,100,fill="black")
        self.monCanvas.create_rectangle(400,500,410,100,fill="black")
        self.monCanvas.create_rectangle(660,500,670,100,fill="black")
        self.monCanvas.create_rectangle(15,500,255,520,fill="black")
        self.monCanvas.create_rectangle(285,500,525,520,fill="black")
        self.monCanvas.create_rectangle(545,500,785,520,fill="black")
        for i in range(len(hanoi)):
            centre=[135,405,665]
            for j in range(len(hanoi[i])):
                color = "%06x" % random.randint(0, 0xFFFFFF)
                self.monCanvas.create_rectangle(centre[i]-10-10*hanoi[i][j],498-20*j,centre[i]+10+10*hanoi[i][j],502-20*j-20,fill=f"#{color}")
        self.visu.update()


        