# S.Velmurugan 31/05/2023
import os
import pygame
import time
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (197, 112, 196)
WHITE = '#ffffff'
BAY_OF_MANY = '#25277a'
SLIVER = '#bcbcbc'
CARIBBEAN_GREEN = '#03bd85'
BITTERSWEET = '#fa7a5b'
KIMBERLY = '#7174a5'
TORCH_RED = '#fb0246'
SCINCE_BLUE = '#0251d6'
TURQUOISE = '#52e0c0'
CAMELOT = '#92364e'


j = 0
SIZE = WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode(SIZE, pygame.NOFRAME)

pygame.init()

pygame.mixer.music.load('Sounds/Marvel Theme Song.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.8)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    Bg = pygame.image.load(f'Progress Bar/ProgressBar.png')
    win.blit(Bg, (0,0))

    Pro = pygame.image.load(f'Progress Bar/Programmer3.png')
    win.blit(Pro, (10, 10))

    font = pygame.font.SysFont('Broadway', 30)
    LoadTxt0 = font.render('Loading', True, TORCH_RED)
    LoadTxt1 = font.render('Loading.', True, TORCH_RED)
    LoadTxt2 = font.render('Loading..', True, TORCH_RED)
    LoadTxt3 = font.render('Loading...', True, TORCH_RED)
    Loading=[LoadTxt0, LoadTxt1, LoadTxt2, LoadTxt3]
    
    font = pygame.font.SysFont('Times', 27)
    Desc = font.render('S.Velmurugan  B.Sc.CS  Presents  AVENGERS  ASSEMBLE', True, WHITE)
    win.blit(Desc, (7, 460))

    for i in range(36):
        win.blit(Loading[j], (280, 270))
        pygame.display.update()
        if j<=2:
            j+=1
        elif j==3:
            j=0

        if i==35:
            import Game
            running = False
        time.sleep(1)
pygame.quit()
