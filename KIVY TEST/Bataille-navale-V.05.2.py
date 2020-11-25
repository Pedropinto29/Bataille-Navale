import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.window import WindowBase
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
import random , glob
import json


# LabelBase.register(name='bright_young_things',fn_regular='Bright Young Things.ttf')
puncte=0


# on definit un ScreenManager au debut ! 
sm = ScreenManager()
#Variable global qui n'esdt pas propre a une classe , donc je peux utiliser dans tout le code


#Ecran d'acueuille 
class MenuScreen(Screen):
    def build(self):
        self.name='Menu'
        self.add_widget(Image(source='Battle.jpeg', allow_stretch=True , keep_ratio= False))
        Menu_Layout=BoxLayout(padding=100,spacing=80,orientation='vertical')

        #Bouton Play 
        self.Bouton_play = Button(text='SINGLEPLAYER')
        self.Bouton_play.font_size= Window.size[0]*0.05
        self.Bouton_play.background_color=[0,0,0,0.5]
        self.Bouton_play.bind(on_press=self._play)
        Menu_Layout.add_widget(self.Bouton_play)

        #Bouton Multiplayer
        self.bouton_multiplayer = Button(text="MULTIPLAYER")
        self.bouton_multiplayer.font_size = Window.size[0]*0.05
        self.bouton_multiplayer.background_color = [0,0,0,0.5]
        self.bouton_multiplayer.bind(on_press = self._multiplayer)
        Menu_Layout.add_widget(self.bouton_multiplayer)

        #Bouton Quitter 
        self.Bouton_quitter = Button(text='QUITTER LE JEU')
        self.Bouton_quitter.font_size= Window.size[0]*0.05
        self.Bouton_quitter.background_color=[0,0,0,0.5]
        self.Bouton_quitter.bind(on_press=self._Quitter)
        Menu_Layout.add_widget(self.Bouton_quitter)
        #Pour appeler box , on met pas return pour pas faire une boucle
        self.add_widget(Menu_Layout)
        #Definir un fonction pour le bouton PLAY
    def _play(self ,src):
        game = GridGameScreen()
        game.build()
        sm.add_widget(game)
        sm.current='Game'
        sm.transition.direction = "left"

    def _multiplayer(self,src):
        multijoueur = Two_players_Screen()
        multijoueur.build()
        sm.add_widget(multijoueur)
        sm.current = 'multiplayer'
        sm.transition.direction = "left"
        
        #Definir un fonction pour le bouton Quitter 
    def _Quitter(self,src):
        # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()



#*****************************************************************CLASSE POUR 1 JOUEUR**********************************************************************

    #Classe pour le jeu
class GridGameScreen(Screen):
    def build(self):
        self.name = 'Game'
        self.add_widget(Image(source='fond du jeu.jpg', allow_stretch=True , keep_ratio= False))
        
      
        self.essai = 0 
        self.touche = 0
        self.touche_torpi =0
        self.touche_croizeur =0
        self.touche_sousmarin =0
        self.touche_porteavion =0
####RANDOM
        # a= ['c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier.txt','c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier_2.txt',

        # 'c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier_3.txt','c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier_4.txt']

        pattern = "C:\\Users\\pedro\\Desktop\\KIVY TEST\\Bateaux\\*.txt"    #etoile pour afficher pour ce qui est du text
        b=random.choice(glob.glob(pattern))
        # print(glob.glob(pattern))
## On ouvre le fichier et on definit la position avec une liste vite
        with open (b,'rt') as f:
            self.pos_sous_marin = []
            self.pos_croiseur = []
            self.pos_porte_avion = []
            self.pos_torpilleur = []
            self.output = ""
            matrice = []
## Declaration de noms pour les bato
            sous_marin= "s"
            croiseur="c"
            porte_avion = "p"
            torpilleur = "t"
## Parcours le fichier et supprime les espaces
            fichier = f.readlines()
            for line in fichier:
                effacer_espace = line.rstrip()
                matrice.append(list(effacer_espace))
            print(matrice)
