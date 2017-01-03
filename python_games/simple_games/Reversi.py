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
        self.put_game_token('B', (3, 3))
        self.put_game_token('B', (4, 4))
        self.put_game_token('W', (3, 4))
        self.put_game_token('W', (4, 3))

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

    def __traverse_horizontal_right(self, opponent_token_value, position_of_token, conquer_condition=False):
        if 8 > position_of_token[1] >= 0:
            token_value = self.game_matrix[position_of_token[0], position_of_token[1]]
            if token_value == 0.0 and conquer_condition == True:
                return position_of_token[1]
            elif token_value == 0.0 and conquer_condition == False:
                return -1
            elif token_value == self.__reverse_game_token_value(opponent_token_value):
                return -1
            else:
                return self.__traverse_horizontal_right(opponent_token_value,
                                                        (position_of_token[0], position_of_token[1] + 1), True)
        else:
            return -1

    def __suggest_horizontal_move_right(self, position_of_token):
        opponent_token_value = self.__reverse_game_token_value(
            self.game_matrix[position_of_token[0], position_of_token[1]])
        column = self.__traverse_horizontal_right(opponent_token_value,
                                                  (position_of_token[0], position_of_token[1] + 1))
        if column == -1:
            return []
        else:
            return [(position_of_token[0], column)]

    # def __suggest_horizontal_move_left(self, position_of_token):

    def __suggest_horizontal_moves(self, position_of_token):
        return self.__suggest_horizontal_move_right(position_of_token)
        # self.__suggest_horizontal_move_left(position_of_token)

    def __suggest_moves_for_a_token(self, position_of_token):
        return self.__suggest_horizontal_moves(position_of_token)
        # self.__suggest_vertical_moves(position_of_token)
        # self.__suggest_diagonal_moves(position_of_token)

    def suggest_all_moves(self, game_token_type):
        suggested_moves = []
        game_token = self.translate_game_token_type(game_token_type)
        for row in range(8):
            for col in range(8):
                if self.game_matrix[row, col] == game_token:
                    suggested_moves += self.__suggest_moves_for_a_token((row, col))
        return suggested_moves
