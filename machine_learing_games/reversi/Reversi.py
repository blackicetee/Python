import numpy as np

class Reversi:
    """Contains rules and logic of the board game Reversi.
    Winning condition of Reversi is to have the most tokens in your color at the end.
    In Reversi you can conquer enemy tokens when they are trapped between two of your tokens.
    Conquering is possible in horizontal, vertical and diagonal.
    Within every move you can put exactly one token.
    The board game needs two players.
    The game ends when the board has no more free spaces.
    The game board is an eight times eight matrix.
    """

    def __init__(self):
        self.__dimension = 8
        self.__game_matrix = np.asmatrix(np.full((self.__dimension, self.__dimension), ' ', dtype=np.matrix))
        self.__game_matrix[3, 3] = 'B'
        self.__game_matrix[4, 4] = 'B'
        self.__game_matrix[4, 3] = 'W'
        self.__game_matrix[3, 4] = 'W'
        self.__action_sequence = []
        self.__black_passed = False
        self.__white_passed = False
        self.__player_to_move = 'B'

    @property
    def game_matrix(self):
        """A matrix which represents the Reversi game board. The game_matrix defines how big the game board is,
        how much game tokens could be placed and where they could be placed. Additionally the game_matrix
        stores the position of every placed game token inside the matrix.

        Returns
        -------
        game_matrix :   numpy.matrix
            The game matrix.
        """
        return self.__game_matrix

    @property
    def action_sequence(self):
        """Is a list of tuples, where every tuple is an action. The list should work like a stack.
        An action is a valid placement of a player token on the game matrix.
        The action sequence is like a representation of every move of one party and a party
        is every move from the beginning until the end of a game.

        Returns
        -------
        list
            A list of tuples, where every tuple is an action. The actions are stored chronologically inside the list,
            from first performed action, to last performed action."""
        return self.__action_sequence

    def printable_game_matrix(self):
        """Returns a good looking string representation of the game matrix property.
        This function is just for better human readability of the game matrix.

        Returns
        -------
        str
            An for human readability optimized string,
            which represents the current state of the game matrix property."""
        print_string = '  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 \n'
        print_string += '----------------------------------\n'
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if col == 0:
                    print_string += str(row) + " | "
                if col == (self.__dimension - 1):
                    print_string += self.__game_matrix[row, col] + '\n'
                    if row != (self.__dimension - 1):
                        print_string += '-' * (4 * self.__dimension + 2) + '\n'
                else:
                    print_string += self.__game_matrix[row, col] + ' | '
        return print_string

    def make_move(self, position):
        if not self.is_victory():
            possible_moves = self.suggest_moves(self.__player_to_move)
            conquered_token_positions = []
            for possible_move in possible_moves:
                if position == possible_move[0]:
                    if self.game_matrix[position] == ' ':
                        self.game_matrix[position] = self.__player_to_move
                    conquered_token_positions += self.conquer_tokens(position, possible_moves)
            self.__action_sequence.append((position, conquered_token_positions))
            self.__player_to_move = self.reverse_player(self.__player_to_move)

    def undo_move(self):
        last_move = self.__action_sequence.pop()
        for conquered_positions in last_move[1]:
            self.__game_matrix[conquered_positions] = self.__player_to_move
        self.__game_matrix[last_move[0]] = ' '
        self.__player_to_move = self.reverse_player(self.__player_to_move)

    def conquer_tokens(self, choosen_position, possible_moves):
        changed_tokens = []
        for move in possible_moves:
            if move[0] == choosen_position:
                for change_token in move[1]:
                    changed_tokens.append(change_token)
                    self.game_matrix[change_token] = self.__player_to_move
        return changed_tokens

    def count_game_tokens(self):
        count = 0
        for row in range(self.__game_matrix.shape[0]):
            for col in range(self.__game_matrix.shape[1]):
                if self.__game_matrix[row, col] != ' ':
                    count += 1
        return count

    def is_free_space_adjacent_to_token_position(self, token_position):
        row = token_position[0]
        col = token_position[1]
        possible_adjacent_free_spaces = []
        if row - 1 >= 0 and col - 1 >= 0:
            possible_adjacent_free_spaces.append((row - 1, col - 1))
        if row + 1 <= 7 and col + 1 <= 7:
            possible_adjacent_free_spaces.append((row + 1, col + 1))
        if row - 1 >= 0 and col + 1 <= 7:
            possible_adjacent_free_spaces.append((row - 1, col + 1))
        if row + 1 <= 7 and col - 1 >= 0:
            possible_adjacent_free_spaces.append((row + 1, col - 1))
        if col + 1 <= 7:
            possible_adjacent_free_spaces.append((row, col + 1))
        if col - 1 >= 0:
            possible_adjacent_free_spaces.append((row, col - 1))
        if row + 1 <= 7:
            possible_adjacent_free_spaces.append((row + 1, col))
        if row - 1 >= 0:
            possible_adjacent_free_spaces.append((row - 1, col))
        for position in possible_adjacent_free_spaces:
            if self.game_matrix[position] == ' ':
                return True
        return False

    def count_black_tokens_with_adjacent_free_space(self):
        count = 0
        black_tokens = self.get_all_token_positions('B')
        for token in black_tokens:
            if self.is_free_space_adjacent_to_token_position(token):
                count += 1
        return count

    def count_white_tokens_with_adjacent_free_space(self):
        count = 0
        white_tokens = self.get_all_token_positions('W')
        for token in white_tokens:
            if self.is_free_space_adjacent_to_token_position(token):
                count += 1
        return count

    def count_all_black_tokens(self):
        black_tokens = self.get_all_token_positions('B')
        return len(black_tokens)

    def count_all_white_tokens(self):
        white_tokens = self.get_all_token_positions('W')
        return len(white_tokens)

    def player_to_move(self):
        black_moves = self.suggest_moves('B')
        white_moves = self.suggest_moves('W')

        if len(black_moves) == 0:
            self.__black_passed = True
        else:
            self.__black_passed = False
        if len(white_moves) == 0:
            self.__white_passed = True
        else:
            self.__white_passed = False

        if self.__player_to_move == 'B' and self.__black_passed:
                self.__player_to_move = 'W'
        elif self.__player_to_move == 'W' and self.__white_passed:
                self.__player_to_move = 'B'
        elif self.__black_passed and self.__white_passed:
            return 'Game Over'

        return self.__player_to_move


    def reverse_player(self, player_to_reverse):
        if player_to_reverse == 'B':
            return 'W'
        elif player_to_reverse == 'W':
            return 'B'

    def get_all_token_positions(self, token_type):
        token_positions = []
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if self.__game_matrix[row, col] == token_type:
                    token_positions.append((row, col))
        return token_positions

    def is_victory(self):
        self.player_to_move()
        if self.__black_passed and self.__white_passed:
            return True
        else:
            return False

    def game_result(self):
        return ('Black', self.count_all_black_tokens()), ('White', self.count_all_white_tokens())

    def suggest_moves(self, player_to_move):
        return self.suggest_horizontal_moves(player_to_move) + self.suggest_vertical_moves(
            player_to_move) + self.suggest_diagonal_moves(player_to_move)


    def suggest_horizontal_moves(self, player_to_move):
        horizontal_moves = []
        token_positions = self.get_all_token_positions(player_to_move)
        for position in token_positions:
            horizontal_move_right = self.suggest_horizontal_move_right(position, player_to_move)
            horizontal_move_left = self.suggest_horizontal_move_left(position, player_to_move)
            if horizontal_move_right is not None:
                horizontal_moves.append(horizontal_move_right)
            if horizontal_move_left is not None:
                horizontal_moves.append(horizontal_move_left)
        return horizontal_moves


    def suggest_horizontal_move_right(self, position, player_to_move):
        conquered_token_positions = []
        for col in range(position[1] + 1, 8):
            if self.__game_matrix[position[0], col] == self.reverse_player(player_to_move):
                conquered_token_positions.append((position[0], col))
            elif self.__game_matrix[position[0], col] == ' ':
                if len(conquered_token_positions) > 0:
                    return (position[0], col), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[position[0], col] == player_to_move:
                return None
        return None


    def suggest_horizontal_move_left(self, position, player_to_move):
        conquered_token_positions = []
        for col in reversed(range(position[1])):
            if self.__game_matrix[position[0], col] == self.reverse_player(player_to_move):
                conquered_token_positions.append((position[0], col))
            elif self.__game_matrix[position[0], col] == ' ':
                if len(conquered_token_positions) > 0:
                    return (position[0], col), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[position[0], col] == player_to_move:
                return None
        return None


    def suggest_vertical_moves(self, player_to_move):
        vertical_moves = []
        token_positions = self.get_all_token_positions(player_to_move)
        for position in token_positions:
            vertical_move_right = self.suggest_vertical_move_bottom(position, player_to_move)
            vertical_move_left = self.suggest_vertical_move_top(position, player_to_move)
            if vertical_move_right is not None:
                vertical_moves.append(vertical_move_right)
            if vertical_move_left is not None:
                vertical_moves.append(vertical_move_left)
        return vertical_moves


    def suggest_vertical_move_bottom(self, position, player_to_move):
        conquered_token_positions = []
        for row in range(position[0] + 1, 8):
            if self.__game_matrix[row, position[1]] == self.reverse_player(player_to_move):
                conquered_token_positions.append((row, position[1]))
            elif self.__game_matrix[row, position[1]] == ' ':
                if len(conquered_token_positions) > 0:
                    return (row, position[1]), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[row, position[1]] == player_to_move:
                return None
        return None


    def suggest_vertical_move_top(self, position, player_to_move):
        conquered_token_positions = []
        for row in reversed(range(position[0])):
            if self.__game_matrix[row, position[1]] == self.reverse_player(player_to_move):
                conquered_token_positions.append((row, position[1]))
            elif self.__game_matrix[row, position[1]] == ' ':
                if len(conquered_token_positions) > 0:
                    return (row, position[1]), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[row, position[1]] == player_to_move:
                return None
        return None


    def suggest_diagonal_moves(self, player_to_move):
        diagonal_moves = []
        token_positions = self.get_all_token_positions(player_to_move)
        for position in token_positions:
            diagonal_move_top_right = self.suggest_diagonal_move_top_right(position, player_to_move)
            diagonal_move_top_left = self.suggest_diagonal_move_top_left(position, player_to_move)
            diagonal_move_bottom_left = self.suggest_diagonal_move_bottom_left(position, player_to_move)
            diagonal_move_bottom_right = self.suggest_diagonal_move_bottom_right(position, player_to_move)
            if diagonal_move_top_right is not None:
                diagonal_moves.append(diagonal_move_top_right)
            if diagonal_move_top_left is not None:
                diagonal_moves.append(diagonal_move_top_left)
            if diagonal_move_bottom_left is not None:
                diagonal_moves.append(diagonal_move_bottom_left)
            if diagonal_move_bottom_right is not None:
                diagonal_moves.append(diagonal_move_bottom_right)
        return diagonal_moves


    def suggest_diagonal_move_top_left(self, position, player_to_move):
        conquered_token_positions = []
        while (position[0] - len(conquered_token_positions)) > 0 and (position[1] - len(conquered_token_positions)) > 0:
            row = (position[0] - 1) - len(conquered_token_positions)
            col = (position[1] - 1) - len(conquered_token_positions)
            if self.__game_matrix[row, col] == self.reverse_player(player_to_move):
                conquered_token_positions.append((row, col))
            elif self.__game_matrix[row, col] == ' ':
                if len(conquered_token_positions) > 0:
                    return (row, col), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[row, col] == player_to_move:
                return None
        return None


    def suggest_diagonal_move_top_right(self, position, player_to_move):
        conquered_token_positions = []
        while (position[0] - len(conquered_token_positions)) > 0 and (position[1] + len(conquered_token_positions)) < 7:
            row = (position[0] - 1) - len(conquered_token_positions)
            col = (position[1] + 1) + len(conquered_token_positions)
            if self.__game_matrix[row, col] == self.reverse_player(player_to_move):
                conquered_token_positions.append((row, col))
            elif self.__game_matrix[row, col] == ' ':
                if len(conquered_token_positions) > 0:
                    return (row, col), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[row, col] == player_to_move:
                return None
        return None


    def suggest_diagonal_move_bottom_left(self, position, player_to_move):
        conquered_token_positions = []
        while (position[0] + len(conquered_token_positions)) < 7 and (position[1] - len(conquered_token_positions)) > 0:
            row = (position[0] + 1) + len(conquered_token_positions)
            col = (position[1] - 1) - len(conquered_token_positions)
            if self.__game_matrix[row, col] == self.reverse_player(player_to_move):
                conquered_token_positions.append((row, col))
            elif self.__game_matrix[row, col] == ' ':
                if len(conquered_token_positions) > 0:
                    return (row, col), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[row, col] == player_to_move:
                return None
        return None


    def suggest_diagonal_move_bottom_right(self, position, player_to_move):
        conquered_token_positions = []
        while (position[0] + len(conquered_token_positions)) < 7 and (position[1] + len(conquered_token_positions)) < 7:
            row = (position[0] + 1) + len(conquered_token_positions)
            col = (position[1] + 1) + len(conquered_token_positions)
            if self.__game_matrix[row, col] == self.reverse_player(player_to_move):
                conquered_token_positions.append((row, col))
            elif self.__game_matrix[row, col] == ' ':
                if len(conquered_token_positions) > 0:
                    return (row, col), conquered_token_positions
                else:
                    return None
            elif self.__game_matrix[row, col] == player_to_move:
                return None
        return None