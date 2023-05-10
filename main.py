"""v0.12"""

import interface
import pygame

pygame.init()
pygame.mixer.music.load('./media/soundtrack.ogg')
pygame.mixer.music.play(-1)


interface.new_play()
