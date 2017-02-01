from python_games.simple_games.NewTicTacToe import NewTicTacToe

# first machine learning approach:
#       The agent gets a training set of action sequences and target value win, lost or draw
#       [(0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (3, 0), (0, 3)], win
#           ...
#       Aim:
#           With this training set the agent creates a decision tree.
#           The tree should define when to choose which action to get a win and avoid a lost.

# second machine learning approach:
#       The agent has no training set, but a strategy which specifies
#       the action the agent should choose in a state.
#
#       Aim:
#           Optimise the strategy for better game results.

class TicTacToeDecisionTreeAgent:

    def __init__(self, current_world_status=NewTicTacToe(4)):
        self.__current_world_status = current_world_status
        self.__possible_actions = current_world_status.get_possible_moves()