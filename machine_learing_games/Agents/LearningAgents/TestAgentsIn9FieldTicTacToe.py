import unittest

from machine_learing_games.Agents import HeuristicSearchAgentTicTacToe
from machine_learing_games.Agents import RandomAgent
from machine_learing_games.Agents.LearningAgents.TicTacToeTDQLearningAgent import TicTacToeTDQLearningAgent, \
    TICTACTOE_3x3_TDQ_AGENT_100_NAME, TICTACTOE_3x3_TDQ_AGENT_1000_NAME, TICTACTOE_3x3_TDQ_AGENT_10000_NAME
from machine_learing_games.tictactoe.TicTacToe import TicTacToe


class TestTDQAgent100TrainingGamesIn9FiledTicTacToe(unittest.TestCase):
    def testAgainstFirstMoveRandomAgentIn100Testgames(self):
        randomAgentWins = 0
        tdqAgent100Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent100 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    ttt.make_move(tdqAgent100.suggestAction(ttt))
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                tdqAgent100Wins += 1
        print 'First Move random agent wins: ' + str(
            randomAgentWins) + ' games against TD-Q-Agent-100 in 9 field Tic Tac Toe!'
        print 'Second Move TD-Q-Agent-100 wins: ' + str(
            tdqAgent100Wins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent100Wins >= 50)

    def testAgainstSecondMoveRandomAgentIn100Testgames(self):
        randomAgentWins = 0
        tdqAgent100Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent100 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
            while not ttt.is_terminal():
                ttt.make_move(tdqAgent100.suggestAction(ttt))
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                tdqAgent100Wins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Second Move random agent wins: ' + str(
            randomAgentWins) + ' games against TD-Q-Agent-100 in 9 field Tic Tac Toe!'
        print 'First Move TD-Q-Agent-100 wins: ' + str(
            tdqAgent100Wins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent100Wins >= 50)

    def testAgainstFirstMoveHeuristikAgentIn100Testgames(self):
        heuristicSearchAgentWins = 0
        tdqAgent100Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent100 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
            while not ttt.is_terminal():
                HeuristicSearchAgentTicTacToe.processAction(ttt)
                if not ttt.is_terminal():
                    ttt.make_move(tdqAgent100.suggestAction(ttt))
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                heuristicSearchAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                tdqAgent100Wins += 1
        print 'First move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against TD-Q-Agent-100 in 9 field Tic Tac Toe!'
        print 'Second move TD-Q-Agent-100 wins: ' + str(
            tdqAgent100Wins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent100Wins >= 50)

    def testAgainstSecondMoveHeuristikAgentIn100Testgames(self):
        heuristicSearchAgentWins = 0
        tdqAgent100Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent100 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
            while not ttt.is_terminal():
                action = tdqAgent100.suggestAction(ttt)
                print action
                ttt.make_move(action)
                if not ttt.is_terminal():
                    HeuristicSearchAgentTicTacToe.processAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                tdqAgent100Wins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                heuristicSearchAgentWins += 1
        print 'Second move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against TD-Q-Agent-100 in 9 field Tic Tac Toe!'
        print 'First move TD-Q-Agent-100 wins: ' + str(
            tdqAgent100Wins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent100Wins >= 50)

class TestTDQAgent1000TrainingGamesIn9FiledTicTacToe(unittest.TestCase):
    def testAgainstFirstMoveRandomAgentIn100Testgames(self):
        randomAgentWins = 0
        tdqAgent1000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent1000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    ttt.make_move(tdqAgent1000.suggestAction(ttt))
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                tdqAgent1000Wins += 1
        print 'First Move random agent wins: ' + str(
            randomAgentWins) + ' games against TD-Q-Agent-1000 in 9 field Tic Tac Toe!'
        print 'Second Move TD-Q-Agent-1000 wins: ' + str(
            tdqAgent1000Wins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent1000Wins >= 50)

    def testAgainstSecondMoveRandomAgentIn100Testgames(self):
        randomAgentWins = 0
        tdqAgent1000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent1000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
            while not ttt.is_terminal():
                ttt.make_move(tdqAgent1000.suggestAction(ttt))
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                tdqAgent1000Wins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Second move random agent wins: ' + str(
            randomAgentWins) + ' games against TD-Q-Agent-1000 in 9 field Tic Tac Toe!'
        print 'First move TD-Q-Agent-1000 wins: ' + str(
            tdqAgent1000Wins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent1000Wins >= 50)

    def testAgainstFirstMoveHeuristikAgentIn100Testgames(self):
        heuristicSearchAgentWins = 0
        tdqAgent1000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent1000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
            while not ttt.is_terminal():
                HeuristicSearchAgentTicTacToe.processAction(ttt)
                if not ttt.is_terminal():
                    ttt.make_move(tdqAgent1000.suggestAction(ttt))
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                heuristicSearchAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                tdqAgent1000Wins += 1
        print 'First move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against TD-Q-Agent-100 in 9 field Tic Tac Toe!'
        print 'Second move TD-Q-Agent-1000 wins: ' + str(
            tdqAgent1000Wins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent1000Wins >= 50)

    def testAgainstSecondMoveHeuristikAgentIn100Testgames(self):
        heuristicSearchAgentWins = 0
        tdqAgent1000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent1000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
            while not ttt.is_terminal():
                action = tdqAgent1000.suggestAction(ttt)
                print action
                ttt.make_move(action)
                if not ttt.is_terminal():
                    HeuristicSearchAgentTicTacToe.processAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                tdqAgent1000Wins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                heuristicSearchAgentWins += 1
        print 'Second move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against TD-Q-Agent-1000 in 9 field Tic Tac Toe!'
        print 'First move TD-Q-Agent-1000 wins: ' + str(
            tdqAgent1000Wins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent1000Wins >= 50)

