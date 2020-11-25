'''@author = Manu PLACINTA

Date 12/12/2019 : Examen

'''
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
import random


global puncte
puncte = 0
# on definit un ScreenManager au debut ! 
sm = ScreenManager()
#Variable global qui n'esdt pas propre a une classe , donc je peux utiliser dans tout le code


##Ecran d'acueuille 
class MenuScreen(Screen):
    def __init__( self ,**kwargs):
        super(MenuScreen , self ).__init__(**kwargs)
        self.add_widget(Image(source='BattleTittleAutor.jpg', allow_stretch=True , keep_ratio= False))
        Menu_Layout=BoxLayout(padding=100,spacing=80,orientation='vertical')

#Bouton Play 
        self.Bouton_play = Button(text='PLAY')
        self.Bouton_play.font_size= Window.size[0]*0.05
        self.Bouton_play.background_color=[0,0,0,0.5]  # couleur verte
        self.Bouton_play.bind(on_press=self._play)
        Menu_Layout.add_widget(self.Bouton_play)

# #Bouton Quitter 
        self.Bouton_quitter = Button(text='QUITTER LE JEU')
        self.Bouton_quitter.font_size= Window.size[0]*0.05
        self.Bouton_quitter.background_color=[0,0,0,0.5]  # couleur rouge 
        self.Bouton_quitter.bind(on_press=self._Quitter)
        Menu_Layout.add_widget(self.Bouton_quitter)
#Pour appeler box , on met pas return pour pas faire une boucle
        self.add_widget(Menu_Layout)
##Definir un fonction pour le bouton PLAY
    def _play(self ,src):
        sm.current = 'Game'
        sm.transition.direction = "left"
        
##Definir un fonction pour le bouton Quitter 
    def _Quitter(self,src):
        # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()

sm.add_widget(MenuScreen(name='Menu'))

#************************************************************  CLASSE POUR LE JEU  !!********************************************************
class GridGameScreen(Screen):
    def __init__(self,**kwargs):
        super(GridGameScreen,self).__init__(**kwargs)
        self.add_widget(Image(source='fond du jeu.jpg', allow_stretch=True , keep_ratio= False))

        # puncte = 0
        self.essai = 0       #Initialize les coup pour essai et touché a zero "0"
        self.touche = 0
        self.touche_torpi =0
        self.touche_croizeur =0
        self.touche_sousmarin =0
        self.touche_porteavion =0
###RANDOM 
        a= ['c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier.txt','c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier_2.txt',

        'c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier_3.txt','c:\\Users\\Nelu8770\\Desktop\\KIVY TEST\\cahier_4.txt']
        b=random.choice(a)
## On ouvre le fichier et on definit la position avec une liste vite
        with open (b,'rt') as f:
            self.pos_sous_marin = []
            self.pos_croiseur = []
            self.pos_porte_avion = []
            self.pos_torpilleur = []
            self.output = ""
            # self.count_letters = 0
            matrice = []
## Declaration de noms pour les bato
            sous_marin= "s"
            croiseur="c"
            porte_avion = "p"
            torpilleur = "t"
## Parcours le fichier et supprime les espaces
            fichier = f.readlines()
            for line in fichier:
                line_rs = line.rstrip()
                matrice.append(list(line_rs))
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
        label_message = BoxLayout(orientation = "vertical")
        grid = GridLayout(rows=12 , cols = 11,padding=15,spacing= 3)

        grid.add_widget(Label(text='ECAM\n17235'))
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
                # print (btn)
#Ecran separe pour afficher text 'touché , coulé , vous avez gagnez ,perdu etc...
        self.output= Label(text="",font_size='30sp',size_hint=(0.7,0.1))
        label_message.add_widget(grid)
        label_message.add_widget(self.output)
        
        self.add_widget(label_message)
        
        

        # return label_message
#Creation de la fonction qui permet d'informer et cliquer sur chaque bato
    def _message(self, src):
