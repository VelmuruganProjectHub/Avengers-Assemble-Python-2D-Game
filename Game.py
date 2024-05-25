# S.Velmurugan 31/05/2023
import os
import random
import pygame

from pygame import mixer
from pygame.locals import *
from Components import World, Player, Button, load_level, text, sounds, Forest

# Window setup
SIZE = WIDTH , HEIGHT = 1000, 650
WHITE = "#ffffff"
TORCH_RED = '#fb0246'
TURQUOISE = '#52e0c0'
win = pygame.display.set_mode((SIZE))
avengers_icon = pygame.image.load('avengers-icon.png')
pygame.display.set_icon(avengers_icon)
pygame.display.set_caption('Avengers Assemble')
clock = pygame.time.Clock()
FPS = 40
tile_size = 50
i,j = 0,0
global hero
hero = 1
global Play_dialoge, Play_Theme
Play_Theme = True

pygame.init()
hover_sound = pygame.mixer.Sound('Sounds/Hover.ogg')
click_sound = pygame.mixer.Sound('Sounds/Click.ogg')
if Play_Theme:
        pygame.mixer.music.load('Sounds/The Avengers Theme Song.mp3')
        pygame.mixer.music.play(-1)

font = pygame.font.SysFont('Broadway', 30)
themetxt = font.render('Theme', True, TURQUOISE)
font = pygame.font.SysFont('Broadway', 20)
jungletxt = font.render('Jungle', True, WHITE)
castletxt = font.render('Castle', True, WHITE)
volcanotxt = font.render('Volcano', True, WHITE)
draftminetxt = font.render('Draft Mine', True, WHITE)
deserttxt = font.render('Desert', True, WHITE)
villagetxt = font.render('Village', True, WHITE)
dungeontxt = font.render('Dungeon', True, WHITE)
wintertxt = font.render('Winter', True, WHITE)

# background images for Main menu screen & Play screen
bg1 = pygame.image.load('Background Screen/BG1.png')
bg2 = pygame.image.load('Background Screen/BG2.png')
bg3 = pygame.image.load('Background Screen/BG3.png')
bg4 = pygame.image.load('Background Screen/BG4.png')
bg5 = pygame.image.load('Background Screen/BG5.png')
bg6 = pygame.image.load('Background Screen/BG6.png')
bg7 = pygame.image.load('Background Screen/BG7.png')
bg8 = pygame.image.load('Background Screen/BG8.png')
bg9 = pygame.image.load('Background Screen/BG9.png')
bg10 = pygame.image.load('Background Screen/BG10.png')
bg11 = pygame.image.load('Background Screen/BG11.png')
bgs = [bg1, bg2, bg3, bg4, bg5, bg6, bg7, bg8, bg9, bg10, bg11]##132

Avengers = [f'Home Screen/Avengers{i+1}.png' for i in range(16)]##144
Avengers_Logo = [f'Logo/logo{i+1}.png' for i in range(25)]##133
Di = pygame.image.load('Blocks/22.png')
Diamond = pygame.transform.scale(Di, (50, 50))
you_won = pygame.image.load('Game Over & Won Screen/won.png')##238

level = 1
max_level = len(os.listdir('Levels/'))
data = load_level(level)

player_pos = (10, 340)

# creating world & Components
water_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
forest_group = pygame.sprite.Group()
diamond_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
bridge_group = pygame.sprite.Group()
groups = [water_group, lava_group, forest_group, diamond_group, exit_group, enemies_group, platform_group, bridge_group]
world = World(win, data, groups)
player = Player(win, player_pos, world, groups, hero)

# creating buttons
play= pygame.image.load('Buttons & Coins/play.png')
replay = pygame.image.load('Buttons & Coins/replay.png')
home = pygame.image.load('Buttons & Coins/home.png')
exit = pygame.image.load('Buttons & Coins/exit.png')
easy = pygame.image.load('Buttons & Coins/Easy.png')
normal = pygame.image.load('Buttons & Coins/Normal.png')
hard = pygame.image.load('Buttons & Coins/Hard.png')
easyg = pygame.image.load('Buttons & Coins/EasyG.png')
normalg = pygame.image.load('Buttons & Coins/NormalG.png')
hardg = pygame.image.load('Buttons & Coins/HardG.png')
setting = pygame.image.load('Buttons & Coins/setting.png')
music_on = pygame.image.load('Buttons & Coins/music-on.png')
music_off = pygame.image.load('Buttons & Coins/music-off.png')
jungle = pygame.image.load('Block1/2.png')
castle = pygame.image.load('Block2/2.png')
volcano = pygame.image.load('Block3/2.png')
draftmine = pygame.image.load('Block4/2.png')
desert = pygame.image.load('Block5/2.png')
village = pygame.image.load('Block6/2.png')
dungeon = pygame.image.load('Block7/2.png')
winter = pygame.image.load('Block8/2.png')

