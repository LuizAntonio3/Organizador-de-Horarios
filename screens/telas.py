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
    def add_materia(self, MyDb):
        materia = self.ids.materia.text
        dificuldade = int(self.ids.dificuldade.value)
        carga_horaria_semanal = self.ids.carga_horaria_semanal.text

        valido = True

        # verifica se todos os campos estão preenchidos
        if materia == '' or carga_horaria_semanal == '':
            print("Todos os campos devem ser preenchidos")
            self.ids.invalidar.text = 'Todos os campos devem ser preenchidos'
            return False
        else:
            MyDb.add_subjects(materia, dificuldade, carga_horaria_semanal)

            # limpa todos os campos
            for id in self.ids:
                self.ids[id].text = ''

            return True

class TelaAdicionarHorarioLivre(Screen):
    def add_free_time(self, MyDb):
        dia = self.ids.dia_semana.text
        horas = self.ids.horas_livres.text

        remove_char = ('\n', '\t', ' ', ' ')
        dia = dia.translate({ord(item): None for item in remove_char})

        if dia == '' or horas == '':
            print("Todos os campos devem ser preenchidos")
            self.ids.invalidar.text = 'Todos os campos devem ser preenchidos'
            return False
        else:
            horas = float(horas)

            MyDb.cursor.execute('''
            UPDATE horario_livre
            SET
                horas_livres = (?)
            WHERE
                dia_semana = (?);
            ''', (horas, dia))

            MyDb.db_conn.commit()

            # limpa todos os campos
            for id in self.ids:
                self.ids[id].text = ''

            return True
