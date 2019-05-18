# cursor.execute("""
# CREATE TABLE horarios_estudo(
#     materia TEXT NOT NULL,
#     horas_estudo FLOAT NOT NULL
# );
# """)
    # def add_study_time(self, materia, horas_livres):
    # def get_study_time(self):

def generate_study_time(MyDb):
    for materia in MyDb.get_subjects():
        nome_materia = materia[1]
        dificuldade = materia[2]
        carga_horaria = materia[3]

        print('nome_materia: {}'.format(nome_materia))
        print('dificuldade: {}'.format(dificuldade))
        print('carga_horaria: {}'.format(carga_horaria))
