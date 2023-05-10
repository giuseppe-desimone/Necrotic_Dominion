"""v0.12"""

import interface
import pygame
import interactions.menu

pygame.init()
pygame.mixer.music.load('./media/soundtrack.ogg')
pygame.mixer.music.play(-1)


interactions.menu.new_play()
