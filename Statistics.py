class Statistics:

    def __init__(self):
        """ Инициализация статистики (информация о состоянии игры) """
        self.misses, self.shoots = 0, 0
        self.missiles_left = 3
        self.refuel_cooldown = 200
        self.score = 0
        self.wave_nuber = 0
        self.hp = 2
        self.boss_hp = 50
        self.cooldown = 120
        self.title_cooldown = 180
        self.win, self.exit = False, False
        self.lose = False
