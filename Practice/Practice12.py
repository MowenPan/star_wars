import sys

import pygame

from Practice.leo import Leo


def show_screen():
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('雷欧奥特曼')

    leo = Leo(screen)

    #  开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #  让最近绘制的屏幕可见
        screen.fill((72, 61, 139))
        leo.show_leo()
        pygame.display.flip()

show_screen()