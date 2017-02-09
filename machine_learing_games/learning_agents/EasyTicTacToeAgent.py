from machine_learing_games.learning_agents.SQLiteTicTacToeAgentExperience import SQLiteTicTacToeAgentExperience
from machine_learing_games.tictactoe.TicTacToe import TicTacToe
from machine_learing_games.tictactoe.TicTacToeZobrist import TicTacToeZobrist


class EasyTicTacToeAgent:
    def __init__(self):
        self.__tictactoe = TicTacToe(4)
        self.__ply = ()
        self.__zobrist_hashing = TicTacToeZobrist()
        self.__agent_experience_db = SQLiteTicTacToeAgentExperience()

    def action(self, tictactoe=TicTacToe(4)):
        self.__calculate_enemy_move(tictactoe)
        zobrist_hash = self.__zobrist_hashing.get_hash(tictactoe.game_matrix)
        use_value = 0
        alpha_beta_window = 0
        self.__ply = tictactoe.get_possible_moves()[0]
        depth = tictactoe.count_of_game_tokens_in_game()
        player_turn = self.__calculate_player_turn(tictactoe)
        self.__agent_experience_db.insert_agent_experience(zobrist_hash, use_value, alpha_beta_window, str(self.__ply), depth, player_turn)
        print self.__tictactoe.printable_game_matrix()
        print tictactoe.printable_game_matrix()
        return self.__ply

    def reward(self, game_result):
        self.__tictactoe = TicTacToe(4)
        self.__ply = ()

    def scan_environment(self, tictactoe):
        self.__tictactoe = tictactoe
        self.__save_data_in_transposition_table()

    def __save_data_in_transposition_table(self, use_value, alpha, beta, optimal_move, depth, player_turn):
        zobrist_hash = self.__zobrist_hashing.get_hash(self.__tictactoe.game_matrix)
        usefulness = 0
        alpha = 0
        beta = 0
        optimal_move = (0, 0)
        depth = self.__tictactoe.count_of_game_tokens_in_game()
        player_turn = self.__calculate_player_turn(self.__tictactoe)
        self.__agent_experience_db.insert_agent_experience(zobrist_hash, usefulness, alpha, beta, str(optimal_move),
                                                           depth, player_turn)

    def __calculate_enemy_move(self, new_state=TicTacToe(4)):
        if self.__ply != ():
            self.__tictactoe.put_game_token('X', self.__ply)
            zobrist_hash = self.__zobrist_hashing.get_hash(self.__tictactoe.game_matrix)
            use_value = 0
            alpha_beta_window = 0
            ply = self.__calculate_ply(self.__tictactoe, new_state)
            depth = self.__tictactoe.count_of_game_tokens_in_game()
            player_turn = self.__calculate_player_turn(self.__tictactoe)
            self.__agent_experience_db.insert_agent_experience(zobrist_hash, use_value, alpha_beta_window,
                                                               str(list(ply[0])), depth, player_turn)
            self.__tictactoe.put_game_token('O', list(ply)[0])

    def __calculate_last_player_turn(self, tictactoe_state=TicTacToe(4)):
        if tictactoe_state.count_of_game_tokens_in_game() % 2 == 0:
            return 'O'
        elif tictactoe_state.count_of_game_tokens_in_game() % 2 == 1:
            return 'X'

    def __calculate_player_turn(self, tictactoe_state=TicTacToe(4)):
        if tictactoe_state.count_of_game_tokens_in_game() % 2 == 0:
            return 'X'
        elif tictactoe_state.count_of_game_tokens_in_game() % 2 == 1:
            return 'O'

    def __calculate_ply(self, old__state, new_state):
        return set(old__state.get_possible_moves()) ^ set(new_state.get_possible_moves())


