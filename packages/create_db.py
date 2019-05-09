import sqlite3 as sql
import os


class Database:
    def __init__(self, _db_name):
        # variavel auxiliar para identificar se o aplicativo esta sendo utilizado pela primeira vez
        self.first_run = True

        # criação do banco de dados e suas tabelas
        self.__db_name = _db_name
        self.db_conn = self.connect_db()

        self.cursor = self.db_conn.cursor()

    def connect_db(self):
        # verifica se o banco de dados com o determinado nome existe
        if not os.path.isfile(self.__db_name):
            conn = sql.connect(self.__db_name)
            self.__create_tables(conn)
            return conn
        else:
            self.first_run = False
            return sql.connect(self.__db_name)

    @staticmethod
    def __create_tables(conn):
        cursor = conn.cursor()

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
            nome TEXT NOT NULL,
            horas_livres FLOAT NOT NULL
        );
        """)

        semana = [('segunda-feira', 0), ('terça-feira', 0), ('quarta-feira', 0), ('quinta-feira', 0), ('sexta-feira', 0), ('sabado', 0), ('domingo', 0)]

        cursor.executemany("""
        INSERT INTO horario_livre(nome, horas_livres)
        VALUES(?, ?)
        """, semana)

        conn.commit()

    def add_user(self, nome, curso):
        # adiciona a tabela usuarios um novo usuario
        self.cursor.execute("""
        INSERT INTO usuarios(nome, curso)
        VALUES (?, ?)
        """, (nome, curso))

        self.db_conn.commit()
        print('usuario adicionado com sucesso')

    def get_users(self):
        # retorna todos os usuarios da tabela usuarios
        self.cursor.execute("""
        SELECT * FROM usuarios
        """)

        return self.cursor.fetchall()

    def add_subjects(self, nome, dificuldade, carga_horaria_semanal):
        self.cursor.execute("""
        INSERT INTO materias(nome, dificuldade, carga_horaria_semanal)
        VALUES (?, ?, ?)
        """, (nome, dificuldade, carga_horaria_semanal))

        self.db_conn.commit()
        print('materia adicionado com sucesso')

    def get_subjects(self):
        self.cursor.execute("""
        SELECT * FROM materias
        """)

        materias = self.cursor.fetchall()

        return materias

    # @ apenas para debugging
    def get_free_time(self):
        self.cursor.execute("""
        SELECT * FROM horario_livre
        """)

        free_time = self.cursor.fetchall()

        return free_time

    def add_free_time(self, dia_semana, horas):
        self.cursor.execute("""
        UPDATE horario_livre
        SET horas_livres = (?)
        WHERE nome = (?)
        """, (horas, dia_semana))

        self.db_conn.commit()
        print('horario atualizado com sucesso')
