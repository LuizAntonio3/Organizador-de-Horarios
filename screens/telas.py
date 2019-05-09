from kivy.uix.screenmanager import Screen
from .adicionais import *
from random import randint

# apenas para teste
materias = ['Calculo I', 'Algebra Linear I', 'Fisica I', 'Mato', 'LP-I']

class TelaCadastroUsuario(Screen):
    def add_user(self, MyDb):
        nome = self.ids.nome.text
        curso = self.ids.curso.text

        # implementação incompleta
        if nome != '' and curso != '':
            if not nome.lower() == 'main':
                MyDb.add_user(nome, curso)
            return True
        else:
            print("Usuario e Curso devem ser preenchidos")
            self.ids.invalidar.text = 'Preencha tudo'
            return False


class TelaPrincipal(Screen):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

        # apenas para teste
        for i in range(24):
            args = {'inicio':'{0:>2}:00 AM'.format(i), 'final':'{0:>2}:00 AM'.format(i+1), 'materia':materias[randint(0, len(materias)-1)]}
            self.ids['container'].add_widget(Celula(args, size_hint_y=None, height=80))


class TelaAdicionarMateria(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.ids['entrada_horarios'].add_widget(Hora(pos=(.5, .5)))

    def add_materia(self, MyDb):
        materia = self.ids.materia.text
        dificuldade = int(self.ids.dificuldade.value)
        dia = self.ids.dia.text
        inicio = self.ids.inicio.text
        termino = self.ids.termino.text

        valido = True

        # verifica se todos os campos estão preenchidos
        for id in self.ids:
            if self.ids[id].text == '':
                valido = False

        if valido:
            MyDb.add_subjects(materia, dia, inicio, termino, dificuldade)

            # limpa todos os campos
            for id in self.ids:
                self.ids[id].text = ''

            return True
        else:
            print("Todos os campos devem ser preenchidos")
            self.ids.invalidar.text = 'Preencha tudo'
            return False
