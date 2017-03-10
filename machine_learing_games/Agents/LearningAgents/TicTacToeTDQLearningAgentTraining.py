from machine_learing_games.Agents.LearningAgents.TicTacToeTDQLearningAgent import TDQLearningAgentTicTacToe


def trainAgentIn100Games():
    agent = TDQLearningAgentTicTacToe('3x3_ttt_tdq_agent_100_.db')
    agent.learnTictactoe(100)
    agent.closeDB()

def trainAgentIn1000Games():
    agent = TDQLearningAgentTicTacToe('3x3_ttt_tdq_agent_1000_.db')
    agent.learnTictactoe(1000)
    agent.closeDB()

def trainAgentIn10000Games():
    agent = TDQLearningAgentTicTacToe('3x3_ttt_tdq_agent_10000_.db')
    agent.learnTictactoe(10000)
    agent.closeDB()

trainAgentIn1000Games()