#Fonction qui afficher si on a touché le sous marin et on change le background en rouge
        for sousmarin in range(len(self.pos_sous_marin)):
            if src.id == str(self.pos_sous_marin[sousmarin]):
                src.disabled = True
                src.background_color = [1,0,0,10] #couleur rouge
                self.touche += 1
                self.touche_sousmarin +=1
                if self.touche_sousmarin == 6:
                    print("YEAHHHH : sous marin coulé")    # pour afficher dans le teminal
                    self.output.text =" FELICITATION : les sous marins ont coulés"
                    print(self.touche , self.output)
                    break
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

        # global puncte
        # puncte=0
        self.essai += 1
        print("Nombres d'essai :", self.essai)
        puncte = 100*(self.touche/self.essai)
        print(puncte)
        # self.label_score.text='Your score:'+ str(puncte)

#Pour dire que la partie est termineé  14 bato
        if self.touche == 17:
            sm.current = "Pseudo"
            print("La partie est terminée")

        return

#pour dire que le GridGameScreen se trouve dans l'ecran GAME
sm.add_widget(GridGameScreen(name='Game'))
#****************************************************CLASSE POUR LE SCORE*************************************************
class pseudoScreen(Screen):
    def __init__(self , **kwargs):
        super(pseudoScreen ,self).__init__(**kwargs)
        # global puncte
        self.title = 'PSEUDO'
        self.add_widget(Image(source='title_screenFIN2.jpg', allow_stretch=True , keep_ratio= False))
        

        self.Score_Layout=BoxLayout(padding=50,spacing=10,orientation='vertical')
        Sous_score_Layout=BoxLayout(orientation='horizontal',size_hint=(1,0.2))
        self.Sous_score_Layout2=BoxLayout(orientation='vertical',size_hint=(1,0.6))
        
        self.label_score=Label(text='Your score:'+ str(puncte))
        print('rrr'+str(puncte))
        self.label_score.font_size=Window.size[0]*0.04
        self.Bouton_enregistrer=Button(text='SAVE', on_press=self._saveScore)
        self.Bouton_enregistrer.font_size=Window.size[0]*0.05
        
        self.Input=TextInput(multiline=False)
        self.Input.font_size=Window.size[0]*0.05
        self.Input.bind(on_text_validate=self._saveScore)

        
        Sous_score_Layout.add_widget(self.label_score)
        Sous_score_Layout.add_widget(self.Input)
        Sous_score_Layout.add_widget(self.Bouton_enregistrer)
        self.Score_Layout.add_widget(Sous_score_Layout)
        
        self.Score_Layout.add_widget(self.Sous_score_Layout2)


        self.Bouton_Fin=Button(text='FINI !',size_hint=(1,0.3))
        self.Bouton_Fin.font_size=Window.size[0]*0.05
        self.Bouton_Fin.background_color=[1,1,1,0.5]
        self.Bouton_Fin.bind(on_press=self._Quitter) 
        self.Score_Layout.add_widget(self.Bouton_Fin) 

        self.Bouton_mainMenu = Button(text='RETOUR AU MENU',size_hint=(1,0.3))
        self.Bouton_mainMenu.font_size=Window.size[0]*0.05
        self.Bouton_mainMenu.background_color=[1,1,1,0.5]
        self.Bouton_mainMenu.bind(on_press=self._AuMenu) 
        self.Score_Layout.add_widget(self.Bouton_mainMenu) 
    
        
        self.add_widget(self.Score_Layout)


# Fontion pour le bouton SAVE pour sauvegarder le score
    def _saveScore(self , src):
        sm.current = 'Game'
        sm.transition.direction = 'left'




    def _AuMenu (self ,src):
        sm.current = 'Menu'
        sm.transition.direction = 'left'


    def _Quitter(self,src):
    # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()

sm.add_widget(pseudoScreen(name='Pseudo'))
        





### Lance le Jeu 
class Test_Jeu_BatailleApp(App):
    def build(self):
        return sm

Test_Jeu_BatailleApp().run()