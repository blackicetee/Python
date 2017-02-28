import random


class TicTacToeHeuristicLearningAgent:

    def __init__(self):
        self.__weight_early_positioning = round(random.random(), 4)
        self.__weight_count_pure_connections = round(random.random(), 4)

    def player(self, state):
        if state.count_of_game_tokens_in_game() % 2 == 0:
            return 'X'
        elif state.count_of_game_tokens_in_game() % 2 == 1:
            return 'O'

    def evaluate(self, state):
        score  = 0
        score += self.__weight_early_positioning * self.early_positioning(state)
        score -= self.__weight_count_pure_connections * self.count_pure_connections(state, 'O')
        score += self.__weight_count_pure_connections * self.count_pure_connections(state, 'X')
        return score

    def early_positioning(self, state):
        score = 0
        interesting_early_positions = [(1,1), (1,2), (2,1), (2,2)]
        x_midfields = [midfield for midfield in interesting_early_positions if state.game_matrix[midfield] == 'X']
        if len(x_midfields) == 1:
            score += 0.01
        elif len(x_midfields) == 2:
            score += state.count_tokens_in_pure_connection(x_midfields[0], x_midfields[1], 'X') * 0.1
        return score


    def count_pure_connections(self, state, player_token):
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
        if self.player(state) == player_token:
            score += score * 2
        return score