class TestTDQAgent10000TrainingGamesIn9FiledTicTacToe(unittest.TestCase):
    def testAgainstFirstMoveRandomAgentIn100Testgames(self):
        randomAgentWins = 0
        tdqAgent10000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent10000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
            while not ttt.is_terminal():
                RandomAgent.processTicTacToeAction(ttt)
                if not ttt.is_terminal():
                    ttt.make_move(tdqAgent10000.suggestAction(ttt))
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                randomAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                tdqAgent10000Wins += 1
        print 'First Move random agent wins: ' + str(
            randomAgentWins) + ' games against TD-Q-Agent-10000 in 9 field Tic Tac Toe!'
        print 'Second Move TD-Q-Agent-10000 wins: ' + str(
            tdqAgent10000Wins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent10000Wins >= 50)

    def testAgainstSecondMoveRandomAgentIn100Testgames(self):
        randomAgentWins = 0
        tdqAgent10000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent10000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
            while not ttt.is_terminal():
                ttt.make_move(tdqAgent10000.suggestAction(ttt))
                if not ttt.is_terminal():
                    RandomAgent.processTicTacToeAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                tdqAgent10000Wins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                randomAgentWins += 1
        print 'Second move random agent wins: ' + str(
            randomAgentWins) + ' games against TD-Q-Agent-10000 in 9 field Tic Tac Toe!'
        print 'First move TD-Q-Agent-10000 wins: ' + str(
            tdqAgent10000Wins) + ' games against random agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent10000Wins >= 50)

    def testAgainstFirstMoveHeuristikAgentIn100Testgames(self):
        heuristicSearchAgentWins = 0
        tdqAgent10000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent10000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
            while not ttt.is_terminal():
                HeuristicSearchAgentTicTacToe.processAction(ttt)
                if not ttt.is_terminal():
                    ttt.make_move(tdqAgent10000.suggestAction(ttt))
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                heuristicSearchAgentWins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                tdqAgent10000Wins += 1
        print 'First move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against TD-Q-Agent-100 in 9 field Tic Tac Toe!'
        print 'Second move TD-Q-Agent-10000 wins: ' + str(
            tdqAgent10000Wins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent10000Wins >= 50)

    def testAgainstSecondMoveHeuristikAgentIn100Testgames(self):
        heuristicSearchAgentWins = 0
        tdqAgent10000Wins = 0
        for testGameCount in range(100):
            ttt = TicTacToe(3)
            tdqAgent10000 = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
            while not ttt.is_terminal():
                action = tdqAgent10000.suggestAction(ttt)
                print action
                ttt.make_move(action)
                if not ttt.is_terminal():
                    HeuristicSearchAgentTicTacToe.processAction(ttt)
            print ttt.printable_game_matrix()
            if ttt.is_victory() and ttt.get_player_which_moved_last() == 'X':
                tdqAgent10000Wins += 1
            elif ttt.is_victory() and ttt.get_player_which_moved_last() == 'O':
                heuristicSearchAgentWins += 1
        print 'Second move heuristic search agent wins: ' + str(
            heuristicSearchAgentWins) + ' games against TD-Q-Agent-10000 in 9 field Tic Tac Toe!'
        print 'First move TD-Q-Agent-10000 wins: ' + str(
            tdqAgent10000Wins) + ' games against heuristic search agent in 9 field Tic Tac Toe!'
        self.assertTrue(tdqAgent10000Wins >= 50)