import pygame
import json
import sys
pygame.init()
#import all files heres

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,0,255)
BLUE = (0,255,0)
GRAY = (255,0,255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.Font(None)
pygame.display.set_caption("POOKEMON FIGHT")
background1 = pygame.image.load("ASSETS/background1.png")
background2 = pygame.image.load("ASSETS/background2.png")

# CLASSES -------------------------------------------------------

class buttonMenu:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color 
        self.hover_color = hover_color #change buttoncolor when hover
        self.action = action
    
    ''''''''
    def draw(self, surface):

        # detect button
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
        else:
            pygame.draw.rect(surface, self.color, self.rect)

        #display text on center
        text_surface = font1.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    ''''''''
    def check_click(self): # and send to action
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):

            if pygame.mouse.get_pressed()[0] and self.action: 
            # defini mouse button who need o be cliked for action (here is right click = [0] )
                self.action()

# Button Actions
def add_user(): 
    input("USER NAME:  ")

def add_pokemon():
    input("Add pokemon to Pokedex: ")

def start_fight():
    screen.blit(background2, (0.0))
    print("A wild Pokemon appears !")

def save_game(self):
        print("Game saved succesfully !")

def quit_game():
    pygame.quit()
    sys.exit()

#create buttons objects
buttons = [
    buttonMenu("User Name", WIDTH // 2 - 100, HEIGHT // 2 - 200, 300, 80, BLUE, GRAY, add_user),
    buttonMenu("Add Pokemon", WIDTH // 2 - 100, HEIGHT // 2 - 150, 300, 80, BLUE, GRAY, add_pokemon),
    buttonMenu("START FIGHT", WIDTH // 2 - 100, HEIGHT // 2 - 100, 300, 80, BLUE, GRAY, start_fight),
    buttonMenu("SAVE GAME", WIDTH // 2 - 100, HEIGHT // 2 - 50, 300, 80, BLUE, GRAY, save_game),
    buttonMenu("QUIT GAME", WIDTH // 2 - 100, HEIGHT // 2 - 0, 300, 80, BLUE, GRAY, quit_game),
]

# ----------------------------------------------------------------------------------------------------

#Variables for mainloop
running = True

# main Loop
while running:
    screen.blit(background1, (0,0)) # 

    ''''''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # if event.type == buttonMenu.check_click() and self.action:
        #     pass
    
    '''''''''''''' # check buttons
    for button in buttons:
        button.draw(screen)
        if pygame.mouse.get_pressed()[0]:  # check clics
            button.check_click()
        
        
    
    pygame.display.flip()

pygame.quit()