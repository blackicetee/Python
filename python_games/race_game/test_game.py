import pygame

display_width = 800
display_height = 600

CAR_IMAGE_NAME = 'transparent_car.png'

# RGB defined variables RED GREEN BLUE(RGB)
# (0, 0, 0) means there is no red no green and no blue
black = (0, 0, 0)
# (255, 255, 255) means red green and blue are all at maximum intensity
white = (255, 255, 255)

# The initialize command from pygame
pygame.init()
# Defines the (width, height) of the main window/display
# (800, 600) is a python tuple
gameDisplay = pygame.display.set_mode((display_width, display_height))
# Defines the caption/headline of the main window
pygame.display.set_caption('A bit Racy')
# The internal clock who measures the game time
clock = pygame.time.Clock()

def game_loop():
    # Boolean variable to check if car is crashed or not
    game_exit = False

    # The main game loop: the business logic is written in this loop
    while not game_exit:
        # Returns every mouse or keyboard input event
        for event in pygame.event.get():
            # Checks if user want to quit the program
            if event.type == pygame.QUIT:
                game_exit = True

        # Overwrites the complete screen with white even the car image so but it before showing the car
        gameDisplay.fill(white)

        # Displays an image of a car at screen position (x, y)
        self.display_position_coordinate_x += self.change_display_position_coordinate_x
        self.display_position_coordinate_y += self.change_display_position_coordinate_y
        gameDisplay.blit(self.car_image, (self.display_position_coordinate_x, self.display_position_coordinate_y))

        if car.display_position_coordinate_x > display_width or car.display_position_coordinate_x < 0:
            game_exit = True

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