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
import random
import json


class pseudoScreen(App):
    def build(self):

        self.title = 'PSEUDO'
        self.add_widget(Image(source='title_screen.jpg', allow_stretch=True , keep_ratio= False))

        self.Score_Layout=BoxLayout(padding=50,spacing=10,orientation='vertical')
        Sous_score_Layout=BoxLayout(orientation='horizontal',size_hint=(1,0.2)) # pour le save et label
        self.Sous_score_Layout2=BoxLayout(orientation='vertical',size_hint=(1,0.8)) # pour le bouton fin
        # print(str(puncte) + 'yoyoyoyoyo')
#[b][/b] pour afficher en BOLD
        self.label_score=Label(text='[b]Your score:[/b]',color =(0,1,0,10),font_size='20sp',italic=True ,markup=True)
        # print('rrr'+str(puncte))

        self.Bouton_enregistrer=Button(text='SAVE', on_press=self._saveScore,font_size='40sp')

        
        self.Input=TextInput(multiline=False,font_size = '40sp')

        self.Input.bind(on_text_validate=self._saveScore)

        
        Sous_score_Layout.add_widget(self.label_score)
        Sous_score_Layout.add_widget(self.Input)
        Sous_score_Layout.add_widget(self.Bouton_enregistrer)
        self.Score_Layout.add_widget(Sous_score_Layout)
        
        self.Score_Layout.add_widget(self.Sous_score_Layout2)

        self.Bouton_Fin=Button(text='FINI !',size_hint=(1,0.2),color = (0,1,0.2,2))
        self.Bouton_Fin.font_size=Window.size[0]*0.05
        self.Bouton_Fin.background_color=[1,1,1,0.5]
        self.Bouton_Fin.bind(on_press=self._Quitter) 
        self.Score_Layout.add_widget(self.Bouton_Fin) 


        self.add_widget(self.Score_Layout)



    def _Quitter(self,src):
    # sm.current = "ecran 1" Pas besoin de mettre le sm.current() car ca quitte.
        Myapp().stop()


    def _saveScore(self , src):

        #ecriture dans fichier json
        try:
            with open('data.txt')as json_file:
                data=json.load(json_file)
            
                data['player_score'].append({
                    'name':self.Input.text,   
                    'score':puncte 
                })
            with open('data.txt','w') as outfile:
                json.dump(data,outfile,indent=4)

        except :
            data={}
            data['player_score']=[]
            data['player_score'].append({
                    'name':self.Input.text,   
                    'score':puncte 
                })
            with open('data.txt','w') as outfile:
                json.dump(data,outfile,indent=4)

        #lecture du fichier json
        score_maximum=0
        index_maximum=0
        all_scores=[]
        all_names=[]
        with open('data.txt') as json_file:
            data=json.load(json_file)
            print(data )#pour verifier 
            for p in data['player_score']:
                
                all_scores.append(int(p['score']))
                all_names.append(p['name'])
                score_maximum=max(all_scores)
                index_maximum=all_scores.index(score_maximum)
                print('BEST SCORE')
                print('SCORE  :' + str(score_maximum))
                print('NAME   :' + all_names[index_maximum])

                print('LAST SCORE')
                print('SCORE  :' + str(all_scores[-1]))
                print('NAME   :' + all_names[-1])    

        sm.current = 'Pseudo'
        sm.transition.direction = 'left'






class Myapp(App):
    def build(self):
        return pseudoScreen()

