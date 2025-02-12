import pygame
import json
import sys

pygame.init()

# Constantes
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GRAY = (255, 0, 255)

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("POOKEMON FIGHT")

# Chargement des ressources
background1 = pygame.image.load("ASSETS/background1.png")
screen.blit(background1, (0,0))
background2 = pygame.image.load("ASSETS/background1.png")
screen.blit(background2, (0,0))


# Police
font = pygame.font.Font(None, 36)

# Données globales
player_data = {
    "user_name": "",
    "pokedex": []
}
pokedex_list = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Jigglypuff", "Meowth", "Psyduck", "Snorlax", "Eevee", "Machop", "Geodude", "Magikarp", "Gengar", "Onix", "Zapdos", "Mewtwo", "Arcanine", "Dragonite"]

# Classe pour les boutons
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.action = action

    def draw(self, surface):
        # Détection du survol
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, current_color, self.rect)

        # Affichage du texte
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def check_click(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.action:
                self.action()

# Fonctions des boutons
def add_user():
    global player_data
    player_name = input("Entrez le nom du joueur : ")
    player_data["user_name"] = player_name
    print(f"Bienvenue, {player_name}!")

def add_pokemon():
    global player_data
    print("Voici le Pokédex :")
    for i, pokemon in enumerate(pokedex_list, 1):
        print(f"{i}. {pokemon}")
    choice = int(input("Choisissez un Pokémon par son numéro : ")) - 1
    if 0 <= choice < len(pokedex_list):
        chosen_pokemon = pokedex_list[choice]
        if chosen_pokemon not in player_data["pokedex"]:
            player_data["pokedex"].append(chosen_pokemon)
            print(f"{chosen_pokemon} a été ajouté à votre Pokédex!")
        else:
            print(f"{chosen_pokemon} est déjà dans votre Pokédex.")
    else:
        print("Choix invalide.")

def start_fight():
    print("Un Pokémon sauvage apparaît!")
    screen.blit(background2, (0, 0))
    pygame.display.flip()

def save_game():
    global player_data
    with open("savegame.json", "w") as save_file:
        json.dump(player_data, save_file)
    print("Sauvegarde réussie!")

def quit_game():
    pygame.quit()
    sys.exit()

def show_pokedex():
    print("Votre Pokédex :")
    for pokemon in player_data["pokedex"]:
        print(f"- {pokemon}")

# Création des boutons
buttons = [
    Button("Nom du Joueur", WIDTH // 2 - 150, 100, 300, 50, BLUE, GRAY, add_user),
    Button("Ajouter un Pokémon", WIDTH // 2 - 150, 160, 300, 50, BLUE, GRAY, add_pokemon),
    Button("Pokédex", WIDTH // 2 - 150, 220, 300, 50, BLUE, GRAY, show_pokedex),
    Button("Commencer Combat", WIDTH // 2 - 150, 280, 300, 50, BLUE, GRAY, start_fight),
    Button("Sauvegarder", WIDTH // 2 - 150, 340, 300, 50, BLUE, GRAY, save_game),
    Button("Quitter", WIDTH // 2 - 150, 400, 300, 50, BLUE, GRAY, quit_game)
]

# Boucle principale
running = True
while running:
    screen.blit(background1, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Affichage des boutons et gestion des clics
    for button in buttons:
        button.draw(screen)
        button.check_click()

    pygame.display.flip()

pygame.quit()
