import numpy as np
# TODO make this class a library of procedures - one procedure should return a random game situation
# TODO Implements this file a production system for reversi game situations?

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
        print_string = ''
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if col == (self.__dimension - 1):
                    print_string += self.__game_matrix[row, col] + '\n'
                    if row != (self.__dimension - 1):
                        print_string += '-' * (4 * self.__dimension - 3) + '\n'
                else:
                    print_string += self.__game_matrix[row, col] + ' | '
        return print_string

    def make_move(self, position):
        possible_moves = self.get_all_possible_moves()
        if position in possible_moves:
            self.game_matrix[position] = self.get_player_to_move()
            #self.__conquer_enemy_game_tokens(position)
            return True
        else:
            return False

    def count_game_tokens(self):
        count = 0
        for row in range(self.__game_matrix.shape[0]):
            for col in range(self.__game_matrix.shape[1]):
                if self.__game_matrix[row, col] != ' ':
                    count += 1
        return count

    def get_player_to_move(self):
        if self.count_game_tokens() % 2 == 0:
            return 'B'
        elif self.count_game_tokens() % 2 == 1:
            return 'W'

    def get_player_not_to_move(self):
        if self.count_game_tokens() % 2 == 0:
            return 'W'
        elif self.count_game_tokens() % 2 == 1:
            return 'B'

    def __conquer_enemy_game_tokens(self, game_token_position):
        self.__conquer_horizontal_enemy_tokens(game_token_position)
        self.__conquer_vertical_enemy_tokens(game_token_position)
        self.__conquer_diagonal_enemy_tokens(game_token_position)

    def __conquer_horizontal_enemy_tokens(self, game_token_position):
        self.__conquer_horizontal_left_enemy_tokens(game_token_position, game_token_position)
        self.__conquer_horizontal_right_enemy_tokens(game_token_position, game_token_position)

    def __conquer_vertical_enemy_tokens(self, game_token_position):
        self.__conquer_vertical_top_enemy_tokens(game_token_position, game_token_position)
        self.__conquer_vertical_bottom_enemy_tokens(game_token_position, game_token_position)

    def __conquer_diagonal_enemy_tokens(self, game_token_position):
        self.__conquer_diagonal_top_left_enemy_tokens(game_token_position, game_token_position)
        self.__conquer_diagonal_bottom_right_enemy_tokens(game_token_position, game_token_position)
        self.__conquer_diagonal_top_right_enemy_tokens(game_token_position, game_token_position)
        self.__conquer_diagonal_bottom_left_enemy_tokens(game_token_position, game_token_position)

    def __conquer_horizontal_left_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[1] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_horizontal_left_enemy_tokens(initial_token_position,
                                                            (current_token_position[0], current_token_position[1] - 1))
            elif current_token_value == initial_token_value:
                self.__conquer_every_left_enemy_token(initial_token_value,
                                                      (current_token_position[0], current_token_position[1] + 1))

    def __conquer_every_left_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_left_enemy_token(initial_token_value,
                                                  (current_token_position[0], current_token_position[1] + 1))

    def __conquer_horizontal_right_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[1] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_horizontal_right_enemy_tokens(initial_token_position,
                                                             (current_token_position[0], current_token_position[1] + 1))
            elif current_token_value == initial_token_value:
                self.__conquer_every_right_enemy_token(initial_token_value,
                                                       (current_token_position[0], current_token_position[1] - 1))

    def __conquer_every_right_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_right_enemy_token(initial_token_value,
                                                   (current_token_position[0], current_token_position[1] - 1))

    def __conquer_vertical_top_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[0] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_vertical_top_enemy_tokens(initial_token_position,
                                                         (current_token_position[0] - 1, current_token_position[1]))
            elif current_token_value == initial_token_value:
                self.__conquer_every_top_enemy_token(initial_token_value,
                                                     (current_token_position[0] + 1, current_token_position[1]))

    def __conquer_every_top_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_top_enemy_token(initial_token_value,
                                                 (current_token_position[0] + 1, current_token_position[1]))

    def __conquer_vertical_bottom_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[0] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_vertical_bottom_enemy_tokens(initial_token_position,
                                                            (current_token_position[0] + 1, current_token_position[1]))
            elif current_token_value == initial_token_value:
                self.__conquer_every_bottom_enemy_token(initial_token_value,
                                                        (current_token_position[0] - 1, current_token_position[1]))

    def __conquer_every_bottom_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_bottom_enemy_token(initial_token_value,
                                                    (current_token_position[0] - 1, current_token_position[1]))

    def __conquer_diagonal_top_left_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[0] >= 0 and 8 > current_token_position[1] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_diagonal_top_left_enemy_tokens(initial_token_position,
                                                              (current_token_position[0] - 1,
                                                               current_token_position[1] - 1))
            elif current_token_value == initial_token_value:
                self.__conquer_every_top_left_enemy_token(initial_token_value,
                                                          (
                                                              current_token_position[0] + 1,
                                                              current_token_position[1] + 1))

    def __conquer_every_top_left_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_top_left_enemy_token(initial_token_value,
                                                      (current_token_position[0] + 1, current_token_position[1] + 1))

    def __conquer_diagonal_bottom_right_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[0] >= 0 and 8 > current_token_position[1] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_diagonal_bottom_right_enemy_tokens(initial_token_position,
                                                                  (current_token_position[0] + 1,
                                                                   current_token_position[1] + 1))
            elif current_token_value == initial_token_value:
                self.__conquer_every_bottom_right_enemy_token(initial_token_value,
                                                              (current_token_position[0] - 1,
                                                               current_token_position[1] - 1))

    def __conquer_every_bottom_right_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_bottom_right_enemy_token(initial_token_value,
                                                          (
                                                              current_token_position[0] - 1,
                                                              current_token_position[1] - 1))

    def __conquer_diagonal_top_right_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[0] >= 0 and 8 > current_token_position[1] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_diagonal_top_right_enemy_tokens(initial_token_position,
                                                               (current_token_position[0] - 1,
                                                                current_token_position[1] + 1))
            elif current_token_value == initial_token_value:
                self.__conquer_every_top_right_enemy_token(initial_token_value,
                                                           (
                                                               current_token_position[0] + 1,
                                                               current_token_position[1] - 1))

    def __conquer_every_top_right_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_top_right_enemy_token(initial_token_value,
                                                       (current_token_position[0] + 1, current_token_position[1] - 1))

    def __conquer_diagonal_bottom_left_enemy_tokens(self, initial_token_position, current_token_position):
        if 8 > current_token_position[0] >= 0 and 8 > current_token_position[1] >= 0:
            current_token_value = self.game_matrix[current_token_position]
            initial_token_value = self.game_matrix[initial_token_position]
            if initial_token_position == current_token_position or current_token_value != initial_token_value:
                self.__conquer_diagonal_bottom_left_enemy_tokens(initial_token_position,
                                                                 (current_token_position[0] + 1,
                                                                  current_token_position[1] - 1))
            elif current_token_value == initial_token_value:
                self.__conquer_every_bottom_left_enemy_token(initial_token_value,
                                                             (
                                                                 current_token_position[0] - 1,
                                                                 current_token_position[1] + 1))

    def __conquer_every_bottom_left_enemy_token(self, initial_token_value, current_token_position):
        if self.__reverse_game_token_value(initial_token_value) == self.game_matrix[current_token_position]:
            self.game_matrix[current_token_position] = initial_token_value
            self.__conquer_every_bottom_left_enemy_token(initial_token_value,
                                                         (current_token_position[0] - 1, current_token_position[1] + 1))


    def __reverse_game_token_value(self, game_token_value):
        if game_token_value == 1.0:
            return 2.0
        elif game_token_value == 2.0:
            return 1.0
        else:
            raise ValueError("game_token_value needs to be '1.0' or '2.0'!")

    def get_all_possible_moves(self):
        """Suggests all possible moves for every token of one color.

        Returns
        -------
        list
            A sorted set of all token move suggestions which are found for every token of one color.
            Set means that the positions are unique.
            The set will be sorted like this [(0, 0), (0, 1), (1, 2) ... (5, 5), (5, 6), (6, 0)].
        """
        suggested_moves = []
        for row in range(8):
            for col in range(8):
                if self.game_matrix[row, col] == self.get_player_to_move():
                    suggested_moves += self.__suggest_moves_for_a_token((row, col))
        return sorted(sorted(set(suggested_moves), key=lambda tup: tup[1]), key=lambda tup: tup[0])

    def __suggest_moves_for_a_token(self, token_position):
        """Suggests all possible moves for a specified token position.

        Parameters
        ----------
        token_position : tuple
            Is a tuple of two integer values.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the column.

        Returns
        -------
        list
            A list of all token move suggestions which are found for a specified token position.

        """
        suggestion_horizontal_left = self.__suggest_horizontal_move(token_position, token_position, True)
        suggestion_horizontal_right = self.__suggest_horizontal_move(token_position, token_position, False)
        suggestion_vertical_top = self.__suggest_vertical_move(token_position, token_position, True)
        suggestion_vertical_bottom = self.__suggest_vertical_move(token_position, token_position, False)
        suggestion_diagonal_top_left = self.__suggest_diagonal_move_from_top_left_to_bottom_right(token_position,
                                                                                                  token_position, True)
        suggestion_diagonal_bottom_right = self.__suggest_diagonal_move_from_top_left_to_bottom_right(token_position,
                                                                                                      token_position,
                                                                                                      False)
        suggestion_diagonal_top_right = self.__suggest_diagonal_move_from_top_right_to_bottom_left(token_position,
                                                                                                   token_position,
                                                                                                   True)
        suggestion_diagonal_bottom_left = self.__suggest_diagonal_move_from_top_right_to_bottom_left(token_position,
                                                                                                     token_position,
                                                                                                     False)
        all_suggestions_for_one_token = suggestion_horizontal_left + suggestion_horizontal_right + \
                                        suggestion_vertical_top + suggestion_vertical_bottom + \
                                        suggestion_diagonal_top_left + suggestion_diagonal_bottom_right + \
                                        suggestion_diagonal_top_right + suggestion_diagonal_bottom_left
        return all_suggestions_for_one_token

    def suggest_horizontal_moves(self):
        horizontal_moves = []
        token_positions = self.get_all_token_positions(self.get_player_to_move())
        for position in token_positions:
            horizontal_move_right = self.suggest_horizontal_move_right(position)
            if horizontal_move_right is not None:
                horizontal_moves.append(horizontal_move_right)
            #horizontal_moves.append(self.suggest_horizontal_move_left)
        return horizontal_moves

    def suggest_horizontal_move_right(self, position):
        conquered_token_positions = []
        for col in range(position[1] + 1, 8):
            if self.__game_matrix[position[0], col] == self.get_player_not_to_move():
                conquered_token_positions.append((position[0], col))
            elif self.__game_matrix[position[0], col] == ' ':
                return (position[0], col), conquered_token_positions
            elif self.__game_matrix[position[0], col] == self.get_player_to_move():
                return None
        return None


    def get_all_token_positions(self, token_type):
        token_positions = []
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if self.__game_matrix[row, col] == token_type:
                    token_positions.append((row, col))
        return token_positions

    def __suggest_horizontal_move(self, initial_token_position, token_position, is_left, is_conquered=False):
        """Suggests a possible horizontal token move to the left or to the right from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_position : tuple
            A tuple which specifies the initial token position.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        token_position : tuple
            A tuple which should be initialized with the initial token position,
            but this token_position will change its value when the function iterates over tokens.

        is_left : bool
            True when a move suggestion in the left direction should be found.
            False when a move suggestion in the right direction should be found.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        list
            If a valid token move suggestion is found it returns the position of it.
            It returns an empty list if no suggestion is found.
        """
        if 8 > token_position[1] >= 0:
            token_value = self.game_matrix[token_position[0], token_position[1]]
            initial_token_value = self.game_matrix[initial_token_position[0], initial_token_position[1]]
            if token_value == 0.0 and is_conquered:
                return [(token_position[0], token_position[1])]
            elif token_value == 0.0 and not is_conquered:
                return []
            elif token_value == initial_token_value and is_conquered:
                return []
            elif initial_token_position == token_position and not is_left:
                return self.__suggest_horizontal_move(initial_token_position,
                                                      (token_position[0], token_position[1] + 1), False,
                                                      False)
            elif token_value != initial_token_value and not is_left:
                return self.__suggest_horizontal_move(initial_token_position,
                                                      (token_position[0], token_position[1] + 1), False,
                                                      True)
            elif initial_token_position == token_position and is_left:
                return self.__suggest_horizontal_move(initial_token_position,
                                                      (token_position[0], token_position[1] - 1), True,
                                                      False)
            elif token_value != initial_token_value and is_left:
                return self.__suggest_horizontal_move(initial_token_position,
                                                      (token_position[0], token_position[1] - 1), True,
                                                      True)
            else:
                return []
        else:
            return []

    def __suggest_vertical_move(self, initial_token_position, token_position, is_top, is_conquered=False):
        """Suggests a possible vertical token move to the top or to the bottom from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_position : tuple
            A tuple which specifies the initial token position.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        token_position : tuple
            A tuple which should be initialized with the initial token position,
            but this token_position will change its value when the function iterates over tokens.

        is_top : bool
            True when a move suggestion in the upper direction should be found.
            False when a move suggestion in the lower direction should be found.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        list
            If a valid token move suggestion is found it returns the position of it.
            It returns an empty list if no suggestion is found.
        """
        if 8 > token_position[0] >= 0:
            token_value = self.game_matrix[token_position[0], token_position[1]]
            initial_token_value = self.game_matrix[initial_token_position[0], initial_token_position[1]]
            if token_value == 0.0 and is_conquered:
                return [(token_position[0], token_position[1])]
            elif token_value == 0.0 and not is_conquered:
                return []
            elif token_value == initial_token_value and is_conquered:
                return []
            elif initial_token_position == token_position and not is_top:
                return self.__suggest_vertical_move(initial_token_position,
                                                    (token_position[0] + 1, token_position[1]), False,
                                                    False)
            elif token_value != initial_token_value and not is_top:
                return self.__suggest_vertical_move(initial_token_position,
                                                    (token_position[0] + 1, token_position[1]), False,
                                                    True)
            elif initial_token_position == token_position and is_top:
                return self.__suggest_vertical_move(initial_token_position,
                                                    (token_position[0] - 1, token_position[1]), True,
                                                    False)
            elif token_value != initial_token_value and is_top:
                return self.__suggest_vertical_move(initial_token_position,
                                                    (token_position[0] - 1, token_position[1]), True,
                                                    True)
            else:
                return []
        else:
            return []

    def __suggest_diagonal_move_from_top_left_to_bottom_right(self, initial_token_position, token_position, is_top_left,
                                                              is_conquered=False):
        """Suggests a possible diagonal token move to the top-left or to the bottom-right from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_position : tuple
            A tuple which specifies the initial token position.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        token_position : tuple
            A tuple which should be initialized with the initial token position,
            but this token_position will change its value when the function iterates over tokens.

        is_top_left : bool
            True when a move suggestion in the top-left direction should be found.
            False when a move suggestion in the bottom-right direction should be found.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        list
            If a valid token move suggestion is found it returns the position of it.
            It returns an empty list if no suggestion is found.
        """
        if 8 > token_position[0] >= 0 and 8 > token_position[1] >= 0:
            token_value = self.game_matrix[token_position[0], token_position[1]]
            initial_token_value = self.game_matrix[initial_token_position[0], initial_token_position[1]]
            if token_value == 0.0 and is_conquered:
                return [(token_position[0], token_position[1])]
            elif token_value == 0.0 and not is_conquered:
                return []
            elif token_value == initial_token_value and is_conquered:
                return []
            elif initial_token_position == token_position and not is_top_left:
                return self.__suggest_diagonal_move_from_top_left_to_bottom_right(initial_token_position,
                                                                                  (token_position[0] + 1,
                                                                                   token_position[1] + 1), False,
                                                                                  False)
            elif token_value != initial_token_value and not is_top_left:
                return self.__suggest_diagonal_move_from_top_left_to_bottom_right(initial_token_position,
                                                                                  (token_position[0] + 1,
                                                                                   token_position[1] + 1), False,
                                                                                  True)
            elif initial_token_position == token_position and is_top_left:
                return self.__suggest_diagonal_move_from_top_left_to_bottom_right(initial_token_position,
                                                                                  (token_position[0] - 1,
                                                                                   token_position[1] - 1), True,
                                                                                  False)
            elif token_value != initial_token_value and is_top_left:
                return self.__suggest_diagonal_move_from_top_left_to_bottom_right(initial_token_position,
                                                                                  (token_position[0] - 1,
                                                                                   token_position[1] - 1), True,
                                                                                  True)
            else:
                return []
        else:
            return []

    def __suggest_diagonal_move_from_top_right_to_bottom_left(self, initial_token_position, token_position,
                                                              is_top_right,
                                                              is_conquered=False):
        """Suggests a possible diagonal token move to the top-left or to the bottom-right from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_position : tuple
            A tuple which specifies the initial token position.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        token_position : tuple
            A tuple which should be initialized with the initial token position,
            but this token_position will change its value when the function iterates over tokens.

        is_top_right : bool
            True when a move suggestion in the top-right direction should be found.
            False when a move suggestion in the bottom-left direction should be found.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        list
            If a valid token move suggestion is found it returns the position of it.
            It returns an empty list if no suggestion is found.
        """
        if 8 > token_position[0] >= 0 and 8 > token_position[1] >= 0:
            token_value = self.game_matrix[token_position[0], token_position[1]]
            initial_token_value = self.game_matrix[initial_token_position[0], initial_token_position[1]]
            if token_value == 0.0 and is_conquered:
                return [(token_position[0], token_position[1])]
            elif token_value == 0.0 and not is_conquered:
                return []
            elif token_value == initial_token_value and is_conquered:
                return []
            elif initial_token_position == token_position and not is_top_right:
                return self.__suggest_diagonal_move_from_top_right_to_bottom_left(initial_token_position,
                                                                                  (token_position[0] + 1,
                                                                                   token_position[1] - 1), False,
                                                                                  False)
            elif token_value != initial_token_value and not is_top_right:
                return self.__suggest_diagonal_move_from_top_right_to_bottom_left(initial_token_position,
                                                                                  (token_position[0] + 1,
                                                                                   token_position[1] - 1), False,
                                                                                  True)
            elif initial_token_position == token_position and is_top_right:
                return self.__suggest_diagonal_move_from_top_right_to_bottom_left(initial_token_position,
                                                                                  (token_position[0] - 1,
                                                                                   token_position[1] + 1), True,
                                                                                  False)
            elif token_value != initial_token_value and is_top_right:
                return self.__suggest_diagonal_move_from_top_right_to_bottom_left(initial_token_position,
                                                                                  (token_position[0] - 1,
                                                                                   token_position[1] + 1), True,
                                                                                  True)
            else:
                return []
        else:
            return []

    def count_black_game_tokens(self):
        """Counts black game tokens inside the game matrix.

        Returns
        -------
        int
            The amount of black game tokens."""
        return self.__iterate_black_game_tokens(0, (0, 0))

    def __iterate_black_game_tokens(self, black_tokens_count, token_position):
        """Iterates through every element of the game matrix and counts the black tokens.

        Parameters
        ----------
        black_tokens_count : int
            Amount of black game tokens.

        token_position : tuple
            Token position coordinates.

        Returns
        -------
        int
            Amount of black game tokens."""
        if token_position[0] == 7 and token_position[1] == 7:
            if self.__is_black_token(token_position):
                black_tokens_count += 1
            return black_tokens_count
        elif token_position[1] == 7:
            if self.__is_black_token(token_position):
                black_tokens_count += 1
            return self.__iterate_black_game_tokens(black_tokens_count, (token_position[0] + 1, token_position[1] - 7))
        else:
            if self.__is_black_token(token_position):
                black_tokens_count += 1
            return self.__iterate_black_game_tokens(black_tokens_count, (token_position[0], token_position[1] + 1))

    def __is_black_token(self, token_position):
        """Checks if a token at a specified token position is a black token.

        Parameters
        ----------
        token_position : tuple
            Token at this token position coordinates should be checked.

        Returns
        -------
        bool
            True if token is black.
            False if token is not black."""
        if self.__game_matrix[token_position] == self.translate_game_token_type('B'):
            return True
        else:
            return False

    def count_white_game_tokens(self):
        """Counts white game tokens inside the game matrix.

        Returns
        -------
        int
            The amount of white game tokens."""
        return self.__iterate_white_game_tokens(0, (0, 0))

    def __iterate_white_game_tokens(self, white_tokens_count, token_position):
        """Iterates through every element of the game matrix and counts the white tokens.

        Parameters
        ----------
        white_tokens_count : int
            Amount of white game tokens.

        token_position : tuple
            Token position coordinates.

        Returns
        -------
        int
            Amount of white game tokens."""
        if token_position[0] == 7 and token_position[1] == 7:
            if self.__is_white_token(token_position):
                white_tokens_count += 1
            return white_tokens_count
        elif token_position[1] == 7:
            if self.__is_white_token(token_position):
                white_tokens_count += 1
            return self.__iterate_white_game_tokens(white_tokens_count, (token_position[0] + 1, token_position[1] - 7))
        else:
            if self.__is_white_token(token_position):
                white_tokens_count += 1
            return self.__iterate_white_game_tokens(white_tokens_count, (token_position[0], token_position[1] + 1))

    def __is_white_token(self, token_position):
        """Checks if a token at a specified token position is a white token.

        Parameters
        ----------
        token_position : tuple
            Token at this token position coordinates should be checked.

        Returns
        -------
        bool
            True if token is white.
            False if token is not white."""
        if self.__game_matrix[token_position] == self.translate_game_token_type('W'):
            return True
        else:
            return False