## Parcours la liste pour determiner la position des sous Marin
            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in sous_marin:
                        position  =([(ligne),(col)])   # determine la position des sous marin
                        self.pos_sous_marin.append(position)
            print("positions des sous marins:",self.pos_sous_marin)
## Parcours la liste pour determiner la position des croiseurs
            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in croiseur:
                        position  =([(ligne),(col)])
                        self.pos_croiseur.append(position)
            print("positions des croisseur:",self.pos_croiseur)
## Parcours la liste pour determiner la position des portes avions
            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in porte_avion:
                        position  =([(ligne),(col)])
                        self.pos_porte_avion.append(position)
            print("positions des porte avions:",self.pos_porte_avion)
## Parcours la liste pour determiner la position des torpilleur
            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in torpilleur:
                        position  =([(ligne),(col)])
                        self.pos_torpilleur.append(position)
            print("positions des torpilleur:",self.pos_torpilleur)

#**********************************************       INTERFACE DU JEU           **************************************************************

        self.title = 'Bataille'
        boite_message = BoxLayout(orientation= 'vertical',spacing=2)
        grid = GridLayout(rows=12 , cols = 11,padding=15,spacing= 3)
        grid.add_widget(Label(text='SINGLE \nPLAYER'))

#Grille pour afficher les chiffres
        for col in range(1,11):
            grid.add_widget(Label(text=str(col)))
#Grille pour afficher les lettre de A-->J + Button 
        Lettre = ['A','B','C','D','E','F','G','H','I','J']
        for A_to_J in range(len(Lettre)):
            grid.add_widget(Label(text=str(Lettre[A_to_J])))
            for col in range(10):
                a = [(A_to_J +1),(col+1)]
                btn = Button(text="",id=str(a))
                # on assigne a chaque bouton la fonction _message
                btn.bind(on_press=self._message)
                grid.add_widget(btn)
        #Ecran separe pour afficher text 'touché , coulé , vous avez gagnez ,perdu etc...
        self.output= Label(font_size='30sp',size_hint_y=0.1,bold=True,color=(1,0,0,10))
        boite_message.add_widget(grid)
        boite_message.add_widget(self.output)
        
        
        self.add_widget(boite_message)

#Creation de la fonction qui permet d'informer et cliquer sur chaque bato
    def _message(self, src):
#Fonction qui afficher si on a touché le sous marin et on change le background en rouge
        for sousmarin in range(len(self.pos_sous_marin)):
            if src.id == str(self.pos_sous_marin[sousmarin]):
                src.disabled = True
                src.background_color = [1,0,0,10] #couleur rouge
                self.touche += 1
                self.touche_sousmarin +=1
                if self.touche_sousmarin == 3:
                    print("YEAHHHH : sous marin coulé")    # pour afficher dans le teminal
                    self.output.text =" FELICITATION : un des deux sous marins a coulé"
                    print(self.touche , self.output)
                    break
                elif self.touche_sousmarin == 6 : 
                    print("yeaahhh tous les sous marins touchés")
                    self.output.text = " FELICITATION : les 2 Sous marins ont coulés"
                else:
                    self.output.text = 'Sous marin touché'



#Fonction qui afficher si on a touché le croisseur et on change le background en rouge
        for croizeur in range(len(self.pos_croiseur)):
            if src.id == str(self.pos_croiseur[croizeur]):
                src.disabled = True
                src.background_color = [1,0,0,10] #couleur rouge
                self.touche += 1
                self.touche_croizeur +=1
                if self.touche_croizeur == 4:
                    print("YEAHHHH : Croisseur coulé")
                    self.output.text = " FELICITATION : le croisseur a coulé"
                    print(self.touche , self.output)
                    break
                else:
                    self.output.text = 'Croisseur touché '


