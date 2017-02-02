from machine_learning_approaches.TicTacToeDescionsionTreeAgent import TicTacToeDecisionTreeAgent
from python_games.simple_games.NewTicTacToe import NewTicTacToe
from random import randint


class TicTacToeEnvironment:
    def __init__(self):
        self.__tictactoe_desision_tree_agent = TicTacToeDecisionTreeAgent()
        self.__tictactoe = NewTicTacToe(4)
        self.__round_count = 0
        self.__target_value = ''

    def __initialize_new_tictactoe_game(self):
        self.__tictactoe = NewTicTacToe(4)
        self.__round_count = 0
        self.__target_value = ''

    def train_decision_tree_agent_x_times_against_random_agent(self, times):
        for game in range(0, times):
            self.__initialize_new_tictactoe_game()
            while self.__target_value == '' and self.__round_count < 15:
                agent_move = self.get_move_from_tictactoe_decision_tree_agent()
                self.__tictactoe.put_game_token('X', agent_move)
                self.__round_count += 1
                self.reward_tictactoe_decision_tree_agent()


    def reward_tictactoe_decision_tree_agent(self):
        if self.__round_count == 15 and not self.__tictactoe.is_victory():
            self.__tictactoe_desision_tree_agent.receive_reward('draw')
        elif (self.__round_count % 2) == 0 and self.__tictactoe.is_victory():
            self.__tictactoe_desision_tree_agent.receive_reward('win')
        elif (self.__round_count % 2) == 1 and self.__tictactoe.is_victory():
            self.__tictactoe_desision_tree_agent.receive_reward('lost')
        else:
            self.__tictactoe_desision_tree_agent.receive_reward('')

    def get_move_from_tictactoe_decision_tree_agent(self):
        self.__tictactoe_desision_tree_agent.update_state(self.__tictactoe, self.tictactoe_random_agent_move())
        agent_action = self.__tictactoe_desision_tree_agent.get_action_decision()
        # self.__tictactoe_desision_tree_agent.give_reward(self.evaluate(agent_action))
        return agent_action

    def tictactoe_random_agent_move(self):
        possible_actions = self.__tictactoe.get_possible_moves()
        random_agent_move = possible_actions[randint(0, (len(possible_actions) - 1))]
        if self.__round_count % 2 == 1:
            self.__tictactoe.put_game_token('O', random_agent_move)
            self.__round_count += 1
            return random_agent_move
        else:
            return ()


"""
    def create_random_tictactoe_training_example():
        tictactoe = NewTicTacToe(4)
        round_count = 0
        target_value = ''
        action_sequence = []
        while target_value == '':
            actions = tictactoe.get_possible_moves()
            random_action = randint(0, (len(actions) - 1))
            action_sequence.append(actions[random_action])
            if (round_count % 2) == 0:
                tictactoe.put_game_token('X', actions[random_action])
            else:
                tictactoe.put_game_token('O', actions[random_action])

            if round_count == 15 and not tictactoe.is_victory():
                target_value = 'draw'

            if (round_count % 2) == 0 and tictactoe.is_victory():
                target_value = 'win'

            if (round_count % 2) == 1 and tictactoe.is_victory():
                target_value = 'lost'

            round_count += 1

        return [action_sequence, target_value, tictactoe]
"""
tictactoe_environment = TicTacToeEnvironment()
tictactoe_environment.train_decision_tree_agent_x_times_against_random_agent(100)
