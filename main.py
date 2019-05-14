# Importar dependencias do kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.lang import Builder
from kivy.config import Config

# Importar Classes extras
from packages.create_db import Database
from screens.telas import *
from screens.kv_lang_screens.loader import load_screens

# apenas para teste e apresentação
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class MyApp(App):
    def __init__(self):
        super(MyApp, self).__init__()

        self.MyDb = Database('MyDb')
        self.sm = ScreenManager(transition=FadeTransition())

    def build(self):
        # Carrega as interfaces gráficas
        load_screens()

        # Adiciona todas as telas ao gerenciador

        # faz a amostragem da tela de cadastro de usuario somente se nenhum usuario existir no banco de dados
        if len(self.MyDb.get_users()) == 0:
            self.sm.add_widget(TelaCadastroUsuario(name='cadastrar_usuario'))
        self.sm.add_widget(TelaPrincipal(name='principal'))
        self.sm.add_widget(TelaAdicionarMateria(name='adicionar_materia'))
        self.sm.add_widget(TelaAdicionarHorarioLivre(name='adicionar_horario_livre'))

        return self.sm


if __name__ == '__main__':
    # executa o Aplicativo
    MyApp().run()
