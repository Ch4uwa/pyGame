import pygame
import os
from .enemy import Enemy


class Goblin(Enemy):
    imgs_l = [pygame.image.load(os.path.join("game_assets/enemy", "L" + str(x) + "E.png")) for x in range(1, 12)]
    imgs_r = [pygame.image.load(os.path.join("game_assets/enemy", "R" + str(i) + "E.png")) for i in range(1, 12)]
