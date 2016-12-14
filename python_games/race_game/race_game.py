# This program will implement a "Tic Tac Toe" game with the pygame 
import pygame

display_width = 800
display_height = 600

# __________Declaration of constants___________

# Reference the path of a race car image
CAR_IMAGE_NAME = 'transparent_car.png'

# RGB defined variables RED GREEN BLUE(RGB) 
# (0, 0, 0) means there is no red no green and no blue
black = (0, 0, 0)
# (255, 255, 255) means red green and blue are all at maximum intensity
white = (255, 255, 255)

# If only the first one is at a maximum and the two last parameters are 0 then its red
red = (255, 0, 0)
#If only the parameter for the green part is at maximum and the other parameters are 0 then its green
green = (0, 255, 0)
# Its equal for the blue parameter
blue = (0, 0, 255)

# The initialize command from pygame
pygame.init()
# Defines the (width, height) of the main window/display
# (800, 600) is a python tuple
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Defines the caption/headline of the main window
pygame.display.set_caption('A bit Racy')
# The internal clock who measures the game time
clock = pygame.time.Clock()

class Car:
    """ This class will handle the functionalities for a car like:
        -drawing the car image on the main screen
        -moving the car on key down and key up"""

    # __________Declaration of member variables__________

    # The coordinates for positioning a car image at the main screen
    display_position_coordinate_x = 0
    display_position_coordinate_y = 0

    change_display_position_coordinate_x = 0
    change_display_position_coordinate_y = 0

    car_image = None
    
    def __init__(self, car_image, display_position_coordinate_x, display_position_coordinate_y):
        """ Will initialize a car object with a car image for screen representation purpose and coordinates for the 
        position"""
        self.car_image = pygame.image.load(car_image)
        self.display_position_coordinate_x = display_position_coordinate_x
        self.display_position_coordinate_y = display_position_coordinate_y

    def move_car_on_event_keypress_direction_arrows(self, event):
        # Is there a key press at all?
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.change_display_position_coordinate_x = -5
            elif event.key == pygame.K_RIGHT:
                self.change_display_position_coordinate_x = 5
            elif event.key == pygame.K_UP:
                self.change_display_position_coordinate_y = -5
            elif event.key == pygame.K_DOWN:
                self.change_display_position_coordinate_y = 5
        self.reset_car_movement_after_keypressing(event)

    def reset_car_movement_after_keypressing(self, event):
        # Is there a key lifted up? (When you take the finger away from a key after pressing it)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.change_display_position_coordinate_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.change_display_position_coordinate_y = 0

    # will draw an image of the car to the main screen
    def draw_car(self):
        self.display_position_coordinate_x += self.change_display_position_coordinate_x
        self.display_position_coordinate_y += self.change_display_position_coordinate_y
        gameDisplay.blit(self.car_image, (self.display_position_coordinate_x, self.display_position_coordinate_y))        

def game_loop():
    # Boolean variable to check if car is crashed or not
    game_exit = False
    
    # Initialize instance of car class
    car = Car(CAR_IMAGE_NAME, (display_width * 0.45), (display_height * 0.8))
    
    #The main game loop: the business logic is written in this loop
    while not game_exit:
        # Returns every mouse or keyboard input event
        for event in pygame.event.get():
            # Checks if user want to quit the program
            if event.type == pygame.QUIT:
                game_exit = True
                       
            car.move_car_on_event_keypress_direction_arrows(event)

        # Overwrites the complete screen with white even the car image so but it before showing the car
        gameDisplay.fill(white)

        # Displays an image of a car at screen position (x, y) 
        car.draw_car()
                            
        # Updates the main window
        pygame.display.update()
        
        # Parameter defines how much frames per second should be shown
        clock.tick(60)

# Call of the main loop function (business logic is handled here)
game_loop()

# Special function for quitting pygame is like pygame.init() for correct quitting the game
pygame.quit()

# A python function to exit the program
quit()
