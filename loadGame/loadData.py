'''
读取数据时的等待窗口
'''
import sys

import pygame
from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, KEYDOWN, K_ESCAPE
from data_io.input_data import input_gamedata, input_rank
from gameWindow.game1 import game_1


def loadGameW(initColors):
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




def loadRankW(initColors):
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    Font = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 72)#基础大小
    Font2 = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 50)#按钮字体大小
    Font3 = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 40)#排名字体大小
    Font.render_to(screen, (150, 345), "读取排名中..", (0, 0, 0), 0)
    pygame.display.flip()
    l=input_rank()
    isRead=True
    if l is None:
        isRead=False
    button_c=1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if 5 <= event.pos[0] <= 130 and 10 <= event.pos[1] <= 50:
                    button_c = 0
                else:
                    button_c = 1
            elif event.type == MOUSEBUTTONDOWN:
                if 5 <= event.pos[0] <= 130 and 10 <= event.pos[1] <= 50:
                    return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
        screen.fill(initColors[0])
        drawButton(screen,"返 回",button_c,(5,10,130,50),Font2)
        if isRead:
            Font.render_to(screen, (150, 20), "最新排名", (0, 0, 0), 0)
            pygame.draw.rect(screen, (225, 115, 115), (140, 90, 440, 600))
            Font3.render_to(screen, (150, 110), "    日期       分数", (0, 0, 0), 0)
            x = 0
            for i in l:
                Font3.render_to(screen, (150, 150 + x * 40), i[0] + ":" + str(i[1]), (0, 0, 0), 0)
                x += 1
        else:
            Font.render_to(screen, (150, 240), "文件数据错误", (0, 0, 0), 0)
            Font.render_to(screen, (200, 345), "读取失败!", (0, 0, 0), 0)

        pygame.display.update()

def drawButton(screen,lable,color,Loc_Dim,bfont):
    if color==1:
        pygame.draw.rect(screen, (255,255,255), Loc_Dim)
    else:
        pygame.draw.rect(screen, (128, 128, 128), Loc_Dim)
    bfont.render_to(screen, (Loc_Dim[0]+6, Loc_Dim[1]+2), lable, (0, 0, 0), 0)