class Settings:
    """存储游戏所有设置"""
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 设置飞船的速度
        self.ship_speed_factor = 1.5

        # 设置子弹的属性
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 6

        # 设置外星人的属性
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_directions = 1
