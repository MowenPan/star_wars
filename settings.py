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
