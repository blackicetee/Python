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

    def __suggest_horizontal_move(self, initial_token_value, position_of_token, is_left, is_conquered=False):
        """Suggests a possible horizontal token move to the left or to the right from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_value : float
            Either 1.0 for a black token or 2.0 for a white token.
            Defines if it is a black token move or a white one.

        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tupel specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        is_left : bool
            True when a move suggestion in the left direction should be found.
            False when a move suggestion in the right direction should be found.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        int
            If a valid token move suggestion is found it returns a value between 0 and 7.
            The value stands for the column index, where the suggested move is located.
            It returns -1 if no suggestion is possible.
        """
        if 8 > position_of_token[1] >= 0:
            token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
            if token_value == 0.0 and is_conquered:
                return position_of_token[1]
            elif token_value == 0.0 and not is_conquered:
                return -1
            elif token_value == initial_token_value and is_conquered:
                return -1
            elif token_value == initial_token_value and not is_conquered and not is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] + 1), False,
                                                      False)
            elif token_value != initial_token_value and not is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] + 1), False,
                                                      True)
            elif token_value == initial_token_value and not is_conquered and is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] - 1), True,
                                                      False)
            elif token_value != initial_token_value and is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] - 1), True,
                                                      True)
            else:
                return -1
        else:
            return -1

    def __suggest_vertival_move(self, initial_token_value, position_of_token, is_top, is_conquered=False):
        """Suggests a possible vertical token move to the top or to the bottom from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_value : float
            Either 1.0 for a black token or 2.0 for a white token.
            Defines if it is a black token move or a white one.

        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tupel specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        is_top : bool
            True when a move suggestion in the upper direction should be found.
            False when a move suggestion in the lower direction should be found.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        int
            If a valid token move suggestion is found it returns a value between 0 and 7.
            The value stands for the row index, where the suggested move is located.
            It returns -1 if no suggestion is possible.
        """
        if 8 > position_of_token[1] >= 0:
            token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
            if token_value == 0.0 and is_conquered:
                return position_of_token[1]
            elif token_value == 0.0 and not is_conquered:
                return -1
            elif token_value == initial_token_value and is_conquered:
                return -1
            elif token_value == initial_token_value and not is_conquered and not is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] + 1), False,
                                                      False)
            elif token_value != initial_token_value and not is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] + 1), False,
                                                      True)
            elif token_value == initial_token_value and not is_conquered and is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] - 1), True,
                                                      False)
            elif token_value != initial_token_value and is_left:
                return self.__suggest_horizontal_move(initial_token_value,
                                                      (position_of_token[0], position_of_token[1] - 1), True,
                                                      True)
            else:
                return -1
        else:
            return -1

    def __suggest_horizontal_move_right(self, initial_token_value, position_of_token, is_conquered=False):
        """Suggests a possible horizontal token move to the right from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_value : float
            Either 1.0 for a black token or 2.0 for a white token.
            Defines if it is a black token move or a white one.

        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tupel specifies in which row of the game matrix the token is located
            and the second part specifies the location of the column.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        int
            If a valid token move suggestion is found it returns a value between 0 and 7.
            The value stands for the column index, where the suggested move is located.
            It returns -1 if no suggestion is possible.
        """
        if 8 > position_of_token[1] >= 0:
            token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
            if token_value == 0.0 and is_conquered:
                return position_of_token[1]
            elif token_value == 0.0 and not is_conquered:
                return -1
            elif token_value == initial_token_value and is_conquered:
                return -1
            elif token_value == initial_token_value and not is_conquered:
                return self.__suggest_horizontal_move_right(initial_token_value,
                                                            (position_of_token[0], position_of_token[1] + 1), False)
            else:
                return self.__suggest_horizontal_move_right(initial_token_value,
                                                            (position_of_token[0], position_of_token[1] + 1), True)
        else:
            return -1

    def __suggest_horizontal_move_left(self, initial_token_value, position_of_token, is_conquered=False):
        """Suggests a possible horizontal token move to the left from an initial token position.
        The token move is only valid if all conditions are true:
            -one or more enemy tokens are crossed
            -token move is still inside the game matrix
            -a free space is at the end of all crossed enemy tokens
            -no own token, except the initial token position, is crossed
        The first free space within the game matrix after all crossed enemy tokens is the suggested position.

        Parameters
        ----------
        initial_token_value : float
            Either 1.0 for a black token or 2.0 for a white token.
            Defines if it is a black token move or a white one.

        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the column.

        is_conquered : bool
            Is initially false and remains false if no enemy token is crossed.
            Changes to true if one or more enemy tokens are crossed.

        Returns
        -------
        int
            If a valid token move suggestion is found it returns a value between 0 and 7.
            The value stands for the column index, where the suggested move is located.
            It returns -1 if no suggestion is possible.
        """
        if 8 > position_of_token[1] >= 0:
            token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
            if token_value == 0.0 and is_conquered:
                return position_of_token[1]
            elif token_value == 0.0 and not is_conquered:
                return -1
            elif token_value == initial_token_value and is_conquered:
                return -1
            elif token_value == initial_token_value and not is_conquered:
                return self.__suggest_horizontal_move_left(initial_token_value,
                                                           (position_of_token[0], position_of_token[1] - 1), False)
            else:
                return self.__suggest_horizontal_move_left(initial_token_value,
                                                           (position_of_token[0], position_of_token[1] - 1), True)
        else:
            return -1

    def __suggest_horizontal_moves_alternative(self, position_of_token):
        """Suggests a possible horizontal token move to the left and to the right from an initial token position.

        Parameters
        ----------
        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the column.

        Returns
        -------
        list
            If no horizontal move suggestion is found then an empty list is returned.
            If just one horizontal suggestion of one direction is found
            then a list with one token position tuple is returned.
            If two horizontal move suggestions are found
            then a list of two token position tuples is returned.
            """
        token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
        suggestion_horizontal_left = self.__suggest_horizontal_move(token_value,
                                                                    (position_of_token[0], position_of_token[1]), True)
        suggestion_horizontal_right = self.__suggest_horizontal_move(token_value,
                                                                     (position_of_token[0], position_of_token[1]),
                                                                     False)
        if suggestion_horizontal_left == -1 and suggestion_horizontal_right == -1:
            return []
        elif suggestion_horizontal_left == -1 and suggestion_horizontal_right != -1:
            return [(position_of_token[0], suggestion_horizontal_right)]
        elif suggestion_horizontal_left != -1 and suggestion_horizontal_right == -1:
            return [(position_of_token[0], suggestion_horizontal_left)]
        else:
            return [(position_of_token[0], suggestion_horizontal_left),
                    (position_of_token[0], suggestion_horizontal_right)]

    def __suggest_horizontal_moves(self, position_of_token):
        """Suggests a possible horizontal token move to the left and to the right from an initial token position.

        Parameters
        ----------
        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the column.

        Returns
        -------
        list
            If no horizontal move suggestion is found then an empty list is returned.
            If just one horizontal suggestion of one direction is found
            then a list with one token position tuple is returned.
            If two horizontal move suggestions are found
            then a list of two token position tuples is returned.
            """
        token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
        suggestion_horizontal_left = self.__suggest_horizontal_move_left(token_value,
                                                                         (position_of_token[0], position_of_token[1]))
        suggestion_horizontal_right = self.__suggest_horizontal_move_right(token_value,
                                                                           (position_of_token[0], position_of_token[1]))
        if suggestion_horizontal_left == -1 and suggestion_horizontal_right == -1:
            return []
        elif suggestion_horizontal_left == -1 and suggestion_horizontal_right != -1:
            return [(position_of_token[0], suggestion_horizontal_right)]
        elif suggestion_horizontal_left != -1 and suggestion_horizontal_right == -1:
            return [(position_of_token[0], suggestion_horizontal_left)]
        else:
            return [(position_of_token[0], suggestion_horizontal_left),
                    (position_of_token[0], suggestion_horizontal_right)]

    def __suggest_moves_for_a_token(self, position_of_token):
        """Suggests all possible moves for a specified token position.

        Parameters
        ----------
        position_of_token : tuple
            Is a tuple of two integer values.
            First part of the tuple specifies in which row of the game matrix the token is located
            and the second part specifies the column.

        Returns
        -------
        list
            A list of all token move suggestions which are found for a specified token position.

        """
        # return self.__suggest_horizontal_moves(position_of_token)
        return self.__suggest_horizontal_moves_alternative(position_of_token)
        # self.__suggest_vertical_moves(position_of_token)
        # self.__suggest_diagonal_moves(position_of_token)

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
            A list of all token move suggestions which are found for every token of one color.
        """
        suggested_moves = []
        game_token = self.translate_game_token_type(game_token_type)
        for row in range(8):
            for col in range(8):
                if self.game_matrix[row, col] == game_token:
                    suggested_moves += self.__suggest_moves_for_a_token((row, col))
        return suggested_moves
