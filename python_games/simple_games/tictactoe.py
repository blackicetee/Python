import numpy as np


class TicTacToe:
    """Represents the game TicTacToe and menages the placement of game tokens on the game matrix,
    winning- and loosing conditions and resetting game field values.

    Attributes
    ----------
    game_matrix
    rows :  int
        Defines how much rows the game_matrix should have.
    columns :   int
        Defines how much columns the game_matrix should have.

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

    def __init__(self, rows, columns):
        self.__game_matrix = np.asmatrix(np.zeros(shape=(rows, columns)))
        self.__rows = rows
        self.__columns = columns

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

    def put_game_token(self, game_token_type, position):
        """Puts/places a game token at a specified position on the game matrix.

        Parameters
        ----------

        game_token_type :   str
            The only valid strings are the string characters 'O' or 'X'.
            'O' and 'X' are the two kinds of game tokens which represent the game decisions of a game player.

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
            The only valid strings are the string characters 'O' or 'X'.
            'O' and 'X' are the two kinds of game tokens which represent the game decisions of a game player.

        Raises
        ------
        ValueError
            When the game_token_type  is not 'O' or 'X' the function will raise a value error exception.

        Returns
        -------
        float
            If input parameter is 'O' it will return the float value 1.0.
            If input parameter is 'X' it will return the float value 2.0.

        """
        if game_token_type == 'O':
            return 1.0
        elif game_token_type == 'X':
            return 2.0
        else:
            raise ValueError("game_token_type needs to be 'O' or 'X'!")

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
        if position[0] < self.__rows and position[1] < self.__columns:
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
        for row in range(self.__rows):
            for col in range(self.__columns):
                self.game_matrix[row, col] = value

    def reset_game_matrix_values(self):
        """Overwrites every element of the game matrix with 0.0."""
        self.__overwrite_game_matrix_with_values(0.0)

    def is_horizontal_victory(self):
        """ Checks if any row in the game matrix contains only game tokens of one type.

        Returns
        -------
        bool
            True if there is no free spot or enemy game token in a row of the game matrix.
            False if the game matrix row contains a free spot(value 0.0) or an enemy game token.
        """
        horizontal_victory_condition = False
        for row in range(self.__rows):
            if not horizontal_victory_condition:
                horizontal_victory_condition = self.__check_equality_of_matrix_row(row)
        return horizontal_victory_condition

    def is_vertical_victory(self):
        """ Checks if any column in the game matrix contains only game tokens of one type.

        Returns
        -------
        bool
            True if there is no free spot or enemy game token in a column of the game matrix.
            False if the game matrix column contains a free spot(value 0.0) or an enemy game token.
        """
        vertical_victory_condition = False
        for col in range(self.__columns):
            if not vertical_victory_condition:
                vertical_victory_condition = self.__check_equality_of_matrix_column(col)
        return vertical_victory_condition

    def __check_equality_of_matrix_row(self, matrix_row):
        """Checks the equality of all elements inside a specified game matrix row.

        Parameters
        ----------
        matrix_row :    int
            Specifies which row inside of the game matrix should be checked.

        Returns
        -------
        bool
            True if there is just one game matrix row in which every element is equal and none of the elements is 0.0.
            False if no game matrix row contains complete equal elements or one or more elements in one row are 0.0.
        """
        row_list = self.__game_matrix[matrix_row].tolist()[0]
        if 0.0 not in row_list:
            return row_list[1:] == row_list[:-1]
        else:
            False

    def __check_equality_of_matrix_column(self, matrix_column):
        """Checks the equality of all elements inside a specified game matrix column.

        Parameters
        ----------
        matrix_column :    int
            Specifies which column inside of the game matrix should be checked.

        Returns
        -------
        bool
            True if there is just one game matrix column in which every element is equal and none of the elements is 0.0.
            False if no game matrix column contains complete equal elements or one or more elements in one row are 0.0.
        """
        column_list = self.__game_matrix.T[matrix_column].tolist()[0]
        if 0.0 not in column_list:
            return column_list[1:] == column_list[:-1]
        else:
            return False
