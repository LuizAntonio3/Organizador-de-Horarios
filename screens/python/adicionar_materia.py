from kivy.uix.screenmanager import Screen


class TelaAdicionarMateria(Screen):
    def generate_study_time(self, MyDb):
        horario_livre = 0

        for item in MyDb.get_free_time():
            horario_livre += item[1]

        print(horario_livre)

        lista_materias = MyDb.get_subjects()
        quantidade_materias = len(lista_materias)

        lista_dificuldades = (int(lista_materias[i][2]) for i in range(quantidade_materias))
        lista_carga_horaria = (float(lista_materias[i][3]) for i in range(quantidade_materias))
        soma_dificuldades = sum(lista_dificuldades)
        carga_horaria_semanal = sum(lista_carga_horaria)

        soma_pesos = 0

        lista_pesos = list()
        for materia in lista_materias:
            peso_qtd_materias = 1/quantidade_materias
            peso_dificuldade = materia[2]/soma_dificuldades
            peso_c_horaria = materia[3]/carga_horaria_semanal

            peso_materia = peso_qtd_materias*peso_c_horaria+peso_dificuldade

            lista_pesos.append(peso_materia)

            soma_pesos += peso_materia

        for i in range(len(lista_pesos)):
            materia = lista_materias[i][1]
            horas = (lista_pesos[i]/soma_pesos)*horario_livre

            comando = "SELECT * FROM horarios_estudo WHERE materia = '{}'".format(materia)
            MyDb.cursor.execute(comando)
            items = MyDb.cursor.fetchall()

            if len(items) == 0:
                MyDb.add_study_time(materia, horas)
            else:
                comando = """UPDATE horarios_estudo
                             SET horas_estudo = '{}'
                             WHERE materia = '{}'""".format(horas, materia)
                MyDb.cursor.execute(comando)


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
            carga_horaria_semanal = float(carga_horaria_semanal.replace(",", "."))
            MyDb.add_subjects(materia, dificuldade, carga_horaria_semanal)
            self.generate_study_time(MyDb)

            # limpa todos os campos
            self.ids['dificuldade'].value = 1
            for id in self.ids:
                self.ids[id].text = ''

            return True
