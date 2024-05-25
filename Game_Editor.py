# S.Velmurugan 31/05/2023
import os
import pygame
from pygame.locals import *
import pickle
from pprint import pprint

if not os.path.exists('levels/'):
        os.mkdir('levels/')


# WINDOW SIZE & TILE SIZE
SIZE = WIDTH , HEIGHT= 1000, 650
tile_size = 50

# Constant Variables
pygame.init()
clock = pygame.time.Clock()
## FPS = 30

cols = WIDTH // tile_size
rows = HEIGHT // tile_size
margin = 210

win_width = WIDTH + margin
win_height = HEIGHT

avengers_icon = pygame.image.load('avengers-icon.png')
pygame.display.set_icon(avengers_icon)
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption('Game Editor')

#load button sound
click_sound = pygame.mixer.Sound('Sounds/Click.ogg')

# load backgrounds
avenegers_logo = pygame.image.load('Logo/Avengers Logo.png')
bg_img = pygame.image.load('Background Screen/BG1.png')
bg_img = pygame.transform.scale(bg_img, (win_width - margin, HEIGHT))

# load buttons
load_img = pygame.image.load('Buttons & Coins/load_btn.png')## 268
save_img = pygame.image.load('Buttons & Coins/save_btn.png')
left_img = pygame.image.load('Buttons & Coins/left.png')
right_img = pygame.image.load('Buttons & Coins/right.png')

# load tiles
tiles = []
for t in sorted(os.listdir('Blocks/'), key=lambda s: int(s[:-4])):
        tile = pygame.image.load('Blocks/' + t)
        tiles.append(tile)


#define game variables
clicked = False
current_level = 1

#define colours
WHITE = (255, 255, 255)#303,73
PINK = (197, 112, 196)#326
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

# Load Font
font = pygame.font.SysFont('Arial Bold', 25)

# Empty world data
world_data = []
for r in range(rows):
        c = [0] * cols
        world_data.append(c)

def text(text_, font, color, pos):
        text = font.render(text_, True, color)
        win.blit(text, pos)

def lines():
        for row in range(rows+1):
                pygame.draw.line(win, WHITE, (0, tile_size*row), (WIDTH, tile_size*row), 2)
        for col in range(cols):
                pygame.draw.line(win, WHITE, (tile_size*col, 0), (tile_size*col, HEIGHT), 2)

