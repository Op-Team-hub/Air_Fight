import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gunner):
        """Инициализация одной пули (класс пули является дочерним от класса Sprite в библиотеке pygame.
        Это нужно для использования уже существующих методов)
        :param screen: экран
        :param gunner: обьект, от которого идет пуля
        """
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 14)
        self.color = 255, 30, 30
        self.direction = 1

        self.rect.centerx = gunner.rect.centerx
        self.rect.centery = gunner.rect.centery
        self.coordinate_y = float(self.rect.y)
        self.speed = 17

    def update_projectile(self):
        """Обновляет позицию пули"""
        self.coordinate_y -= (self.speed * self.direction)
        self.rect.y = self.coordinate_y

    def output_projectile(self):
        """Добавляет пулю на экран (отрисовывает её)"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class ZeusStrike(Bullet):

    def __init__(self, screen, dude):
        super(ZeusStrike, self).__init__(screen, dude)
        self.rect = pygame.Rect(0, 0, 200, 20)
        self.color = 30, 30, 255

        self.rect.centerx = dude.rect.centerx
        self.rect.top = dude.rect.top
        self.coordinate_y = float(self.rect.y)
        self.speed = 19


class Missile(pygame.sprite.Sprite):

    def __init__(self, screen, dude):
        """Инициализация одной ракеты (класс ракеты является дочерним от класса Sprite в библиотеке pygame.
        Это нужно для использования уже существующих методов)
        :param screen: экран
        :param dude: игрок, от которого идет ракета
        """
        super(Missile, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('assets/Missile_2.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = dude.rect.centerx
        self.rect.top = dude.rect.top
        self.coordinate_y = float(self.rect.y)
        self.speed = 9

    def update_missile(self):
        """Обновляет позицию ракеты"""
        self.coordinate_y -= self.speed
        self.rect.y = self.coordinate_y

    def output_missile(self):
        """Добавляет ракету на экран (отрисовывает её)"""
        self.screen.blit(self.image, self.rect)
