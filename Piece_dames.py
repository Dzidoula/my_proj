#from tkinter import *
from math import *

class piece_dames():
    """ Piece de dame """
    def __init__(self,inter,x,y,fill= 'white',var = 30,tags_el=None):
        self.x ,self.y= x,y
        self.tags_el = tags_el
        self.var = var
        self.inter = inter
        self.fill = fill
        (self.A,self.B )= self.coord_piece(x,y)
        self.piece = self.inter.create_oval(self.A,self.B,fill=fill,width = 2,outline='light grey',tags = ('oval'+fill,self.tags_el+','+fill))

       # self.inter.bind()

    def coord_piece(self,x,y):
        A = (x - self.var,y - self.var)
        B = (x + self.var, y + self.var)
        return A,B

    def center_coords(self,A):
        x,y = A[0] + self.var,A[1] + self.var
        return x,y

    def change_color(self,color):
        self.inter.delete(self.piece)
        self.piece = self.inter.create_oval(self.A,self.B,fill=color,width = 2,outline='light grey',tags = ('oval',self.tags_el))


    def a_deplacement(self,x,y):
        self.inter.after(500)
        d_x = abs(x - self.x)
        d_y = abs(y - self.y)

        if self.x > x:
            d_x = -d_x

        if self.y > y:
            d_y = - d_y

        self.inter.move(self.piece, d_x, d_y)

        # Remise à niveau
        self.x = x
        self.y = y

    def destruction(self):
        self.inter.delete(self.piece)

