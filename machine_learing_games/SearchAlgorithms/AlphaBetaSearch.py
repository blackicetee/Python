from machine_learing_games.tictactoe.TicTacToe import TicTacToe
import sys, time
from numpy import argmax

count = 1

def alpha_beta_search(state):
    list_of_actions = actions(state)
    list_of_action_utilities = []
    for action in list_of_actions:
        list_of_action_utilities.append(min_value(result(state, action), -sys.maxint, sys.maxint))
    best_action_index = argmax(list_of_action_utilities)
    return list_of_actions[best_action_index], list_of_action_utilities[best_action_index]


def max_value(state, alpha, beta):
    global count
    count += 1
    if terminal_test(state):
        return utility(state)
    for a in actions(state):
        alpha = max(alpha, min_value(result(state, a), alpha, beta))
        if alpha >= beta:
            return beta
    return alpha


def min_value(state, alpha, beta):
    global count
    count += 1
    if terminal_test(state):
        return utility(state)
    for a in actions(state):
        beta = min(beta, max_value(result(state, a), alpha, beta))
        print alpha, beta
        if beta <= alpha:
            return alpha
    return beta


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
        return -1
    elif player(state) != 'X' and state.is_victory():
        return 1
    elif state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens() and not state.is_victory():
        return 0

ttt_state = TicTacToe(3)
# state = result(result(result(result(result(result(ttt_state, (0, 0)), (0, 1)), (0,2)), (1,0)), (1,2)), (1,1))
state = result(result(ttt_state, (1, 1)), (2, 0))
#state = result(result(ttt_state, (0, 0)), (0, 1))
print state.printable_game_matrix()
time_before_funciton_call = time.time()
print alpha_beta_search(state)
print 'Time in milliseconds: ' + str(int((time.time() - time_before_funciton_call) * 1000))
print count

