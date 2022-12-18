import Controls
import pygame
from Player import Player, Propeller
from Boss import Boss, Smoke, Fire
from BackGround import Background
from Statistics import Statistics
from Bonus import MissileRefuel
from UI import UI


def run_game():
    """ Функция, которая запускает игру"""
    width, height, fps = 720, 900, 60
    bg_color = (208, 199, 130)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Air Combat')
    clock = pygame.time.Clock()
    background = Background(screen)
    statistics = Statistics()
    interface = UI(screen, statistics)

    dude = Player(screen)
    propeller = Propeller(screen, dude)
    enemies = pygame.sprite.Group()
    billy = Boss(screen)
    smoke = Smoke(screen, billy, statistics)
    fire = Fire(screen, billy, statistics)

    refuel = MissileRefuel(screen)
    bullets, missiles, thunder = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    bullets_enemy = pygame.sprite.Group()

    Controls.spread_your_wings(screen, enemies, billy, statistics)

    while dude.running == 1:
        clock.tick(fps)
        if len(enemies) == 0 and statistics.wave_nuber < 5:
            statistics.cooldown -= 1
            if statistics.cooldown == 0:
                Controls.spread_your_wings(screen, enemies, billy, statistics)
                statistics.score += 1000
        Controls.events(screen, dude, statistics, refuel, bullets, missiles, thunder)
        propeller.propeller_update()
        refuel.moving()

        Controls.update_bullets(bullets, thunder, missiles, bullets_enemy, statistics)
        Controls.update_enemies(screen, statistics, enemies, bullets, missiles, thunder, bullets_enemy)
        Controls.screen_update(bg_color, background, screen, dude, propeller, bullets, missiles,
                               thunder, enemies, bullets_enemy, billy, refuel, statistics, interface, smoke, fire)

    while dude.running == 0:
        clock.tick(fps)
        Controls.after_lose(dude, statistics, interface)

    game_result = [False, '']
    if dude.running == -1:
        game_result[0] = True
    if statistics.misses != 0 and dude.running != 1:
        game_result[1] = (f'Accuracy: {round((statistics.shoots - statistics.misses) / statistics.shoots * 1000) / 10}'
                          f'%\nYour score is {Controls.score(statistics)}')
    return game_result


while True:
    result = run_game()
    if result[0] is True:
        print(result[1])
        break