#Fonction qui afficher si on a touché le porte avion et on change le background en rouge
        for porteavion in range(len(self.pos_porte_avion)):
            if src.id == str(self.pos_porte_avion[porteavion]):
                src.disabled = True
                src.background_color = [1,0,0,10] #couleur rouge
                self.touche += 1
                self.touche_porteavion += 1
                if self.touche_porteavion == 5:
                    print("YEAHHHH : Porte avion coulé")
                    self.output.text =" FELICITATION : le porte-avion a coulé"
                    print(self.touche , self.output)
                    break
                else:
                    self.output.text = 'Porte avion touché '


#Fonction qui afficher si on a touché le torpilleur et on change le background en rouge
        for torpieur in range(len(self.pos_torpilleur)):
            if src.id == str(self.pos_torpilleur[torpieur]):
                src.disabled = True
                src.background_color = [1,0,0,10] #couleur rouge
                self.touche_torpi += 1
                self.touche +=1
                if self.touche_torpi == 2:
                    print("YEAHHHH : Torpilleur touché")
                    self.output.text =" FELICITATION : Le torpilleur a coulé"
                    print(self.touche , self.output)
                    break
                else:
                    self.output.text= 'Torpilleur touché'


#Si on touche un autre case que le bateau et on change le background en bleu 
        if src.disabled == False :
            src.background_color = [0.2,0.7,1,10]  # Couleur bleu
            src.disabled = True
            self.output.text = "Failed : Aucun un bateau à été touché"
            print(self.output)

        global puncte
        self.essai += 1
        print("Nombre d'essai :" , self.essai)
        puncte = 100*(self.touche/self.essai)
        # a= round(puncte,2)
        # print(a)     #pour tester dans le terminal
        print('Your score:'+str(puncte))
        print("\n")

        #Pour dire que la partie est termineé  17 bato
        if self.touche == 17:
            pseudo = pseudoScreen()
            pseudo.build()
            sm.add_widget(pseudo)
            sm.current = "Pseudo"
            print('La partie est terminée')



"""
2 JOUEURS
"""

#****************************************************CLASSE POUR 2 JOUEURS************************************************

class Two_players_Screen(Screen):
    def build(self):
        self.name = "multiplayer"
        self.title = "2 PLAYERS"
        self.add_widget(Image(source='image3.png',allow_stretch=True, keep_ratio=False))
        # self.add_widget(Image(source='fond du jeu.jpg', allow_stretch=True , keep_ratio= False))

        #compteurs pour chaque joueur
        self.essai_joueur1 = 0
        self.essai_joueur2 = 0
        self.touche_joueur1 = 0
        self.touche_joueur2 = 0
        self.touche_s1 = 0
        self.touche_s2 = 0
        self.touche_c1 = 0
        self.touche_c2 = 0
        self.touche_p1 = 0
        self.touche_p2 = 0
        self.touche_t1 = 0
        self.touche_t2 = 0
    
### Charger la position des bateaux pour chaque joueur

#chargement de la positions des bateaux pour le joueur 1

        pattern = "C:\\Users\\pedro\\Desktop\\KIVY TEST\\Bateaux 2 joueurs\\Joueur 1\\*.txt"    #etoile pour afficher pour ce qui est du text
        b=random.choice(glob.glob(pattern))
        with open (b) as file:
            sous_marin = "s"
            croiseur = "c"
            porte_avions = "p"
            torpilleur = "t"

            self.pos_sous_marin1 = []
            self.pos_croiseur1 = []
            self.pos_porte_avions1 = []
            self.pos_torpilleur1 = []

            joueur1 = []

            fichier1 = file.readlines()
            for ligne1 in fichier1:
                ligne1_rs = ligne1.rstrip()
                joueur1.append(list(ligne1_rs))
            
            print (joueur1)

            #sous-marin
            for line in range (len(joueur1)):
                for col in range(len(joueur1[line])):
                    if joueur1 [line][col] in sous_marin:
                        position = ([(line),(col)])
                        self.pos_sous_marin1.append (position)
            print("Position des sous-marins joueur 1:",self.pos_sous_marin1)
            
            #croiseur
            for line in range (len(joueur1)):
                for col in range(len(joueur1[line])):
                    if joueur1 [line][col] in croiseur:
                        position = ([(line),(col)])
                        self.pos_croiseur1.append (position)
            print("Position du croiseur joueur 1:",self.pos_croiseur1)
     
            #porte-avions
            for line in range (len(joueur1)):
                for col in range(len(joueur1[line])):
                    if joueur1 [line][col] in porte_avions:
                        position = ([(line),(col)])
                        self.pos_porte_avions1.append (position)
            print("Position du porte-avions joueur 1:",self.pos_porte_avions1)

            #torpilleur
            for line in range (len(joueur1)):
                for col in range(len(joueur1[line])):
                    if joueur1 [line][col] in torpilleur:
                        position = ([(line),(col)])
                        self.pos_torpilleur1.append (position)
            print("Position du torpilleur joueur 1:",self.pos_torpilleur1)


