from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist
from machine_learing_games.SQLite.SQLiteDB import SQLiteDB
import sys, time
from numpy import argmax, argmin

#TODO alpha beta is incorrect see AlphaBetaSearch.py is fixed alpha beta algorithm
class PrincipalVariationSearch:
    SQLITE_DB_NAME = 'pvs_transition_table.db'

    def __init__(self, zobrist):
        self.__zobrist = zobrist
        self.__transition_table = SQLiteDB(self.SQLITE_DB_NAME)

    def zobrist_alpha_beta_search(self, state):
        hash_key = self.__zobrist.get_hash(state.game_matrix)
        print hash_key
        print state.printable_game_matrix()
        if self.__transition_table.is_zobrist_hash_in_db(hash_key):
            return self.__transition_table.get_best_move_of_zobrist_hash_entry(
                hash_key), self.__transition_table.get_usefulness_of_zobrist_hash_entry(hash_key)
        list_of_actions = self.actions(state)
        list_of_action_utilities = []
        for action in list_of_actions:
            list_of_action_utilities.append(self.min_value(self.result(state, action), -sys.maxint, sys.maxint))
        best_action_index = argmax(list_of_action_utilities)

        usefulness = list_of_action_utilities[best_action_index]
        best_move = str(list_of_actions[best_action_index])
        self.__transition_table.insert_transposition(hash_key, usefulness, -sys.maxint, sys.maxint, best_move,
                                                     state.count_of_game_tokens_in_game(),
                                                     self.__calculate_player_turn(state))
        return list_of_actions[best_action_index], list_of_action_utilities[best_action_index]

    def max_value(self, state, alpha, beta):
        hash_key = self.__zobrist.get_hash(state.game_matrix)
        print hash_key
        print state.printable_game_matrix()
        if self.__transition_table.is_zobrist_hash_in_db(hash_key):
            return self.__transition_table.get_usefulness_of_zobrist_hash_entry(hash_key)
        else:
            if self.terminal_test(state):
                usefulness = self.utility(state)
                self.__transition_table.insert_transposition(hash_key, usefulness, None, None, None,
                                                             state.count_of_game_tokens_in_game(), None)
                return usefulness
            usefulness = -sys.maxint
            list_of_actions = self.actions(state)
            list_of_action_utilities = []
            for a in list_of_actions:
                list_of_action_utilities.append(max(usefulness, self.min_value(self.result(state, a), alpha, beta)))
            best_action_index = argmax(list_of_action_utilities)
            usefulness = list_of_action_utilities[best_action_index]
            best_move = str(list_of_actions[best_action_index])
            self.__transition_table.insert_transposition(hash_key, usefulness, alpha, beta, best_move,
                                                         state.count_of_game_tokens_in_game(),
                                                         self.__calculate_player_turn(state))
            return list_of_action_utilities[best_action_index]

    def min_value(self, state, alpha, beta):
        hash_key = self.__zobrist.get_hash(state.game_matrix)
        print hash_key
        print state.printable_game_matrix()
        if self.__transition_table.is_zobrist_hash_in_db(hash_key):
            return self.__transition_table.get_usefulness_of_zobrist_hash_entry(hash_key)
        else:
            if self.terminal_test(state):
                usefulness = self.utility(state)
                self.__transition_table.insert_transposition(hash_key, usefulness, None, None, None,
                                                             state.count_of_game_tokens_in_game(), None)
                return usefulness
            usefulness = sys.maxint
            list_of_actions = self.actions(state)
            list_of_action_utilities = []
            for a in list_of_actions:
                list_of_action_utilities.append(min(usefulness, self.max_value(self.result(state, a), alpha, beta)))
                if usefulness <= alpha:
                    return usefulness
                beta = min(beta, usefulness)
            best_action_index = argmin(list_of_action_utilities)
            usefulness = list_of_action_utilities[best_action_index]
            best_move = str(list_of_actions[best_action_index])
            self.__transition_table.insert_transposition(hash_key, usefulness, alpha, beta, best_move,
                                                         state.count_of_game_tokens_in_game(),
                                                         self.__calculate_player_turn(state))
            return list_of_action_utilities[best_action_index]

    def actions(self, state):
        return state.get_possible_moves()

    def result(self, state, action):
        copy_state = TicTacToe(3)
        copy_state.initialize_game_matrix_with_another_game_matrix(state.game_matrix)
        copy_state.put_game_token(self.player(copy_state), action)
        return copy_state

    def player(self, state):
        if state.count_of_game_tokens_in_game() % 2 == 0:
            return 'X'
        elif state.count_of_game_tokens_in_game() % 2 == 1:
            return 'O'

    def terminal_test(self, state):
        if state.is_victory():
            return True
        elif not state.is_victory() and state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens():
            return True
        else:
            return False

    def utility(self, state):
        if self.player(state) == 'X' and state.is_victory():
            return -1
        elif self.player(state) != 'X' and state.is_victory():
            return 1
        elif state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens() and not state.is_victory():
            return 0

    def __calculate_player_turn(self, tictactoe_state=TicTacToe(4)):
        if tictactoe_state.count_of_game_tokens_in_game() % 2 == 0:
            return 'X'
        elif tictactoe_state.count_of_game_tokens_in_game() % 2 == 1:
            return 'O'


# state = result(result(result(result(result(result(ttt_state, (0, 0)), (0, 1)), (0,2)), (1,0)), (1,2)), (1,1))
ttt_state = TicTacToe(3)
zobrist_hasing = TicTacToeZobrist()
pvs = PrincipalVariationSearch(zobrist_hasing)
# ttt_state = pvs.result(
#     pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0)), (2, 2)),
#     (1, 1))
ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0))
print ttt_state.printable_game_matrix()
time_before_funciton_call = time.time()
print pvs.zobrist_alpha_beta_search(ttt_state)
print 'Time in milliseconds: ' + str(int((time.time() - time_before_funciton_call) * 1000))
