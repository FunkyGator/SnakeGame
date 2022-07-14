import pygame as pg
import time
import random


# This class defines the snek and its methods
class Snek:
    # Initialization
    def __init__(self):
        self.x = screen_width / 2
        self.y = screen_height / 2
        self.width = 10
        self.height = 10
        self.velocity = 10          # How far to move the head when the snek moves
        self.direction = 0          # 0 = stopped, 1 = up, 2 = down, 3 = left, 4 = right
        self.body = []              # list to contain the segments of the body
        self.head_color = lt_green
        self.body_color = brown

    # Draws the snek
    def draw_snek(self, surface):
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
        global frogs_left
        # Did player collide with himself?
        for segment in self.seg:
            if self.head.colliderect(segment):
                if frogs_left > 0:
                    frogs_left -= 1
                    return False
                else:
                    return True

        # Did player collide with the boundaries?
        if self.y < 40 or self.y > (screen_height - border_width) - self.height or self.x < 10 or self.x > (screen_width - border_width) - self.height:
            return True

    # The body of the snek follows the head
    def move(self):
        for index in range(len(self.body)-1, 0, -1):
            x = self.body[index - 1][0]
            y = self.body[index - 1][1]
            self.body[index] = [x, y]
        if len(self.body) > 0:
            self.body[0] = [self.x, self.y]
        if self.direction == 1:         # move up
            self.y -= self.velocity
        if self.direction == 2:         # move down
            self.y += self.velocity
        if self.direction == 3:         # move left
            self.x -= self.velocity
        if self.direction == 4:         # move right
            self.x += self.velocity

    # changes the direction of the head
    def change_direction(self, direction):
        # make sure that the snek cannot turn back on itself
        if self.direction != 2 and direction == 1:
            self.direction = 1                      # sets direction to up
        if self.direction != 4 and direction == 3:
            self.direction = 3                      # sets direction to down
        if self.direction != 1 and direction == 2:
            self.direction = 2                      # sets direction to left
        if self.direction != 3 and direction == 4:
            self.direction = 4                      # sets direction to right


# Food class - chooses a random food each time an instance is created
class Food:
    def __new__(cls):
        other = random.choice([Apple, Chicken, Turtle, Frog, Mouse])
        instance = super().__new__(other)
        return instance


# This is the Apple class - worth 1 point - has no special ability
class Apple:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(10, (screen_width - border_width) - self.width)
        self.y = random.randrange(40, (screen_height- border_width) - self.height)
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
        return


# This is the Chicken class - worth 10 points - when eaten the snek will move faster
class Chicken:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(10, (screen_width - border_width) - self.width)
        self.y = random.randrange(40, (screen_height - border_width) - self.height)
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
        global clock_speed
        clock_speed = clock_speed * 1.5
        if clock_speed > 60:
            clock_speed = 60    # maximum speed it 60


# This is the Turtle class - worth 5 points - when eaten the snek will move slower
class Turtle:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(10, (screen_width - border_width) - self.width)
        self.y = random.randrange(40, (screen_height - border_width) - self.height)
        self.color = dk_green
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

    # activate the turtles power - slows down the speed of the snek
    @staticmethod
    def power():
        global clock_speed
        clock_speed = clock_speed / 2
        if clock_speed < 15:
            clock_speed = 15


# This is the Frog class - worth 5 points - when eaten the snek will be able to jump over itself one time
class Frog:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(10, (screen_width - border_width) - self.width)
        self.y = random.randrange(40, (screen_height - border_width) - self.height)
        self.color = lt_green
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
        global frogs_left
        if frogs_left < 5:
            frogs_left += 1


# This is the Mouse class - worth 10 points - when eaten the snek will move in a random direction
class Mouse:
    # Initialization
    def __init__(self):
        self.width = 10
        self.height = 10
        self.x = random.randrange(10, (screen_width - border_width) - self.width)
        self.y = random.randrange(40, (screen_height - border_width) - self.height)
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
        if s.direction == 1 or s.direction == 2:    # if snek is moving up or down will randomly move it left or right
            rnd = random.randint(3, 4)
        else:                                       # if snek is moving left or right will randomly move it up or down
            rnd = random.randint(1, 2)
        s.change_direction(rnd)
        s.move()


# Establish color variables
red = pg.Color(255, 0, 0)
lt_green = pg.Color(0, 255, 0)
dk_green = pg.Color(0, 100, 0)
black = pg.Color(0, 0, 0)
white = pg.Color(255, 255, 255)
brown = pg.Color(165, 42, 42)
gray = pg.Color(128, 128, 128)
yellow = pg.Color(255, 255, 0)

# Screen size variables
screen_width = 440
screen_height = 460
border_width = 10

# Initialize pygame
pg.init()

# Create the screen
wn = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Snek: A story of survival')


# initialize the score and high score variables
score, high_score = (0, 0)
frogs_left = 0
clock = pg.time.Clock()


