import numpy


class Reversi:
    """Contains rules and logic of the board game Reversi.
    Winning condition of Reversi is to have the most tokens in your color at the end.
    In Reversi you can conquer enemy tokens when they are trapped between two of your tokens.
    Conquering is possible in horizontal, vertical and diagonal.
    Within every move you can put exactly one token.
    The board game needs two players.
    The game ends when the board has no more free spaces.
    The game field is an eight times eight matrix.
    """

    def __init__(self):
        self.__game_matrix = numpy.asmatrix(numpy.zeros(shape=(8, 8)))

    @property
    def game_matrix(self):
        """A matrix which represents the Reversi game field. The game_matrix defines how big the game field is,
        how much game tokens could be placed and where they could be placed. Additionally the game_matrix
        stores the position of every placed game token inside the matrix.

        Returns
        -------
        game_matrix :   numpy.matrix
            The game_matrix.
        """
        return self.__game_matrix

    def game_token_move(self, game_token_type, game_token_position):
        suggested_moves_set = self.suggest_all_moves(game_token_type)
        if game_token_position in suggested_moves_set:
            self.put_game_token(game_token_type, game_token_position)
            self.__conquer_enemy_game_tokens(game_token_position)
            return True
        else:
            return False

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

    def put_game_token(self, game_token_type, position):
        """Puts/places a game token at a specified position on the game matrix.

        Parameters
        ----------

        game_token_type :   str
            The only valid strings are the string characters 'B' or 'W'.
            'B' and 'W' are the two kinds of game tokens which represent the game decisions of a game player.
            'B' stands for 'black token' and 'W' stands for 'white token'.

        position :  tuple
            A tuple of coordinates which specifies the position, where to put the game token, on the game matrix.

        Raises
        ------
        ValueError
            Raises a value error exception if the position tuple is not in range of the game matrix.

        Returns
        -------
        bool
            True if the game token is placed successfully.
            False if placement of game token failed, because position is already taken.
        """
        game_token = self.translate_game_token_type(game_token_type)
        if self.is_position_free(position):
            self.game_matrix[position[0], position[1]] = game_token
            return True
        else:
            return False

    def translate_game_token_type(self, game_token_type):
        """Translates a game token type into a predefined float value, because inside the game matrix
         the game tokens will be represented by float values.

        Parameters
        ----------

        game_token_type :   str
            The only valid strings are the string characters 'B' or 'W'.
            'B' and 'W' are the two kinds of game tokens which represent the game decisions of a game player.
            'B' stands for 'black token' and 'W' stands for 'white token'.

        Raises
        ------
        ValueError
            When the game_token_type  is not 'B' or 'W' the function will raise a value error exception.

        Returns
        -------
        float
            If input parameter is 'B' it will return the float value 1.0.
            If input parameter is 'W' it will return the float value 2.0.

        """
        if game_token_type == 'B':
            return 1.0
        elif game_token_type == 'W':
            return 2.0
        else:
            raise ValueError("game_token_type needs to be 'B' or 'W'!")

    def __reverse_game_token_value(self, game_token_value):
        if game_token_value == 1.0:
            return 2.0
        elif game_token_value == 2.0:
            return 1.0
        else:
            raise ValueError("game_token_value needs to be '1.0' or '2.0'!")

    def is_position_free(self, position):
        """Checks if a specified position on the game matrix is free,
        so no game token could be placed on a taken position.

        Parameters
        ----------
        position :  tuple
            A tuple of coordinates for the game matrix, it describes which position
            inside of the game matrix should be checked.

        Raises
        ------
        ValueError
            Raises a value error exception if the position tuple is not in range of the game matrix.

        Returns
        -------
        bool
            True if the position inside the game matrix is free.
            False if the position inside the game matrix is taken.
        """
        if position[0] < 8 and position[1] < 8:
            if self.game_matrix[position[0], position[1]] == 0.0:
                return True
            else:
                return False
        else:
            raise ValueError("The position tuple is outside of the game matrix!")

    def __overwrite_game_matrix_with_values(self, value):
        """Overwrites every element of the game matrix with a specified value.

        Parameters
        ----------
        value : float
                Overwrites every game matrix elements with this value.
        """
        for row in range(8):
            for col in range(8):
                self.game_matrix[row, col] = value

    def reset_game_matrix_values(self):
        """Overwrites every element of the game matrix with 0.0."""
        self.__overwrite_game_matrix_with_values(0.0)

    def suggest_all_moves(self, game_token_type):
        """Suggests all possible moves for every token of one color.

        Parameters
        ----------
        game_token_type : str
            Defines for which color the suggestions should be searched.
            It is either 'B' for black token or 'W' for white token.

        Returns
        -------
        list
            A sorted set of all token move suggestions which are found for every token of one color.
            Set means that the positions are unique.
            The set will be sorted like this [(0, 0), (0, 1), (1, 2) ... (5, 5), (5, 6), (6, 0)].
        """
        suggested_moves = []
        game_token = self.translate_game_token_type(game_token_type)
        for row in range(8):
            for col in range(8):
                if self.game_matrix[row, col] == game_token:
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
