import numpy as np


class TicTacToe:
    """Represents the game TicTacToe and menages the rules, winning- and loosing conditions"""

    def __init__(self, rows, columns):
        self._game_matrix = np.asmatrix(np.zeros(shape=(rows, columns)))
        self._rows = rows
        self._columns = columns

    @property
    def game_matrix(self):
        """Represents the game filed"""
        return self._game_matrix

    def put_game_token(self, game_token_type, position):
        """ Puts a game token at a specified position on the game matrix.

        game_token_type: Represents the game token of a player,
        it is either a 'X' or an 'O'.

        position: A tuple of coordinates which specifies the position
        where to put the game token on the game matrix.

        return: True if the game token is placed successfully,
        False if placement of game token failed."""
        game_token = self.translate_game_token_type(game_token_type)
        if self.is_position_free(position):
            self.game_matrix[position[0], position[1]] = game_token
            return True
        else:
            return False

    def translate_game_token_type(self, game_token_type):
        """ Translates a game token type into a predefined float value,
        because inside the game matrix the game tokens
        will be represented by float values.

        game_token_type: A character 'O' or 'X'. 'O' and 'X' are the two
        kinds of game tokens which represent the game decisions of
        a game player.

        Exception: When the game_token_type  is not 'O' or 'X'
        the function will raise a value error.

        return: 1.0 for if game_token_type is 'O' and
        2.0 if game_token_type is 'X'."""
        if game_token_type == 'O':
            return 1.0
        elif game_token_type == 'X':
            return 2.0
        else:
            raise ValueError("game_token_type needs to be 'O' or 'X'!")

    def is_position_free(self, position):
        """ Checks if a specified position on the game matrix is free,
        so no game token is placed there before.

        position: A tuple of coordinates for the game matrix,
        it describes which position inside of the game matrix
        should be checked.

        return: True if the position inside the game matrix is free
        and otherwise it will return False."""
        if position[0] < self._rows and position[1] < self._columns:
            if self.game_matrix[position[0], position[1]] == 0.0:
                return True
            else:
                return False
        else:
            raise ValueError("The position tuple is outside of the game matrix!")
