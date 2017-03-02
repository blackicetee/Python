import sqlite3


class SQLiteTicTacToeAgentExperience:
    def __init__(self):
        self.connection = sqlite3.connect('tictactoe_agent_experience.dp')
        self.cursor = self.connection.cursor()
        self.create_table_agentExperience()
        self.create_transpositionTable()

    def create_table_agentExperience(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS agentExperience(zobrist_hash INTEGER, use_value REAL, alpha_beta_window INTEGER, ply INTEGER, depth INTEGER, player_turn INTEGER)')

    def create_transpositionTable(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS transpositionTable(zobrist_hash INTEGER, usefulness REAL, alpha INTEGER, beta INTEGER, best_move TEXT, depth INTEGER, player_turn TEXT)')

    def insert_agent_experience(self, zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn):
        self.cursor.execute(
            "INSERT INTO agentExperience(zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn) VALUES (?, ?, ?, ?, ?, ?)",
            (zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn))
        self.connection.commit()

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
        return self.cursor.fetchone()

    def update_usefulness(self, usefulness, z_hash):
        self.cursor.execute("UPDATE transpositionTable Set usefulness = ? WHERE zobrist_hash = ?", [usefulness, z_hash])

    def update_best_move(self, best_move, z_hash):
        self.cursor.execute("UPDATE transpositionTable Set best_move = ? WHERE zobrist_hash = ?", [best_move, z_hash])

    def read_from_db(self):
        self.cursor.execute("SELECT * FROM agentExperience WHERE depth=3")
        for row in self.cursor.fetchall():
            print row

    def close_db(self):
        self.cursor.close()
        self.connection.close()
