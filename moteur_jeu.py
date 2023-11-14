from tkinter import *

class Case():
    def __init__(self,tk,long_larg,color,emp=[0,0]):
        self.tk = tk
        self.long_larg = long_larg
        self.emp = emp
        self.color = color
        self.case = Canvas(self.tk,width=self.long_larg[0],height = self.long_larg[1],bg=self.color,borderwidth=0,)
        self.case.grid(row=self.emp[0],column=self.emp[1],rowspan=None)




class App():

    def __init__(self):
        self.root = Tk()
        self.table_case = []
        self.long_larg = [70]*2

        couleur = ['tan1','chocolate1']
        ind_color = 0
        emp1,emp2 = 0,0
        case = Case(self.root, self.long_larg, color=couleur[ind_color], emp=[emp1, emp2])
        for elt in range(100):
            case = Case(self,self.long_larg,color=couleur[ind_color],emp=[emp1,emp2])
            self.table_case.append(case)
            ind_color = (ind_color+1)%2
            emp2+=1
            if (elt + 1)% 10 == 0:
                emp1+=1
                emp2 = 0
        self.root.mainloop()


root = Tk()
table_case = []
long_larg = [70]*2

couleur = ['tan1','chocolate1']
ind_color = 0
emp1,emp2 = 0,0
#case = Case(root, long_larg, color=couleur[ind_color], emp=[emp1, emp2])
for elt in range(100):
    case = Case(root,long_larg,color=couleur[ind_color],emp=[emp1,emp2])
    table_case.append(case)
    ind_color = (ind_color+1)%2
    emp2+=1
    if (elt + 1)% 10 == 0:
        emp1+=1
        emp2 = 0
        ind_color = (ind_color + 1) % 2


root.mainloop()
