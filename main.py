from tkinter import *
from Piece_dames import piece_dames
from Echiquier import echiquier
from random import randint


root = Tk()
#root.overrideredirect()
canvas = Canvas(root,width=700,height=700,bg= 'grey',borderwidth=0)
canvas.grid(rowspan = 2,column= 0)

cv1 = Canvas(root,width=200,height=350,bg='white')
cv1.grid(row = 0,column=1)
cv2 = Canvas(root,width=200,height=350,bg='black')
cv2.grid(row = 1,column=1)



echic = echiquier(canvas)
table_coords = echic.coords
pions_blancs = []
pions_noirs = []
mon_tour = 'black'
tab_mon_tour = ['ovalblack','ovalwhite']
ind_mon_tour = 0
point_noir = 0
point_blanc = 0


i=0
for elt in table_coords:
    (x, y) = elt[0]
    piece = piece_dames(canvas,x,y,tags_el=str(i))
    pions_blancs.append(piece)
    table_coords[table_coords.index(elt)][1] = piece
    i+=1
    if i == 20:
        break

i=0
for elt in list(reversed(table_coords)):
    (x, y)= elt[0]
    piece = piece_dames(canvas,x,y,fill='black',tags_el=str(i))
    pions_noirs.append(piece)
    table_coords[table_coords.index(elt)][1] = piece
    i+=1
    if i == 20:
        break


#print(table_coords)
# Pour le déplacement d'un pion
enr_clics = [0,0]
ind_enr_clics = 0




def coords (arg):
    """ Les coordonnées de la case correspondant au pion dessus"""
    if arg[0][1] == 'black':
        for elt in table_coords:
            if pions_noirs[int(arg[0][0])] == elt[1] :
                return elt[0]

    elif arg[0][1] == 'white':
        for elt in table_coords:
            if pions_blancs[int(arg[0][0])] == elt[1] :
                return elt[0]

def up_date_table_coords(arg):
    """ Remettre à niveau le tableau de coords"""
    global table_coords,pions_noirs,pions_blancs
    #coords_oval, coords_npoint = coords(arg),arg[1]

    if arg[0][1] == 'black':
        for elt in table_coords:
            if pions_noirs[int(arg[0][0])] == elt[1] :
                table_coords[table_coords.index(elt)] = [elt[0],'']
            if arg[1] == elt[0]:
                table_coords[table_coords.index(elt)] = [elt[0], pions_noirs[int(arg[0][0])]]

    else :

        for elt in table_coords:

            if pions_blancs[int(arg[0][0])] == elt[1]:
                table_coords[table_coords.index(elt)] = [elt[0], '']

            if arg[1] == elt[0]:
                table_coords[table_coords.index(elt)] = [elt[0], pions_blancs[int(arg[0][0])]]




def case_vide(coords,vecteur,nature = 'pion'):
    global table_coords
    case_vide = []
    # Points appartenants à la diagonales selon l'échiquier
    i = 1
    while True:
        point =[coords[j] + i*vecteur[j] for j in range(2) if (coords[j] + i*vecteur[j]) > 0 and (coords[j] + i*vecteur[j]) < 700  ]
        i = i + 1
        if len(point) == 2:
            case_vide.append([point,''])
        else:
            break



    #cases au dessus desquelles il n'y a pas de pions
    n_case = len(case_vide)
    for case in range(n_case):
        for elt in table_coords:
            if case_vide[case][0] == elt[0] and elt[1] == '':
                case_vide[case][1] = 'v' # v pour dire valide


    # cases valides selon la nature du pion
    if nature == 'pion':
        for i in range(n_case):
            if i == 0:
                if case_vide[i][1] == 'v':
                    return [case_vide[i][0],'r',0] # Aucun gain
            elif i == 1:
                if case_vide[i][1] == 'v':
                    # Vérifions s'il y a un gain
                    for elt in table_coords:
                        if elt[0] == case_vide[0][0] and elt[1].fill != mon_tour:
                            print(elt[1].fill)
                            return [case_vide[i][0],'g',elt] # Gain
            else:
                return []


