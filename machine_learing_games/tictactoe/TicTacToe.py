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
        self.__action_sequence = []

    @property
    def game_matrix(self):
        """A matrix which represents the TicTacToe game board. The game_matrix defines how big the game board is,
        how much game tokens could be placed and where they could be placed. Additionally the game_matrix
        stores the position of every placed game token inside the matrix.

        Returns
        -------
        numpy.matrix
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

    def initialize_game_matrix_with_another_game_matrix(self, another_tictactoe_game):
        """Initializes the game matrix property with another game matrix.
        Careful this functio

        Parameters
        ----------
        another_game_matrix : numpy.matrix
            The other game matrix."""
        self.__action_sequence = another_tictactoe_game.action_sequence
        self.__game_matrix[:] = another_tictactoe_game.game_matrix[:]

    def initialize_game_matrix_with_action_sequence(self, action_sequence):
        """Initializes the game matrix property with an action sequence.

        Parameters
        ----------
        action_sequence : list
            The action sequence is a list of tuples.
            Every tuple specifies a position at the game matrix property.
            Tuple element one is the row and tuple element two is the column of the game matrix."""
        if len(action_sequence) <= (self.__dimension * self.__dimension):
            self.__init__(self.__dimension)
            for action in action_sequence:
                self.make_move(action)

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

    def count_of_game_tokens_in_game(self):
        """Counts how much game tokens are currently inside the game matrix property.

        Returns
        -------
        int
            Count of game tokens inside the game matrix property."""
        count = 0
        for row in range(self.__dimension):
            for col in range(self.__dimension):
                if self.__game_matrix[row, col] == 'X' or self.__game_matrix[row, col] == 'O':
                    count += 1
        return count

    def get_maximal_amount_of_game_tokens(self):
        """Returns how much fields the game board will have,
         according to initialized dimensionality when the object is created.

         Returns
         -------
         int
            The maximal amount of game tokens,
            which can be placed inside the game matrix property."""
        return self.__dimension * self.__dimension

    def count_tokens_in_pure_connection(self, x_position, y_position, player_token):
        """Counts game tokens from a player inside a connection of two positions but only if the connection is pure.
        For more information about what a pure connection is
        or what a connection of two positions is,
        please read the description of function 'is_connection_pure(...)'.

        Parameters
        ----------
        x_position : tuple
            Specifies the position of point one inside the game matrix property.

        y_position : tuple
            Specifies the position of point two inside the game matrix property.

        player_token : str
            Is either an 'X' or an 'O' and specifies which player tokens should be counted.

        Returns
        -------
        int
            The amount of game tokens of one player, which are in a pure connection of two points.
            Will always return zero if the connection is not pure or
            if no valid connection of those two points can be created."""
        count = 0
        victory_relevant_positions = self.get_victory_relevant_positions_by_two_given_positions(x_position, y_position)
        if self.is_connection_pure(x_position, y_position, player_token):
            for position in victory_relevant_positions:
                if self.__game_matrix[position] == player_token:
                    count += 1
        return count

    def get_victory_relevant_positions_by_two_given_positions(self, x_position, y_position):
        """Returns a list of tuples, according to two given position points,
         where every tuple specifies a victory relevant position.
         The two position points define if the relevant positions are ordered in a horizontal,
         vertical or diagonal line.
         Victory relevant means, if every horizontal, vertical or diagonal field is filled with game tokens of one player,
         then this player will win the Tic Tac Toe game.

        Parameters
        ----------
        x_position : tuple
            Specifies the position of point one inside the game matrix property.

        y_position : tuple
            Specifies the position of point two inside the game matrix property.

        Returns
        -------
        list
            A list of positions(tuples), these list depends on the input position point .
            The list is empty if the input positions are in no horizontal, vertical or diagonal relation to one another.

         """
        victory_relevant_positions = []
        if x_position[0] == y_position[0] and x_position[1] != y_position[1]:
            for d in range(self.__dimension):
                victory_relevant_positions.append((x_position[0], d))
        elif x_position[0] != y_position[0] and x_position[1] == y_position[1]:
            for d in range(self.__dimension):
                victory_relevant_positions.append((d, x_position[1]))
        elif x_position[0] == x_position[1] and y_position[0] == y_position[1]:
            for d in range(self.__dimension):
                victory_relevant_positions.append((d, d))
        elif x_position == ((self.__dimension - 1) - x_position[1], (self.__dimension - 1) - x_position[0]) and y_position == ((self.__dimension - 1) - y_position[1], (self.__dimension - 1) - y_position[0]):
            for d in range(self.__dimension):
                victory_relevant_positions.append(((self.__dimension - 1) - d, d))
        return victory_relevant_positions

    def is_connection_pure(self, x_position, y_position, player_token):
        """Checks if a connection is pure.
        A pure connection is a horizontal, vertical or diagonal line which only contains empty game matrix fields or
        fields which contain the specified player tokens. If an enemy player token is found within the connection,
        then the counting is cancelled and will return always zero.
        A connection is like a linear line,
        where the length of this line is equal to the dimension of the game matrix property.
        If the two given position points are not inside of one of the possible linear lines,
        then the position points are invalid and will not be considered.

        Parameters
        ----------
        x_position : tuple
            Specifies the position of point one inside the game matrix property.

        y_position : tuple
            Specifies the position of point two inside the game matrix property.

        player_token : str
            Is either an 'X' or an 'O' and specifies which player tokens should be counted.

        Returns
        -------
        bool
            True if the connection is pure
            and the two input positions are in a horizontal, vertical or diagonal relation.
            False if not.
            Additionally:
                A horizontal relation means, the two input positions are in the same row of the game matrix property.
        """
        pure = True
        victory_relevant_positions = self.get_victory_relevant_positions_by_two_given_positions(x_position, y_position)
        for position in victory_relevant_positions:
            if self.game_matrix[position] != ' ' and self.game_matrix[position] != player_token:
                pure = False
        return pure

    def undo_move(self):
        last_move = self.__action_sequence.pop()
        self.__game_matrix[last_move] = ' '

    def make_move(self, position):
        """Puts/places a game token at a specified position on the game matrix.

        Parameters
        ----------

        game_token :   str
            The only valid strings are the string characters 'O' or 'X'.
            'O' and 'X' are the two kinds of game tokens which represent the game decisions of a game player.

        position :  tuple
            A tuple of coordinates which specifies the position, where to put the game token, on the game matrix.
        """
        if self.__is_position_free(position):
            if self.count_of_game_tokens_in_game() % 2 == 0:
                self.__game_matrix[position] = 'X'
                self.__action_sequence.append(position)
            elif self.count_of_game_tokens_in_game() % 2 == 1:
                self.__game_matrix[position] = 'O'
                self.__action_sequence.append(position)

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
                        self.__game_matrix[position[0], position[1]] == ' ':
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
            diagonal_values_top_left_to_bottom_right.append(self.__game_matrix[coordinate, coordinate])
            diagonal_values_top_right_to_bottom_left.append(
                self.__game_matrix[coordinate, (self.__dimension - 1) - coordinate])
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