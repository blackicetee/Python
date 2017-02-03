from random import randint

from machine_learing_games.learning_agents.TicTacToeDescionsionTreeAgent import TicTacToeDecisionTreeAgent
from machine_learing_games.tictactoe.TicTacToe import TicTacToe


class TicTacToeEnvironment:
    def __init__(self):
        self.__tictactoe_desision_tree_agent = TicTacToeDecisionTreeAgent()
        self.__tictactoe = TicTacToe(4)
        self.__round_count = 0
        self.__action_sequence = []
        self.__game_result = ''

    def __initialize_new_tictactoe_game(self):
        self.__tictactoe = TicTacToe(4)
        self.__round_count = 0
        self.__action_sequence = []
        self.__game_result = ''

    def train_decision_tree_agent_x_times_against_random_agent(self, times):
        for game in range(0, times):
            self.__initialize_new_tictactoe_game()
            while self.__game_result == '' and self.__round_count < 16:
                self.process_move_from_tictactoe_decision_tree_agent()
                self.process_move_from_tictactoe_random_agent()
            self.__tictactoe_desision_tree_agent.receive_reward(self.__game_result, self.__action_sequence)


    def evaluate_game_result(self):
        if self.__round_count == 16 and not self.__tictactoe.is_victory():
            self.__game_result = 'draw'
        elif (self.__round_count % 2) == 0 and self.__tictactoe.is_victory():
            print self.__action_sequence
            print self.__tictactoe.printable_game_matrix()
            self.__game_result = 'lost'
        elif (self.__round_count % 2) == 1 and self.__tictactoe.is_victory():
            self.__game_result = 'win'

    def process_move_from_tictactoe_decision_tree_agent(self):
        if self.__game_result == '':
            self.__round_count += 1
            agent_move = self.get_move_from_tictactoe_decision_tree_agent()
            self.__tictactoe.put_game_token('X', agent_move)
            self.evaluate_game_result()


    def get_move_from_tictactoe_decision_tree_agent(self):
        agent_action = self.__tictactoe_desision_tree_agent.get_action_decision(self.__tictactoe)
        self.__action_sequence.append(agent_action)
        return agent_action

    def process_move_from_tictactoe_random_agent(self):
        if self.__game_result == '':
            self.__round_count += 1
            random_agent_move = self.get_move_from_tictactoe_random_agent()
            self.__tictactoe.put_game_token('O', random_agent_move)
            self.evaluate_game_result()

    def get_move_from_tictactoe_random_agent(self):
        possible_actions = self.__tictactoe.get_possible_moves()
        random_agent_move = possible_actions[randint(0, (len(possible_actions) - 1))]
        self.__action_sequence.append(random_agent_move)
        return random_agent_move


tictactoe_environment = TicTacToeEnvironment()
tictactoe_environment.train_decision_tree_agent_x_times_against_random_agent(20)
