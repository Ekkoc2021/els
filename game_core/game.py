#game1 为竞技模式的模块,包含用竞技模式的主函数 game1()
import random
import sys
import pygame
from pygame import *
from draw.initWindow import iniTdraw, drawButton
from game_core.core.allclass.blockClass import Block_1, Block_2, Block_5, Block_3, Block_7

'''
游戏界面:
进入游戏:传入一个颜色列表
'''
font_s="C:\Windows\Fonts\STXINWEI.TTF"
isPAUSE=1
isQuit=2
isSETTING=3
isOver=4

def randomBlock():
    i=random.randint(0,4)
    if i==0:
        return Block_1(random.randint(0,100))
    if i==1:
        return Block_2(random.randint(0,100))
    if i==2:
        return Block_5(random.randint(0,100))
    if i==3:
        return Block_3(random.randint(0,100))
    if i==4:
        return Block_7(random.randint(0,100))
def playing(screen, colorsOp, grade, gameD):
    #todo:grade形式参数已经失效
    #-----------------------------------
    allcolors= colorsOp[3][2]
    # ['2022-10-05 20:50:42', 0, [None, None]]
    queue=gameD.gameData[0][2]
    if queue[0]==None:
        queue[0]=randomBlock()
        queue[1]=randomBlock()
        queue[2]=randomBlock()
    fps=100
    #----------------------------------

    print(queue[0]==None)



    fpsClock = pygame.time.Clock()
    speed=0.05
    dirc=0
    while True:
        grade = gameD.gameData[0][1]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                # print(event.pos)
                # drawButton(screen, "暂停", colors[0], (470, 15, 55, 25), bFont)
                # drawButton(screen, "退出", colors[1], (545, 15, 55, 25), bFont)
                # drawButton(screen, "设置", colors[2], (615, 15, 55, 25), bFont)
                if 470 <= event.pos[0] <= 525 and 15 <= event.pos[1] <= 40:
                    colorsOp[0] = 0
                else:
                    colorsOp[0] = 1
                if 545 <= event.pos[0] <= 600 and 15 <= event.pos[1] <= 40:
                    colorsOp[1] = 0
                else:
                    colorsOp[1] = 1
                if 615 <= event.pos[0] <= 670 and 15 <= event.pos[1] <= 40:
                    colorsOp[2] = 0
                else:
                    colorsOp[2] = 1
            elif event.type == MOUSEBUTTONDOWN:
                if 470 <= event.pos[0] <= 525 and 15 <= event.pos[1] <= 40:
                    return isPAUSE
                if 545 <= event.pos[0] <= 600 and 15 <= event.pos[1] <= 40:
                    return isQuit
                if  615 <= event.pos[0] <= 670 and 15 <= event.pos[1] <= 40:
                    return isSETTING

            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    dirc=1
                    print("2,→/D:右移动")

                if event.key == K_LEFT or event.key == K_a:
                    dirc=-1
                    print("1,←/A:左移动")

                if event.key == K_UP or event.key == K_w:
                    # todo:完成方块顺时针旋转
                    queue[0].changeShape(gameD)
                    print("3,↑/W:顺时针旋转")

                if event.key == K_DOWN or event.key == K_s:
                    fps=1000000
                    print("4,↓/S:向下加速移动")
                if event.key == K_ESCAPE:
                    return isQuit
            elif event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    fps = 100
        iniTdraw(screen, colorsOp, grade)

        #-------
        #todo:方块提示1
        if gameD.gameData[0][3]>100:
            queue[1].drawBlock(screen, allcolors)
        else:
            gameD.gameData[0][3]+=1
        #todo:方块降落
            #todo:从队列中取出方块,
        #todo:在预告区预告第三个图形
        queue[2].drawInForeshow( screen, allcolors)
        queue[0].drawBlock(screen, allcolors)
        live=queue[0].blockMove(speed, gameD, dirc)
        if not live:#如果方块消亡,向queue中添加方块,并为方块重新赋值
            #todo:写入方块数据,同时获取新方块
            queue[0]. writeData(gameD)
            queue.append(randomBlock())
            gameD.gameData[0][3]=1
            queue.pop(0)
        dirc=0
        speed=0.04

        #todo:触底,方块生命周期结束将方块数据写入gameD上
                #3,绘制写入后的图像,图像返回值代表游戏结束与否
        gameD.Paint(screen, allcolors)
        pygame.display.update()
        #写完数据:第三行有方块就直接退出游戏
        if gameD.gameData[3][0]:
            return isOver
        if gameD.isWin():
            #todo:5,如果得分了重绘游戏区域
            iniTdraw(screen, colorsOp,gameD.gameData[0][1])
            gameD.Paint(screen, allcolors)
        #得分重绘后如果第4行有数据直接退出游戏
        if gameD.gameData[4][0]:
            return isOver
        #-----------
        pygame.display.update()
        fpsClock.tick(fps)

