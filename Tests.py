import Controls
import pygame

from Player import Player, Propeller
from Statistics import Statistics
from Bonus import MissileRefuel
from UI import UI


def run_game():
    width, height, fps = 720, 900, 60
    bg_color = (208, 199, 130)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Air Combat test')
    clock = pygame.time.Clock()
    statistics = Statistics()
    interface = UI(screen, statistics)

    dude = Player(screen)
    propeller = Propeller(screen, dude)
    enemies = pygame.sprite.Group()
    Controls.spread_your_wings(screen, enemies, statistics, testing=True)

    refuel = MissileRefuel(screen)
    bullets, missiles, thunder = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
    bullets_enemy = pygame.sprite.Group()

    while dude.running == 1:
        clock.tick(fps)
        Controls.events(screen, dude, statistics, refuel, bullets, missiles, thunder)
        propeller.propeller_update()
        refuel.moving()

        Controls.update_bullets(bullets, thunder, missiles, bullets_enemy, statistics)
        Controls.update_enemies(screen, statistics, enemies, bullets, missiles, thunder, bullets_enemy)
        Controls.screen_update(bg_color, None, screen, dude, propeller, bullets, missiles,
                               thunder, enemies, bullets_enemy, refuel, statistics, interface)

    if statistics.misses != 0:
        print(f'accuracy: {round((statistics.shoots - statistics.misses) / statistics.shoots * 1000) / 10}%')
        print(f'your score is {Controls.score(statistics)}')
    if dude.running == -1:
        return -1


cont, keep = 'y', ['y', 'yes']
while cont == 'y':
    if run_game() == -1:
        break
    print('Do you want to continue? (y/n)')
    cont = input()