#chargement des positions des bateaux pour le joueur 2:

        pattern = "C:\\Users\\pedro\\Desktop\\KIVY TEST\\Bateaux 2 joueurs\\Joueur 2\\*.txt"    #etoile pour afficher pour ce qui est du text
        b=random.choice(glob.glob(pattern))
        with open (b) as file:
            self.pos_sous_marin2 = []
            self.pos_croiseur2 = []
            self.pos_porte_avions2 = []
            self.pos_torpilleur2 = []

            joueur2 = []

            fichier2 = file.readlines()
            for row in fichier2:
                row_rs = row.rstrip()
                joueur2.append(list(row_rs))
            print(joueur2)

            #sous marins
            for rows in range (len(joueur2)):
                for cols in range (len(joueur2[rows])):
                    if joueur2[rows][cols] in sous_marin:
                        position = ([(rows),(cols)])
                        self.pos_sous_marin2.append(position)
            print ("Position des sous-marins joueur 2:", self.pos_sous_marin2)

            #croiseur
            for rows in range (len(joueur2)):
                for cols in range (len(joueur2[rows])):
                    if joueur2[rows][cols] in croiseur:
                        position = ([(rows),(cols)])
                        self.pos_croiseur2.append(position)
            print ("Position du croisseur joueur 2:", self.pos_croiseur2)

            #porte-avions
            for rows in range (len(joueur2)):
                for cols in range (len(joueur2[rows])):
                    if joueur2[rows][cols] in porte_avions:
                        position = ([(rows),(cols)])
                        self.pos_porte_avions2.append(position)
            print ("Position du porte_avions joueur 2:", self.pos_porte_avions2)

            #torpilleur
            for rows in range (len(joueur2)):
                for cols in range (len(joueur2[rows])):
                    if joueur2[rows][cols] in torpilleur:
                        position = ([(rows),(cols)])
                        self.pos_torpilleur2.append(position)
            print ("Position du torpilleur joueur 2:", self.pos_torpilleur2)


###Grille pour 2 joueurs

        # self.add_widget(Image(source='image3.png',allow_stretch=True, keep_ratio=False))


        BOX= BoxLayout(orientation = "vertical")

        BOITE = BoxLayout(orientation="horizontal")
        Lettres = ['A','B','C','D','E','F','G','H','I','J'] 


#grille joueur 1

        box1= BoxLayout(orientation="vertical")
        grid_1= GridLayout(rows = 12,cols=11,padding=15,spacing=1)
        grid_1.add_widget(Label(text="Player\n   1",color=[0,0,0,5],font_size="15sp"))

        for col in range(1,11):
            grid_1.add_widget(Label(text=str(col),font_size="20sp",color = [0,0,0,5]))

        for A_to_J in range(len(Lettres)):
            grid_1.add_widget(Label(text=str(Lettres[A_to_J]),font_size="20sp",color=[0,0,0,5]))

            for col in range (10):
                a1 = [(A_to_J + 1), (col+1)]
                btn_1 = Button(text = "",id=str(a1))
                btn_1.bind(on_press=self._pressed_1)
                grid_1.add_widget(btn_1)
        
        box1.add_widget(grid_1)
        self.output_1 = Label(size_hint=(1,0.1),font_size="20sp")
        box1.add_widget(self.output_1)