# function to display text on the surface
def disp_text(surface, text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.midtop = (x, y)
    surface.blit(textSurf, textRect)


# draw the border around the screen
def draw_border(surface):
    pg.draw.rect(surface, white, (0, 0, screen_width, screen_height), border_width)
    pg.draw.rect(surface, white, (0, 0, screen_width, 40), 10)


# Display and update the score and high score
def draw_score(surface):
    global high_score
    global frogs_left
    font_name = pg.font.match_font('arial')
    if score > high_score:
        high_score = score
    # Draw the score
    font = pg.font.Font(font_name, 18)
    text_surface = font.render('Score: {} High Score: {}'.format(score, high_score), True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (100, 10)
    surface.blit(text_surface, text_rect)
    text2_surface = font.render('Frogs Remaining: {}'.format(frogs_left), True, white)
    text2_rect = text2_surface.get_rect()
    text2_rect.midtop = (350, 10)
    surface.blit(text2_surface, text2_rect)


# Function
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Function to draw a button and execute the function tied to it
def button(text, x, y, w, h, bc, hc, action=None):
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pg.draw.rect(wn, hc, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(wn, bc, (x, y, w, h))
    smallText = pg.font.SysFont("arial", 20)
    textSurf, textRect = text_objects(text, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    wn.blit(textSurf, textRect)


# Display the Menu Screen
def main_menu():
    mm = True
    print("TEST!")
    while mm:
        global high_score
        print("TEST2!")
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        disp_text(wn, 'Snek', 64, white, 200, 10)
        disp_text(wn, 'A story of survival', 24, white, 200, 70)
        disp_text(wn, "Direct the snek around the screen using the arrow keys or 'W A S D'", 16, yellow, 200, 110)
        disp_text(wn, 'Do not let the snek hit the boundries or itself', 16, yellow, 200, 130)
        disp_text(wn, 'Eat the food to earn points. But be aware, eating the food makes', 16, white, 200, 150)
        disp_text(wn, 'your snek grow', 16, white, 200, 170)
        disp_text(wn, 'Each food also causes an effect on you snek', 16, yellow, 200, 190)
        disp_text(wn, '= Apple - 1 point - No special effect', 16, red, 200, 210)
        disp_text(wn, '= Chicken - 10 points - Makes your snek move faster', 16, yellow, 200, 230)
        disp_text(wn, '= Turtle - 5 points - Makes your snek move slower', 16, dk_green, 200, 250)
        disp_text(wn, '= Frog - 5 points - Allows your snek to jump over itself', 16, lt_green, 200, 270)
        disp_text(wn, '= Mouse - 10 points - Your snek moves in a random direction', 16, gray, 200, 290)
        pg.draw.rect(wn, red, rect=(80, 215, 10, 10))
        pg.draw.rect(wn, yellow, rect=(30, 235, 10, 10))
        pg.draw.rect(wn, dk_green, rect=(40, 255, 10, 10))
        pg.draw.rect(wn, lt_green, rect=(30, 275, 10, 10))
        pg.draw.rect(wn, gray, rect=(10, 295, 10, 10))

        button("Start", 175, 330, 75, 30, dk_green, lt_green, play_game)

        pg.display.update()

        clock.tick(15)


# Game Over
def game_over():
    global score
    global frogs_left
    # display 'Game Over' on screen
    disp_text(wn, 'Game Over', 24, white, 200, 50)
    score = 0
    pg.display.flip()
    time.sleep(2)
    # reinitialize the snek, frogs left and start a new game
    s.__init__()
    frogs_left = 0
    play_game()


# The Game Loop
def play_game():
    global clock_speed
    # create a food and initialize it
    s.__init__()
    fd = Food()
    fd.__init__()
    global score
    run = True
    clock_speed = 15
    start = time.time()
    while run:
        # Control the FPS
        clock.tick(clock_speed)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        # Draw food, snek, score
        wn.fill(black)
        draw_border(wn)
        fd.draw_food(wn)
        s.draw_snek(wn)
        draw_score(wn)
        # Check for movement keys
        pressed = pg.key.get_pressed()
        if pressed[pg.K_UP] or pressed[pg.K_w]:
            s.change_direction(1)                   # up
        if pressed[pg.K_LEFT] or pressed[pg.K_a]:
            s.change_direction(3)                   # left
        if pressed[pg.K_DOWN] or pressed[pg.K_s]:
            s.change_direction(2)                   # down
        if pressed[pg.K_RIGHT] or pressed[pg.K_d]:
            s.change_direction(4)                   # right
        # let's make the snek move
        s.move()
        # if the snek eats something activate the power, add to score, and drop a random food item
        if fd.is_eaten(s.head):
            fd.power()
            score += fd.points
            fd = Food()
            fd.__init__()
            fd.new_pos()
            s.add_unit()
            start = time.time()
        # If the snek runs into itself or the borders
        if s.is_collision():
            run = False
            game_over()
        # if food is around for 10 seconds remove it and add a new food
        if time.time() - start > 5:
            fd = Food()
            fd.__init__()
            fd.new_pos()
            start = time.time()
        pg.display.update()


# initialize the snek, display the main menu, and start the game
s = Snek()
main_menu()
play_game()
pg.quit()
quit()
