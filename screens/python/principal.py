from kivy.uix.screenmanager import Screen
from .adicionais import *


class TelaPrincipal(Screen):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

        # apenas para teste
        # for i in range(24):
        #     args = {'inicio':'{0:>2}:00 AM'.format(i), 'final':'{0:>2}:00 AM'.format(i+1), 'materia':materias[randint(0, len(materias)-1)]}
        #     self.ids['container'].add_widget(Celula(args, size_hint_y=None, height=80))
