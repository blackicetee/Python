from random import randint

from machine_learing_games.tictactoe.TicTacToe import TicTacToe

TICTACTOE_TRAINING_SET = "tictactoe_training_set.txt"


def create_random_tictactoe_training_example():
    tictactoe = TicTacToe(4)
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


def write_every_element_in_list_to_open_textfile(open_textfile, list):
    for element in list:
        open_textfile.write("{}|".format(str(element)))


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
        column_label = "LvL 1 |LvL 2 |LvL 3 |LvL 4 |LvL 5 |LvL 6 |LvL 7 |LvL 8 |LvL 9 |LvL 10|LvL 11|LvL 12|LvL 13|LvL 14|LvL 15|LvL 16|Target Value"
        table_limits = "______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|____________"
        text_file.write("{}\n".format(column_label))
        text_file.write("{}\n".format(table_limits))
        for amount in range(amount_of_tictactoe_training_sets):
            result_list = create_random_tictactoe_training_example()
            white_space_buffer = 16 - len(result_list[0])
            write_every_element_in_list_to_open_textfile(text_file, result_list[0])
            text_file.write("{}\n".format(("      |" * white_space_buffer) + result_list[1]))


generate_amount_of_tictactoe_training_sets(10)
