from machine_learing_games.tictactoe.TicTacToe import TicTacToe
import sys, time
from numpy import argmax, argmin

count = 1
count_ab_cuts = 0

def alpha_beta_iterative_deepening_search(state):
    list_of_action_utilities = []
    action_list = actions(state)
    for action in action_list:
        state.make_move(action)
        list_of_action_utilities.append(max_value(state, -sys.maxint, sys.maxint, 0, 3))
        state.undo_move()
    if player(state) == 'X':
        best_action_index = argmax(list_of_action_utilities)
    else:
        best_action_index = argmin(list_of_action_utilities)
    return action_list[best_action_index], list_of_action_utilities[best_action_index]


def max_value(state, alpha, beta, depth, depth_bound):
    global count, count_ab_cuts
    count += 1
    if cutoff_test(state, depth, depth_bound):
        return evaluate(state)
    for a in actions(state):
        state.make_move(a)
        alpha = max(alpha, min_value(state, alpha, beta, depth+1, depth_bound))
        state.undo_move()
        if alpha >= beta:
            count_ab_cuts += 1
            return beta
    return alpha


def min_value(state, alpha, beta, depth, depth_bound):
    global count, count_ab_cuts
    count += 1
    if cutoff_test(state, depth, depth_bound):
        return evaluate(state)
    for a in actions(state):
        state.make_move(a)
        beta = min(beta, max_value(state, alpha, beta, depth+1, depth_bound))
        state.undo_move()
        if beta <= alpha:
            count_ab_cuts += 1
            return alpha
    return beta

def actions(state):
    return state.get_possible_moves()

def player(state):
    if state.count_of_game_tokens_in_game() % 2 == 0:
        return 'X'
    elif state.count_of_game_tokens_in_game() % 2 == 1:
        return 'O'


def cutoff_test(state, depth, depth_bound):
    if state.is_victory():
        return True
    elif not state.is_victory() and state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens():
        return True
    elif depth >= depth_bound:
        return True
    else:
        return False


def terminal_test(state):
    if state.is_victory():
        return True
    elif not state.is_victory() and state.count_of_game_tokens_in_game() == state.get_maximal_amount_of_game_tokens():
        return True
    else:
        return False


def evaluate(state):
    score  = 0
    score += early_positioning(state)
    score -= count_pure_connections(state, 'O')
    score += count_pure_connections(state, 'X')
    return score

def early_positioning(state):
    score = 0
    interesting_early_positions = [(1,1), (1,2), (2,1), (2,2)]
    x_midfields = [midfield for midfield in interesting_early_positions if state.game_matrix[midfield] == 'X']
    if len(x_midfields) == 1:
        score += 0.01
    elif len(x_midfields) == 2:
        score += state.count_tokens_in_pure_connection(x_midfields[0], x_midfields[1], 'X') * 0.1
    return score


def count_pure_connections(state, player_token):
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
    for value in victory_relevant_connections.itervalues():
        if value == 1:
            score += 0.01
        if value == 2:
            score += 0.1
        if value == 3:
            score += 0.3
        if value == 4:
            score += 2
    if player(state) == player_token:
        score += score * 2
    return score

state = TicTacToe(4)
state.make_move((1, 1))
state.make_move((2, 0))
state.make_move((1, 0))
state.make_move((2, 1))
state.make_move((1, 2))
state.make_move((2, 2))
print state.printable_game_matrix()
time_before_funciton_call = time.time()
print alpha_beta_iterative_deepening_search(state)
print 'Time in milliseconds: ' + str(int((time.time() - time_before_funciton_call) * 1000))
print count
print count_ab_cuts

