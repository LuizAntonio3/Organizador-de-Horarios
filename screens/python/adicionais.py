from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Celula(Widget):
    inicio = ObjectProperty('')
    final = ObjectProperty('')
    materia = ObjectProperty('')

    def __init__(self, values={}, **kwargs):
        super(Celula, self).__init__(**kwargs)

        self.inicio = values['inicio']
        self.final = values['final']
        self.materia = values['materia']


class Hora(Widget):
    def __init__(self, **kwargs):
        super(Hora, self).__init__(**kwargs)
        self.ids.horas.text = '00'
        self.ids.minutos.text = '00'
        self.ids.turno.text = 'AM'

    def incrementar_horas(self):
        horas = int(self.ids.horas.text)

        if horas < 12:
            horas += 1
            self.ids.horas.text = '{:0>2}'.format(horas)

    def decrementar_horas(self):
        horas = int(self.ids.horas.text)

        if horas > 0:
            horas -= 1
            self.ids.horas.text = '{:0>2}'.format(horas)

    def incrementar_minutos(self):
        minutos = int(self.ids.minutos.text)

        if minutos < 59:
            minutos += 1
        else:
            minutos = 0
            horas = int(self.ids.horas.text)
            horas += 1
            if horas > 12:
                horas = 12
            self.ids.horas.text = '{:0>2}'.format(horas)

        self.ids.minutos.text = '{:0>2}'.format(minutos)

    def decrementar_minutos(self):
        minutos = int(self.ids.minutos.text)

        if minutos > 0:
            minutos -= 1
            self.ids.minutos.text = '{:0>2}'.format(minutos)
        else:
            minutos = 59
            horas = int(self.ids.horas.text)
            horas -= 1
            if horas < 0:
                horas = 0
            self.ids.horas.text = '{:0>2}'.format(horas)

        self.ids.minutos.text = '{:0>2}'.format(minutos)
