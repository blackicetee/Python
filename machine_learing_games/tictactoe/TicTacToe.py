import numpy as np


class TicTacToe:
    """Represents the game TicTacToe and menages the placement of game tokens on the game matrix,
    winning- and loosing conditions and resetting game field values.

    Attributes
    ----------
    game_matrix : numpy.matrix
        Represents the game field and stores the current game status.
        Every placed game token is inserted here.
    dimension :  int
        Defines how much rows and columns the game_matrix should have.

     Methods
     --------
    put_game_token(game_token_type, position)
        Places a game token with a specified game_token_type at a position on the game_matrix.

    translate_game_token_type(game_token_type)
        Translates either a single character string 'O' or 'X' into a float value,
        because of internal game_matrix representation purposes.

    is_position_free(position)
        Checks if a position on the game_matrix is taken or free.
        Raises a ValueError exception if the given position is not in range of the game_matrix.

    reset_game_matrix_values()
        Resets every game_matrix game token value back to 0.0.

    is_horizontal_victory()
        Checks if any row of the game matrix contains only game tokens from one player,
        without empty or enemy elements.

    is_vertical_victory()
        Checks if any column of the game matrix contains only game tokens from one player,
        without empty or enemy elements.
     """

    def __init__(self, dimension):
        self.__dimension = dimension
        self.__game_matrix = self.__create_game_matrix(dimension, ' ')

    @property
    def game_matrix(self):
        """A matrix which represents the TicTacToe game field. The game_matrix defines how big the game field is,
        how much game tokens could be placed and where they could be placed. Additionally the game_matrix
        stores the position of every placed game token inside the matrix.

        Returns
        -------
        game_matrix :   numpy.matrix
            The game_matrix.
        """
        return self.__game_matrix

    def initialize_game_matrix_with_action_sequence(self, action_sequence, starting_player_token):
        self.__init__(4)
        actions_processed = 0
        for action in action_sequence:
            if actions_processed % 2 == 0:
                self.put_game_token(starting_player_token, action)
                actions_processed += 1
            else:
                game_token_type = self.__get_opposite_game_token_type(starting_player_token)
                if game_token_type is not None:
                    self.put_game_token(str(game_token_type), action)
                    actions_processed += 1

    def printable_game_matrix(self):
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

    def put_game_token(self, game_token, position):
        """Puts/places a game token at a specified position on the game matrix.

        Parameters
        ----------

        game_token :   str
            The only valid strings are the string characters 'O' or 'X'.
            'O' and 'X' are the two kinds of game tokens which represent the game decisions of a game player.

        position :  tuple
            A tuple of coordinates which specifies the position, where to put the game token, on the game matrix.
        """
        if self.__is_correct_game_token_type(game_token):
            if self.__is_position_free(position):
                self.game_matrix[position[0], position[1]] = game_token

    def get_possible_moves(self):
        """Suggests at which positions a player could place his game token.

        Returns
        -------
        list
            The list contains tuples of coordinates for every possible token move."""
        possible_moves = []
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if self.__game_matrix[row, col] == ' ':
                    possible_moves.append((row, col))
        return possible_moves

    def __is_correct_game_token_type(self, game_token_type):
        """Checks the game token type of correctness.

        Parameters
        ----------

        game_token_type :   str
            The only valid characters are 'O' or 'X'.
            'O' and 'X' are the two kinds of game tokens which represent the playing piece of a game player.

        Returns
        -------
        bool
            True if game_token_type is either an 'O' or an 'X'.
            False if not.
        """
        if game_token_type == 'O' or game_token_type == 'X':
            return True
        else:
            return False

    def __get_opposite_game_token_type(self, game_token_type):
        """Returns the opposite game_token_type.

        Parameters
        ----------

        game_token_type :   str
            The only valid characters are 'O' or 'X'.
            'O' and 'X' are the two kinds of game tokens which represent the playing piece of a game player.

        Returns
        -------
        bool
            'O' if the game_token_type is 'X'.
            'X' it the game_token_type is 'O'.
            None if the game_token_type is something else.
        """
        if game_token_type == 'X':
            return 'O'
        elif game_token_type == 'O':
            return 'X'
        else:
            return None

    def __is_position_free(self, position):
        """Checks if a specified position is free and inside the game matrix,
        so no game token could be placed on a taken game_matrix position or outside of the game_matrix.

        Parameters
        ----------
        position :  tuple
            A tuple of coordinates, it describes which position of the game matrix should be checked.

        Returns
        -------
        bool
            True if the position inside the game matrix is free.
            False if the position inside the game matrix is taken or the position is outside the game matrix.
        """
        if (position[0] < self.__dimension and position[1] < self.__dimension) and \
                        self.game_matrix[position[0], position[1]] == ' ':
            return True
        else:
            return False

    def __create_game_matrix(self, dimension, fill_value):
        """Creates a x dimensional matrix which is filled with values.

        Parameters
        ----------
        dimension : int
            Defines the row and column count of the matrix.

        fill_value : scalar
            Created matrix is completely filled with those values.

        Returns
        -------
        numpy.matrix
            X dimensional matrix initialised with values.
        """
        return np.asmatrix(np.full((dimension, dimension), fill_value, dtype=np.matrix))

    def __check_equality_of_list_elements(self, input_list):
        """Checks the equality of all elements inside a list.

        Parameters
        ----------
        input_list :    list
            Elements inside this list are tested for equality.

        Returns
        -------
        bool
            True if all elements inside the list are equal and unequal ' '.
            False if the elements differ or if ' ' occurs inside the list.
        """
        if ' ' not in input_list:
            return input_list[1:] == input_list[:-1]
        else:
            return False

    def is_horizontal_victory(self):
        """ Checks if any row in the game matrix contains only game tokens of one type.

        Returns
        -------
        bool
            True if there is no free spot or enemy game token in a row of the game matrix.
            False if the game matrix row contains a free spot or an enemy game token.
        """
        horizontal_victory_condition = False
        for row in range(self.__dimension):
            if not horizontal_victory_condition:
                horizontal_victory_condition = self.__check_equality_of_list_elements(
                    self.__game_matrix[row].tolist()[0])
        return horizontal_victory_condition

    def is_vertical_victory(self):
        """ Checks if any column in the game matrix contains only game tokens of one type.

        Returns
        -------
        bool
            True if there is no free spot or enemy game token in a column of the game matrix.
            False if the game matrix column contains a free spot or an enemy game token.
        """
        vertical_victory_condition = False
        for col in range(self.__dimension):
            if not vertical_victory_condition:
                vertical_victory_condition = self.__check_equality_of_list_elements(
                    self.__game_matrix.T[col].tolist()[0])
        return vertical_victory_condition

    def is_diagonal_victory(self):
        """Checks if any diagonal in the game matrix contains only game tokens of one type.
        A diagonal is a connection between two corners which are not in the same row.
        For example the connection between the top right corner and the bottom left corner
        is a valid diagonal of the game matrix.
        """
        diagonal_values_top_left_to_bottom_right = []
        diagonal_values_top_right_to_bottom_left = []
        for coordinate in range(self.__dimension):
            diagonal_values_top_left_to_bottom_right.append(self.game_matrix[coordinate, coordinate])
            diagonal_values_top_right_to_bottom_left.append(
                self.game_matrix[coordinate, (self.__dimension - 1) - coordinate])
        return self.__check_equality_of_list_elements(
            diagonal_values_top_left_to_bottom_right) or self.__check_equality_of_list_elements(
            diagonal_values_top_right_to_bottom_left)

    def is_victory(self):
        """Checks if any horizontal, vertical or diagonal line contains only game tokens
         of one type in the game matrix

         Returns
         -------
         bool
            True if any horizontal, vertical or diagonal line inside the matrix, containing only game tokens
            from one type, is found.
            False if no horizontal, vertical or diagonal line inside the matrix, containing only game tokens
            from one type, is found.
            """
        return self.is_horizontal_victory() or self.is_vertical_victory() or self.is_diagonal_victory()