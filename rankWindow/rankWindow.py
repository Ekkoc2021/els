'''
读取数据时的等待窗口
'''
import sys

import pygame
from pygame import QUIT
from data_io.input_data import input_gamedata
from gameWindow.game1 import game_1


def rankWindows(initColors):
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    Font = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 72)
    Font.render_to(screen, (150, 345), "读取游戏中..", (0, 0, 0), 0)
    pygame.display.flip()

    #读取成功
    gamedata=input_gamedata()
    if gamedata is not None:
        game_1(initColors)
    else :
        #读取失败
        screen.fill(initColors[0])
        Font = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 72)
        Font.render_to(screen, (150, 240), "文件数据错误", (0, 0, 0), 0)
        Font.render_to(screen, (200, 345), "读取失败!", (0, 0, 0), 0)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    # 玩家强制结束游戏

                    # todo:保存游戏数据然后再退出:用户名称+当前游戏数据矩阵
                    pygame.quit()
                    sys.exit()