def control_gain(g_r):
    global mon_tour,point_noir,point_blanc

    # Partie Score
    if mon_tour == 'black' and g_r == 'g':
        point_noir += 1
        cv2.configure(bg='green')
    elif mon_tour == 'white' and g_r == 'g':
        point_blanc += 1

    print(point_blanc,'   ',point_noir)

def pion_a_detruire(pion_emp):
    global table_coords
    # Partie pion à détruire
    if pion_emp != 0:
        pion_emp[1].destruction()
        table_coords[table_coords.index(pion_emp)] = [pion_emp[0],'']
    return





def verif(arg):
    """ Vérifions si le pion veut suivre une diagonale en avant"""
    coords_oval = coords(arg)
    coords_npoint = arg[1]
    cases_possibles = []

    # Les cases possibles dans lesquelles le pion peut se diriger
    # 70 est le sq_cote de échiquier
    # Definissons deux vecteurs ( u et u_p) pour le déplacement des blancs et deux autres (v et v_p) pour le déplacements des noirs
    sq_cote = 70
    u,u_p = [sq_cote,sq_cote],[-sq_cote,sq_cote]
    v,v_p = [-sq_cote,-sq_cote],[sq_cote,-sq_cote]
    # Pour les noirs
    if arg[0][1] == 'black':
        # Déterminons d'abords les cases vides suivant les diagonales valides

        for vect in [v,v_p]:
            if case_vide(coords_oval,vect,nature='pion') != []:
                cases_possibles.append(case_vide(coords_oval,vect,nature='pion'))
    else:

        for vect in [u,u_p]:
            if case_vide(coords_oval,vect,nature='pion') != []:
                cases_possibles.append(case_vide(coords_oval,vect,nature='pion'))

    cases_possibles = [elt for elt in cases_possibles if elt != None]
    if coords_npoint in [elt[0] for elt in cases_possibles ]: # Vérification
        up_date_table_coords(arg)
        print([[control_gain(elt[1]),pion_a_detruire(elt[2])] for elt in cases_possibles if elt[0] == coords_npoint],mon_tour)
        return True
    else:
        return False

def gest_echic_color(arg,color):
    # Déterminer l'indice de la piece dans table_coords
    for i in range(len(table_coords)):
        if arg[0][1] == 'black':
            if table_coords[i][1] == pions_noirs[int(arg[0][0])]:
                echic.change_couleur_case(i, color)
                break

        if arg[0][1] == 'white' :
            if table_coords[i][1] == pions_blancs[int(arg[0][0])]:
                echic.change_couleur_case(i, color)
                break





def affiche_tags(event):

    global ind_enr_clics,enr_clics,mon_tour,ind_mon_tour
    objet_clic = canvas.find_closest(event.x,event.y)

    if objet_clic:
        tags = canvas.gettags(objet_clic)
        proche = canvas.find_above(objet_clic)
        #print(proche,canvas.find_below(objet_clic))

        if ind_enr_clics == 0 and tags[0] == tab_mon_tour[ind_mon_tour]:
            enr_clics[ind_enr_clics] = [i for i in tags[1].split(',')]
            gest_echic_color(enr_clics,'green')
            print(tags)
            ind_enr_clics = 1
        elif ind_enr_clics == 1 and tags[0] == 'rect_chocolate1':

            enr_clics[ind_enr_clics] = [int(i[:-2]) for i in tags[1].split(',') ]
            print(tags)
            ind_enr_clics = 0
            print(enr_clics)
            mon_tour = enr_clics[0][1]
            gest_echic_color(enr_clics, 'chocolate1')

            # Déplacement de pion
            if verif(enr_clics):
                if enr_clics[0][1] == 'black':
                    pions_noirs[int(enr_clics[0][0])].a_deplacement(enr_clics[1][0], enr_clics[1][1])
                    ind_mon_tour = (ind_mon_tour + 1) % 2

                else:
                    pions_blancs[int(enr_clics[0][0])].a_deplacement(enr_clics[1][0], enr_clics[1][1])
                    ind_mon_tour = (ind_mon_tour + 1) % 2

canvas.bind('<Button-1>',affiche_tags)

"""
"""
root.mainloop()
