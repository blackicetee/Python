# This program will implement a "Tic Tac Toe" game with the pygame 
import pygame

display_width = 800
display_height = 600

x_change = 0

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

car_image = pygame.image.load(CAR_IMAGE_NAME)

def car(x, y):
	# blit will draw the image to the surface/main display at position (x, y)
	gameDisplay.blit(car_image, (x, y))

# Variables for coordinates on the screen
x = (display_width * 0.45)
y = (display_height * 0.8)



# Boolean variable to check if car is crashed or not
crashed = False

# The main game loop: the business logic is written in this loop
while not crashed:
	# Returns every mouse or keyboard input event
	for event in pygame.event.get():
		# Checks if user want to quit the program
		if event.type == pygame.QUIT:
			crashed = True
		
		# Is there a key press at all?
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x_change = -5
			elif event.key == pygame.K_RIGHT:
				x_change = 5
		
		# Is there a key lifted up? (When you take the finger away from a key after pressing it)
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x_change = 0


		x += x_change

		# Overwrites the complete screen with white even the car image so but it before showing the car
		gameDisplay.fill(white)

		# Displays an image of a car at screen position (x, y) 
		car(x, y)
			
	# Updates the main window
	pygame.display.update()
	# Parameter defines how much frames per second should be shown
	clock.tick(60)

# Special function for quitting pygame is like pygame.init() for correct quitting the game
pygame.quit()

# A python function to exit the program
quit()