def pause(screen, colorsOp, grade, gameD):
    #todo:grade形式参数已经失效
    #----------
    grade=gameD.gameData[0][1]
    allcolors = colorsOp[3][2]
    queue=gameD.gameData[0][2]
    sp=gameD.gameData[0][3]
    #-------------
    colorsOp[0]=1
    # print("pause")
    button_c_op=[1,1]
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
            #----------------------
            gameD.Paint(screen, allcolors)
            if sp > 100 and queue[1] is not None:
                queue[1].drawBlock(screen, allcolors)
            #------------------------------------
            if  queue[0] is not None:
                queue[0].drawBlock(screen, allcolors)
            drawButton(screen, "退出游戏", button_c_op[0], (250, 284, 200, 50), bFont)
            drawButton(screen, "继续游戏", button_c_op[1], (250, 370, 200, 50), bFont)
            pygame.display.update()

def setting(screen, colorsOp, grade,gameD):#colors的第5个元素是代表所有的颜色
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    #  colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    # //我以为colorOp的第5个元素是代表所有的颜色,实际是initc的第三个元素,也就是colorop的第四个的第三个
    # setting(screen, colorsOp, grade)
    # print(colorsOp[3][2][1])
    #todo:grade形式参数已经失效
    #----------
    grade=gameD.gameData[0][1]
    queue=gameD.gameData[0][2]
    #----------



    colorsOp[2]=1#设置的颜色恢复白色
    allcolor=colorsOp[3][2]
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
    allcolor = colorsOp[3][2]
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
                    screenBgTemp += 1
                    if screenBgTemp >= allcolorLength:
                        screenBgTemp = 0
                if  (250 <= event.pos[0] <= 455 and 300 <= event.pos[1] <= 350):
                    playingBgTemp += 1
                    if playingBgTemp >= allcolorLength:
                        playingBgTemp = 0
                if (250 <= event.pos[0] <= 455 and 370 <= event.pos[1] <= 420):
                    # initColors = [allcolor[36], allcolor[97]]  # 背景颜色,操作界面颜色
                    # colorsOp = [1, 1, 1, initColors, allcolor]
                    colorsOp[3][0]=allcolor[playingBgTemp]
                    colorsOp[3][1]=allcolor[screenBgTemp]
                    return
                if (250 <= event.pos[0] <= 455 and 440 <= event.pos[1] <= 490):
                    return

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # 玩家按下了esc键,退出游戏
                    return isQuit
            iniTdraw(screen, colorsOp, grade)
            gameD.Paint(screen,allcolor)
            if gameD.gameData[0][3] > 100 and queue[1] is not None:
                queue[1].drawBlock(screen, allcolor)
            if gameD.gameData[0][2][0] is not None:
                gameD.gameData[0][2][0].drawBlock(screen, allcolor)
            bfont = pygame.freetype.Font(font_s, 15)
            drawButton2(screen, "  操作界面颜色", allcolor[screenBgTemp], (250, 230, 205, 50))
            drawButton2(screen, "  游戏背景颜色", allcolor[playingBgTemp], (250, 300, 205, 50))
            drawButton2(screen, "      保存设置 ", c2[save], (250, 370, 205, 50))
            drawButton2(screen, "          取消 ", c2[cancel], (250, 440, 205, 50))
            if tipLocation[2]:
                pygame.draw.rect(screen, (255,255,255),(tipLocation[0],tipLocation[1],220,17),border_radius=4)
                bfont.render_to(screen, (tipLocation[0],tipLocation[1]+2), "Tip:点击按钮进行更换背景颜色", (0, 0, 0), 0)
            pygame.display.update()

def drawButton2(screen,lable,color,Loc_Dim):
    bfont = pygame.freetype.Font(font_s, 30)
    pygame.draw.rect(screen, color, Loc_Dim,border_radius=7)
    pygame.draw.rect(screen, (0, 0, 0), Loc_Dim, 1, border_radius=7)
    bfont.render_to(screen, (Loc_Dim[0], Loc_Dim[1]+9), lable, (0, 0, 0), 0)


def game_1(initColors, gameD):#传入一个界面颜色,游戏操作界面颜色,所有颜色,游戏数据
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    colorsOp = [1, 1, 1, initColors]#前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    while True:
        #----------------------每次都这样获取可能影响效率,可以只有在win时,才能获取分数,冲洗赋值
        grade = gameD.gameData[0][1]
        # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
        # colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
        Op=playing(screen, colorsOp, grade, gameD)
        if Op==isPAUSE:
            if pause(screen, colorsOp , grade, gameD)==isQuit:
                #todo:保存游戏,这里的退出是暂停后的退出
                print("保存游戏,然后退出")
                return
        elif Op==isQuit:
            # todo:保存游戏,这里的退出是游戏结束,或者playing界面的退出
            print("保存游戏,然后退出")
            return
        elif Op==isSETTING:
            setting(screen, colorsOp, grade, gameD)
        elif Op==isOver:
            print("游戏结束了,保存分数然后退出游戏")
            return

