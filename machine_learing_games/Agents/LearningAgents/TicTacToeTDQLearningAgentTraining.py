from machine_learing_games.Agents.LearningAgents.TicTacToeTDQLearningAgent import TicTacToeTDQLearningAgent, \
    TICTACTOE_3x3_TDQ_AGENT_100_NAME, TICTACTOE_3x3_TDQ_AGENT_1000_NAME, TICTACTOE_3x3_TDQ_AGENT_10000_NAME, \
    TICTACTOE_4x4_TDQ_AGENT_100_NAME, TICTACTOE_4x4_TDQ_AGENT_1000_NAME, TICTACTOE_4x4_TDQ_AGENT_10000_NAME


def train3x3TicTacToeAgentIn100Games():
    agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_100_NAME, 3)
    agent.learnTictactoe(100)
    agent.closeDB()

def train3x3TicTacToeAgentIn1000Games():
    agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_1000_NAME, 3)
    agent.learnTictactoe(1000)
    agent.closeDB()

def train3x3TicTacToeAgentIn10000Games():
    agent = TicTacToeTDQLearningAgent(TICTACTOE_3x3_TDQ_AGENT_10000_NAME, 3)
    agent.learnTictactoe(10000)
    agent.closeDB()

def train4x4TicTacToeAgentIn100Games():
    agent = TicTacToeTDQLearningAgent(TICTACTOE_4x4_TDQ_AGENT_100_NAME, 4)
    agent.learnTictactoe(100)
    agent.closeDB()

def train4x4TicTacToeAgentIn1000Games():
    agent = TicTacToeTDQLearningAgent(TICTACTOE_4x4_TDQ_AGENT_1000_NAME, 4)
    agent.learnTictactoe(1000)
    agent.closeDB()

def train4x4TicTacToeAgentIn10000Games():
    agent = TicTacToeTDQLearningAgent(TICTACTOE_4x4_TDQ_AGENT_10000_NAME, 4)
    agent.learnTictactoe(10000)
    agent.closeDB()

train3x3TicTacToeAgentIn10000Games()