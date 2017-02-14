import sqlite3


class SQLiteDB:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_transpositionTable()

    def create_transpositionTable(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS transpositionTable(zobrist_hash INTEGER, usefulness REAL, alpha INTEGER, beta INTEGER, best_move TEXT, depth INTEGER, player_turn TEXT)')

    def drop_transitionTable(self):
        self.cursor.execute('DROP TABLE IF EXISTS transpositionTable')

    def insert_transposition(self, zobrist_hash, usefulness, alpha, beta, best_move, depth, player_turn):
        self.cursor.execute(
            "INSERT INTO transpositionTable(zobrist_hash, usefulness, alpha, beta, best_move, depth, player_turn) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (zobrist_hash, usefulness, alpha, beta, best_move, depth, player_turn))
        self.connection.commit()

    def is_zobrist_hash_in_db(self, z_hash):
        self.cursor.execute("SELECT * FROM transpositionTable WHERE zobrist_hash = ?", [z_hash])
        if len(self.cursor.fetchall()) == 0:
            return False
        else:
            return True

    def get_zobrist_hash_entry(self, z_hash):
        self.cursor.execute("SELECT * FROM transpositionTable WHERE zobrist_hash = ?", [z_hash])
        return self.cursor.fetchall()

    def get_usefulness_of_zobrist_hash_entry(self, z_hash):
        self.cursor.execute("SELECT usefulness FROM transpositionTable WHERE zobrist_hash = ?", [z_hash])
        result = self.cursor.fetchone()
        return result[0]

    def get_best_move_of_zobrist_hash_entry(self, z_hash):
        self.cursor.execute("SELECT best_move FROM transpositionTable WHERE zobrist_hash = ?", [z_hash])
        result = str(self.cursor.fetchone()[0])
        result = result.translate(None, '()').split(', ')
        result = (int(result[0]), int(result[1]))
        return result


    def update_usefulness(self, usefulness, z_hash):
        self.cursor.execute("UPDATE transpositionTable Set usefulness = ? WHERE zobrist_hash = ?", [usefulness, z_hash])

    def update_best_move(self, best_move, z_hash):
        self.cursor.execute("UPDATE transpositionTable Set best_move = ? WHERE zobrist_hash = ?", [best_move, z_hash])

    def close_db(self):
        self.cursor.close()
        self.connection.close()
