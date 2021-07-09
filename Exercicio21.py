import pygame

pygame.mixer.init()

pygame.mixer.music.load('yamete.wav')

pygame.mixer.music.play()

parar = input('Digite para parar: ')