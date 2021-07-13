import pygame
import pytmx
import pyscroll
from player import Player

class Game:

    def __init__(self):
        #creer la fenetre du jeu
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon - Aventure")

        #charger la carte
        tmx_data = pytmx.util_pygame.load_pygame("carte.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        #generer un joueur
        player_position = tmx_data.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        #definir une liste qui va stocker les rectangles de collisons
        self.walls =[]

        for object in tmx_data.objects:
            if object.type == "collision":
                self.walls.append(pygame.Rect(object.x, object.y, object.width, object.height))


        #dessiner le groupe de calque, le calque le plus en amont est la calque 3
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer = 3)
        self.group.add(self.player)

    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")

    def update(self):
        self.group.update()

        #verification collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
            
                sprite.move_back()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            #centre sur le joueur
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        #met 60 images par secondes (nombre de FPS par seconde)
            clock.tick(60)

        pygame.quit()