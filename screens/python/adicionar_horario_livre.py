from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex


class TelaAdicionarHorarioLivre(Screen):
    def add_free_time(self, MyDb):
        dia = self.ids.dia_semana.text
        horas = self.ids.horas_livres.text

        remove_char = ('\n', '\t', ' ', ' ')
        dia = dia.translate({ord(item): None for item in remove_char})

        if dia == '' or horas == '':
            print("Todos os campos devem ser preenchidos")
            self.ids.invalidar.color = get_color_from_hex('#FF0000')
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

            print('horario livre adicionado com sucesso')
            self.ids.invalidar.color = get_color_from_hex('#00FF00')
            self.ids.invalidar.text = 'Horário adicionado'
            return True
