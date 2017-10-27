from game_object import *

foodimg = pygame.image.load("food.png")

class Food(game_object):

    def __init__(self):
        game_object.__init__(self, foodimg)