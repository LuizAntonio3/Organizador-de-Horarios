# tabela de usuarios futuramente num servidor?
cursor.execute("""
       CREATE TABLE usuarios(
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           nome TEXT NOT NULL,
           curso TEXT NOT NULL
       );
       """)

# tabela de materias
cursor.execute("""
       CREATE TABLE materias(
           id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
           nome TEXT NOT NULL,
           dificuldade INTEGER NOT NULL,
           carga_horaria_semanal FLOAT NOT NULL
       );
       """)

# Tabela de horarios livres na semana
cursor.execute("""
       CREATE TABLE horario_livre(
           dia_semana TEXT NOT NULL,
           horas_livres FLOAT NOT NULL
       );
       """)

# Tabela de horarios de estudo
cursor.execute("""
       CREATE TABLE horarios_estudo(
           materia TEXT NOT NULL,
           horas_estudo FLOAT NOT NULL
       );
       """)

Algoritmo :

