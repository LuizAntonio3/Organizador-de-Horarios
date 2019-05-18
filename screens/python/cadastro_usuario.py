from kivy.uix.screenmanager import Screen


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
