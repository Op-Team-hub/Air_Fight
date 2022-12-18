import pygame.image


class Boss(pygame.sprite.Sprite):

    def __init__(self, screen):
        """ Инициализация босса
        :param screen: экран
        """
        super(Boss, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("assets/Bomber.png")
        self.image_2 = pygame.image.load("assets/Bomber_heatbox.png")
        self.image_3 = pygame.image.load("assets/Bomber_dead.png")
        self.rect_sprite = self.image.get_rect()
        self.rect = self.image_2.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.rect_sprite.centerx = self.screen_rect.centerx
        self.rect_sprite.centery = self.rect.centery = self.screen_rect.top + 200
        self.coordinate_x = float(self.rect.centerx)
        self.coordinate_y = float(self.rect.bottom)

        self.speed = 1
        self.cooldown, self.charging = 0, 200
        self.win = True

    def output(self):
        """ Добавляет босса на экран (отрисовывает его)"""
        self.screen.blit(self.image, self.rect_sprite)

    def update_position(self):
        """ Обновляет позицию босса"""

        self.rect_sprite.centerx = self.rect.centerx = self.coordinate_x
        self.rect_sprite.centery = self.rect.centery = self.coordinate_y

        self.coordinate_x += self.speed
        if self.rect_sprite.right > self.screen_rect.right - 35:
            self.speed = -1
        elif self.rect_sprite.left < self.screen_rect.left + 35:
            self.speed = 1

        self.charging -= 1
        self.cooldown -= 1

    def dead(self):
        self.rect_sprite.centery = self.rect.centery = self.coordinate_y
        self.coordinate_y += 3
        self.screen.blit(self.image_3, self.rect_sprite)


class Smoke:

    def __init__(self, screen, boss, statistics):
        """ Инициализация визуальных эффектов (дыма) при уменьшении здоровья босса
        :param screen: экран
        :param boss: объект босса
        :param statistics: объект статистики
        """

        self.screen = screen
        self.boss = boss
        self.statistics = statistics

        self.change = 23
        self.image = pygame.image.load('assets/smoke.png')
        self.image_rev = pygame.image.load('assets/smoke_reverse.png')
        self.rect = self.image.get_rect()

        self.rect.right = self.boss.rect.centerx - 15
        self.rect.top = self.boss.rect.centery - 20

    def update(self):
        """Обновляет позицию эффектов'"""
        self.change -= 1
        self.rect.top = self.boss.rect.centery - 30

        if self.change > 0:
            self.rect.right = self.boss.rect.centerx - 15
        elif self.change > -23:
            self.rect.right = self.boss.rect.centerx
        else:
            self.change = 23

    def output(self):
        """Добавляет эффекты на экран (отрисовывает их)"""
        if self.change > 0:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image_rev, self.rect)


class Fire(Smoke):

    def __init__(self, screen, boss, statistics):
        """ Инициализация визуальных эффектов (огня) при уменьшении здоровья босса
        :param screen: экран
        :param boss: объект босса
        :param statistics: объект статистики
        """
        super(Fire, self).__init__(screen, boss, statistics)

        self.image = pygame.image.load('assets/fire.png')
        self.image_rev = pygame.image.load('assets/fire_reverse.png')
        self.change = 15

    def update(self):
        """Обновляет позицию эффектов'"""
        self.change -= 1
        self.rect.top = self.boss.rect.centery - 30

        if self.change > 0:
            self.rect.left = self.boss.rect.centerx
        elif self.change > -15:
            self.rect.left = self.boss.rect.centerx + 15
        else:
            self.change = 15
