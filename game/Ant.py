from game_object import *

antimg = pygame.image.load("ant.png")

class Ant(game_object):

    def __init__(self):
        game_object.__init__(self, antimg)
