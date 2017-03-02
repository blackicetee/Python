from random import randint

from machine_learing_games.Agents.LearningAgents.EasyTicTacToeAgent import EasyTicTacToeAgent
from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from playground_machine_learing.decision_tree_agent.TicTacToeDescionsionTreeAgent import TicTacToeDecisionTreeAgent


class TicTacToeEnvironment:
    def __init__(self):
        self.__tictactoe_desision_tree_agent = TicTacToeDecisionTreeAgent()
        self.__easy_tictactoe_agent = EasyTicTacToeAgent()
        self.__tictactoe = TicTacToe(4)
        self.__round_count = 0
        self.__action_sequence = []
        self.__game_result = ''

    def __initialize_new_tictactoe_game(self):
        self.__tictactoe = TicTacToe(4)
        self.__round_count = 0
        self.__action_sequence = []
        self.__game_result = ''

    def train_easy_tictactoe_agent(self, times):
        for game in range(0, times):
            self.__initialize_new_tictactoe_game()
            while self.__game_result == '' and self.__round_count < 16:
                self.easy_agent_move()
                self.random_agent_move()
            self.__easy_tictactoe_agent.reward(self.__game_result)

    def easy_agent_move(self):
        if self.__game_result == '':
            self.__round_count += 1
            agent_move = self.__easy_tictactoe_agent.action()
            self.__tictactoe.make_move(agent_move)
            self.evaluate_game_result()


    def train_decision_tree_agent_x_times_against_random_agent(self, times):
        for game in range(0, times):
            self.__initialize_new_tictactoe_game()
            while self.__game_result == '' and self.__round_count < 16:
                self.decision_tree_agent_move()
                self.random_agent_move()
            self.__tictactoe_desision_tree_agent.receive_reward(self.__game_result, self.__action_sequence)


    def evaluate_game_result(self):
        if self.__round_count == 16 and not self.__tictactoe.is_victory():
            self.__game_result = 'draw'
        elif (self.__round_count % 2) == 0 and self.__tictactoe.is_victory():
            self.__game_result = 'lost'
        elif (self.__round_count % 2) == 1 and self.__tictactoe.is_victory():
            self.__game_result = 'win'

    def decision_tree_agent_move(self):
        if self.__game_result == '':
            self.__round_count += 1
            agent_move = self.get_move_from_tictactoe_decision_tree_agent()
            self.__tictactoe.make_move(agent_move)
            self.evaluate_game_result()


    def get_move_from_tictactoe_decision_tree_agent(self):
        agent_action = self.__tictactoe_desision_tree_agent.get_action_decision(self.__tictactoe)
        self.__action_sequence.append(agent_action)
        return agent_action

    def random_agent_move(self):
        if self.__game_result == '':
            self.__round_count += 1
            random_agent_move = self.get_move_from_tictactoe_random_agent()
            self.__tictactoe.make_move(random_agent_move)
            self.evaluate_game_result()

    def get_move_from_tictactoe_random_agent(self):
        possible_actions = self.__tictactoe.get_possible_moves()
        random_agent_move = possible_actions[randint(0, (len(possible_actions) - 1))]
        self.__action_sequence.append(random_agent_move)
        return random_agent_move


tictactoe_environment = TicTacToeEnvironment()
#tictactoe_environment.train_decision_tree_agent_x_times_against_random_agent(20)
tictactoe_environment.train_easy_tictactoe_agent(10)
