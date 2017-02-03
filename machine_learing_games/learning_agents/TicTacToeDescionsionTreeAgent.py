import os
from random import randint

from machine_learing_games.MachineLearingGamesRoot import ROOT_DIR
from machine_learing_games.tictactoe.TicTacToe import TicTacToe


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

TICTACTOE_TRAINING_SET = os.path.join(ROOT_DIR, "tictactoe_training_sets\\tictactoe_training_set.txt")
TICTACTOE_AGENT_EXPERIENCE = os.path.join(ROOT_DIR, "learning_agents\\tictactoe_agent_experience.txt")

class TicTacToeDecisionTreeAgent:
    def __init__(self):
        self.__possible_actions = []
        self.__tictactoe = TicTacToe(4)
        self.__training_set = self.__read_tictactoe_training_set(TICTACTOE_TRAINING_SET)

    @property
    def training_set(self):
        return self.__training_set

    def get_action_decision(self, tictactoe_state):
        self.__tictactoe = tictactoe_state
        self.__possible_actions = self.__tictactoe.get_possible_moves()
        # TODO dont return random action, return strategic action
        random_action = randint(0, (len(self.__possible_actions) - 1))
        return self.__possible_actions[random_action]

    def receive_reward(self, reward, action_sequence):
        if reward != '' and action_sequence != []:
            self.__create_tictactoe_agent_experience_file_if_not_exist()
            with open(TICTACTOE_AGENT_EXPERIENCE, "a") as text_file:
                white_space_buffer = 16 - len(action_sequence)
                self.__write_every_element_in_list_to_open_textfile(text_file, action_sequence)
                text_file.write("{}\n".format(("      |" * white_space_buffer) + reward))

    def __create_tictactoe_agent_experience_file_if_not_exist(self):
        if not os.path.isfile(TICTACTOE_AGENT_EXPERIENCE):
            with open(TICTACTOE_AGENT_EXPERIENCE, "w") as text_file:
                column_label = "LvL 1 |LvL 2 |LvL 3 |LvL 4 |LvL 5 |LvL 6 |LvL 7 |LvL 8 |LvL 9 |LvL 10|LvL 11|LvL 12|LvL 13|LvL 14|LvL 15|LvL 16|Target Value"
                table_limits = "______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|____________"
                text_file.write("{}\n".format(column_label))
                text_file.write("{}\n".format(table_limits))

    def __write_every_element_in_list_to_open_textfile(self, open_textfile, list):
        for element in list:
            open_textfile.write("{}|".format(str(element)))

    def __read_tictactoe_training_set(self, training_set_filename):
        with open(training_set_filename, "r") as text_file:
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

# TODO write tests for the functions
"""
agent1 = TicTacToeDecisionTreeAgent()
results = agent1.training_set
print len(results)
print agent1.count_target_value_appearance()
print agent1.count_level_appearance()
target_values_in_level = agent1.count_target_value_appearance_inside_levels()
for index in target_values_in_level:
    print str(index) + str(target_values_in_level[index])
"""
