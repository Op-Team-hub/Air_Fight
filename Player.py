import pygame.image


class Player:
    running = 1

    def __init__(self, screen):
        """ Инициализация игрока
        :param screen: экран
        """
        self.screen = screen
        self.image_1 = pygame.image.load("assets/Avenger.png")
        self.image_2 = pygame.image.load("assets/Avenger_heatbox.png")
        self.image_left = pygame.image.load("assets/Avenger_left.png")
        self.image_right = pygame.image.load("assets/Avenger_right.png")
        self.rect_sprite = self.image_1.get_rect()
        self.rect = self.image_2.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect_sprite.centerx = self.rect.centerx
        self.rect_sprite.centery = self.rect.centery = self.screen_rect.bottom - 150
        self.coordinate_x = float(self.rect.centerx)
        self.coordinate_y = float(self.rect.bottom)

        self.moving_left, self.moving_right = False, False
        self.moving_up, self.moving_down = False, False
        self.speed = 5
        self.zeus_strike = False

    def output(self):
        """Добавляет игрока на экран (отрисовывает его)"""
        if self.moving_left:
            self.screen.blit(self.image_left, self.rect_sprite)
        elif self.moving_right:
            self.screen.blit(self.image_right, self.rect_sprite)
        else:
            self.screen.blit(self.image_1, self.rect_sprite)
        # self.screen.blit(self.image_2, self.rect)

    def update_position(self):
        """Обновляет позицию игрока"""
        if self.moving_left and self.rect_sprite.left > self.screen_rect.left:
            self.coordinate_x -= 1 * self.speed
        if self.moving_right and self.rect_sprite.right < self.screen_rect.right:
            self.coordinate_x += 1 * self.speed
        if self.moving_up and self.rect_sprite.top > self.screen_rect.centery:
            self.coordinate_y -= 1.5 * self.speed
        if self.moving_down and self.rect_sprite.bottom < self.screen_rect.bottom:
            self.coordinate_y += 1.5 * self.speed

        self.rect.centerx = self.coordinate_x
        self.rect_sprite.centerx = self.rect.centerx
        self.rect_sprite.centery = self.rect.centery = self.coordinate_y

    def game_over(self):
        """Прекращает игру в случае поражения"""
        self.running = 0

    def exit(self):
        """Прекращает работу программы в случае принудительного закрытия"""
        self.running = -1


class Propeller:

    def __init__(self, screen, dude):
        self.dude = dude
        self.screen = screen
        self.propeller_position = 0
        self.update_speed = 1
        self.image_1 = pygame.image.load("assets/Propeller_1.png")
        self.image_2 = pygame.image.load("assets/Propeller_2.png")
        self.image_3 = pygame.image.load("assets/Propeller_3.png")
        self.image_4 = pygame.image.load("assets/Propeller_4.png")
        self.image = self.image_1
        self.rect = self.image_1.get_rect()

    def propeller_update(self):
        if self.propeller_position < 1 * self.update_speed:
            self.image = self.image_1
            self.propeller_position += 1
        elif self.propeller_position < 2 * self.update_speed:
            self.image = self.image_2
            self.propeller_position += 1
        elif self.propeller_position < 3 * self.update_speed:
            self.image = self.image_3
            self.propeller_position += 1
        elif self.propeller_position < 4 * self.update_speed:
            self.image = self.image_4
            self.propeller_position += 1
        else:
            self.propeller_position = 0

        self.rect.centerx = self.dude.rect.centerx - 5
        self.rect.centery = self.dude.rect.centery - 20

    def output_propeller(self):
        if self.propeller_position < 1 * self.update_speed:
            self.screen.blit(self.image_1, self.rect)
            self.propeller_position += 1
        elif self.propeller_position < 2 * self.update_speed:
            self.screen.blit(self.image_2, self.rect)
            self.propeller_position += 1
        elif self.propeller_position < 3 * self.update_speed:
            self.screen.blit(self.image_3, self.rect)
            self.propeller_position += 1
        elif self.propeller_position < 4 * self.update_speed:
            self.screen.blit(self.image_4, self.rect)
            self.propeller_position += 1
        else:
            self.propeller_position = 0