#grille joueur 2

        box2 = BoxLayout(orientation="vertical")
        grid_2 = GridLayout(rows=12,cols=11,padding=15,spacing=1)
        grid_2.add_widget(Label(text="Player\n   2",color=[0,0,0,5],font_size="15sp"))

        for cols in range (1,11):
            grid_2.add_widget(Label(text=str(cols),font_size="20sp",color=[0,0,0,5]))

        for A_to_J in range (len(Lettres)):
            grid_2.add_widget(Label(text=str(Lettres[A_to_J]),font_size="20sp",color=[0,0,0,5]))

            for cols in range (10):
                a2 = [(A_to_J + 1),(cols + 1)]
                btn_2 = Button(text = "",id=str(a2))
                btn_2.bind(on_press=self._pressed_2)
                grid_2.add_widget(btn_2)
        
        box2.add_widget(grid_2)
        self.output_2 = Label(size_hint=(1,0.1),font_size="20sp")
        box2.add_widget(self.output_2)

#ajoute les grille a l'ecran

        BOITE.add_widget(box1)
        BOITE.add_widget(box2)
        BOX.add_widget(BOITE)
        self.add_widget(BOX)


#Informer des résultats de nos tirs

#Informations grille 1

    def _pressed_1(self,source):
        print(id(source))
        self.essai_joueur1 +=1

        #sous-marin
        for sous_marin in range(len(self.pos_sous_marin1)):
            if source.id == str (self.pos_sous_marin1[sous_marin]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur1 +=1
                self.touche_s1 += 1

                while self.touche_s1 < 7:
                    if self.touche_s1 == 3:
                        self.output_1.text = " FELICITATION : un des deux sous marins a coulé"
                    elif self.touche_s1 == 6:
                        self.output_1.text = " FELICITATION : les 2 Sous marins ont coulés"
                    else:
                        self.output_1.text = "Sous-marin touché"
                    break
        
        #croiseur
        for croiseur in range(len(self.pos_croiseur1)):
            if source.id == str (self.pos_croiseur1[croiseur]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur1 +=1
                self.touche_c1 +=1

                while self.touche_c1 < 5:
                    if self.touche_c1 == 4:
                        self.output_1.text = " FELICITATION : le croisseur a coulé"
                    else:
                        self.output_1.text = "Croiseur touché"
                    break
            

        #porte-avions
        for porte_avions in range(len(self.pos_porte_avions1)):
            if source.id == str(self.pos_porte_avions1[porte_avions]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur1 +=1
                self.touche_p1 +=1

                while self.touche_p1 < 6:
                    if self.touche_p1 == 5:
                        self.output_1.text = " FELICITATION : le porte-avions a coulé"
                    else:
                        self.output_1.text = "Porte-avions touché"
                    break

        #torpilleur
        for torpilleur in range (len(self.pos_torpilleur1)):
            if source.id == str(self.pos_torpilleur1[torpilleur]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur1 +=1
                self.touche_t1 +=1

                while self.touche_t1 <3:
                    if self.touche_t1 == 2:
                        self.output_1.text = " FELICITATION : Le torpilleur a coulé"
                    else:
                        self.output_1.text = "Torpilleur touché"
                    break

        
        #eau
        if source.disabled == False:
            source.background_color = [0,0,1,10]
            source.disabled = True
            self.output_1.text = "Eau"

#calcule le score du joueur 1
        global puncte
        puncte = 100 * (self.touche_joueur1/self.essai_joueur1)
        print(puncte)

#Joueur 1 gagne

        if self.touche_joueur1 == 17:
            pseudos = pseudoScreen()
            pseudos.build()
            sm.add_widget(pseudos)
            
            self.popup_1 = Popup()

            self.popup_1.title = "PLAYER 1 WINS"
            self.popup_1.title_align + "center"
            self.popup_1.title_size = "100sp"
            self.popup_1.title_color = [0,1,0,10]

            save_1 = Button(text="Save Score",font_size="50sp",color=[0,1,0,10])
            save_1.bind(on_press=self._save_1)
            self.popup_1.add_widget(save_1)

            self.popup_1.open()


#Informations joueur 2

    def _pressed_2(self,source):

        self.essai_joueur2 +=1
        #sous-marin
        for sous_marin in range(len(self.pos_sous_marin2)):
            if source.id == str(self.pos_sous_marin2[sous_marin]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur2 +=1
                self.touche_s2 +=1

                while self.touche_s2 < 7:
                    if self.touche_s2 == 3:
                        self.output_2.text = " FELICITATION : un des deux sous marins a coulé"
                    elif self.touche_s2 == 6:
                        self.output_2.text = " FELICITATION : les 2 Sous marins ont coulés"
                    else:
                        self.output_2.text = "Sous-marin touché"
                    break

        #croiseur
        for croiseur in range(len(self.pos_croiseur2)):
            if source.id == str (self.pos_croiseur2[croiseur]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur2 +=1
                self.touche_c2 +=1

                while self.touche_c2 < 5:
                    if self.touche_c2 == 4:
                        self.output_2.text = " FELICITATION : le croisseur a coulé"
                    else:
                        self.output_2.text = "Croiseur touché"
                    break
            

        #porte-avions
        for porte_avions in range(len(self.pos_porte_avions2)):
            if source.id == str(self.pos_porte_avions2[porte_avions]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur2 +=1
                self.touche_p2 +=1

                while self.touche_p2 < 6:
                    if self.touche_p2 == 5:
                        self.output_2.text = " FELICITATION : le porte-avions a coulé"
                    else:
                        self.output_2.text = "Porte-avions touché"
                    break

        #torpilleur
        for torpilleur in range (len(self.pos_torpilleur2)):
            if source.id == str(self.pos_torpilleur2[torpilleur]):
                source.disabled = True
                source.background_color = [1,0,0,10]
                self.touche_joueur2 +=1
                self.touche_t2 +=1

                while self.touche_t2 <3:
                    if self.touche_t2 == 2:
                        self.output_2.text = " FELICITATION : Le torpilleur a coulé"
                    else:
                        self.output_2.text = "Torpilleur touché"
                    break
    
        #eau
        if source.disabled == False:                                #si on touche pas les batteaux, donc les btns sont clicable => on a touché l'eau
            source.background_color = [0,0,1,10]
            source.disabled = True
            self.output_2.text = "Failed : Aucun un bateau à été touché"

#Score joueur 2
        global puncte
        puncte = 100* (self.touche_joueur2/self.essai_joueur2)
        print(puncte)

#Joueur 2 gagne

        if self.touche_joueur2 == 17:
            pseudo = pseudoScreen()
            pseudo.build()
            sm.add_widget(pseudo)
            # sm.current = 'Pseudo'

            self.popup_2 = Popup()

            self.popup_2.title = "PLAYER 2 WINS"
            self.popup_2.title_align + "center"
            self.popup_2.title_size = "100sp"
            self.popup_2.title_color = [0,1,0,10]

            save_2 = Button(text="Save Score",font_size="50sp",color=[0,1,0,10])
            save_2.bind(on_press=self._save_2)
            self.popup_2.add_widget(save_2)

            self.popup_2.open()


#fontions boutons popup
    def _save_1(self,source):
        sm.current = "Pseudo"
        self.popup_1.dismiss()
    
    def _save_2(self,source):
        sm.current = "Pseudo"
        self.popup_2.dismiss()


        
"""
DERNIER ECRAN
"""
        

#****************************************************CLASSE POUR LE SCORE*************************************************

class pseudoScreen(Screen):
    def build(self):
        self.name = 'Pseudo'
        self.title = 'PSEUDO'
        self.add_widget(Image(source='title_screen.jpg', allow_stretch=True , keep_ratio= False))

        self.Score_Layout=BoxLayout(padding=50,spacing=80,orientation='vertical')
        self.Sous_score_Layout2=BoxLayout(orientation='vertical') # pour le bouton SAVE + Lable
        Sous_score_Layout=BoxLayout(orientation='horizontal',size_hint=(1,0.8)) # pour le save et label et input

    
        # print(str(puncte) + 'yoyoyoyoyo')
#[b][/b] + markup = True pour afficher en BOLD
        self.label_score=Label(text='[b]Your score:[/b]'+'\n' + str(round(puncte,2)),color =(0,5,0,10),font_size='30sp',italic=True ,markup=True)
        # print('rrr'+str(puncte))

        self.Bouton_enregistrer=Button(text='SAVE', on_press=self._saveScore,font_size='40sp')
        self.Input=TextInput(multiline=False,font_size = '35sp')
        self.Input.bind(on_text_validate=self._saveScore)

        
        Sous_score_Layout.add_widget(self.label_score)
        Sous_score_Layout.add_widget(self.Input)
        Sous_score_Layout.add_widget(self.Bouton_enregistrer)
        
        
# Pour afficher le pseudo dans le label 
        self.display_score = Label(text='')
        self.Score_Layout.add_widget(Sous_score_Layout)
        self.Score_Layout.add_widget(self.display_score)

        self.Score_Layout.add_widget(self.Sous_score_Layout2)

        self.Bouton_Fin=Button(text='FINI !',color = (1,0,0.2,2))
        self.Bouton_Fin.font_size=Window.size[0]*0.05
        self.Bouton_Fin.background_color=[1,1,1,0.5]
        self.Bouton_Fin.bind(on_press=self._Quitter) 
        self.Score_Layout.add_widget(self.Bouton_Fin) 


        self.add_widget(self.Score_Layout)

    def _Quitter(self,src):
    # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()


    def _saveScore(self , src):

        # score_maximum=0
        # index_maximum=0
        tous_les_scores=[]
        tous_les_noms=[]
        #ecriture dans fichier json
        try:
            with open('data.json')as json_file:
                data=json.load(json_file)  #lecture du fichier json
            
                data['player_score'].append({
                    'name':self.Input.text,   
                    'score':puncte 
                })
                for dictionnaire in data['player_score']:      # mettre a jour la clé player _score
                
                    tous_les_scores.append(int(dictionnaire['score']))
                    tous_les_noms.append(dictionnaire['name'])
                    score_maximum=max(tous_les_scores)
                    name_maximum=tous_les_scores.index(score_maximum)
                    # print('***BEST SCORE***')
                    # print('SCORE  :' + str(score_maximum))
                    # print('NAME   :' + all_names[index_maximum])
                    # print("\n")
                    # print('***LAST SCORE***')
                    # print('SCORE  :' + str(all_scores[-1]))
                    # print('NAME   :' + all_names[-1])    

        


            with open('data.json','w') as outfile:
                json.dump(data,outfile,indent=4)

        except :
            data={}
            data['player_score']=[]
            data['player_score'].append({
                    'name':self.Input.text,   
                    'score':puncte 
                })
            with open('data.json','w') as outfile:
                json.dump(data,outfile,indent=4)


#Pour afficher les pseudo dans le display
        self.display_score= Label(text=" [u][b]Pseudo[/b][/u]:{}   [b]Last Score[/b] :{} \n [u][b]Pseudo[/b][/u] :{}  [b]Best Score[/b]:{}".format(tous_les_noms[-1],tous_les_scores[-1],tous_les_noms[name_maximum],score_maximum)
        ,font_size ='50sp',markup= True)

        self.Sous_score_Layout2.add_widget(self.display_score)

        # sm.current = 'Pseudo'





### Lance le Jeu 
class Test_Jeu_BatailleApp(App):
    def build(self):
        menu = MenuScreen()
        menu.build()
        sm.add_widget(menu)
        sm.current='Menu'
        return sm

Test_Jeu_BatailleApp().run()