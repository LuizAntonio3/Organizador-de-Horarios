import os
from kivy.lang import Builder


def load_screens():
    path = 'screens/kv_lang_screens/'

    # implementar algo melhor para ignorar as pastas/arquivos de formatos diferentes de .kv
    ignore = ['__init__.py', 'loader.py', '__pycache__']
    files = os.listdir(path)
    # remove os arquivos que não fazem parte da construção das telas

    for file in ignore:
        if file in files:
            files.remove(file)

    # carrega cada tela
    for file in files:
        with open(path + file, 'r') as screen:
            Builder.load_string(screen.read())
