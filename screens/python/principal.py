from kivy.uix.screenmanager import Screen
from .adicionais import *


class TelaPrincipal(Screen):
    def __init__(self,  MyDb, **kwargs):
        super().__init__(**kwargs)
        self.MyDb = MyDb

    def on_enter(self):
        self.atualiza()

    def atualiza(self):
        self.ids['container'].clear_widgets()

        materias = self.MyDb.get_subjects()
        horarios_estudo = self.MyDb.get_study_time()

        for materia in materias:
            for horario in horarios_estudo:
                if materia[1] == horario[0]:
                    args = {'materia': materia[1], 'dificuldade': materia[2], 'carga_horaria_semanal': materia[3], 'tempo_estudo': horario[1]}
                    self.ids['container'].add_widget(Celula(args, size_hint_y=None, height=80))
                    break

        return True
