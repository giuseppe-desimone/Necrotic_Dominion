"""v0.13"""

import pygame
import interactions.menu

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

pygame.init()
pygame.mixer.music.load('./media/soundtrack.ogg')
pygame.mixer.music.play(-1)


interactions.menu.new_play()
