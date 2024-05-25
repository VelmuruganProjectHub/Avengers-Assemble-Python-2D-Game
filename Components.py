# S.Velmurugan 31/05/2023
import os
import pickle
import random
import pygame
from pygame import mixer
from pygame.locals import *

SIZE = WIDTH , HEIGHT= 1000, 650
tile_size = 50

pygame.font.init()
score_font = pygame.font.SysFont('Broadway', 30)

WHITE = (255,255,255) ##Score Color


# load sounds
mixer.init()

diamond_fx = pygame.mixer.Sound('Sounds/Coin.wav')
diamond_fx.set_volume(0.5)
jump = pygame.mixer.Sound('Sounds/jump.wav')
dead = pygame.mixer.Sound('Sounds/gameover.mp3')
sounds = [diamond_fx, ]

dead_img = pygame.image.load('Game Over & Won Screen/Thanos.png')#370
game_over_1 = pygame.image.load('Game Over & Won Screen/GameOver1.png')
game_over_2 = pygame.image.load('Game Over & Won Screen/GameOver2.png')
GameOver = [game_over_1, game_over_2]
game_over_img = pygame.transform.scale(GameOver[0], (1000, 650))#374
game_over_rect = game_over_img.get_rect(topleft=(0,0))


# creates background
class World:
        b = 1
        def theme(self, t):
                j = "jungle"
                c = "castle"
                v = "volcano"
                m = "draftmine"
                d = "desert"
                vi = "village"
                dg = "dungeon"
                w = "winter"
                
                if j == t:
                        World.b=1
                elif c == t:
                        World.b=2
                elif v == t:
                        World.b=3
                elif m == t:
                        World.b=4
                elif d == t:
                        World.b=5
                elif vi == t:
                        World.b=6
                elif dg == t:
                        World.b=7
                elif w == t:
                        World.b=8
                        
        def __init__(self, win, data, groups):
                self.tile_list  = []
                self.win = win
                self.groups = groups

                tiles = []
                b=World.b
                for t in sorted(os.listdir(f'Block{b}/'), key=lambda s: int(s[:-4])):
                        tile = pygame.image.load(f'Block{b}/' + t)
                        tiles.append(tile)

                row_count = 0
                for row in data:
                        col_count = 0
                        for col in row:
                                if col > 0:
                                        if col in range(1,16) or col == 23:
                                                # direct blocks
                                                img = pygame.transform.scale(tiles[col-1], (tile_size, tile_size))
                                                rect = img.get_rect()
                                                rect.x = col_count * tile_size
                                                rect.y = row_count * tile_size
                                                tile = (img, rect)
                                                self.tile_list.append(tile)
                                        if col == 16:
                                                #Side moving platform
                                                platform = MovingPlatform('side', col_count * tile_size, row_count * tile_size)
                                                self.groups[6].add(platform)
                                        if col == 17:
                                                #top moving platform
                                                platform = MovingPlatform('up', col_count * tile_size, row_count * tile_size)
                                                self.groups[6].add(platform)
                                        if col == 18:
                                                # lava
                                                lava = Fluid('lava_flow', col_count * tile_size, row_count * tile_size + tile_size // 2)
                                                self.groups[1].add(lava)
                                        if col == 19:
                                                #lava tile block
                                                lava = Fluid('lava_still', col_count * tile_size, row_count * tile_size)
                                                self.groups[1].add(lava)
                                        if col == 20:
                                                # water block
                                                water = Fluid('water_flow', col_count * tile_size, row_count * tile_size + tile_size // 2)
                                                self.groups[1].add(water)
                                        if col == 21:
                                                # water tile block
                                                water = Fluid('water_still', col_count * tile_size, row_count * tile_size)
                                                self.groups[1].add(water)
                                        if col == 22:
                                                # diamond
                                                diamond = Diamond(col_count * tile_size, row_count * tile_size)
                                                self.groups[3].add(diamond)
                                        if col == 24:
                                                # tree
                                                tree = Forest('tree', (col_count-1) * tile_size + 10, (row_count-2) * tile_size + 5)
                                                self.groups[2].add(tree)
                                        if col == 27:
                                                # Flying Mysterio
                                                fms = Flying_Enemies('Flying_Mysterio', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(fms)
                                        if col == 25:
                                                #Gate blocks
                                                gate = ExitGate(col_count * tile_size - tile_size//4, row_count * tile_size - tile_size//4)
                                                self.groups[5].add(gate)
                                        if col == 26:
                                                # bridge
                                                bridge = Bridge((col_count-2) * tile_size + 10, row_count * tile_size + tile_size // 4)
                                                self.groups[7].add(bridge)
                                        if col == 28:
                                                #Walking Loki
                                                wl = Walking_Enemies('Walking_Loki', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(wl)
                                        if col == 29:
                                                #Walking Ultron
                                                wu1 = Walking_Enemies('Walking_Ultron', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(wu1)
                                        if col == 30:
                                                #Flying Ultron
                                                wu2 = Flying_Enemies('Flying_Ultron', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(wu2)
                                        if col == 31:
                                                #Walking Thanos
                                                wt = Walking_Enemies('Walking_Thanos', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(wt)
                                        if col == 32:
                                                #Walking Venom
                                                wv = Walking_Enemies('Walking_Venom', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(wv)
                                        if col == 33:
                                                #Walking Octopus
                                                wo = Walking_Enemies('Walking_Octopus', col_count * tile_size - 10, row_count * tile_size)
                                                self.groups[4].add(wo)
                                        if col == 34:
                                                # Flying Loki
                                                fl = Flying_Enemies('Flying_Loki', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(fl)
                                        if col == 35:
                                                # Flying Thanos
                                                ft = Flying_Enemies('Flying_Thanos', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(ft)
                                        if col == 36:
                                                # Flying Magneto
                                                fm = Flying_Enemies('Flying_Magneto', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(fm)
                                        if col == 37:
                                                # Flying Osborn_Green_Goblin
                                                fg = Flying_Enemies('Flying_Osborn', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(fg)
                                        if col == 38:
                                                # Walking Dr.Doom
                                                wdd = Walking_Enemies('Walking_Dr_Doom', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(wdd)
                                        if col == 39:
                                                # Flying Dr.Doom
                                                fdd = Flying_Enemies('Flying_Dr_Doom', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(fdd)
                                        if col == 40:
                                                # Walking Galactus
                                                wgs = Walking_Enemies('Walking_Galactus', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(wgs)
                                        if col == 41:
                                                # Flying Galactus
                                                fgs = Flying_Enemies('Flying_Galactus', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(fgs)
                                        if col == 42:
                                                # Walking Red_Skull
                                                wrs = Walking_Enemies('Walking_Red_Skull', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(wrs)
                                        if col == 43:
                                                # Walking Modok
                                                wm = Walking_Enemies('Walking_Modok', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(wm)
                                        if col == 44:
                                                # Flying Modok
                                                fm = Flying_Enemies('Flying_Modok', col_count * tile_size, row_count * tile_size)
                                                self.groups[4].add(fm)


                                col_count += 1
                        row_count += 1

                        diamond = Diamond(WIDTH+10,HEIGHT+10)
                        self.groups[5].add(diamond)

        def draw(self):
                for tile in self.tile_list:
                        self.win.blit(tile[0], tile[1])

# Player
class Player:
        MODE = -20
        def __init__(self, win, pos, world, groups, hero):
                self.reset(win, pos, world, groups, hero)

        def mode(self, m):
                e = "easymode"
                n = "normalmode"
                h = "hardmode"
                if e == m:
                        Player.MODE = -21
                if n == m:
                        Player.MODE = -20
                if h == m:
                        Player.MODE = -19

        def update(self, pressed_keys, game_over, level_won, game_won):
                dx = 0
                dy = 0
                walk_cooldown = 3
                col_threshold = 20



                if not game_over and not game_won:
                        
                        if pressed_keys[K_UP] and not self.jumped and not self.in_air:
                                self.vel_y = Player.MODE
                                jump.play()
                                self.jumped = True
                        if pressed_keys[K_UP] == False:
                                self.jumped = False
                        if pressed_keys[K_LEFT]:
                                dx -= 5
                                self.counter += 1
                                self.direction = -1
                        if pressed_keys[K_RIGHT]:
                                dx += 5
                                self.counter += 1
                                self.direction = 1

                        if pressed_keys[K_LEFT] and pressed_keys[K_RIGHT] == False:
                                self.counter = 0
                                self.index = 0
                                self.image = self.img_right[self.index]

                                # Flip the image on right & left direction
                                if self.direction == 1:
                                        self.image = self.img_right[self.index]
                                elif self.direction == -1:
                                        self.image = self.img_left[self.index]

                        if self.counter > walk_cooldown:
                                self.counter = 0
                                self.index += 1
                                if self.index >= len(self.img_right):
                                        self.index = 0

                                if self.direction == 1:
                                        self.image = self.img_right[self.index]
                                elif self.direction == -1:
                                        self.image = self.img_left[self.index]


                        # add gravity
                        self.vel_y += 1
                        if self.vel_y > 10:
                                self.vel_y = 10
                        dy += self.vel_y

                        # check for collision
                        self.in_air = True
                        for tile in self.world.tile_list:
                                # check for collision in x direction
                                if tile[1].colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                                        dx = 0
                                        
                                # check for collision in y direction
                                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        # check if below the ground
                                        if self.vel_y < 0:
                                                dy = tile[1].bottom - self.rect.top
                                                self.vel_y = 0
                                        elif self.vel_y >= 0:
                                                dy = tile[1].top - self.rect.bottom
                                                self.vel_y = 0
                                                self.in_air = False

                        if pygame.sprite.spritecollide(self, self.groups[0], False):#Water
                                game_over  = True
                        if pygame.sprite.spritecollide(self, self.groups[1], False):#Lava
                                game_over  = True
                        if pygame.sprite.spritecollide(self, self.groups[4], False):#Enemies
                                game_over = True

                        for gate in self.groups[5]:
                                if gate.rect.colliderect(self.rect.x - tile_size//2, self.rect.y, self.width, self.height):
                                        level_won = True

                        if game_over:
                                dead.play()
                                

                        # check for collision with moving platform
                        for platform in self.groups[6]:
                                # collision in x direction
                                if platform.rect.colliderect(self.rect.x+dx, self.rect.y, self.width, self.height):
                                        dx = 0

                                # collision in y direction
                                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        # check if below platform
                                        if abs((self.rect.top + dy) - platform.rect.bottom) < col_threshold:
                                                self.vel_y = 0
                                                dy = (platform.rect.bottom - self.rect.top)

                                        # check if above platform
                                        elif abs((self.rect.bottom + dy) - platform.rect.top) < col_threshold:
                                                self.rect.bottom = platform.rect.top - 1
                                                self.in_air = False
                                                dy = 0
                                        # move sideways with the platform
                                        if platform.move_x:
                                                self.rect.x += platform.move_direction

                        for bridge in self.groups[7]:
                                # collision in x direction
                                if ( bridge.rect.colliderect(self.rect.x+dx, self.rect.y, self.width, self.height) and 
                                                        ( bridge.rect.bottom < self.rect.bottom + 5)):
                                        dx = 0

                                # collision in y direction
                                if bridge.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                                        if abs((self.rect.top + dy) - bridge.rect.bottom) < col_threshold:
                                                self.vel_y = 0
                                                dy = (bridge.rect.bottom - self.rect.top)

                                        # check if above platform
                                        elif abs((self.rect.bottom + dy) - bridge.rect.bottom) < 8:
                                                self.rect.bottom = bridge.rect.bottom - 12
                                                self.in_air = False
                                                dy = 0


                        # updating player position
                        self.rect.x += dx
                        self.rect.y += dy
                        # if self.rect.x == self.width:
                        #       self.rect.x = self.width
                        if self.rect.x >= WIDTH - self.width:
                                self.rect.x = WIDTH - self.width
                        if self.rect.x <= 0:
                                self.rect.x = 0


                elif game_over:
                        self.image = dead_img
                        if self.rect.top > 0:
                                self.rect.y -= 5

                        self.win.blit(game_over_img, game_over_rect)
                                
                # displaying player on window
                self.win.blit(self.image, self.rect)
        
                return game_over, level_won

        def reset(self, win, pos, world, groups, hero):
                x, y  = pos
                self.win = win
                self.world = world
                self.groups = groups

                self.img_right = []
                self.img_left = []
                self.index = 0
                self.counter = 0

                img = pygame.image.load(f'Players/hero{hero}.png')
                img_right = pygame.transform.scale(img, (50,100))
                img_left = pygame.transform.flip(img_right, True, False)
                self.img_right.append(img_right)
                self.img_left.append(img_left)
                
                self.image = self.img_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.direction = 1
                self.vel_y = 0
                self.jumping = False
                self.in_air = True

## Button
class Button(pygame.sprite.Sprite):
        def __init__(self, img, scale, x, y):
                super(Button, self).__init__()

                self.image = pygame.transform.scale(img, scale)
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

                self.clicked = False

        def draw(self, win):
                action = False
                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                        if pygame.mouse.get_pressed()[0] and not self.clicked:
                                action = True
                                self.clicked = True

                        if not pygame.mouse.get_pressed()[0]:
                                self.clicked = False

                win.blit(self.image, self.rect)
                return action
        

class MovingPlatform(pygame.sprite.Sprite):
        def __init__(self, type_, x, y):
                super(MovingPlatform, self).__init__()

                img = pygame.image.load('Buttons & Coins/moving.png')
                self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

                direction = random.choice([-1,1])
                self.move_direction = direction
                self.move_counter = 0
                self.move_x = 0
                self.move_y = 0

                if type_ == 'side':
                        self.move_x = 1
                elif type_ == 'up':
                        self.move_y = 1

        def update(self):
                self.rect.x += self.move_direction * self.move_x
                self.rect.y += self.move_direction * self.move_y
                self.move_counter += 1
                if abs(self.move_counter) >= 50:
                        self.move_direction *= -1
                        self.move_counter *= -1

class Bridge(pygame.sprite.Sprite):
        def __init__(self, x, y):
                super(Bridge, self).__init__()

                img = pygame.image.load('Blocks/26.png')
                self.image = pygame.transform.scale(img, (5*tile_size + 20, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Fluid(pygame.sprite.Sprite):
        def __init__(self, type_, x, y):
                super(Fluid, self).__init__()

                if type_ == 'lava_flow':
                        img = pygame.image.load('Blocks/18.png')
                        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2 + tile_size // 4))
                if type_ == 'lava_still':
                        img = pygame.image.load('Blocks/19.png')
                        self.image = pygame.transform.scale(img, (tile_size, tile_size))
                elif type_ == 'water_flow':
                        img = pygame.image.load('Blocks/20.png')
                        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2 + tile_size // 4))
                elif type_ == 'water_still':
                        img = pygame.image.load('Blocks/21.png')
                        self.image = pygame.transform.scale(img, (tile_size, tile_size))

                
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class ExitGate(pygame.sprite.Sprite):
        def __init__(self, x, y):
                super(ExitGate, self).__init__()
                                        
                img_list = [f'Buttons & Coins/gate{i+1}.png' for i in range(4)]
                self.gate_open = pygame.image.load('Buttons & Coins/gate5.png')
                self.image = pygame.image.load(random.choice(img_list))

                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()

        def update(self, player):
                if player.rect.colliderect(self.rect.x , self.rect.y, self.width, self.height):
                        self.image = self.gate_open


class Forest(pygame.sprite.Sprite):
        b = 1
        def theme(self, t):
                j = "jungle"
                c = "castle"
                v = "volcano"
                m = "draftmine"
                d = "desert"
                vi = "village"
                dg = "dungeon"
                w = "winter"
                
                if j == t:
                        Forest.b=1
                elif c == t:
                        Forest.b=2
                elif v == t:
                        Forest.b=3
                elif m == t:
                        Forest.b=4
                elif d == t:
                        Forest.b=5
                elif vi == t:
                        Forest.b=6
                elif dg == t:
                        Forest.b=7
                elif w == t:
                        Forest.b=8

        def __init__(self, type_, x, y):
                super(Forest, self).__init__()

                b=Forest.b
                if type_ == 'tree':
                        img = pygame.image.load(f'Block{b}/24.png')
                        self.image = pygame.transform.scale(img, (3*tile_size, 3 * tile_size))

                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

class Diamond(pygame.sprite.Sprite):
        def __init__(self, x, y):
                super(Diamond, self).__init__()

                img_list = [f'Buttons & Coins/d{i+1}.png' for i in range(4)]
                img = pygame.image.load(random.choice(img_list))
                self.image = pygame.transform.scale(img, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


class Flying_Enemies(pygame.sprite.Sprite):
        def __init__(self, type_ , x, y):
                super(Flying_Enemies, self).__init__()
                
                if type_ == 'Flying_Mysterio':
                        img = pygame.image.load('Blocks/27.png')
                if type_ == 'Flying_Loki':
                        img = pygame.image.load('Blocks/34.png')
                if type_ == 'Flying_Ultron':
                        img = pygame.image.load('Blocks/30.png')
                if type_ == 'Flying_Thanos':
                        img = pygame.image.load('Blocks/35.png')
                if type_ == 'Flying_Magneto':
                        img = pygame.image.load('Blocks/36.png')
                if type_ == 'Flying_Osborn':
                        img = pygame.image.load('Blocks/37.png')
                if type_ == 'Flying_Dr_Doom':
                        img = pygame.image.load('Blocks/39.png')
                if type_ == 'Flying_Galactus':
                        img = pygame.image.load('Blocks/41.png')
                if type_ == 'Flying_Modok':
                        img = pygame.image.load('Blocks/44.png')


                self.img_left = pygame.transform.scale(img, (1.2*50,100))
                self.img_right = pygame.transform.flip(self.img_left, True, False)
                self.image = self.img_left
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

                self.pos = self.rect.y
                self.dx = 2

        def update(self, player):
                if self.rect.x >= player.rect.x:
                        self.image = self.img_left
                else:
                        self.image = self.img_right

                if self.rect.y >= self.pos:
                        self.dx *= -1
                if self.rect.y <= self.pos - tile_size * 3:
                        self.dx *= -1

                self.rect.y += self.dx


class Walking_Enemies(pygame.sprite.Sprite):
        def __init__(self, type_, x, y):
                super(Walking_Enemies, self).__init__()

                if type_ == 'Walking_Loki':
                        img = pygame.image.load('Blocks/28.png')
                if type_ == 'Walking_Ultron':
                        img = pygame.image.load('Blocks/29.png')
                if type_ == 'Walking_Thanos':
                        img = pygame.image.load('Blocks/31.png')
                if type_ == 'Walking_Venom':
                        img = pygame.image.load('Blocks/32.png')
                if type_ == 'Walking_Octopus':
                        img = pygame.image.load('Blocks/33.png')
                if type_ == 'Walking_Dr_Doom':
                        img = pygame.image.load('Blocks/38.png')
                if type_ == 'Walking_Galactus':
                        img = pygame.image.load('Blocks/40.png')
                if type_ == 'Walking_Red_Skull':
                        img = pygame.image.load('Blocks/42.png')
                if type_ == 'Walking_Modok':
                        img = pygame.image.load('Blocks/43.png')

                self.img_left = pygame.transform.scale(img, (1.2*50, 100))
                self.img_right = pygame.transform.flip(self.img_left, True, False)
                self.imlist = [self.img_left, self.img_right]
                self.index = 0

                self.image = self.imlist[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y

                self.move_direction = -1
                self.move_counter = 0

        def update(self, player):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if abs(self.move_counter) >= 50:
                        self.index = (self.index + 1) % 2
                        self.image = self.imlist[self.index]
                        self.move_direction *= -1
                        self.move_counter *= -1


def lines(win):
        for row in range(HEIGHT // tile_size + 1):
                pygame.draw.line(win, WHITE, (0, tile_size*row), (WIDTH, tile_size*row), 2)
        for col in range(WIDTH // tile_size):
                pygame.draw.line(win, WHITE, (tile_size*col, 0), (tile_size*col, HEIGHT), 2)

def load_level(level):
        game_level = f'Levels/level{level}_data'
        data = None
        if os.path.exists(game_level):
                f = open(game_level, 'rb')
                data = pickle.load(f)
                f.close()

        return data

def text(win, text, pos):
        img = score_font.render(text, True, WHITE)
        win.blit(img, pos)
