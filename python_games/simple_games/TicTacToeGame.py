# This program will implement a "Tic Tac Toe" game with the pygame
import pygame
from python_games.simple_games.TicTacToe import TicTacToe

display_width = 400
display_height = 500

# RGB defined variables RED GREEN BLUE(RGB)
# (0, 0, 0) means there is no red no green and no blue
black = (0, 0, 0)
# (255, 255, 255) means red green and blue are all at maximum intensity
white = (255, 255, 255)
red = (255, 0, 0)

TICTACTOE_GAME_MATRIX_PICTURE = 'simple_games_pictures/vier_mal_vier_matrix_400px.png'
GAME_TOKEN_X = 'simple_games_pictures/X.png'
GAME_TOKEN_O = 'simple_games_pictures/O.png'

# The initialize command from pygame
pygame.init()
# Defines the (width, height) of the main window/display
# (800, 600) is a python tuple
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Defines the caption/headline of the main window
pygame.display.set_caption('TicTacToe 4x4')
# The internal clock who measures the game time
clock = pygame.time.Clock()


class TicTacToeGame:
    """"""

    def __init__(self):
        self.__tictactoe_game = TicTacToe(4, 4)
        self.__tictactoe_game_matrix_picture = pygame.image.load(TICTACTOE_GAME_MATRIX_PICTURE)
        self.__game_token_x = pygame.image.load(GAME_TOKEN_X)
        self.__game_token_o = pygame.image.load(GAME_TOKEN_O)
        self.draw_tictactoe_game_matrix()
        # Updates the main window
        pygame.display.update()

    def start_game(self, name_player_one, name_player_two):

        game_round = 0

        while not self.__tictactoe_game.is_victory() and game_round <= 15:
            if game_round % 2 == 0:
                self.__request_message_player_move(name_player_one)
                self.__player_move('X', name_player_one)
            else:
                self.__request_message_player_move(name_player_two)
                self.__player_move('O', name_player_two)

            game_round += 1

        if self.__tictactoe_game.is_victory():
            game_round -= 1
            if game_round % 2 == 0:
                self.__victory_message(name_player_one)
            else:
                self.__victory_message(name_player_two)
        elif game_round >= 15:
            self.__draw_message()

    def draw_tictactoe_game_matrix(self):
        gameDisplay.fill(white)
        gameDisplay.blit(self.__tictactoe_game_matrix_picture, (0, 0))
        for row in range(4):
            for col in range(4):
                if self.__tictactoe_game.game_matrix[row, col] == 1.0:
                    gameDisplay.blit(self.__game_token_o, (row * 100, col * 100))
                elif self.__tictactoe_game.game_matrix[row, col] == 2.0:
                    gameDisplay.blit(self.__game_token_x, (row * 100, col * 100))

    def __player_move(self, game_token, player):
        col = self.__is_input_valid()
        row = self.__is_input_valid()
        if not self.__tictactoe_game.put_game_token(game_token, (row, col)):
            self.__repeat_request_message_player_move(player)
            self.__player_move(game_token, player)

    def __evaluate_keypress(self, event):
        if event.key == pygame.K_0:
            return 0
        elif event.key == pygame.K_1:
            return 1
        elif event.key == pygame.K_2:
            return 2
        elif event.key == pygame.K_3:
            return 3
        else:
            self.__wrong_key_input()
            return -1

    def __check_quit_querry(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def __is_input_valid(self):
        correct_player_move = False
        while not correct_player_move:
            for event in pygame.event.get():
                self.__check_quit_querry(event)
                if event.type == pygame.KEYDOWN:
                    key_press = self.__evaluate_keypress(event)
                    if key_press != -1:
                        correct_player_move = True
        return key_press

    def __wrong_key_input(self):
        self.draw_tictactoe_game_matrix()
        my_font = pygame.font.SysFont("monospace", 15)
        label1 = my_font.render('Falsche Tastatureingabe:', True, black)
        label2 = my_font.render('Nur die Tasten 0, 1, 2 und 3 sind erlaubt!', True, black)
        label3 = my_font.render('Moegliche Beispiele [00, 01, 10, ..., 32, 33]', True, black)
        gameDisplay.blit(label1, (0, 400))
        gameDisplay.blit(label2, (0, 420))
        gameDisplay.blit(label3, (0, 440))
        pygame.display.update()

    def __request_message_player_move(self, player):
        self.draw_tictactoe_game_matrix()
        my_font = pygame.font.SysFont("monospace", 15)
        label1 = my_font.render(player + ':', True, black)
        label2 = my_font.render('Bitte setze deinen Spielstein!', True, black)
        gameDisplay.blit(label1, (0, 400))
        gameDisplay.blit(label2, (0, 420))
        pygame.display.update()

    def __repeat_request_message_player_move(self, player):
        self.draw_tictactoe_game_matrix()
        my_font = pygame.font.SysFont("monospace", 15)
        label1 = my_font.render(player + ':', True, black)
        label2 = my_font.render('Die gewaehlte Position ist besetzt!', True, black)
        label3 = my_font.render('Bitte waehle eine andere Position.', True, black)
        gameDisplay.blit(label1, (0, 400))
        gameDisplay.blit(label2, (0, 420))
        gameDisplay.blit(label3, (0, 440))
        pygame.display.update()

    def __victory_message(self, player):
        self.draw_tictactoe_game_matrix()
        my_font = pygame.font.SysFont("monospace", 40)
        label1 = my_font.render(player + ' gewinnt', True, red)
        label2 = my_font.render('das Spiel :D', True, red)
        gameDisplay.blit(label1, (0, 400))
        gameDisplay.blit(label2, (0, 440))
        pygame.display.update()
        pygame.time.delay(5000)

    def __draw_message(self):
        self.draw_tictactoe_game_matrix()
        my_font = pygame.font.SysFont("monospace", 40)
        label = my_font.render('Unentschieden', True, red)
        gameDisplay.blit(label, (0, 400))
        pygame.display.update()
        pygame.time.delay(5000)



while True:
    tictactoe_game = TicTacToeGame()
    tictactoe_game.start_game("Thilo", "Ingo")

# Parameter defines how much frames per second should be shown
clock.tick(60)

# Special function for quitting pygame is like pygame.init() for correct quitting the game
pygame.quit()

# A python function to exit the program
quit()
