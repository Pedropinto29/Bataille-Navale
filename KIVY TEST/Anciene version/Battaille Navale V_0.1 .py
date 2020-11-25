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
class StartScreen(Screen):
    def __init__( self ,**kwargs):
        super(StartScreen , self ).__init__(**kwargs)
        self.add_widget(Image(source='Battle.jpeg', allow_stretch=True , keep_ratio= False))
        
#Bouton Play 
        box = FloatLayout(size=(150,150))
        play = Button(text="PLAY", size_hint=(0.4,0.3) , pos=(50,250))
        play.bind(on_press=self._play)
        box.add_widget(play)
#Bouton Quitter 
        Quitter = Button(text="QUIT THE GAME", size_hint=(0.4, 0.3) , pos=(450,250))
        Quitter.bind(on_press=self._Quitter)
        box.add_widget(Quitter)
#Pour appeler box , on met pas return pour pas faire une boucle
        self.add_widget(box)    
##Definir un fonction pour le bouton PLAY
    def _play(self ,src):
        sm.current = 'ecran 2'
        sm.transition.direction = "left"
        
##Definir un fonction pour le bouton Quitter 
    def _Quitter(self,src):
        # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()

sm.add_widget(StartScreen(name='ecran 1'))


#Classe pour le entrer le nom , score etc..

class pseudoScreen(Screen):
    def __init__(self , **kwargs):
        super(pseudoScreen ,self).__init__(**kwargs)
        self.title = 'PSEUDO'

        box =BoxLayout(orientation = 'vertical', size_hint=(0.5,0.5))
       
        pos = AnchorLayout(anchor_x = 'center', anchor_y = 'center')
       
        self.output= Label()
        box.add_widget(self.output)
        box.add_widget(Label(text='Enter your Name'))
        box.add_widget(TextInput(multiline=False))
        self.output.font_size = 150

        play = Button(text="PLAY")
        play.bind(on_press=self._play)
        box.add_widget(play)
        
        pos.add_widget(box)
        self.add_widget(pos)

    def _play(self , src):
        sm.current = 'ecran 3'
        sm.transition.direction = 'left'
sm.add_widget(pseudoScreen(name='ecran 2'))
        



#Classe pour la Grille de jeu
class GridGameScreen(Screen):
    def __init__(self,**kwargs):
        super(GridGameScreen,self).__init__(**kwargs)

        self.title = 'Bataille'
        grid = GridLayout(rows=12 , cols = 11)
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
sm.add_widget(GridGameScreen(name='ecran 3'))





















### Lance le Jeu 
class Test_Jeu_BatailleApp(App):
    def build(self):
        return sm

Test_Jeu_BatailleApp().run()
