#game1 为竞技模式的模块,包含用竞技模式的主函数 game1()
import sys
import pygame
from pygame import *
from draw.initWindow import iniTdraw, drawButton

'''
游戏界面:
进入游戏:传入一个颜色列表
'''
font_s="C:\Windows\Fonts\simkai.ttf"
isPAUSE=1
isQuit=2
isSETTING=3
ALLCOLORS=[]
def playing(screen,button_c,grade,gamedata):
    fpsClock = pygame.time.Clock()
    speed=0
    print("playing")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if 40 <= event.pos[0] <= 95 and 5 <= event.pos[1] <= 30:
                    button_c[0] = 0
                else:
                    button_c[0] = 1
                if 105 <= event.pos[0] <= 160 and 5 <= event.pos[1] <= 30:
                    button_c[1] = 0
                else:
                    button_c[1] = 1
                if 170 <= event.pos[0] <= 225 and 5 <= event.pos[1] <= 30:
                    button_c[2] = 0
                else:
                    button_c[2] = 1
            elif event.type == MOUSEBUTTONDOWN:
                if 40 <= event.pos[0] <= 95 and 5 <= event.pos[1] <= 30:
                    return isPAUSE
                if 105 <= event.pos[0] <= 160 and 5 <= event.pos[1] <= 30:
                    return isQuit
                if 170 <= event.pos[0] <= 225 and 5 <= event.pos[1] <= 30:
                    print("设置")
                    return isSETTING

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    # todo:完成方块右移动
                    print("2,→/D:右移动")

                if event.key == K_LEFT or event.key == K_a:
                    # todo:完成方块左移动
                    print("1,←/A:左移动")

                if event.key == K_UP or event.key == K_w:
                    # todo:完成方块顺时针旋转
                    print("3,↑/W:顺时针旋转")

                if event.key == K_DOWN or event.key == K_s:
                    # todo:方块向下加速
                    print("4,↓/S:向下加速移动")

                if event.key == K_ESCAPE:
                    return isQuit
        iniTdraw(screen, button_c, grade)

        # 测试:方块下落----------------------------------------------------------------
        pygame.draw.rect(screen, (255, 255, 255), (120, 80 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 120 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 160 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 200 + speed * 40, 40, 40))
        pygame.draw.rect(screen, (255, 255, 255), (120, 240 + speed * 40, 40, 40))
        pygame.draw.line(screen, (0, 0, 0), (120, 80 + 40 + speed * 40), (160, 80 + 40 + speed * 40), 1)
        pygame.draw.line(screen, (0, 0, 0), (120, 120 + 40 + speed * 40), (160, 120 + 40 + speed * 40), 1)
        pygame.draw.line(screen, (0, 0, 0), (120, 160 + 40 + speed * 40), (160, 160 + 40 + speed * 40), 1)
        pygame.draw.line(screen, (0, 0, 0), (120, 200 + 40 + speed * 40), (160, 200 + 40 + speed * 40), 1)
        speed += 0.05
        pygame.display.update()
        fpsClock.tick(100)

def pause(screen, colorsOp, grade):
    colorsOp[0]=1
    # print("pause")
    button_c_op=[1,1]
    fpsClock = pygame.time.Clock()
    bFont = pygame.freetype.Font(font_s, 48)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if 250 <= event.pos[0] <= 450 and 284 <= event.pos[1] <= 334:
                    button_c_op[0] = 0
                else:
                    button_c_op[0] = 1
                if 250 <= event.pos[0] <= 450 and 370 <= event.pos[1] <= 420:
                    button_c_op[1] = 0
                else:
                    button_c_op[1] = 1
            elif event.type == MOUSEBUTTONDOWN:
                if 250 <= event.pos[0] <= 450 and 284 <= event.pos[1] <= 334:
                    return isQuit
                if 250 <= event.pos[0] <= 450 and 370 <= event.pos[1] <= 420:
                    return 1000

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # 玩家按下了esc键,退出游戏
                    return isQuit
            iniTdraw(screen, colorsOp, grade)
            #todo:这里暂停界面还差游戏数据部分的图没有绘制
            drawButton(screen, "退出游戏", button_c_op[0], (250, 284, 200, 50), bFont)
            drawButton(screen, "继续游戏", button_c_op[1], (250, 370, 200, 50), bFont)
            pygame.display.update()

