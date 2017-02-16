from random import randint

from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist
from machine_learing_games.SQLite.SQLiteDB import SQLiteDB
import sys, time
from numpy import argmax, argmin

count = 1

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
        copy_state = TicTacToe(4)
        copy_state.initialize_game_matrix_with_another_game_matrix(state.game_matrix)
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

    def evaluate(self, state):
        score  = 0
        level_coefficient = state.count_of_game_tokens_in_game()
        score += self.__early_positioning(state)
        score -= self.__count_pure_connections(state, 'O')
        score += self.__count_pure_connections(state, 'X')
        return score

    def __pick_random_position(self, positions):
        random_agent_move = positions[randint(0, (len(positions) - 1))]
        return random_agent_move

    def __early_positioning(self, state):
        score = 0
        interesting_early_positions = [(1,1), (1,2), (2,1), (2,2)]
        x_midfields = [midfield for midfield in interesting_early_positions if state.game_matrix[midfield] == 'X']
        if len(x_midfields) == 1:
            score += 0.01
        elif len(x_midfields) == 2:
            score += state.count_tokens_in_pure_connection(x_midfields[0], x_midfields[1], 'X') * 0.1
        return score

    def __count_pure_connections(self, state, player_token):
        score = 0
        victory_relevant_connections = {"h0": state.count_tokens_in_pure_connection((0, 0), (0, 1), player_token),
                                        "h1": state.count_tokens_in_pure_connection((1, 0), (1, 1), player_token),
                                        "h2": state.count_tokens_in_pure_connection((2, 0), (2, 1), player_token),
                                        "h3": state.count_tokens_in_pure_connection((3, 0), (3, 1), player_token),
                                        "v0": state.count_tokens_in_pure_connection((0, 0), (1, 0), player_token),
                                        "v1": state.count_tokens_in_pure_connection((0, 1), (1, 1), player_token),
                                        "v2": state.count_tokens_in_pure_connection((0, 2), (1, 2), player_token),
                                        "v3": state.count_tokens_in_pure_connection((0, 3), (1, 3), player_token),
                                        "d0": state.count_tokens_in_pure_connection((0, 0), (1, 1), player_token),
                                        "d1": state.count_tokens_in_pure_connection((3, 0), (2, 1), player_token)}
        print victory_relevant_connections
        for value in victory_relevant_connections.itervalues():
            if value == 1:
                score += 0.01
            if value == 2:
                score += 0.1
            if value == 3:
                score += 0.3
        if self.__calculate_player_turn(state) == player_token:
            score += score * 2
        return score

    def __calculate_player_turn(self, tictactoe_state=TicTacToe(4)):
        if tictactoe_state.count_of_game_tokens_in_game() % 2 == 0:
            return 'X'
        elif tictactoe_state.count_of_game_tokens_in_game() % 2 == 1:
            return 'O'


# state = result(result(result(result(result(result(ttt_state, (0, 0)), (0, 1)), (0,2)), (1,0)), (1,2)), (1,1))
ttt_state = TicTacToe(4)
zobrist_hasing = TicTacToeZobrist()
pvs = PrincipalVariationSearch(zobrist_hasing)
# ttt_state = pvs.result(
#     pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0)), (2, 2)),
#     (1, 1))
#ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0))
ttt_state = pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(pvs.result(ttt_state, (1, 1)), (2, 0)), (2, 1)), (0, 0)), (0, 1)), (3, 1)), (2, 2)), (1, 0))
#ttt_state = pvs.result(pvs.result(ttt_state, (1, 1)), (2, 0))
# print ttt_state.printable_game_matrix()
# time_before_funciton_call = time.time()
# print pvs.zobrist_alpha_beta_search(ttt_state)
# print 'Time in milliseconds: ' + str(int((time.time() - time_before_funciton_call) * 1000))
# print count
print ttt_state.printable_game_matrix()
print pvs.evaluate(ttt_state)