# Je présente ici l'interface de l'échiquier

from tkinter import *

class echiquier():
    def __init__(self,inter):
        self.inter = inter
        self.sq_cote = 70
        self.x1=self.y1=0
        self.x2=self.y2=self.sq_cote
        self.rect_table = []
        self.coords = []
        self.graphique()

    def graphique(self):
        color = ['tan1','chocolate1']
        ind = 0
        for elt in range(100):
            tags_el = str(self.x1 + self.sq_cote/2) + ',' + str(self.y1 + self.sq_cote/2)
            rect = self.inter.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=color[ind], outline='',
                                               tags=('rect' + '_' + color[ind], tags_el))
            if ind == 1 :
                self.coords.append([[self.x1 + self.sq_cote / 2, self.y1 + self.sq_cote / 2],''])
                self.rect_table.append(rect)
            self.x1 += self.sq_cote
            self.x2 += self.sq_cote
            ind = (ind + 1) % 2

            if (elt + 1) % 10 == 0 :
                self.x1,self.x2 = 0, self.sq_cote
                self.y1 += self.sq_cote
                self.y2 += self.sq_cote
                ind = (ind + 1) % 2

    def change_couleur_case(self,ind,color):

        self.inter.itemconfig(self.rect_table[ind],fill=color)
