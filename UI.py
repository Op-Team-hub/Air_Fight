import pygame.font
from Controls import score


class UI:

    def __init__(self, screen, statistics):
        """Инициализация шрифтов для выведения информации на экран (интерфейс)
        :param screen: экран
        :param statistics: объект статистики, содержит необходимую информацию для выведения на экран
        """

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.statistics = statistics
        self.text_color = (210, 50, 70)
        self.title_color = (15, 120, 35)
        self.font_1 = pygame.font.SysFont('font', 40, True)
        self.font_2 = pygame.font.SysFont('font', 70, True)

    def update_user(self):
        """Обновление информации (интерфейса)"""

        """Обновление количества здоровья у игрока"""
        self.image_hp = self.font_1.render(str(self.statistics.hp), True, self.text_color)
        self.image_hp_rect = self.image_hp.get_rect()
        self.image_hp_rect.right = self.screen_rect.right - 20
        self.image_hp_rect.bottom = self.screen_rect.bottom - 30

        """Обновление количества оставшихся ракет"""
        self.image_missiles = self.font_1.render(str(self.statistics.missiles_left), True, self.text_color)
        self.image_missiles_rect = self.image_missiles.get_rect()
        self.image_missiles_rect.right = self.screen_rect.right - 20
        self.image_missiles_rect.bottom = self.image_hp_rect.top - 10

        """Обновление значения текущей волны"""
        self.image_wave = self.font_2.render("WAVE " + str(self.statistics.wave_nuber), False, self.title_color)
        self.image_wave_rect = self.image_wave.get_rect()
        self.image_wave_rect.top = self.screen_rect.top + 20
        self.image_wave_rect.centerx = self.screen_rect.centerx

        """Обновление текущего счета игрока"""
        self.image_score = self.font_1.render(str(self.statistics.score), True, self.text_color)
        self.image_score_rect = self.image_score.get_rect()
        self.image_score_rect.left = self.screen_rect.left + 20
        self.image_score_rect.bottom = self.screen_rect.bottom - 30

        """Обновление количества здоровья у босса"""
        self.image_boss_hp = self.font_1.render(str(self.statistics.boss_hp), True, self.text_color)
        self.image_boss_hp_rect = self.image_boss_hp.get_rect()

        self.boss_hp_rect_in = pygame.Rect(0, 0, self.statistics.boss_hp * 7, 30)
        self.boss_hp_rect_out = pygame.Rect(0, 0, 360, 40)
        self.color_in = (250, 30, 30)
        self.color_out = (30, 30, 30)

        self.boss_hp_rect_out.centerx = self.screen_rect.centerx
        self.boss_hp_rect_in.x = self.boss_hp_rect_out.x + 5
        self.boss_hp_rect_out.top = self.screen_rect.top + 30
        self.boss_hp_rect_in.centery = self.boss_hp_rect_out.centery

        """Экран победы"""
        self.image_win = self.font_2.render("YOU WIN", False, self.title_color)
        self.image_win_rect = self.image_win.get_rect()
        self.image_win_rect.centery = self.screen_rect.centery - 30
        self.image_win_rect.centerx = self.screen_rect.centerx

        if self.statistics.shoots != 0:
            self.image_score_1 = self.font_1.render(f'Your score is {score(self.statistics)}', False, self.title_color)
            self.image_score_1_rect = self.image_score_1.get_rect()
            self.image_score_1_rect.centery = self.screen_rect.centery + 30
            self.image_score_1_rect.centerx = self.screen_rect.centerx

        self.image_exit = self.font_1.render("press Space to exit", False, self.title_color)
        self.image_exit_rect = self.image_exit.get_rect()
        self.image_exit_rect.centery = self.screen_rect.centery + 80
        self.image_exit_rect.centerx = self.screen_rect.centerx

        """Экран поражения"""
        self.image_lose = self.font_2.render("YOU LOSE", False, self.title_color)
        self.image_lose_rect = self.image_lose.get_rect()
        self.image_lose_rect.centery = self.screen_rect.centery - 30
        self.image_lose_rect.centerx = self.screen_rect.centerx

        self.image_cont = self.font_1.render("press Space to try again", False, self.title_color)
        self.image_cont_rect = self.image_cont.get_rect()
        self.image_cont_rect.centery = self.screen_rect.centery + 30
        self.image_cont_rect.centerx = self.screen_rect.centerx

    def show(self):
        """Добавляет информацию на экран (отрисовывает интерфейс)"""
        if self.statistics.lose is False:
            if self.statistics.win is False:
                self.screen.blit(self.image_hp, self.image_hp_rect)
                self.screen.blit(self.image_missiles, self.image_missiles_rect)
                self.screen.blit(self.image_score, self.image_score_rect)

            if self.statistics.wave_nuber != 5:
                self.screen.blit(self.image_wave, self.image_wave_rect)
            elif self.statistics.boss_hp > 0:
                pygame.draw.rect(self.screen, self.color_out, self.boss_hp_rect_out)
                pygame.draw.rect(self.screen, self.color_in, self.boss_hp_rect_in)
            if self.statistics.win:
                self.screen.blit(self.image_win, self.image_win_rect)
                if self.statistics.title_cooldown < 70 and self.statistics.shoots != 0:
                    self.screen.blit(self.image_score_1, self.image_score_1_rect)
                if self.statistics.exit:
                    self.screen.blit(self.image_exit, self.image_exit_rect)
        else:
            self.screen.blit(self.image_lose, self.image_lose_rect)
            if self.statistics.title_cooldown < 0:
                self.screen.blit(self.image_cont, self.image_cont_rect)
