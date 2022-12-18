import pygame

from Ammo import Bullet, ZeusStrike, Missile
from Enemy import Enemy
from random import randint


def events(screen, dude, statistics, bonus, bullets, missiles, thunder):
    """ Функция обрабатывает входящие данные от игрока (взаимодецствия с клавиатурой) и реагирует на них
    Обновляет значения переменных в соответствии с действиями игрока
    :param screen: экран
    :param dude: объект игрока
    :param statistics: объект статистики
    :param bonus: объект бонусов
    :param bullets: объект контейнер пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param missiles: объект контейнер ракет (не одна ракета, а массив, содержащий данные о каждой)
    :param thunder: объект контейнер мощных пуль (не одна пуля, а массив, содержащий данные о каждой)
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dude.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dude.moving_left = True
            elif event.key == pygame.K_RIGHT:
                dude.moving_right = True
            elif event.key == pygame.K_UP:
                dude.moving_up = True
            elif event.key == pygame.K_DOWN:
                dude.moving_down = True

            elif event.key == pygame.K_SPACE:
                if statistics.exit:
                    dude.exit()
                if dude.zeus_strike:
                    new_lighting = ZeusStrike(screen, dude)
                    thunder.add(new_lighting)
                else:
                    new_bullet = Bullet(screen, dude)
                    bullets.add(new_bullet)
                    statistics.shoots += 1
            elif event.key == pygame.K_LALT and statistics.missiles_left > 0:
                statistics.missiles_left -= 1
                new_missile = Missile(screen, dude)
                missiles.add(new_missile)
                statistics.shoots += 1
            elif event.key == pygame.K_r:
                statistics.missiles_left = 3

            elif event.key == pygame.K_RALT:
                if dude.zeus_strike:
                    dude.zeus_strike = False
                else:
                    dude.zeus_strike = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dude.moving_left = False
            elif event.key == pygame.K_RIGHT:
                dude.moving_right = False
            elif event.key == pygame.K_UP:
                dude.moving_up = False
            elif event.key == pygame.K_DOWN:
                dude.moving_down = False

        if pygame.sprite.collide_rect(dude, bonus):
            statistics.refuel_cooldown = 300 + randint(100, 500)
            bonus.on_screen = False
            bonus.rect.centery = bonus.rect_out.centery = 0
            statistics.missiles_left = 3


def update_bullets(bullets, thunder, missiles, bullets_enemy, statistics):
    """ Обновление позиций всех пуль, удаление пуль, если они за пределами экрана
    :param bullets: объект контейнер пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param thunder: объект контейнер мощных пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param missiles: объект контейнер ракет (не одна ракета, а массив, содержащий данные о каждой)
    :param bullets_enemy: объект контейнер вражеских пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param statistics: объект статистики
    """
    for bullet in bullets:
        bullet.update_projectile()
        if bullet.rect.bottom < 0:
            statistics.misses += 1
            bullets.remove(bullet)
    for lighting in thunder:
        lighting.update_projectile()
        if lighting.rect.bottom < 0:
            thunder.remove(lighting)
    for missile in missiles:
        missile.update_missile()
        if missile.rect.bottom < 0:
            missiles.remove(missile)
            statistics.misses += 1
    for bullet in bullets_enemy:
        bullet.update_projectile()
        if bullet.rect.top > 900:
            bullets_enemy.remove(bullet)


def update_enemies(screen, statistics, enemies, bullets, missiles, thunder, bullets_enemy):
    """ Обновление позиций врагов, проверка на пересечение с пулями/ракетами
    :param screen: экран
    :param statistics: объект статистики
    :param enemies: объект контейнер врагов (не один враг, а массив, содержащий данные о каждом)
    :param bullets: объект контейнер пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param missiles: объект контейнер ракет (не одна ракета, а массив, содержащий данные о каждой)
    :param thunder: объект контейнер мощных пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param bullets_enemy: объект контейнер вражеских пуль (не одна пуля, а массив, содержащий данные о каждой)
    """
    for enemy in enemies:
        if enemy.shot_down_1 != 0:
            enemy.shot_down_1 -= 1
        if enemy.shot_down_2 != 0:
            enemy.shot_down_2 -= 1
        if enemy.cooldown <= 0:
            new_bullet = Bullet(screen, enemy)
            new_bullet.direction = -1
            new_bullet.speed = 7 + statistics.wave_nuber
            bullets_enemy.add(new_bullet)
            enemy.cooldown += (125 - statistics.wave_nuber * 5)
        if pygame.sprite.spritecollide(enemy, bullets, True):
            enemy.health -= 1
            statistics.score += 100
            enemy.shot_down_1 = 7
        if pygame.sprite.spritecollide(enemy, missiles, True):
            enemy.health -= 5
            statistics.score += 650
            enemy.shot_down_2 = 12
        if pygame.sprite.spritecollide(enemy, thunder, False):
            enemy.health -= 100
        enemy.update_position()
        if enemy.health <= 0:
            statistics.score += 100
            enemies.remove(enemy)


def boss_update(screen, boss, statistics, bullets, missiles, thunder, bullets_enemy):
    """ Обновляет позицию босса, проверка на пересечение с пулями/ракетами
    :param screen: экран
    :param boss: объект босса
    :param statistics: объект статистики
    :param bullets: объект контейнер пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param missiles: объект контейнер ракет (не одна ракета, а массив, содержащий данные о каждой)
    :param thunder: объект контейнер мощных пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param bullets_enemy: объект контейнер вражеских пуль (не одна пуля, а массив, содержащий данные о каждой)
    """
    boss.update_position()

    if boss.charging <= 0 < statistics.boss_hp:
        if boss.cooldown <= 0:
            new_bullet = Bullet(screen, boss)
            new_bullet.direction = -1
            new_bullet.speed = 13
            bullets_enemy.add(new_bullet)
            boss.cooldown = 7
            if boss.charging < -250:
                boss.charging = 300
    if pygame.sprite.spritecollide(boss, bullets, True):
        statistics.boss_hp -= 0.7
        statistics.score += 100
        boss.shot_down_1 = 7
    if pygame.sprite.spritecollide(boss, missiles, True):
        statistics.boss_hp -= 3.5
        statistics.score += 650
        boss.shot_down_2 = 12
    if pygame.sprite.spritecollide(boss, thunder, False):
        statistics.boss_hp -= 4
    if statistics.boss_hp <= 0:
        boss.win = True


def score(statistics):
    """ Подсчёт счета игрока
    :param statistics: объект статистики
    """
    return round(statistics.score * (1 + (statistics.shoots - statistics.misses) / statistics.shoots))


def spread_your_wings(screen, enemies, boss, statistics, testing=False):
    """ Функция создает новую волну врагов (чем выше волна, тем больше врагов появляется и тем быстрее они перемещаются)
    :param screen: экран
    :param enemies: объект контейнер врагов (не один враг, а массив, содержащий данные о каждом)
    :param boss: объект босса
    :param statistics: объект статистики
    :param testing: по умолчанию выключена, используется для проведения тестирования поведения врагов
    """
    statistics.wave_nuber += 1
    enemy = Enemy(screen)
    number_of_enemies = 4 + (statistics.wave_nuber // 2)
    if testing:
        number_of_enemies = 1
    statistics.cooldown = 120
    delta_x = int((720 - 2 * enemy.rect.width) / (number_of_enemies + 1))

    if statistics.wave_nuber < 5:
        for enemy_number in range(1, number_of_enemies + 1):
            enemy = Enemy(screen)
            enemy.speed_x += ((enemy_number - 1) * (5 + statistics.wave_nuber) / 100)
            enemy.temp += enemy_number * 0.5
            enemy.start_y += (25 * enemy_number * ((-1) ** enemy_number))
            enemy.amplitude_y *= (1 + 0.1 * ((-1) ** enemy_number))
            enemy.coordinate_x = enemy.rect.width + delta_x * enemy_number
            enemy.rect.x = enemy.coordinate_x
            enemy.cooldown += (30 * (enemy_number - 3))

            if testing:
                enemy.speed_x = enemy.speed_y = enemy.amplitude_y = 0
                enemy.health = 100
            enemies.add(enemy)
    else:
        boss.win = False


def screen_update(bg_color, background, screen, dude, propeller, bullets, missiles, thunder,
                  enemies, bullets_enemy, boss, bonus, statistics, interface, smoke, fire):
    """ Функция отрисовки экрана. Выводин всех объекты и информацию на экран.
    :param bg_color: цвет заливки заднего фона
    :param background: объект заднего фона (двигающееся изображение)
    :param screen: экран
    :param dude: объект игрока
    :param propeller: объект лопостей вертолёта
    :param bullets: объект контейнер пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param missiles: объект контейнер ракет (не одна ракета, а массив, содержащий данные о каждой)
    :param thunder: объект контейнер мощных пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param enemies: объект контейнер врагов (не один враг, а массив, содержащий данные о каждом)
    :param bullets_enemy: объект контейнер вражеских пуль (не одна пуля, а массив, содержащий данные о каждой)
    :param boss: объект босса
    :param bonus: объект бонуса
    :param statistics: объект статистики
    :param interface: объет интерфейса
    :param smoke: объект визуальных эффектов (дым) для босса
    :param fire: объект визуальных эффектов (огонь) для босса
    """
    screen.fill(bg_color)
    if background is not None:
        background.fill()

    dude.update_position()

    if pygame.sprite.spritecollide(dude, bullets_enemy, True):
        statistics.hp -= 1
        if statistics.hp <= 0:
            statistics.title_cooldown = 100
            dude.game_over()
            statistics.lose = True

    interface.update_user()

    for bullet in bullets_enemy:
        bullet.output_projectile()
    for enemy in enemies.sprites():
        enemy.enemy_output()
        screen.blit(propeller.image, enemy.rect_r)

    if statistics.wave_nuber == 5:
        if statistics.boss_hp > 0:
            boss_update(screen, boss, statistics, bullets, missiles, thunder, bullets_enemy)
            boss.output()
            if 0 < statistics.boss_hp < 30:
                smoke.update()
                smoke.output()
            if 0 < statistics.boss_hp < 7:
                fire.update()
                fire.output()
        else:
            boss.dead()
            if boss.rect.top > 700:
                statistics.win = True
                if statistics.title_cooldown < 0:
                    statistics.exit = True
                else:
                    statistics.title_cooldown -= 1

    for bullet in bullets.sprites():
        bullet.output_projectile()
    for missile in missiles.sprites():
        missile.output_missile()
    for lighting in thunder:
        lighting.output_projectile()

    if bonus.on_screen is False and statistics.refuel_cooldown <= 0 and statistics.win is False:
        bonus.on_screen = True
        if randint(0, 1):
            bonus.rect.centerx = bonus.rect_out.centerx = -30
            bonus.rect.centery = bonus.rect_out.centery = 700 + randint(0, 100)
        else:
            bonus.rect.centerx = bonus.rect_out.centerx = 750
            bonus.rect.centery = bonus.rect_out.centery = 700 + randint(0, 100)
            bonus.speed = -1
    elif bonus.on_screen is False:
        statistics.refuel_cooldown -= 1
    if bonus.rect.centerx < -50 or bonus.rect.centerx > 1000:
        bonus.on_screen = False

    if bonus.on_screen:
        bonus.output()
    dude.output()
    interface.show()
    pygame.display.flip()


def after_lose(dude, statistics, interface):
    """ Функция, необхрдимая после проигрыша в игре
    :param dude: объект игрока
    :param statistics: объект статистики 
    :param interface: объект интерфейса
    """
    if statistics.title_cooldown >= 0:
        statistics.title_cooldown -= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dude.running = -1
        elif event.type == pygame.KEYDOWN and statistics.title_cooldown < 0:
            if event.key == pygame.K_SPACE:
                dude.running = 1
    interface.show()
    pygame.display.flip()
