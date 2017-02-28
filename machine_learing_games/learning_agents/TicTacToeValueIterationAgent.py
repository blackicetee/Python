

class TicTacToeValueIterationAgent:

    def __init__(self, start_state):
        # initializes table V*(s) for every s in S with 0.
        self.learn_optimal_strategy(start_state)

    def learn_optimal_strategy(self, start_state):
        pass

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