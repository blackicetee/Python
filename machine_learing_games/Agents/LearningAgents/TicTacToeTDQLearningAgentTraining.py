from machine_learing_games.Agents.LearningAgents.TicTacToeTDQLearningAgent import TDQLearningAgentTicTacToe

TICTACTOE_TDQ_AGENT_100_NAME = '3x3_ttt_tdq_agent_100_.db'
TICTACTOE_TDQ_AGENT_1000_NAME = '3x3_ttt_tdq_agent_1000_.db'
TICTACTOE_TDQ_AGENT_10000_NAME = '3x3_ttt_tdq_agent_10000_.db'

def trainAgentIn100Games():
    agent = TDQLearningAgentTicTacToe(TICTACTOE_TDQ_AGENT_100_NAME)
    agent.learn3x3Tictactoe(5)
    agent.closeDB()

def trainAgentIn1000Games():
    agent = TDQLearningAgentTicTacToe(TICTACTOE_TDQ_AGENT_1000_NAME)
    agent.learn3x3Tictactoe(1000)
    agent.closeDB()

def trainAgentIn10000Games():
    agent = TDQLearningAgentTicTacToe(TICTACTOE_TDQ_AGENT_10000_NAME)
    agent.learn3x3Tictactoe(10000)
    agent.closeDB()

trainAgentIn100Games()