play_btn = Button(play, (128, 64), WIDTH//2 - 65, HEIGHT//2 - 50)
replay_btn  = Button(replay, (45,42), WIDTH//2 - 110, HEIGHT//2 + 20)
home_btn  = Button(home, (45,42), WIDTH//2 - 20, HEIGHT//2 + 20)
exit_btn  = Button(exit, (45,42), WIDTH//2 + 70, HEIGHT//2 + 20)
easy_btn = Button(easy, (128, 64), WIDTH/2 - 200, HEIGHT - 100)
normal_btn = Button(normal, (128, 64), WIDTH//2 - 65, HEIGHT - 100)
hard_btn = Button(hard, (128, 64), (WIDTH//2 - 65) + 135, HEIGHT - 100)
easyg_btn = Button(easyg, (128, 64), WIDTH/2 - 200, HEIGHT - 100)
normalg_btn = Button(normalg, (128, 64), WIDTH//2 - 65, HEIGHT - 100)
hardg_btn = Button(hardg, (128, 64), (WIDTH//2 - 65) + 135, HEIGHT - 100)
setting_btn = Button(setting, (45,42), WIDTH-980, HEIGHT-620)
music_on_btn = Button(music_on, (45, 42), WIDTH-980, HEIGHT-560)
music_off_btn = Button(music_off, (45, 42), WIDTH-980, HEIGHT-505)
jungle_btn = Button(jungle, (50, 50), WIDTH-85, HEIGHT-615)
castle_btn = Button(castle, (50, 50), WIDTH-85, HEIGHT-540)
volcano_btn = Button(volcano, (50, 50), WIDTH-85, HEIGHT-465)
draftmine_btn = Button(draftmine, (50, 50), WIDTH-85, HEIGHT-390)
desert_btn = Button(desert, (50, 50), WIDTH-85, HEIGHT-315)
village_btn = Button(village, (50, 50), WIDTH-85, HEIGHT-240)
dungeon_btn = Button(dungeon, (50, 50), WIDTH-85, HEIGHT-165)
winter_btn = Button(winter, (50, 50), WIDTH-85, HEIGHT-90)

# function to reset a level
def reset_level(level):
        global cur_score
        cur_score = 0
        global hero
        data = load_level(level)
        if data:
                for group in groups:
                        group.empty()
                world = World(win, data, groups)
                if hero <= 25:
                        hero += 1
                if hero == 26:
                        hero = 1
                player.reset(win, player_pos, world, groups, hero)
        return world

score = 0
cur_score = 0

main_menu = True
game_over = False
level_won = False
game_won = False
running = True

while running:
        for event in pygame.event.get():
                if event.type == QUIT:
                        running = False
        pressed_keys = pygame.key.get_pressed()

        bg = bgs[i]
        win.blit(bg, (0,0))
        logo = pygame.image.load(Avengers_Logo[hero-1])
        win.blit(logo, (40,40))
        win.blit(Diamond, (WIDTH-160,HEIGHT-623))
        world.draw()
        for group in groups:
                group.draw(win)

        if main_menu:

                Avenger = pygame.image.load(Avengers[j])
                win.blit(Avenger, (0,0))

                play_game = play_btn.draw(win)
                easy_mode = easy_btn.draw(win)
                normal_mode = normal_btn.draw(win)
                hard_mode = hard_btn.draw(win)
                setting = setting_btn.draw(win)
                musicOn = music_on_btn.draw(win)
                musicOff = music_off_btn.draw(win)
                        
                if easy_mode:
                        click_sound.play()
                        easy_mode = easyg_btn.draw(win)
                        m = "easymode"
                        player.mode(m)
                if normal_mode:
                        click_sound.play()
                        normal_mode = normalg_btn.draw(win)
                        m = "normalmode"
                        player.mode(m)
                if hard_mode:
                        click_sound.play()
                        hard_mode = hardg_btn.draw(win)
                        m = "hardmode"
                        player.mode(m)
 
                if setting:
                        click_sound.play()
                        pygame.mixer.music.stop()
                        import Game_Editor
                        running = False
                if musicOn:
                        click_sound.play()
                        pygame.mixer.music.play(-1)
                if musicOff:
                        click_sound.play()
                        pygame.mixer.music.stop()

                if play_game:
                        click_sound.play()
                        main_menu = False
                        game_over = False
                        game_won = False
                        score = 0

        else:
                if not game_over and not game_won:
                        
                        enemies_group.update(player)
                        platform_group.update()
                        exit_group.update(player)
                        if pygame.sprite.spritecollide(player, diamond_group, True):
                                sounds[0].play()
                                cur_score += 1
                                score += 1


                        text(win, f'{score}', ((WIDTH//tile_size - 2) * tile_size, tile_size//2 + 10))
                        
                game_over, level_won = player.update(pressed_keys, game_over, level_won, game_won)

                if game_over and not game_won:
                        replay = replay_btn.draw(win)
                        home = home_btn.draw(win)
                        exit = exit_btn.draw(win)
                        setting = setting_btn.draw(win)
                        jungle = jungle_btn.draw(win)
                        castle = castle_btn.draw(win)
                        volcano = volcano_btn.draw(win)
                        draftmine = draftmine_btn.draw(win)
                        desert = desert_btn.draw(win)
                        village = village_btn.draw(win)
                        dungeon = dungeon_btn.draw(win)
                        winter = winter_btn.draw(win)
                        win.blit(themetxt, (WIDTH-120,HEIGHT-647))
                        win.blit(jungletxt, (WIDTH-98, HEIGHT-565))
                        win.blit(castletxt, (WIDTH-95, HEIGHT-490))
                        win.blit(volcanotxt, (WIDTH-105, HEIGHT-415))
                        win.blit(draftminetxt, (WIDTH-123, HEIGHT-340))
                        win.blit(deserttxt, (WIDTH-95, HEIGHT-265))
                        win.blit(villagetxt, (WIDTH-100, HEIGHT-190))
                        win.blit(dungeontxt, (WIDTH-108, HEIGHT-115))
                        win.blit(wintertxt, (WIDTH-98, HEIGHT-40))


                        if setting:
                                click_sound.play()
                                pygame.mixer.music.stop()
                                import Game_Editor
                                running = False
                                
                        if jungle:
                                click_sound.play()
                                t = "jungle"
                                world.theme(t)
                        if castle:
                                click_sound.play()
                                t = "castle"
                                world.theme(t)
                        if volcano:
                                click_sound.play()
                                t = "volcano"
                                world.theme(t)
                        if draftmine:
                                click_sound.play()
                                t = "draftmine"
                                world.theme(t)
                        if desert:
                                click_sound.play()
                                t = "desert"
                                world.theme(t)
                        if village:
                                click_sound.play()
                                t = "village"
                                world.theme(t)
                        if dungeon:
                                click_sound.play()
                                t = "dungeon"
                                world.theme(t)
                        if winter:
                                click_sound.play()
                                t = "winter"
                                world.theme(t)

                        if game_over:
                                pygame.mixer.music.stop()
                                
                        if replay:
                                click_sound.play()
                                score -= cur_score
                                world = reset_level(level)
                                if i < 11:
                                        i=i+1
                                if i >= 11:
                                        i=0
                                game_over = False
                                pygame.mixer.music.play(-1)

                        if home:
                                click_sound.play()
                                game_over = True
                                main_menu = True
                                level = 1
                                if i < 11:
                                        i=i+1
                                if i >= 11:
                                        i=0
                                world = reset_level(level)
                                if j < 16:
                                        j=j+1
                                if j >= 16:
                                        j=0
                                pygame.mixer.music.play(-1)
                        if exit:
                                click_sound.play()
                                running = False

                if level_won:
                        if level <= max_level:
                                level += 1
                                game_level = f'Levels/level{level}_data'
                                if os.path.exists(game_level):
                                        data = []
                                        world = reset_level(level)
                                        level_won = False
                                        score += cur_score
                                        if i < 11:
                                                i=i+1
                                        if i >= 11:
                                                i=0

                        else:
                                game_won = True
                                bg = bg1
                                win.blit(you_won, (0,0))
                                home = home_btn.draw(win)
                                settings = setting_btn.draw(win)
                                musicOn = music_on_btn.draw(win)
                                musicOff = music_off_btn.draw(win)

                                if setting:
                                        click_sound.play()
                                        pygame.mixer.music.stop()
                                        import Game_Editor
                                        running = False
                                if musicOn:
                                        click_sound.play()
                                        pygame.mixer.music.play(-1)
                                if musicOff:
                                        click_sound.play()
                                        pygame.mixer.music.stop()
                                
                                if home:
                                        click_sound.play()
                                        game_over = True
                                        main_menu = True
                                        level_won = False
                                        level = 1
                                        if i < 11:
                                                i=i+1
                                        if i >= 11:
                                                i=0
                                        world = reset_level(level)
                                        if j < 16:
                                                j=j+1
                                        if j >= 16:
                                                j=0

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()
