from python_games.simple_games.NewTicTacToe import NewTicTacToe
from random import randint

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

    TICTACTOE_TRAINING_SET = "tictactoe_training_set.txt"
    TICTACTOE_AGENT_EXPERIENCE = "tictactoe_agent_experience.txt"

    def __init__(self, tictactoe_status=NewTicTacToe(4)):
        self.__tictactoe_status = tictactoe_status
        self.__possible_actions = tictactoe_status.get_possible_moves()
        self.__training_set = self.__read_tictactoe_training_set()

    @property
    def training_set(self):
        return self.__training_set

    def __read_tictactoe_training_set(self):
        with open(self.TICTACTOE_TRAINING_SET, "r") as text_file:
            results = []
            list_of_sequences = []
            text_file.readline()
            text_file.readline()
            for line in text_file.readlines():
                list_of_sequences.append(line.strip('\n').split('|'))
            for sequence in list_of_sequences:
                target_value = sequence.pop()
                results.append((sequence, target_value))
            return results

    def count_target_value_appearance(self):
        count_of_target_value_appearance = {"wins": 0, "loses": 0, "draws": 0}
        for target_value in self.training_set:
            if target_value[1] == "win":
                count_of_target_value_appearance["wins"] += 1
            elif target_value[1] == "lost":
                count_of_target_value_appearance["loses"] += 1
            elif target_value[1] == "draw":
                count_of_target_value_appearance["draws"] += 1
        return count_of_target_value_appearance

    def count_level_appearance(self):
        length_of_action_sequences = []
        count_of_level_appearance = {7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0}
        for action_sequence in self.training_set:
            action_sequence = [element for element in action_sequence[0] if element != '      ']
            length_of_action_sequences.append(len(action_sequence))
        for length_index in range(7, 17):
            count_of_level_appearance[length_index] = length_of_action_sequences.count(length_index)
        return count_of_level_appearance

    def count_target_value_appearance_inside_levels(self):
        list_of_aciton_sequence_length_and_target_value = []
        target_values_in_level = {7: {"wins": 0, "loses": 0, "draws": 0}, 8: {"wins": 0, "loses": 0, "draws": 0},
                                  9: {"wins": 0, "loses": 0, "draws": 0}, 10: {"wins": 0, "loses": 0, "draws": 0},
                                  11: {"wins": 0, "loses": 0, "draws": 0}, 12: {"wins": 0, "loses": 0, "draws": 0},
                                  13: {"wins": 0, "loses": 0, "draws": 0}, 14: {"wins": 0, "loses": 0, "draws": 0},
                                  15: {"wins": 0, "loses": 0, "draws": 0}, 16: {"wins": 0, "loses": 0, "draws": 0}}
        for set in self.training_set:
            list_of_aciton_sequence_length_and_target_value.append(
                (len([element for element in set[0] if element != '      ']), set[1]))
        for length_index in range(7, 17):
            target_values_in_level[length_index]["wins"] = list_of_aciton_sequence_length_and_target_value.count(
                (length_index, "win"))
            target_values_in_level[length_index]["loses"] = list_of_aciton_sequence_length_and_target_value.count(
                (length_index, "lost"))
            target_values_in_level[length_index]["draws"] = list_of_aciton_sequence_length_and_target_value.count(
                (length_index, "draw"))
        return target_values_in_level

    #def play_tictactoe(self):


agent1 = TicTacToeDecisionTreeAgent(NewTicTacToe(4))
results = agent1.training_set
print len(results)
print agent1.count_target_value_appearance()
print agent1.count_level_appearance()
target_values_in_level = agent1.count_target_value_appearance_inside_levels()
for index in target_values_in_level:
    print str(index) + str(target_values_in_level[index])
