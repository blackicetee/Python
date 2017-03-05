import sys

from numpy import argmax, argmin

from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from playground_machine_learing.PVS.SQLite import SQLiteDB

count = 1


# TODO alpha beta is incorrect see AlphaBetaSearch.py is fixed alpha beta algorithm
class PVSAB:
    SQLITE_DB_NAME = 'pvsab_transition_table.db'

    def __init__(self, zobrist):
        self.__zobrist = zobrist
        self.__transition_table = SQLiteDB(self.SQLITE_DB_NAME)

    def suggest_action(self, state):
        hash_key = self.__zobrist.get_hash(state.game_matrix)
        if self.__transition_table.is_zobrist_hash_in_db(hash_key):
            return self.__transition_table.get_best_move_of_zobrist_hash_entry(
                self.__zobrist.get_hash(state.game_matrix))
        else:
            self.zobrist_alpha_beta_search(state)
            return self.__transition_table.get_best_move_of_zobrist_hash_entry(
                self.__zobrist.get_hash(state.game_matrix))

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
            list_of_action_utilities.append(self.max_value(self.result(state, action), -sys.maxint, sys.maxint))
        if self.player(state) == 'X':
            best_action_index = argmax(list_of_action_utilities)
        else:
            best_action_index = argmin(list_of_action_utilities)
        usefulness = list_of_action_utilities[best_action_index]
        best_move = str(list_of_actions[best_action_index])
        self.__transition_table.insert_transposition(hash_key, usefulness, -sys.maxint, sys.maxint, best_move,
                                                     state.count_of_game_tokens_in_game(),
                                                     self.__calculate_player_turn(state))
        return list_of_actions[best_action_index], list_of_action_utilities[best_action_index]

    def max_value(self, state, alpha, beta):
        global count
        count += 1
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
            list_of_actions = self.actions(state)
            list_of_action_utilities = []
            for a in list_of_actions:
                alpha = max(alpha, self.min_value(self.result(state, a), alpha, beta))
                list_of_action_utilities.append(alpha)
                if alpha >= beta:
                    return beta
            best_action_index = argmax(list_of_action_utilities)
            alpha = list_of_action_utilities[best_action_index]
            best_move = str(list_of_actions[best_action_index])
            self.__transition_table.insert_transposition(hash_key, alpha, alpha, beta, best_move,
                                                         state.count_of_game_tokens_in_game(),
                                                         self.__calculate_player_turn(state))
            return alpha

    def min_value(self, state, alpha, beta):
        global count
        count += 1
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
            list_of_actions = self.actions(state)
            list_of_action_utilities = []
            for a in list_of_actions:
                beta = min(beta, self.max_value(self.result(state, a), alpha, beta))
                list_of_action_utilities.append(beta)
                if beta <= alpha:
                    return alpha
            best_action_index = argmin(list_of_action_utilities)
            beta = list_of_action_utilities[best_action_index]
            best_move = str(list_of_actions[best_action_index])
            self.__transition_table.insert_transposition(hash_key, beta, alpha, beta, best_move,
                                                         state.count_of_game_tokens_in_game(),
                                                         self.__calculate_player_turn(state))
            return beta

    def actions(self, state):
        return state.get_possible_moves()

    def result(self, state, action):
        copy_state = TicTacToe(4)
        copy_state.initialize_game_matrix_with_another_game_matrix(state)
        copy_state.make_move(action)
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

# ttt_state = TicTacToe(3)
# zobrist_hasing = TicTacToeZobrist()
# pvs = PVSAB(zobrist_hasing)
# #ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0)), (2, 2)),(1, 1))
# #ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0)), (2, 2)), (0, 1))
# #ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (1, 1)), (2, 0)), (1, 2)), (0, 0))
# #ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0))
# #ttt_state = pvs.result(pvs.result(ttt_state, (1, 1)), (2, 0))
# print ttt_state.printable_game_matrix()
# time_before_funciton_call = time.time()
# print pvs.zobrist_alpha_beta_search(ttt_state)
# print 'Time in milliseconds: ' + str(int((time.time() - time_before_funciton_call) * 1000))
# print count
