from machine_learing_games.learning_agents import sqllite
from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist


class EasyTicTacToeAgent:
    def __init__(self):
        self.__tictactoe = TicTacToe(4)
        self.__zobrist_hashing = TicTacToeZobrist()
        self.__db_lite =

    def get_move(self, tictactoe):
        self.__tictactoe = tictactoe
        zobrist_hash = self.__zobrist_hashing.get_hash(tictactoe)

    def __update_experience(self, zobrist_hash, use_value, alpha_beta_window, ply, depth, player_turn):


