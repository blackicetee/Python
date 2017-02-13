from machine_learing_games.tictactoe.TicTacToe import TicTacToe
import sys
import time
from numpy import argmax


def mini_max_decision(state):
    list_of_actions = actions(state)
    list_of_action_utilities = []
    for action in list_of_actions:
        list_of_action_utilities.append(min_value(result(state, action)))
    best_action_index = argmax(list_of_action_utilities)
    return list_of_actions[best_action_index], list_of_action_utilities[best_action_index]


def max_value(state):
    if terminal_test(state):
        return utility(state)
    usefulness = -sys.maxint
    for a in actions(state):
        usefulness = max(usefulness, min_value(result(state, a)))
    return usefulness

def min_value(state):
    if terminal_test(state):
        return utility(state)
    usefulness = sys.maxint
    for a in actions(state):
        usefulness = min(usefulness, max_value(result(state, a)))
    return usefulness


def actions(state):
    return state.get_possible_moves()


def result(state, action):
    copy_state = TicTacToe(3)
    copy_state.initialize_game_matrix_with_another_game_matrix(state.game_matrix)
    copy_state.put_game_token(player(copy_state), action)
    return copy_state


def player(state):
    if state.count_of_game_tokens_in_game() % 2 == 0:
        return 'X'
    elif state.count_of_game_tokens_in_game() % 2 == 1:
        return 'O'


def terminal_test(state):
    if state.is_victory():
        return True
    elif not state.is_victory() and state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens():
        return True
    else:
        return False


def utility(state):
    if player(state) == 'X' and state.is_victory():
        if state.game_matrix[1,0] == 'X':
            print state.printable_game_matrix()
        return -1
    elif player(state) != 'X' and state.is_victory():
        return 1
    elif state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens() and not state.is_victory():
        return 0

ttt_state = TicTacToe(3)
#state = result(result(result(result(result(result(ttt_state, (0, 0)), (0, 1)), (0,2)), (1,0)), (2, 2)), (1, 2))
#state = result(result(result(result(result(result(ttt_state, (0, 0)), (0, 1)), (0,2)), (1,0)), (1, 2)), (2, 0))
state = result(result(result(result(ttt_state, (2, 1)), (2, 0)), (1, 2)), (0, 0))

print state.printable_game_matrix()
time_before_funciton_call = time.time()
print mini_max_decision(state)
print 'Time in milliseconds: ' + str(int((time.time() - time_before_funciton_call) * 1000))