def world():
        for row in range(rows):
                for col in range(cols):
                        index = world_data[row][col]
                        if index > 0:
                                if index in range(1,16) or index in (16,17):
                                        #Platform block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 18:
                                        #lava block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, int(tile_size * 0.50)))
                                        win.blit(img, (col * tile_size, row * tile_size + tile_size // 2))
                                if index == 19:
                                        #Lava till block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 20:
                                        #Water block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, int(tile_size * 0.50)))
                                        win.blit(img, (col * tile_size, row * tile_size + tile_size // 2))
                                if index == 21:
                                        #Water tile block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 22:
                                        #Diamond block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 23:
                                        #Crate block
                                        img = pygame.transform.scale(tiles[index-1], (tile_size, tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 24:
                                        #tree block
                                        img = pygame.transform.scale(tiles[index-1], (3*tile_size, 3 * tile_size))
                                        win.blit(img, ((col-1) * tile_size + 10, (row-2) * tile_size + 5))
                                if index == 27:
                                        #Flying Mysterio block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 25:
                                        #Gate block
                                        img = tiles[index-1]
                                        win.blit(img, (col * tile_size - tile_size//4, row * tile_size - tile_size//4))
                                if index == 26:
                                        #Bridge block
                                        img = pygame.transform.scale(tiles[index-1], (5*tile_size + 20, tile_size))
                                        win.blit(img, ((col-2) * tile_size + 10, row * tile_size + tile_size // 4))
                                if index == 28:
                                        #Walking Loki block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size+10))
                                if index == 29:
                                        #Walking Ultron block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 30:
                                        #Flying Ultron block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 31:
                                        #Walking Thanos block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 32:
                                        #Walking Venom block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 33:
                                        #Walking Octopus block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 34:
                                        #Flying Loki blocks
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 35:
                                        #Flying Thanos blocks
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 36:
                                        #Flying Magneto block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 37:
                                        #Flying Osborn_Green_Goblin block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 38:
                                        #Walking Dr.Doom block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 39:
                                        #Flying Dr.Doom block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 40:
                                        #Walking Galactus block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 41:
                                        #Flying Galactus block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))
                                if index == 42:
                                        #Walking Red Skull block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 43:
                                        #Walking Modok block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size - 10, row * tile_size))
                                if index == 44:
                                        #Flying Modok block
                                        img = pygame.transform.scale(tiles[index-1], (int(1.2*tile_size), 2*tile_size))
                                        win.blit(img, (col * tile_size, row * tile_size))

class Button:
        def __init__(self, pos, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.topleft = pos
                self.clicked = False

        def draw(self):
                action = False

                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                action = True
                                self.clicked = True

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                win.blit(self.image, self.rect)

                return action

class Tile():
        def __init__(self, pos, image, index):
                image = pygame.transform.scale(image, (40,40))
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.topleft = pos
                self.clicked = False
                self.index = index

        def update(self):
                action = False

                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                                action = self.index
                                self.clicked = True

                if pygame.mouse.get_pressed()[0] == 0:
                        self.clicked = False

                win.blit(self.image, self.rect)

                return action

tile_group = []
for index, tile in enumerate(tiles):
        row = index // (margin // (40 + 5) )
        column = index %  (margin // (40 + 5) )
        pos = (WIDTH + 5 +(column * tile_size) + 5, 5 + row * tile_size + 5)
        t = Tile(pos, tile, index+1)
        tile_group.append(t)

## create load, save, left and right buttons
load_button = Button((WIDTH + 10, HEIGHT - 80), load_img)
save_button = Button((WIDTH + 110, HEIGHT - 80), save_img)
left_button = Button((WIDTH + 30, HEIGHT - 35), left_img)
right_button = Button((WIDTH + 140, HEIGHT - 35), right_img)

initial_r = pygame.Rect(1*tile_size,1*tile_size,tile_size, tile_size)
rect = [initial_r, [1,1]]

running = True
while running:
        for event in pygame.event.get():
                if event.type == QUIT:
                        running = False

                if event.type == MOUSEBUTTONDOWN and clicked == False:
                        clicked = True
                        pos = pygame.mouse.get_pos()
                        if pos[0] <= WIDTH:
                                x = pos[0] // tile_size
                                y = pos[1] // tile_size
                                if pygame.mouse.get_pressed()[0]:
                                        r = rect[1]
                                        if r == [x,y]:
                                                world_data[y][x] += 1
                                                if world_data[y][x] >= len(tiles) + 1:
                                                        world_data[y][x] = 0
                                        else:
                                                r1 = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                                                r2 = [x,y]
                                                rect = [r1, r2]
                                elif pygame.mouse.get_pressed()[2]:
                                        r = rect[1]
                                        if r == [x,y]:
                                                world_data[y][x] -= 1
                                                if world_data[y][x] < 0:
                                                        world_data[y][x] = len(tiles)
                                        else:
                                                r1 = pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size)
                                                r2 = [x,y]
                                                rect = [r1, r2]


                if event.type == KEYDOWN:
                        pos = rect[1]
                        if event.key == K_LEFT:
                                if pos[0] > 0:
                                        pos[0] -= 1
                        elif event.key == K_RIGHT:
                                if pos[0] < cols-1:
                                        pos[0] += 1
                        elif event.key == K_UP:
                                if pos[1] > 0:
                                        pos[1] -= 1
                        elif event.key == K_DOWN:
                                if pos[1] < rows-1:
                                        pos[1] += 1

                        rect[0] = pygame.Rect(pos[0]*tile_size, pos[1]*tile_size, tile_size, tile_size)
                        rect[1] = pos

                if event.type == pygame.MOUSEBUTTONUP:
                        clicked = False

        win.fill(KIMBERLY)
        win.blit(bg_img, (0,0))
        win.blit(avenegers_logo, (80,60))
        lines()
        world()
        pygame.draw.rect(win, (255,0,0), rect[0], 3)

        for tile in tile_group:
                index = tile.update()
                if index:
                        current_tile = index
                        r = rect[1]
                        world_data[r[1]][r[0]] = index

        if save_button.draw():
                click_sound.play()
                #save level data
                pickle_out = open(f'Levels/Level{current_level}_data', 'wb')
                pickle.dump(world_data, pickle_out)
                pickle_out.close()
        if load_button.draw():
                click_sound.play()
                #load in level data
                if os.path.exists(f'Levels/Level{current_level}_data'):
                        pickle_in = open(f'Levels/Level{current_level}_data', 'rb')
                        world_data = pickle.load(pickle_in)

        if left_button.draw():
                click_sound.play()
                current_level -= 1
                if current_level < 1:
                        current_level = 1
        if right_button.draw():
                click_sound.play()
                current_level += 1

        # Current level text
        text(f'Level: {current_level}', font, WHITE, (WIDTH + 70, win_height - 25))

        pygame.display.flip()

pygame.quit()
