import pygame as pg

# Establish color variables
red = pg.Color(255, 0, 0)
green = pg.Color(0, 255, 0)
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
brown = pg.Color(165, 42, 42)
gray = pg.Color(128, 128, 128)
yellow = pg.Color(255, 255, 0)

# Screen variables
screen_width = 400
screen_height = 400

# Initialize pygame
pg.init()

# Create the screen
wn = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('A simple game of Snake')

# The mainloop
game_is_running = True
while game_is_running:
    # This loop captures the events of the game
    for event in pg.event.get():
        # When you press the close button sets gameIs Running to False
        if event.type == pg.QUIT:
            game_is_running = False
    # Sets the screen to black
    wn.fill(black)
# Exits pygame when gameIsRunning is set to False
pg.quit()
