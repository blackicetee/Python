from machine_learing_games.tictactoe.TicTacToe import TicTacToe


def iterative_deepening(state, aim):
    depth_bound = 0
    result = None
    while result is None or result != aim:
        result = depth_search(state, aim, 0, depth_bound)
        depth_bound += 1
    print state.printable_game_matrix()
    return result, state.action_sequence


def depth_search(state, aim, current_depth, depth_bound):
    if terminal_test(state):
        return utility(state)
    list_of_actions = actions(state)
    while len(list_of_actions) != 0 and current_depth < depth_bound:
        state.make_move(list_of_actions.pop())
        result = depth_search(state, aim, current_depth + 1, depth_bound)
        if result == aim:
            return result
        else:
            state.undo_move()
    return "no result found!"


def actions(state):
    return state.get_possible_moves()


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

ttt = TicTacToe(4)
ttt.make_move((1, 1))
ttt.make_move((2, 1))
ttt.make_move((2, 2))
ttt.make_move((1, 2))
print ttt.printable_game_matrix()
print iterative_deepening(ttt, 1)