'''
选择窗口
'''
# 竞技模式选择窗口
import sys
import pygame
from pygame import *


# 模式选择窗口
from data_io.input_data import input_rank
from draw.initWindow import drawButton

def choose1(bgColor):
    screen = pygame.display.set_mode((700, 760))
    screen.fill(bgColor)
    button_c = [1, 1, 1]
    Font = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 72)
    tytleFont = pygame.freetype.Font("C:\Windows\Fonts\STHUPO.TTF", 100)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                # 200,240,300,70
                # print(event.pos)
                if 200 <= event.pos[0] <= 500 and 240 <= event.pos[1] <= 310:
                    button_c[0] = 0
                else:
                    button_c[0] = 1
                # 200, 345, 300, 70
                if 200 <= event.pos[0] <= 500 and 345 <= event.pos[1] <= 415:
                    button_c[1] = 0
                else:
                    button_c[1] = 1
                # 200, 450, 300, 70
                if 200 <= event.pos[0] <= 500 and 450 <= event.pos[1] <= 520:
                    button_c[2] = 0
                else:
                    button_c[2] = 1
            elif event.type == MOUSEBUTTONDOWN:
                if 200 <= event.pos[0] <= 500 and 240 <= event.pos[1] <= 310:
                    return 1
                # 200, 345, 300, 70
                if 200 <= event.pos[0] <= 500 and 345 <= event.pos[1] <= 415:
                    return 2
                # 200, 450, 300, 70
                if 200 <= event.pos[0] <= 500 and 450 <= event.pos[1] <= 520:
                    return 3
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return 3
        screen.fill(bgColor)
        tytleFont.render_to(screen, (100, 70), "俄罗斯方块", (0, 0, 0), 0)
        # def drawButton(screen,lable,color,Loc_Dim,bfont):
        drawButton(screen, "竞技模式", button_c[0], (200, 240, 300, 70), Font)
        drawButton(screen, "创造模式", button_c[1], (200, 345, 300, 70), Font)
        drawButton(screen, "    退出", button_c[2], (200, 450, 300, 70), Font)
        pygame.display.update()

# 竞技模式选择窗口:新游戏,继续游戏,排名,退出
def choose2(bgColor):
    screen = pygame.display.set_mode((700, 760))
    screen.fill(bgColor)
    Font = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 72)
    tytleFont=pygame.freetype.Font("C:\Windows\Fonts\STHUPO.TTF", 100)
    button_c = [1, 1, 1, 1]
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                # 200,240,300,70
                # print(event.pos)
                if 200 <= event.pos[0] <= 500 and 240 <= event.pos[1] <= 310:
                    button_c[0] = 0
                else:
                    button_c[0] = 1
                # 200, 345, 300, 70
                if 200 <= event.pos[0] <= 500 and 345 <= event.pos[1] <= 415:
                    button_c[1] = 0
                else:
                    button_c[1] = 1
                # 200, 450, 300, 70
                if 200 <= event.pos[0] <= 500 and 450 <= event.pos[1] <= 520:
                    button_c[2] = 0
                else:
                    button_c[2] = 1
                if 200 <= event.pos[0] <= 500 and 545 <= event.pos[1] <= 615:
                    button_c[3] = 0
                else:
                    button_c[3] = 1
            elif event.type == MOUSEBUTTONDOWN:
                # 新游戏
                if 200 <= event.pos[0] <= 500 and 240 <= event.pos[1] <= 310:
                    return 1
                # 200, 345, 300, 70 继续游戏
                if 200 <= event.pos[0] <= 500 and 345 <= event.pos[1] <= 415:
                    return 2
                # 200, 450, 300, 70 排名
                if 200 <= event.pos[0] <= 500 and 450 <= event.pos[1] <= 520:
                    return 4
                # 200, 545, 300, 70 退出
                if 200 <= event.pos[0] <= 500 and 545 <= event.pos[1] <= 615:
                    return 5
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return 5
        screen.fill(bgColor)
        tytleFont.render_to(screen, (100, 70), "俄罗斯方块", (0, 0, 0), 0)
        # def drawButton(screen,lable,color,Loc_Dim,bfont):
        drawButton(screen, "  新游戏", button_c[0], (200, 240, 300, 70), Font)
        drawButton(screen, "继续游戏", button_c[1], (200, 345, 300, 70), Font)
        drawButton(screen, "    排名", button_c[2], (200, 450, 300, 70), Font)
        drawButton(screen, "    退出", button_c[3], (200, 545, 300, 70), Font)
        pygame.display.update()
