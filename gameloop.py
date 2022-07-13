import pygame as pg
import time
import random


class Snek:
    # Initialization
    def __init__(self):
        self.x = screen_width/2
        self.y = screen_height/2
        self.width = 10
        self.height = 10
        self.velocity = 10
        self.direction = 0
        self.body = []
        self.head_color = green
        self.body_color = brown

    # Draws the snek
    def draw_player(self, surface):
        self.seg = []
        self.head = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(surface, self.head_color, self.head)
        if len(self.body) > 0:
            for unit in self.body:
                segment = pg.Rect(unit[0], unit[1], self.width, self.height)
                pg.draw.rect(surface, self.body_color, segment)
                self.seg.append(segment)

    # Increase the length of the snek
    def add_unit(self):
        if len(self.body) != 0:
            index = len(self.body) - 1
            x = self.body[index][0]
            y = self.body[index][1]
            self.body.append([x, y])
        else:
            self.body.append([1000, 1000])

    # Checking for a collision
    def is_collision(self):
        # Did player collide with himself?
        for segment in self.seg:
            if self.head.colliderect(segment):
                return True
        # Did player collide with the boundaries?
        if self.y < 0 or self.y > screen_height - self.height or self.x < 0 or self.x > screen_width - self.width:
            return True

    # The body of the snek follows the head
    def move(self):
        for index in range(len(self.body)-1, 0, -1):
            x = self.body[index - 1][0]
            y = self.body[index - 1][1]
            self.body[index] = [x, y]
        if len(self.body) > 0:
            self.body[0] = [self.x, self.y]
        if self.direction == 1:
            self.y -= self.velocity
        if self.direction == 2:
            self.y += self.velocity
        if self.direction == 3:
            self.x -= self.velocity
        if self.direction == 4:
            self.x += self.velocity

    # changes the direction of the head
    def change_direction(self, direction):
        if self.direction != 2 and direction == 1:
            self.direction = 1
        if self.direction != 4 and direction == 3:
            self.direction = 3
        if self.direction != 1 and direction == 2:
            self.direction = 2
        if self.direction != 3 and direction == 4:
            self.direction = 4


# Food class
class Food:
    def __new__(cls):
        other = random.choice([Apple, Chicken, Turtle, Frog, Mouse])
        instance = super().__new__(other)
        return instance


class Apple:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(0, screen_width - self.width)
        self.y = random.randrange(0, screen_height - self.height)
        self.color = red
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 1

    # Displays the apple on screen
    def draw_food(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snek eat the apple?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the apple when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

    # active the apples power
    @staticmethod
    def power():
        # TODO : add the apples power
        return


class Chicken:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(0, screen_width - self.width)
        self.y = random.randrange(0, screen_height - self.height)
        self.color = yellow
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 10

    # Displays the chicken on screen
    def draw_food(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snek eat the chicken?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the chicken when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

    # activate the chickens power
    @staticmethod
    def power():
        # TODO: add the chickens power
        return


class Turtle:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(0, screen_width - self.width)
        self.y = random.randrange(0, screen_height - self.height)
        self.color = brown
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 5

    # Displays the turtle on screen
    def draw_food(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snek eat the turtle?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the turtle when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

    # activate the turtles power
    @staticmethod
    def power():
        # TODO: add the turtles power
        return


class Frog:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(0, screen_width - self.width)
        self.y = random.randrange(0, screen_height - self.height)
        self.color = green
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 5

    # Displays the frog on screen
    def draw_food(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snek eat the frog?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the frog when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

    # Activate the frogs power
    @staticmethod
    def power():
        # TODO: add the frogs power
        return


class Mouse:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(screen_width - self.width)
        self.y = random.randrange(screen_height - self.height)
        self.color = gray
        self.food = pg.Rect(self.x, self.y, self.width, self.height)
        self.points = 10

    # Displays the mouse on screen
    def draw_food(self, surface):
        pg.draw.rect(surface, self.color, self.food)

    # Did the snek eat the mouse?
    def is_eaten(self, head):
        return self.food.colliderect(head)

    # Update new position for the mouse when eaten
    def new_pos(self):
        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

    # activate the mouses power - sends the snek in a random direction
    @staticmethod
    def power():
        # send the snek in a random direction
        if s.direction == 1 or s.direction == 2:
            rnd = random.randint(3, 4)
        else:
            rnd = random.randint(1, 2)
        s.change_direction(rnd)
        print(s.direction)
        s.move()


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
pg.display.set_caption('Snek: A story of survival')

score, high_score = (0, 0)
clock = pg.time.Clock()


# Create a random number
def rnd_num(x, y):
    return random.randint(x, y)


def disp_text(surface, text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.midtop = (x, y)
    surface.blit(textSurf, textRect)


# Display the score
def draw_score(surface):
    global high_score
    font_name = pg.font.match_font('arial')
    if score > high_score:
        high_score = score
    # Draw the score
    font = pg.font.Font(font_name, 18)
    text_surface = font.render('Score: {} High Score: {}'.format(score, high_score), True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (200, 10)
    surface.blit(text_surface, text_rect)


# Display the Menu Screen
def main_menu(surface):
    global high_score
    # surface.fill(black)
    disp_text(surface, 'Snek', 64, white, 200, 10)
    disp_text(surface, 'A story of survival', 24, white, 200, 70)
    disp_text(surface, "Direct the snek around the screen using the arrow keys or 'W A S D'", 12, white, 200, 100)
    pg.display.flip()
    time.sleep(5)


# Game Over
def game_over():
    global score
    # display 'Game Over' on screen
    disp_text(wn, 'Game Over', 24, white, 200, 50)
    score = 0
    pg.display.flip()
    time.sleep(2)
    # reinitialize the snek and start a new game
    s.__init__()
    play_game(s)


# The Game
def play_game(s):
    fd = Food()
    fd.__init__()
    global score
    run = True
    while run:
        # Control the FPS
        clock.tick(15)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        # Draw food, snek, score
        wn.fill(black)
        fd.draw_food(wn)
        s.draw_player(wn)
        draw_score(wn)
        # Check for movement keys
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP] or pressed[pg.K_w]:
            s.change_direction(1)
        if pressed[pg.K_LEFT] or pressed[pg.K_a]:
            s.change_direction(3)
        if pressed[pg.K_DOWN] or pressed[pg.K_s]:
            s.change_direction(2)
        if pressed[pg.K_RIGHT] or pressed[pg.K_d]:
            s.change_direction(4)
        # let's make the snek move
        s.move()
        # if the snek eats something add to score and drop a random food item
        if fd.is_eaten(s.head):
            fd.power()
            score += fd.points
            fd = Food()
            fd.__init__()
            fd.new_pos()
            s.add_unit()
        # If the snek runs into itself or the borders
        if s.is_collision():
            run = False
            game_over()

        pg.display.update()


s = Snek()
main_menu(wn)
play_game(s)
