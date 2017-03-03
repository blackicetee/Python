import numpy as np
from random import SystemRandom


class TicTacToeZobrist:
    def __init__(self):
        secure_random = SystemRandom()
        # for every field(total 16 fields) of the tictactoe game matrix two random values for X's and O's are created.
        self.zArray = [[secure_random.randrange(1000000000), secure_random.randrange(1000000000)] for i in range(16)]

    def get_zobrist_board_position_array(self):
        return self.zArray

    def set_zobrist_board_positoin_array(self, zobrist_board_position_array):
        self.zArray = zobrist_board_position_array

    def get_hash(self, tictactoe_game_matrix):
        zobrist_key = 0
        tictactoe_game_fields = self.transform_game_matrix_to_one_dimensional_list(tictactoe_game_matrix)
        for i in range(len(tictactoe_game_fields)):
            if tictactoe_game_fields[i] == 'X':
                zobrist_key ^= self.zArray[i][0]
            elif tictactoe_game_fields[i] == 'O':
                zobrist_key ^= self.zArray[i][1]
        return zobrist_key

    def transform_game_matrix_to_one_dimensional_list(self, tictactoe_game_matrix):
        one_dimensional_list = []
        for row in range(tictactoe_game_matrix.shape[0]):
            for col in range(tictactoe_game_matrix.shape[1]):
                one_dimensional_list.append(tictactoe_game_matrix[row, col])
        return one_dimensional_list

    def getFixedTicTacToeZobristBoardPositionArray(self):
        return [[945187131, 648139399],
                [717098135, 182172448],
                [815387026, 923854592],
                [187502661, 689921202],
                [347529029, 550423936],
                [703800998, 718138000],
                [509475670, 322874787],
                [139421107, 312807264],
                [873091254, 304573307],
                [193740030, 858228105],
                [747189435, 505301406],
                [545830171, 203578078],
                [293355347, 858867448],
                [483082797, 357710513],
                [789749577, 154225799],
                [864851688, 344911706]]


