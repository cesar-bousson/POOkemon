import pygame
import random

#import de tous les fichiers a faire 

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
GREEN = (0,0,255)
FONT = 0# trouver la police du jeu pokemon de base

# ------------------
    #main loop :

class Game: 
    def __init__(self):       
        self.running = True 
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def gameplay(self):
        while self.running:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False






            pygame.display.update()
            

        pygame.quit()

# -------------------------------------------


class Fight:
    def __init__(self, lvl_attack, life, lvl_defense):
        self.lvl_attck = lvl_attack
        self.life = life
        self.lvl_defense = lvl_defense
        self.pokedex = {} # creer la liste

    def pokemon_enemy(self):
        ''' La methode choisit un pokemon random dans la liste general des pokemons pour l'adversaire.'''
        pass

    def choose_pokemon(self):
        '''Une fois le pokemon adversaire choisit par le systeme, nous pouvons choisir parmis les 
        3 pokemons disponible dans le pokedex.'''
        pass

    def victory(self): 
        '''si le joueur atteind la fin de vie (nombre de point) 
        adverse par son nombre d'attaque, le joueur gagne. La fonction retourne le 
        joueur gagnant et renvoie au menu.'''
        pass

    def defeat(self):
        ''' Si un joueur est attaqué autant de fois qu'il à de points de vie, 
        le joueur perd avec message de defaite. Le pokemon est enlevé du pokedex
          et la fonction renvois au menu '''
        pass

    def choose_attack(self):
        ''' Le Joueur actuel peut choisir parmis 3 attaques, '''

    def attack(self):
        ''' Le joueur actuel attaque le pokemon adverse. (#turnover)
        SI l'attaque passe (random) il lui inflige 1 point.
        SI elle ne passe pas, message de loupé et passage au tour du joueur suivant.
        La fonction retourne les degats et/ou les points de vie (barre de vie).
        Le premier joueur qui atteind le nombre max de point de vie du joueur adverse lorsqu'il attaque
        a gagner.
        '''
        pass

    def defense(self):
        '''De maniere aleatoire, le pokemon peut se proteger avec une probabilité 30%
        (ou à definir en fonction du pokemon).
        Le message de defense s'affiche, et c'est au joueur suivant de jouer.'''
        pass

# ----------------------------------

class Turnover: # changement du joueur
    def __init__(self, turn = "joueur"):
        self.turn = turn

    def change_player(self, player):
        ''' La fonction definit le joueur actuel. 
        Si le joueur actuel à realisé son attaque, c'est au tour du joueur suivant.
        Sinon le joueur actuel peut attaquer. '''
        self.player = player 

# -----------------------------------

class Pokedex:
    def __init__(self):
        pass
    
    def all_pokemons(self):
        ''' definit une liste de tous les pokemons du jeu'''

    def pokemon_activ(self):
        'definit une liste des pokemons disponibles dans le pokedex '
    
    def catch_pokemon(self):
        ''' definit une liste des pokemons battu lors du combat et donc attrapé dans le pokedex.
        Il y en a 3/6 par default dans le pokedex. 
        Une fois que le pokedex est plein le jeu est terminé. Donc si le nombre de pokemon attrapé est egal à 6, 
        le jeu peu se terminer ou recommencer.'''
    
    def choose_pokemon(self):
        '''La methode permet de chosir son pokemon dans le pokedex pour l'envoyer au combat.'''

# -----------------------------------

class Pokemon:
    def __init__(self, name, level, life):
        pass 

    def type(self, type, name_evolution):
        ''' Definit le type du pokemon parmis les 18 disponible dans la liste.'''
        pass

    def powers(self, atk_power, df_power):
        '''La fonction définit la puissance d'attaque et de defense du pokemon en fonction de leur type.
         exemple: Si type eau: attaque 8/10 / defense 5/10. 
         Si attaque 10, probabilité de loupé des attaques de 80%. Si defense 5, probabilité ennemi d'attaque de 50% (1/2).'''



    def info_pokemon(self):
        '''La methode retourne les infos du pokemon a savoir nom, type, level, puissance d'attaque, puissance de defense'''
        pass


# ----------------------------------

class displayPlayer:
    def __init__(self, name, type, level): 
        #type = ennemi ou joueur ? 
        # (bonus) le joueur peut acquerir des points de niveau (level), au fur et a mesure des victoires
        pass

    def draw_poke_ennemy(self):
        ''' affiche le pokemon adverse en debut de combat. 
        L'enemi execute un mouvement lorsqu'il attaque.
        Son attaque est visible sur le pokemon du joueur.'''
        pass
    
    def draw_poke_user(self):
        ''' Apres avoir choisit son pokemon dans le pokedex, la methode affiche le pokemon au bon endroit 
        sur le background de combat. '''
        pass


# -------------------------------------------------------
class button:
    ''' cette classe permet de gerer tous les boutons ''' 
    pass

class Menu:
    def __init__(self,): 
        pass

    def draw_menu(self):
        ''' La methode affiche le menu du jeu avec 
        3 boutons cliquables / 1 saisie user
        (nom de joueur personnel, sauvegarde, recommencer la partie , quitter le jeu.)'''

    def save(self):
        '''la methode permet la sauvegarde du jeu lorsqu'on clique sur son bouton affiché dans le menu'''
    
    def user_name(self):
        ''' La methode permet d'ecrire le nom de l'utilisateur et lui assigner la partie en cours. 
        La sauvegarde sera donc à son nom.'''
    
    def load_game(self): 
        ''' la methode permet de charger une nouvelle partie en partant de 0 lorsque le bouton est cliqué'''

    def quit_game(self):
        '''la methode permet de quitter le jeu lorsque le bouton est cliqué. 
        La fenetre du jeu se ferme.'''


# --------------------------

class Random:
    def __init__(self):
        pass

    def ennemy_random(self):
        ''' La methode permet de definir le choix random des pokemon ennemis dans la liste general pour le combat.'''

    def random_defense(self):
        ''' La methode permet de definir la defense aleatoire des pokemons (adverse et joueur) pendant le combat,
         en fonction des pouvoir de defense et d'attaque du pokemon visé. '''
    