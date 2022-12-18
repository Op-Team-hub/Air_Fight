import pygame


class Background:

    def __init__(self, screen):
        """ Инициализация заднего фона (двигающегося изображения)
        :param screen: экран
        """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image_1 = pygame.image.load("assets/desert.png")
        self.rect = self.image_1.get_rect()

        self.rect.x, self.rect.y = 0, -750

    def fill(self):
        """ Добавляет задний фон на экран (отрисовывает его) """
        self.screen.blit(self.image_1, self.rect)
        self.rect.y += 3
        if self.rect.y >= 0:
            self.rect.y = -805
