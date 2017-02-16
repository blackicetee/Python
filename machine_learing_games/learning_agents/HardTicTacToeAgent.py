from machine_learing_games.SearchAlgorithms.PVSAB import PVSAB
from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist
import os

class HardTicTacToeAgent:
    def __init__(self):
        self.__tictactoe = TicTacToe(4)
        self.__ply = ()
        self.__initial_zobtist_array = [[618042568, 930327299], [284711804, 240899320], [452972366, 197023573],
                                        [836929421, 554519585], [268539658, 436146761], [418134785, 778622066],
                                        [306000926, 271913880], [64684604, 747921650], [562074100, 966704345],
                                        [237831172, 520822074], [543782683, 573029485], [69752107, 839681167],
                                        [905138023, 13271461], [189369632, 699607941], [790205890, 642672719],
                                        [767124818, 229722781]]
        self.__zobrist_hashing = TicTacToeZobrist()
        self.__zobrist_hashing.set_zobrist_board_positoin_array(self.__initial_zobtist_array)
        self.__pvsab = PVSAB(self.__zobrist_hashing)

    def action(self, state):
        return self.__pvsab.suggest_action(state)




hard_agent = HardTicTacToeAgent()
ttt = TicTacToe(4)
ttt.make_move(hard_agent.action(ttt))
print ttt.printable_game_matrix()