def setting(screen, colorsOp, grade):#colors的第5个元素是代表所有的颜色
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    #  colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    # //我以为colorOp的第5个元素是代表所有的颜色,实际是initc的第三个元素,也就是colorop的第四个的第三个
    # setting(screen, colorsOp, grade)
    # print(colorsOp[3][2][1])
    colorsOp[2]=1#设置的颜色恢复白色
    allcolor=colorsOp[3][2]
    print("setting")
    allcolorLength=len(allcolor)
    playingBg=0
    for i in allcolor:
        if i[0] == colorsOp[3][0][0] and i[1] == colorsOp[3][0][1] and i[2] == colorsOp[3][0][2]:
            break
        playingBg+=1
    screenBg=0
    for i in allcolor:
        if i[0] == colorsOp[3][1][0] and i[1] == colorsOp[3][1][1] and i[2] == colorsOp[3][1][2]:
            break
        screenBg += 1

    #提升作用域
    playingBgTemp = playingBg
    screenBgTemp = screenBg
    #提示
    tipLocation=[0,0,False]
    #保存取消按键的不同状态下的颜色
    c2=[(128,128,128),(255,255,255)]
    save=1
    cancel=1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (250 <= event.pos[0] <= 455 and 230 <= event.pos[1] <= 280) \
                        or(250 <= event.pos[0] <= 455 and 300 <= event.pos[1] <=350 ):
                    #提示
                   tipLocation[2] = True
                   tipLocation[0]=event.pos[0]
                   tipLocation[1]=event.pos[1]+10
                else:
                    tipLocation[2] =False

                # 250, 370, 205, 50
                # 250, 440, 205, 50
                if (250 <= event.pos[0] <= 455 and 370 <= event.pos[1] <= 420) :
                    save=0
                else:
                    save=1
                if (250 <= event.pos[0] <= 455 and 440 <= event.pos[1] <= 490) :
                    cancel=0
                else:
                    cancel=1
            elif event.type == MOUSEBUTTONDOWN:
                if (250 <= event.pos[0] <= 455 and 230 <= event.pos[1] <= 280) :
                    playingBgTemp += 1
                    if playingBgTemp>=allcolorLength:
                        playingBgTemp=0
                if  (250 <= event.pos[0] <= 455 and 300 <= event.pos[1] <= 350):
                    screenBgTemp += 1
                    if screenBgTemp >= allcolorLength:
                        screenBgTemp = 0
                if (250 <= event.pos[0] <= 455 and 370 <= event.pos[1] <= 420):
                    # initColors = [allcolor[36], allcolor[97]]  # 背景颜色,操作界面颜色
                    # colorsOp = [1, 1, 1, initColors, allcolor]
                    colorsOp[3][0]=allcolor[screenBgTemp]
                    colorsOp[3][1]=allcolor[playingBgTemp]
                    return
                if (250 <= event.pos[0] <= 455 and 440 <= event.pos[1] <= 490):
                    return

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # 玩家按下了esc键,退出游戏
                    return isQuit
            iniTdraw(screen, colorsOp, grade)
            #todo:这里暂停界面还差游戏数据部分的图没有绘制
            bfont = pygame.freetype.Font(font_s, 15)
            drawButton2(screen, "操作界面颜色", allcolor[playingBgTemp], (250, 230, 205, 50))
            drawButton2(screen, "游戏背景颜色", allcolor[screenBgTemp], (250, 300, 205, 50))
            drawButton2(screen, "    保存 ", c2[save], (250, 370, 205, 50))
            drawButton2(screen, "    取消 ", c2[cancel], (250, 440, 205, 50))
            if tipLocation[2]:
                pygame.draw.rect(screen, (255,255,255),(tipLocation[0],tipLocation[1],220,15) )
                bfont.render_to(screen, tipLocation, "Tip:点击按钮进行更换背景颜色", (0, 0, 0), 0)
            pygame.display.update()

def drawButton2(screen,lable,color,Loc_Dim):
    bfont = pygame.freetype.Font(font_s, 34)
    pygame.draw.rect(screen, color, Loc_Dim)
    bfont.render_to(screen, (Loc_Dim[0], Loc_Dim[1]+9), lable, (0, 0, 0), 0)


def game_1(initColors, gameData):#传入一个界面颜色,游戏操作界面颜色,所有颜色,游戏数据
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    grade = 0
    colorsOp = [1, 1, 1, initColors]#前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    while True:
        Op=playing(screen, colorsOp,grade,gameData)
        if Op==isPAUSE:
            if pause(screen,colorsOp ,grade)==isQuit:
                #todo:保存游戏,这里的退出是暂停后的退出
                print("保存游戏,然后退出")
                return
        elif Op==isQuit:
            # todo:保存游戏,这里的退出是游戏结束,或者playing界面的退出
            print("保存游戏,然后退出")
            return
        elif Op==isSETTING:
            #todo:设置
            setting(screen,colorsOp,grade)
            print("设置?还没做好啊")
