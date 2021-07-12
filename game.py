import pygame
import pytmx
import pyscroll

class Game:

    def __init__(self):
        #creer la fenetre du jeu
        pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Aventure")


    def run(self):

        # boucle du jeu
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()