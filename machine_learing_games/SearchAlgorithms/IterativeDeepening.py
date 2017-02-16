from machine_learing_games.tictactoe.TicTacToe import TicTacToe


def iterative_deepening(state, aim):
    depth_bound = 0
    result = None
    while result is None or result != aim:
        result = depth_search(state, aim, 0, depth_bound)
        depth_bound += 1
    return result


def depth_search(state, aim, current_depth, depth_bound):
    if terminal_test(state):
        return utility(state)
    list_of_actions = actions(state)
    while len(list_of_actions) != 0 and current_depth < depth_bound:
        result = depth_search(move(state, list_of_actions.pop()), aim, current_depth + 1, depth_bound)
        if result == aim:
            return result
    return "no result found!"


def actions(state):
    return state.get_possible_moves()


def move(state, action):
    copy_state = TicTacToe(3)
    copy_state.initialize_game_matrix_with_another_game_matrix(state.game_matrix)
    copy_state.make_move(action)
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

ttt = TicTacToe(3)
print iterative_deepening(ttt, 1)