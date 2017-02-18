import unittest

import numpy as np

from machine_learing_games.reversi.Reversi import Reversi


class TestInitializeReversi(unittest.TestCase):
    def test_initialize_reversi_1(self):
        reversi = Reversi()
        print reversi.printable_game_matrix()
        print reversi.get_all_token_positions('W')
        print reversi.suggest_horizontal_moves()
        reversi.make_move((0,0))