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
class Screen_Menu(Screen):
    def build (self):
        self.name = 'MENU'
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
        # sm.transition.direction = "left"
        pseudo = pseudoScreen()
        pseudo.build()
        sm.add_widget(pseudo)
        sm.current = 'NOM_JOUEUR'
##Definir un fonction pour le bouton Quitter 
    def _Quitter(self,src):
        # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Test_Jeu_BatailleApp().stop()



#Classe pour le entrer le nom , score etc..

class pseudoScreen(Screen):
    def build (self):

        self.name ='NOM_JOUEUR'
        self.add_widget(Image(source='title_screen.jpg', allow_stretch=True , keep_ratio= False))

        box = AnchorLayout(anchor_x='center', anchor_y='center')
        
        line1= BoxLayout(orientation='vertical',size_hint=(0.5,0.5))
        box.add_widget(line1)
       
        self.name_player= TextInput(font_size="50sp",multiline=False)

        bouton_ok = Button(text="ENTER")
        bouton_ok.bind(on_press=self._play)

        line1.add_widget(Label(text='ENTER YOUR NAME'))
        line1.add_widget(self.name_player)
        line1.add_widget(bouton_ok)

        bouton_play_anchor = AnchorLayout(anchor_x='right',anchor_y='bottom',size_hint=(0.2,0.1))
        btn=Button(text='PLAY')
        btn.bind(on_press=self._play)
        bouton_play_anchor.add_widget(btn)

        # play = Button(text="PLAY")
        # play.bind(on_press=self._play)
        # box.add_widget(play)
        
        self.add_widget(box)
        self.add_widget(bouton_play_anchor)

    def _play(self , src):
        game= Screen_Game()
        game.build()
        sm.add_widget(game)
        sm.current = 'Game'
        sm.transition.direction = 'left'

class Screen_Game(Screen):
    def build (self):
        self.name = 'Game'
        Game_Layout = GameApp().build()
        self.add_widget(Game_Layout)



#Classe pour la Grille de jeu
class GameApp(App):
    def build(self):
        
        self.add_widget(Image(source='fond du jeu.jpg', allow_stretch=True , keep_ratio= False ))

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































### Lance le Jeu 
class Test_Jeu_BatailleApp(App,Screen):
    def build(self):
        Menu= Screen_Menu()
        Menu.build()
        sm.add_widget(Menu)
        sm.current ='MENU'
        return sm

Test_Jeu_BatailleApp().run()
