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




# on definit un ScreenManager au debut ! 
sm = ScreenManager()

##Ecran d'acueuille 
class MenuScreen(Screen):
    def __init__( self ,**kwargs):
        super(MenuScreen , self ).__init__(**kwargs)
        self.add_widget(Image(source='Battle.jpeg', allow_stretch=True , keep_ratio= False))
        Menu_Layout=BoxLayout(padding=100,spacing=80,orientation='vertical')

#Bouton Play 
        self.Bouton_play = Button(text='PLAY')
        self.Bouton_play.font_size= Window.size[0]*0.05
        self.Bouton_play.background_color=[0,0,0,0.5]
        self.Bouton_play.bind(on_press=self._play)
        Menu_Layout.add_widget(self.Bouton_play)

# #Bouton Quitter 
        self.Bouton_quitter = Button(text='QUITTER LE JEU')
        self.Bouton_quitter.font_size= Window.size[0]*0.05
        self.Bouton_quitter.background_color=[0,0,0,0.5]
        self.Bouton_quitter.bind(on_press=self._Quitter)
        Menu_Layout.add_widget(self.Bouton_quitter)
#Pour appeler box , on met pas return pour pas faire une boucle
        self.add_widget(Menu_Layout)
##Definir un fonction pour le bouton PLAY
    def _play(self ,src):
        sm.current = 'Pseudo'
        sm.transition.direction = "left"
        
##Definir un fonction pour le bouton Quitter 
    def _Quitter(self,src):
        # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()

sm.add_widget(MenuScreen(name='Menu'))


#Classe pour le entrer le nom , score etc..

class pseudoScreen(Screen):
    def __init__(self , **kwargs):
        super(pseudoScreen ,self).__init__(**kwargs)
        self.title = 'PSEUDO'
        self.add_widget(Image(source='title_screen.jpg', allow_stretch=True , keep_ratio= False))

        box =BoxLayout(orientation = 'vertical', size_hint=(0.5,0.5))
       
        pos = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
       
        self.output= Label()
        box.add_widget(self.output)
        box.add_widget(Label(text='Enter your Name', font_size='30sp'))
        box.add_widget(TextInput(multiline=False,font_size='50sp'))
        self.output.font_size = 150

        play = Button(text="PLAY")
        play.bind(on_press=self._play)
        box.add_widget(play)
        
        pos.add_widget(box)
        self.add_widget(pos)

    def _play(self , src):
        sm.current = 'Game'
        sm.transition.direction = 'left'
sm.add_widget(pseudoScreen(name='Pseudo'))
        



#Classe pour la Grille de jeu
class GridGameScreen(Screen):
    def __init__(self,**kwargs):
        super(GridGameScreen,self).__init__(**kwargs)
        self.add_widget(Image(source='fond du jeu.jpg', allow_stretch=True , keep_ratio= False))

        self.title = 'Bataille'
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
                grid.add_widget(btn)
#Ecran separe pour afficher text 'touché , coulé , vous avez gagnez ,perdu etc...
        self.output= Label()
        grid.add_widget(self.output)
        self.add_widget(grid)
#pour dire que le GridGameScreen se trouve dans l'ecran 1
sm.add_widget(GridGameScreen(name='Game'))



##Charge les bateaux
class GrilleScreen(Screen):
    def __init__(self, **kwargs):
        super(GrilleScreen, self).__init__(**kwargs)

        self.score = 0
        self.essai = 0 
        self.touche = 0

        with open ('cahier.txt','r') as f:
            self.pos_sous_marin = []
            self.pos_croiseur = []
            self.pos_porte_avion = []
            self.pos_torpilleur = []
            self.output = ""
            self.count_letters = 0
            matrice = []

            sous_marin= "s"
            croiseur="c"
            porte_avion = "p"
            torpilleur = "t"

            fichier = f.readlines()
            for line in fichier:
                line_rs = line.rstrip()
                matrice.append(list(line_rs))
            print(matrice)


            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in sous_marin:
                        position  =([(ligne),(col)])   # determine la position des sous marin
                        self.pos_sous_marin.append(position)
            print("positions des sous marins:",self.pos_sous_marin)


            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in croiseur:
                        position  =([(ligne),(col)])
                        self.pos_croiseur.append(position)
            print("positions des croisseur:",self.pos_croiseur)

            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in porte_avion:
                        position  =([(ligne),(col)])
                        self.pos_porte_avion.append(position)
            print("positions des porte avions:",self.pos_porte_avion)

            for ligne in range(len(matrice)):
                for col in range (len(matrice[ligne])):
                    if matrice [ligne][col] in torpilleur:
                        position  =([(ligne),(col)])
                        self.pos_torpilleur.append(position)
            print("positions des torpilleur:",self.pos_torpilleur)

        def Informer(self, instance):

            for sousmarin in range(len(self.pos_sous_marin)):
                if instance.id == str(self.pos_sous_marin[sousmarin]):
                    instance.disabled = True
                    instance.background_color = [1,0,0,10] #couleur rouge
                    self.touche += 1
                    if self.touche == self.count_letters:
                        print("YEAHHHHHH!!!!")

                    self.output.text =" Sous marin touché"
                    print(self.touche , self.output)
                    break

















### Lance le Jeu 
class Test_Jeu_BatailleApp(App):
    def build(self):
        return sm

Test_Jeu_BatailleApp().run()
