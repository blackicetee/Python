from python_games.simple_games.NewTicTacToe import NewTicTacToe
from random import randint

TICTACTOE_TRAINING_SET = "tictactoe_training_set.txt"


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


def write_string_in_file(string, file_name):
    with open(file_name, "w") as text_file:
        text_file.write("{}".format(string))

def generate_amount_of_tictactoe_training_sets_with_representatoin(amount_of_tictactoe_training_sets):
    with open(TICTACTOE_TRAINING_SET, "w") as text_file:
        for amount in range(amount_of_tictactoe_training_sets):
            result_list = create_random_tictactoe_training_example()
            string = result_list[2].printable_game_matrix() + 'action_sequence: ' + str(
                    result_list[0]) + '\n' + 'target_value: ' + result_list[1] + '\n\n'
            text_file.write("{}".format(string))

def generate_amount_of_tictactoe_training_sets(amount_of_tictactoe_training_sets):
    with open(TICTACTOE_TRAINING_SET, "w") as text_file:
        for amount in range(amount_of_tictactoe_training_sets):
            result_list = create_random_tictactoe_training_example()
            string = str(result_list[0]) + result_list[1] + '\n'
            text_file.write("{}".format(string))
generate_amount_of_tictactoe_training_sets(10000)