import sqlite3


class SQLiteTicTacToeAgentExperience:
    def __init__(self):
        self.connection = sqlite3.connect('tictactoe_agent_experience.dp')
        self.cursor = self.connection.cursor()
        self.create_table_agentExperience()

    def create_table_agentExperience(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS agentExperience(zobrist_hash INTEGER, use_value REAL, alpha_beta_window INTEGER, ply INTEGER, depth INTEGER, player_turn INTEGER)')

    def insert_agent_experience(self, zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn):
        self.cursor.execute(
            "INSERT INTO agentExperience(zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn) VALUES (?, ?, ?, ?, ?, ?)",
            (zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn))
        self.connection.commit()

    def read_from_db(self):
        self.cursor.execute("SELECT * FROM agentExperience WHERE depth=3")
        for row in self.cursor.fetchall():
            print row

    def close_db(self):
        self.cursor.close()
        self.connection.close()
