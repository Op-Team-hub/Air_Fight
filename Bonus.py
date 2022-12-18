import pygame


class MissileRefuel:

    def __init__(self, screen):
        """ Инициализация бонуса, который пополняет запас ракет у игрока
        :param screen: экран
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.rect_out = pygame.Rect(0, 0, 30, 30)
        self.color_in = (250, 30, 30)
        self.color_out = (30, 30, 30)

        self.on_screen = False
        self.speed = 1
        self.rect.centerx = self.rect_out.centerx = -20
        self.rect.centery = self.rect_out.centery = 700

    def moving(self):
        """Обновление позиции бонуса"""
        self.rect.centerx += self.speed
        self.rect_out.centerx += self.speed

    def output(self):
        """Добавляет бонус на экран (отрисовывает его)"""
        pygame.draw.rect(self.screen, self.color_out, self.rect_out)
        pygame.draw.rect(self.screen, self.color_in, self.rect)
