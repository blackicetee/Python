# This program will implement a "Tic Tac Toe" game with the pygame
import pygame
from python_games.simple_games.Reversi import Reversi

display_width = 700
display_height = 450

# RGB defined variables RED GREEN BLUE(RGB)
# (0, 0, 0) means there is no red no green and no blue
black = (0, 0, 0)
# (255, 255, 255) means red green and blue are all at maximum intensity
white = (255, 255, 255)
red = (255, 0, 0)

REVERSI_GAME_MATRIX_PICTURE = 'simple_games_pictures/reversi_pictures/reversi_spielfeld_450px.png'
BLACK_GAME_TOKEN = 'simple_games_pictures/reversi_pictures/black_token_50px.png'
WHITE_GAME_TOKEN = 'simple_games_pictures/reversi_pictures/white_token_50px.png'
GREY_SUGGESTION_TOKEN = 'simple_games_pictures/reversi_pictures/grey_suggestion_50px.png'

# The initialize command from pygame
pygame.init()
# Defines the (width, height) of the main window/display
# (800, 600) is a python tuple
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Defines the caption/headline of the main window
pygame.display.set_caption('REVERSI')
# The internal clock who measures the game time
clock = pygame.time.Clock()

class ReversiGame:
    """"""

    def __init__(self):
        self.__reversi = Reversi()
        self.__move_suggestions = set()
        self.__reversi.put_game_token('B', (3, 3))
        self.__reversi.put_game_token('B', (4, 4))
        self.__reversi.put_game_token('W', (3, 4))
        self.__reversi.put_game_token('W', (4, 3))
        self.__reversi_game_matrix_picture = pygame.image.load(REVERSI_GAME_MATRIX_PICTURE)
        self.__black_game_token = pygame.image.load(BLACK_GAME_TOKEN)
        self.__white_game_token = pygame.image.load(WHITE_GAME_TOKEN)
        self.__grey_suggestion_token = pygame.image.load(GREY_SUGGESTION_TOKEN)


    def start_game(self, name_player_one, name_player_two):

        game_round = 0

        #while not self.__reversi.is_finished():
        while game_round < 40:
            if game_round % 2 == 0:
                self.__move_suggestions = self.__reversi.suggest_all_moves('B')
                self.draw_reversi_game_matrix()
                self.__request_message_player_move(name_player_one)
                self.__player_move('B', name_player_one)
            else:
                self.__move_suggestions = self.__reversi.suggest_all_moves('W')
                self.draw_reversi_game_matrix()
                self.__request_message_player_move(name_player_two)
                self.__player_move('W', name_player_two)

            print(self.__move_suggestions)
            game_round += 1

        """
        if self.__reversi.is_finished():
            game_round -= 1
            if game_round % 2 == 0:
                self.__victory_message(name_player_one)
            else:
                self.__victory_message(name_player_two)
        elif self.__reversi.is_draw():
            self.__draw_message()
            """

    def draw_reversi_game_matrix(self):
        gameDisplay.fill(white)
        gameDisplay.blit(self.__reversi_game_matrix_picture, (0, 0))
        for row in range(8):
            for col in range(8):
                if self.__reversi.game_matrix[row, col] == 1.0:
                    gameDisplay.blit(self.__black_game_token, ((col + 1) * 50, (row + 1) * 50))
                elif self.__reversi.game_matrix[row, col] == 2.0:
                    gameDisplay.blit(self.__white_game_token, ((col + 1) * 50, (row + 1) * 50))
        self.draw_move_suggestions()
        self.draw_score()

    def draw_move_suggestions(self):
        for move_suggestion in self.__move_suggestions:
            gameDisplay.blit(self.__grey_suggestion_token, ((move_suggestion[1] + 1) * 50, (move_suggestion[0] + 1) * 50))
            pygame.display.update()

    def draw_score(self):
        black_token_count = str(self.__reversi.count_black_game_tokens())
        white_token_count = str(self.__reversi.count_white_game_tokens())
        gameDisplay.blit(self.__black_game_token, (500, 50))
        my_font = pygame.font.SysFont("arial", 35)
        black_token_count_label = my_font.render(black_token_count, True, black)
        gameDisplay.blit(black_token_count_label, (560, 50))
        gameDisplay.blit(self.__white_game_token, (500, 150))
        white_token_count_label = my_font.render(white_token_count, True, black)
        gameDisplay.blit(white_token_count_label, (560, 150))
        pygame.display.update()

    def __player_move(self, game_token_type, player):
        row = self.__is_input_valid()
        col = self.__is_input_valid()
        if not self.__reversi.game_token_move(game_token_type, (row, col)):
            self.__repeat_request_message_player_move(player)
            self.__player_move(game_token_type, player)

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

    def __check_quit_querry(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    def __evaluate_keypress(self, event):
        if event.key == pygame.K_0:
            return 0
        elif event.key == pygame.K_1:
            return 1
        elif event.key == pygame.K_2:
            return 2
        elif event.key == pygame.K_3:
            return 3
        elif event.key == pygame.K_4:
            return 4
        elif event.key == pygame.K_5:
            return 5
        elif event.key == pygame.K_6:
            return 6
        elif event.key == pygame.K_7:
            return 7
        else:
            self.__wrong_key_input()
            return -1

    def __wrong_key_input(self):
        self.draw_reversi_game_matrix()
        my_font = pygame.font.SysFont("arial", 15)
        label1 = my_font.render('Falsche Tastatureingabe', True, black)
        label2 = my_font.render('Nur die Tasten 0 bis 7 sind erlaubt!', True, black)
        label3 = my_font.render('Moegliche Beispiele:', True, black)
        label4 = my_font.render('[00, 01, 10, ..., 76, 77]', True, black)
        gameDisplay.blit(label1, (451, 210))
        gameDisplay.blit(label2, (451, 230))
        gameDisplay.blit(label3, (451, 250))
        gameDisplay.blit(label4, (451, 270))
        pygame.display.update()


    def __request_message_player_move(self, player):
        self.draw_reversi_game_matrix()
        my_font = pygame.font.SysFont("arial", 15)
        label1 = my_font.render(player + ':', True, black)
        label2 = my_font.render('Bitte setze deinen Spielstein!', True, black)
        gameDisplay.blit(label1, (451, 210))
        gameDisplay.blit(label2, (451, 230))
        pygame.display.update()

    def __repeat_request_message_player_move(self, player):
        self.draw_reversi_game_matrix()
        my_font = pygame.font.SysFont("arial", 15)
        label1 = my_font.render(player + ':', True, black)
        label2 = my_font.render('Dies ist kein zugelassene Position!', True, black)
        label3 = my_font.render('Zugelassene Positionen werden durch', True, black)
        label4 = my_font.render('einen kleinen grauen Kreis makiert.', True, black)
        label5 = my_font.render('Bitte waehle eine andere Position.', True, black)
        gameDisplay.blit(label1, (451, 210))
        gameDisplay.blit(label2, (451, 230))
        gameDisplay.blit(label3, (451, 250))
        gameDisplay.blit(label4, (451, 270))
        gameDisplay.blit(label5, (451, 290))
        pygame.display.update()


    def __victory_message(self, player):
        self.draw_reversi_game_matrix()
        my_font = pygame.font.SysFont("arial", 40)
        label1 = my_font.render(player + ' gewinnt', True, red)
        label2 = my_font.render('das Spiel :D', True, red)
        gameDisplay.blit(label1, (451, 210))
        gameDisplay.blit(label2, (451, 250))
        pygame.display.update()
        pygame.time.delay(5000)

    def __draw_message(self):
        self.draw_reversi_game_matrix()
        my_font = pygame.font.SysFont("arial", 40)
        label = my_font.render('Unentschieden', True, red)
        gameDisplay.blit(label, (451, 210))
        pygame.display.update()
        pygame.time.delay(5000)




while True:
    reversi_game = ReversiGame()
    reversi_game.start_game("Thilo", "Ingo")

# Parameter defines how much frames per second should be shown
clock.tick(60)

# Special function for quitting pygame is like pygame.init() for correct quitting the game
pygame.quit()

# A python function to exit the program
quit()