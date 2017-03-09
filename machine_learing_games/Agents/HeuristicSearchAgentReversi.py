from machine_learing_games.Agents import RandomAgent
from machine_learing_games.Reversi.Reversi import Reversi
import sys
from numpy import argmax, argmin

def processAction(reversiState=Reversi()):
    action = alpha_beta_iterative_deepening_search(reversiState)
    reversiState.make_move(action[0][0])

def alpha_beta_iterative_deepening_search(state):
    list_of_action_utilities = []
    action_list = actions(state)
    for action in action_list:
        state.make_move(action[0])
        list_of_action_utilities.append(max_value(state, -sys.maxint, sys.maxint, 0, 2))
        state.undo_move()
    if state.player_to_move() == 'B':
        best_action_index = argmax(list_of_action_utilities)
    else:
        best_action_index = argmin(list_of_action_utilities)
    return action_list[best_action_index], list_of_action_utilities[best_action_index]


def max_value(state, alpha, beta, depth, depth_bound):
    if cutoff_test(state, depth, depth_bound):
        return evaluate(state)
    for a in actions(state):
        state.make_move(a[0])
        alpha = max(alpha, min_value(state, alpha, beta, depth+1, depth_bound))
        state.undo_move()
        if alpha >= beta:
            return beta
    return alpha


def min_value(state, alpha, beta, depth, depth_bound):
    if cutoff_test(state, depth, depth_bound):
        return evaluate(state)
    for a in actions(state):
        state.make_move(a[0])
        beta = min(beta, max_value(state, alpha, beta, depth+1, depth_bound))
        state.undo_move()
        if beta <= alpha:
            return alpha
    return beta

def actions(state):
    playerToMove = state.player_to_move()
    return state.suggest_moves(playerToMove)

def cutoff_test(state, depth, depth_bound):
    if state.is_victory():
        return True
    elif depth >= depth_bound:
        return True
    else:
        return False

def evaluate(state):
    score  = 0
    if state.player_to_move() == 'B':
        score += current_mobility(state)
        score += potential_mobility(state)
    elif state.player_to_move() == 'W':
        score -= current_mobility(state)
        score -= potential_mobility(state)
    score += corner_ratio(state)
    score += edge_table(state)
    return score

def current_mobility(state):
    return (len(state.suggest_moves(state.player_to_move())) * 0.01) + (len(state.suggest_moves(state.reverse_player(state.player_to_move()))) * -0.01)

def potential_mobility(state):
    return (state.count_white_tokens_with_adjacent_free_space() * 0.01) + (state.count_black_tokens_with_adjacent_free_space() * -0.01)

def edge_table(state):
    score = 0
    x_squares = [(1,1), (6,1), (1,6), (6,6)]
    c_squares = [(1,0), (0,1), (6,0), (0,6), (7,1), (1,7), (7,6), (6,7)]
    a_squares = [(2,0), (0,2), (5,0), (0,5), (7,2), (2,7), (7,5), (5,7)]
    b_squares = [(3,0), (0,3), (4,0), (0,4), (7,3), (3,7), (7,4), (4,7)]

    for position in x_squares:
        if state.game_matrix[position] == 'B':
            score -= 0.15
        elif state.game_matrix[position] == 'W':
            score += 0.15

    for position in c_squares:
        if state.game_matrix[position] == 'B':
            score -= 0.08
        elif state.game_matrix[position] == 'W':
            score += 0.08

    for position in a_squares:
        if state.game_matrix[position] == 'B':
            score += 0.08
        elif state.game_matrix[position] == 'W':
            score -= 0.08

    for position in b_squares:
        if state.game_matrix[position] == 'B':
            score += 0.06
        elif state.game_matrix[position] == 'W':
            score -= 0.06
    return score

def corner_ratio(state):
    score = 0
    corners = [(0,0), (7,7), (7,0), (0,7)]
    for position in corners:
        if state.game_matrix[position] == 'W':
            score -= 0.25
        elif state.game_matrix[position] == 'B':
            score += 0.25
    return score