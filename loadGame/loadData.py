'''
读取数据时的等待窗口
'''
import random
import sys

import pygame
from pygame import QUIT, MOUSEBUTTONDOWN, MOUSEMOTION, KEYDOWN, K_ESCAPE
from data_io.input_data import input_gamedata, input_rank
from data_io.output_data import output_gamedata
from game_core.core.allclass.coreData import GameData

'''
检查读取到的数据
'''
def identity(gamedata):
    try:
        if gamedata!=None and type(gamedata).__name__=="list":
            for i in range(200):
                if type(gamedata[random.randint(1,17)][0]).__name__!="bool" \
                        and type(gamedata[random.randint(1,17)][random.randint(1,8)][0]).__name__!="bool" \
                        and type(gamedata[random.randint(1, 17)][random.randint(1, 8)][1]).__name__ != "list" :
                    return False
            return True
        else :
            return False
    except:
        return False
'''
从硬盘上加载数据
'''
def loadGameW(initColors):
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    Font = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 72)
    Font.render_to(screen, (150, 345), "读取游戏中..", (0, 0, 0), 0)
    pygame.display.flip()
    gamedata = input_gamedata()
    # output_gamedata(GameData().gamedate)
    #读取成功
    if identity(gamedata):#检查数据
        return gamedata
    else :
        #读取失败
        button_c = 1
        Font2 = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 50)  # 按钮字体大小
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    # 玩家强制结束游戏
                    # todo:保存游戏数据然后再退出:用户名称+当前游戏数据矩阵
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEMOTION:
                    if 5 <= event.pos[0] <= 130 and 10 <= event.pos[1] <= 50:
                        button_c = 0
                    else:
                        button_c = 1
                elif event.type == MOUSEBUTTONDOWN:
                    if 5 <= event.pos[0] <= 130 and 10 <= event.pos[1] <= 50:
                        return None
            screen.fill(initColors[0])
            drawButton(screen, "返 回", button_c, (5, 10, 130, 50), Font2)
            Font = pygame.freetype.Font("C:\Windows\Fonts\simkai.ttf", 72)
            Font.render_to(screen, (150, 240), "文件数据错误", (0, 0, 0), 0)
            Font.render_to(screen, (200, 345), "读取失败!", (0, 0, 0), 0)
            pygame.display.update()


def loadRankW(initColors):
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    Font = pygame.freetype.Font("C:\Windows\Fonts\STXINGKA.TTF", 72)#基础大小
    Font2 = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 50)#按钮字体大小
    Font3 = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 40)#排名字体大小
    Font4 = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 30)  # 排名字体大小
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
            Font3.render_to(screen, (150, 110), "      日期                 分数", (0, 0, 0), 0)
            x = 0
            for i in l:
                Font4.render_to(screen, (150, 160 + x * 50), str(x+1)+":"+i[0] + ":  " + str(i[1]), (0, 0, 0), 0)
                x += 1
        else:
            Font.render_to(screen, (150, 240), "文件数据错误", (0, 0, 0), 0)
            Font.render_to(screen, (200, 345), "读取失败!", (0, 0, 0), 0)

        pygame.display.update()

def drawButton(screen,lable,color,Loc_Dim,bfont):
    if color==1:
        pygame.draw.rect(screen, (255,255,255), Loc_Dim,border_radius=8)
    else:
        pygame.draw.rect(screen, (128, 128, 128), Loc_Dim,border_radius=8)
    pygame.draw.rect(screen, (0,0,0), Loc_Dim, 1,border_radius=8)
    bfont.render_to(screen, (Loc_Dim[0]+6, Loc_Dim[1]+2), lable, (0, 0, 0), 0)