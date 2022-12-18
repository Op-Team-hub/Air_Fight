import math
import pygame
from random import randint


class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen):
        """Инициализация одного врага (класс врага является дочерним от класса Sprite в библиотеке pygame.
        Это нужно для использования уже существующих методов)
        :param screen: экран
        """
        super(Enemy, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load("assets/Helicopter_back.png")
        self.shoot_1 = pygame.image.load("assets/shoot.png")
        self.shoot_2 = pygame.image.load("assets/big_shoot.png")
        self.rect = self.image.get_rect()
        self.rect_r = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.shot_down_1 = self.shot_down_2 = 0

        self.coordinate_x = float(self.rect.x)
        self.coordinate_y = float(self.rect.y)
        self.speed_x = 2
        self.speed_y = 1

        self.rect_r.centerx = self.rect.centerx + 5
        self.rect_r.centery = self.rect.centery + 20

        self.amplitude_y = 40
        self.start_y = 150
        self.temp = float(0)

        self.health = 6
        self.cooldown = 120

    def update_position(self):
        """Обновляет позицию врага"""
        if self.rect.right >= self.screen_rect.right - 20 or self.rect.left <= self.screen_rect.left + 20:
            self.speed_x *= -1
        self.coordinate_x += self.speed_x
        if self.rect.centery <= 80:
            self.speed_y = 1
        elif self.rect.centery >= 480:
            self.speed_y = -1
        self.start_y += self.speed_y
        self.coordinate_y = self.start_y + ((math.cos(self.temp / 3) + math.sin(self.temp)) * self.amplitude_y)
        self.temp += 0.05

        self.rect.x = self.coordinate_x
        self.rect.y = self.coordinate_y
        self.rect_r.centerx = self.rect.centerx - 30
        self.rect_r.centery = self.rect.centery + 22

        self.cooldown -= 1

    def enemy_output(self):
        """Добавляет врага на экран (отрисовывает его)"""
        self.screen.blit(self.image, self.rect)
        if self.shot_down_1 != 0:
            self.screen.blit(self.shoot_1, (self.rect.x + randint(10, 40), self.rect.bottom - 15))
        if self.shot_down_2 != 0:
            self.screen.blit(self.shoot_2, (self.rect.x + randint(10, 40), self.rect.bottom - 40))
