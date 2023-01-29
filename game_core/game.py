#game1 为竞技模式的模块,包含用竞技模式的主函数 game1()
import random
import sys
import pygame
from pygame import *

from data_io.input_data import input_rank
from data_io.output_data import output_gamedata, output_rank, output_setting
from draw.initWindow import iniTdraw, drawButton
from game_core.core.allclass.Factory import blockFactory
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
continueGame=5

def isNewRecord(gameD):
    # print("游戏结束了,保存分数然后退出游戏")
    isInsert=False
    rank = input_rank()
    # 对比游戏排名
    # ['2022-10-06 16:57:41', 0, [None, None]]
    s = [gameD.gameData[0][0], gameD.gameData[0][1]]
    if rank is None:
        rank = [s]
        isInsert=True
    else:
        x = 0
        while x < len(rank):
            if s[1] > rank[x][1]:
                rank.insert(x, s)
                isInsert = True
                break
            x += 1
        if not isInsert:
            if x < 9:
                rank.append(s)
                isInsert=True
        if len(rank) > 10:
            rank.pop(10)
    output_rank(rank)
    # 重置gameD的数据
    return isInsert

def GameOver(screen, colorsOp,gameD):#colors的第5个元素是代表所有的颜色
    #----------
    grade=gameD.gameData[0][1]
    queue=gameD.gameData[0][2]
    #----------
    isNewReco=isNewRecord(gameD)
    c2=[(128,128,128),(255,255,255)]
    cancel=1
    allcolor = colorsOp[3][2]
    tytleFont = pygame.freetype.Font("C:\Windows\Fonts\STHUPO.TTF", 100)
    Font2 = pygame.freetype.Font("C:\Windows\Fonts\STHUPO.TTF", 70)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (250 <= event.pos[0] <= 455 and 350<= event.pos[1] <= 400) :
                    cancel=0
                else:
                    cancel=1
            elif event.type == MOUSEBUTTONDOWN:
                if 250 <= event.pos[0] <= 455 and 350 <= event.pos[1] <= 400:
                    gameD.ReSetGameData()
                    return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
        iniTdraw(screen, colorsOp, grade)
        gameD.Paint(screen,allcolor)
        if gameD.gameData[0][3] > 100 and queue[1] is not None:
            queue[1].drawBlock(screen, allcolor)
        if gameD.gameData[0][2][0] is not None:
            gameD.gameData[0][2][0].drawBlock(screen, allcolor)
        if queue[2] is not None:
            queue[2].drawInForeshow(screen, allcolor)
        if isNewReco:
            Font2.render_to(screen, (240, 250), "新排名!", (0, 0, 0), 0)
        tytleFont.render_to(screen, (140, 120), "游戏结束", (0, 0, 0), 0)
        drawButton2(screen, "          确定 ", c2[cancel], (250, 350, 205, 50))
        pygame.display.update()
def playing(screen, colorsOp, gameD,isPause):
    if isPause:
        return isPAUSE
    #-----------------------------------
    factory=blockFactory()
    allcolors= colorsOp[3][2]
    # ['2022-10-05 20:50:42', 0, [None, None]]
    queue=gameD.gameData[0][2]
    if queue[0]==None:
        queue[0]=factory.getRandomBlock(allcolors,colorsOp[3][1])
        queue[1]=factory.getRandomBlock(allcolors,colorsOp[3][1])
        queue[2]=factory.getRandomBlock(allcolors,colorsOp[3][1])
    fps=100
    #----------------------------------
    fpsClock = pygame.time.Clock()
    speed=gameD.gameData[0][4]
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
                    # print("2,→/D:右移动")

                if event.key == K_LEFT or event.key == K_a:
                    dirc=-1
                    # print("1,←/A:左移动")

                if event.key == K_UP or event.key == K_w:
                    # 完成方块旋转
                    queue[0].changeShape(gameD)
                    # print("3,↑/W:顺时针旋转")

                if event.key == K_DOWN or event.key == K_s:
                    fps=1000000
                    queue[0].blockMove(speed, gameD, dirc)
                    queue[0].blockMove(speed, gameD, dirc)
                    # print("4,↓/S:向下加速移动")
                if event.key == K_SPACE:
                    for i in range(400):
                        queue[0].blockMove(speed, gameD, dirc)
                if event.key == K_ESCAPE:
                    return isQuit
                if event.key == K_j:
                    return isSETTING
                if event.key ==K_p:
                    return isPAUSE
            elif event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    fps = 100
        iniTdraw(screen, colorsOp, grade)

        #-------
        #方块提示1
        if gameD.gameData[0][3]>120:
            queue[1].drawBlock(screen, allcolors)
        else:
            gameD.gameData[0][3]+=1
        #方块降落
            #从队列中取出方块,
        #在预告区预告第三个图形
        queue[2].drawInForeshow( screen, allcolors)
        queue[0].drawBlock(screen, allcolors)
        live=queue[0].blockMove(speed, gameD, dirc)
        if not live:#如果方块消亡,向queue中添加方块,并为方块重新赋值
            #写入方块数据,同时获取新方块
            queue[0]. writeData(gameD)
            queue.append(factory.getRandomBlock(allcolors,colorsOp[3][1]))
            gameD.gameData[0][3]=1
            queue.pop(0)
        dirc=0

        #触底,方块生命周期结束将方块数据写入gameD上
                #3,绘制写入后的图像,图像返回值代表游戏结束与否
        gameD.Paint(screen, allcolors)
        pygame.display.update()
        #写完数据:第三行有方块就直接退出游戏
        if gameD.gameData[3][0]:
            GameOver(screen, colorsOp, gameD)
            return isOver
        if gameD.isWin():
            #5,如果得分了重绘游戏区域
            iniTdraw(screen, colorsOp,gameD.gameData[0][1])
            gameD.Paint(screen, allcolors)
        #得分重绘后如果第4行有数据直接退出游戏
        if gameD.gameData[4][0]:
            GameOver(screen,colorsOp,gameD)
            return isOver
        #-----------
        pygame.display.update()
        fpsClock.tick(fps)

def pause(screen, colorsOp, gameD):
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
                    return continueGame

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
            if  queue[2] is not None:
                queue[2]. drawInForeshow(screen, allcolors)
            drawButton(screen, "退出游戏", button_c_op[0], (250, 284, 200, 50), bFont)
            drawButton(screen, "继续游戏", button_c_op[1], (250, 370, 200, 50), bFont)
            pygame.display.update()

def setting(screen, colorsOp,gameD):#colors的第5个元素是代表所有的颜色
    # todo 2022 : 所有数据格式设计得和shit一样! 我会考虑重构
    # 2023/1/29: 函数设计和shit一样,能跑就行,放弃重构!

    #这里colorOp的数据格式的设计相对复杂了点,对后续的代码书写难度加大了
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    #  colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    #我以为colorOp的第5个元素是代表所有的颜色,实际是initc的第三个元素,也就是colorop的第四个的第三个
    # setting(screen, colorsOp, grade)
    # print(colorsOp[3][2][1])
    #----------
    grade=gameD.gameData[0][1]
    queue=gameD.gameData[0][2]
    #----------

    colorsOp[2]=1#设置的颜色恢复白色
    allcolor=colorsOp[3][2]
    allcolorLength=len(allcolor)
    playingBg=0
    screenBg=0
    # playingbg 和 screenbg 这里命名好像弄反了,这个问题出现的原因是:设计不够规范
    for i in allcolor:
        if i[0] == colorsOp[3][0][0] and i[1] == colorsOp[3][0][1] and i[2] == colorsOp[3][0][2]:
            break
        playingBg+=1
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
                    output_setting(colorsOp[3])
                    return
                if (250 <= event.pos[0] <= 455 and 440 <= event.pos[1] <= 490):
                    return

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return isQuit
            # 对背景进行绘制
            iniTdraw(screen, colorsOp, grade)
            gameD.Paint(screen,allcolor)
            if gameD.gameData[0][3] > 100 and queue[1] is not None:
                queue[1].drawBlock(screen, allcolor)
            if gameD.gameData[0][2][0] is not None:
                gameD.gameData[0][2][0].drawBlock(screen, allcolor)
            if  queue[2] is not None:
                queue[2]. drawInForeshow(screen, allcolor)

            # 显示设置对应的按钮
            bfont = pygame.freetype.Font(font_s, 15)
            drawButton2(screen, "  操作界面颜色", allcolor[screenBgTemp], (250, 230, 205, 50))
            drawButton2(screen, "  游戏背景颜色", allcolor[playingBgTemp], (250, 300, 205, 50))
            drawButton2(screen, "      保存设置 ", c2[save], (250, 370, 205, 50))
            drawButton2(screen, "          取消 ", c2[cancel], (250, 440, 205, 50))
            if tipLocation[2]:
                pygame.draw.rect(screen, (255,255,255),(tipLocation[0],tipLocation[1],220,17),border_radius=4)
                bfont.render_to(screen, (tipLocation[0],tipLocation[1]+2), "Tip:点击按钮进行更换背景颜色", (0, 0, 0), 0)
            pygame.display.update()


def setting2(screen, colorsOp):
    # 这里colorOp的数据格式相对复杂了点,对后续的代码书写难度加大了
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    #  colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    # 我以为colorOp的第5个元素是代表所有的颜色,实际是initc的第三个元素,也就是colorop的第四个的第三个
    # setting(screen, colorsOp, grade)
    # print(colorsOp[3][2][1])
    # ----------
    tytleFont=pygame.freetype.Font("C:\Windows\Fonts\STHUPO.TTF", 100)
    colorsOp[2] = 1  # 设置的颜色恢复白色
    allcolor = colorsOp[3][2]
    allcolorLength = len(allcolor)
    playingBg = 0
    for i in allcolor:
        if i[0] == colorsOp[3][0][0] and i[1] == colorsOp[3][0][1] and i[2] == colorsOp[3][0][2]:
            break
        playingBg += 1
    screenBg = 0
    for i in allcolor:
        if i[0] == colorsOp[3][1][0] and i[1] == colorsOp[3][1][1] and i[2] == colorsOp[3][1][2]:
            break
        screenBg += 1

    screen.fill(colorsOp[3][0])
    # 提升作用域
    playingBgTemp = playingBg
    screenBgTemp = screenBg
    # 提示
    tipLocation = [0, 0, False]
    # 保存取消按键的不同状态下的颜色
    c2 = [(128, 128, 128), (255, 255, 255)]
    save = 1
    cancel = 1
    allcolor = colorsOp[3][2]
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (250 <= event.pos[0] <= 455 and 230 <= event.pos[1] <= 280) \
                        or (250 <= event.pos[0] <= 455 and 300 <= event.pos[1] <= 350):
                    # 提示
                    tipLocation[2] = True
                    tipLocation[0] = event.pos[0]
                    tipLocation[1] = event.pos[1] + 10
                else:
                    tipLocation[2] = False

                # 250, 370, 205, 50
                # 250, 440, 205, 50
                if (250 <= event.pos[0] <= 455 and 370 <= event.pos[1] <= 420):
                    save = 0
                else:
                    save = 1
                if (250 <= event.pos[0] <= 455 and 440 <= event.pos[1] <= 490):
                    cancel = 0
                else:
                    cancel = 1
            elif event.type == MOUSEBUTTONDOWN:
                if (250 <= event.pos[0] <= 455 and 230 <= event.pos[1] <= 280):
                    screenBgTemp += 1
                    if screenBgTemp >= allcolorLength:
                        screenBgTemp = 0
                if (250 <= event.pos[0] <= 455 and 300 <= event.pos[1] <= 350):
                    playingBgTemp += 1
                    if playingBgTemp >= allcolorLength:
                        playingBgTemp = 0
                if (250 <= event.pos[0] <= 455 and 370 <= event.pos[1] <= 420):
                    # initColors = [allcolor[36], allcolor[97]]  # 背景颜色,操作界面颜色
                    # colorsOp = [1, 1, 1, initColors, allcolor]
                    colorsOp[3][0] = allcolor[playingBgTemp]
                    colorsOp[3][1] = allcolor[screenBgTemp]
                    output_setting(colorsOp[3])
                    return
                if (250 <= event.pos[0] <= 455 and 440 <= event.pos[1] <= 490):
                    return

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return isQuit
            # 对背景进行绘制
            screen.fill(colorsOp[3][0])
            tytleFont.render_to(screen, (100, 70), "俄罗斯方块", (0, 0, 0), 0)
            # 显示设置对应的按钮
            bfont = pygame.freetype.Font(font_s, 15)
            drawButton2(screen, "  操作界面颜色", allcolor[screenBgTemp], (250, 230, 205, 50))
            drawButton2(screen, "  游戏背景颜色", allcolor[playingBgTemp], (250, 300, 205, 50))
            drawButton2(screen, "      保存设置 ", c2[save], (250, 370, 205, 50))
            drawButton2(screen, "          取消 ", c2[cancel], (250, 440, 205, 50))
            if tipLocation[2]:
                pygame.draw.rect(screen, (255, 255, 255), (tipLocation[0], tipLocation[1], 220, 17), border_radius=4)
                bfont.render_to(screen, (tipLocation[0], tipLocation[1] + 2), "Tip:点击按钮进行更换背景颜色", (0, 0, 0), 0)
            pygame.display.update()


def drawButton2(screen,lable,color,Loc_Dim):
    bfont = pygame.freetype.Font(font_s, 30)
    pygame.draw.rect(screen, color, Loc_Dim,border_radius=7)
    pygame.draw.rect(screen, (0, 0, 0), Loc_Dim, 1, border_radius=7)
    bfont.render_to(screen, (Loc_Dim[0], Loc_Dim[1]+9), lable, (0, 0, 0), 0)

def game_1(initColors, gameD,isPuse):#传入一个界面颜色,游戏操作界面颜色,所有颜色,游戏数据
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    colorsOp = [1, 1, 1, initColors]#前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    ispuse = isPuse
    while True:
        # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
        # colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
        Op=playing(screen, colorsOp, gameD,ispuse)
        if Op==isPAUSE:
            Op2=pause(screen, colorsOp, gameD)
            if Op2==isQuit:
                # 保存游戏,游戏没有结束
                gameD.saveData()
                # 清除游戏数据,可以开始新游戏
                gameD.ReSetGameData()
                return
            elif Op2 == continueGame:
                ispuse = False
        elif Op==isQuit:
            #保存游戏,游戏没有结束
            gameD.saveData()
            # print("保存游戏,然后退出")
            gameD.ReSetGameData()
            return
        elif Op==isSETTING:
            setting(screen, colorsOp, gameD)
        elif Op==isOver:
            return
        elif Op==continueGame:
            ispuse=False

#--------------创造模式--
def GameOver_2(screen, colorsOp,gameD):#colors的第5个元素是代表所有的颜色
    #----------
    grade=gameD.gameData[0][1]
    queue=gameD.gameData[0][2]
    #----------
    c2=[(128,128,128),(255,255,255)]
    cancel=1
    allcolor = colorsOp[3][2]
    tytleFont = pygame.freetype.Font("C:\Windows\Fonts\STHUPO.TTF", 100)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                if (250 <= event.pos[0] <= 455 and 350<= event.pos[1] <= 400) :
                    cancel=0
                else:
                    cancel=1
            elif event.type == MOUSEBUTTONDOWN:
                if 250 <= event.pos[0] <= 455 and 350 <= event.pos[1] <= 400:
                    gameD.ReSetGameData()
                    return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
        iniTdraw(screen, colorsOp, grade)
        gameD.Paint(screen,allcolor)
        if gameD.gameData[0][3] > 100 and queue[1] is not None:
            queue[1].drawBlock(screen, allcolor)
        if gameD.gameData[0][2][0] is not None:
            gameD.gameData[0][2][0].drawBlock(screen, allcolor)
        if queue[2] is not None:
            queue[2].drawInForeshow(screen, allcolor)
        tytleFont.render_to(screen, (140, 120), "游戏结束", (0, 0, 0), 0)
        drawButton2(screen, "          确定 ", c2[cancel], (250, 350, 205, 50))
        pygame.display.update()

def playing_2(screen, colorsOp, gameD,isPause):
    if isPause:
        return isPAUSE
    #-----------------------------------
    allcolors= colorsOp[3][2]
    # ['2022-10-05 20:50:42', 0, [None, None]]
    factory=blockFactory()
    queue=gameD.gameData[0][2]
    if queue[0]==None:
        queue[0]=factory.getRandomBlock(allcolors,colorsOp[3][1])
        queue[1]=factory.getRandomBlock(allcolors,colorsOp[3][1])
        queue[2]=factory.getRandomBlock(allcolors,colorsOp[3][1])
    fps=100
    #----------------------------------
    fpsClock = pygame.time.Clock()
    speed=gameD.gameData[0][4]
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
                    # print("2,→/D:右移动")

                if event.key == K_LEFT or event.key == K_a:
                    dirc=-1
                    # print("1,←/A:左移动")

                if event.key == K_UP or event.key == K_w:
                    # 完成方块旋转
                    queue[0].changeShape(gameD)
                    # print("3,↑/W:顺时针旋转")

                if event.key == K_DOWN or event.key == K_s:
                    fps=1000000
                    queue[0].blockMove(speed, gameD, dirc)
                    queue[0].blockMove(speed, gameD, dirc)
                    # print("4,↓/S:向下加速移动")
                if event.key == K_SPACE:
                    for i in range(400):
                        queue[0].blockMove(speed, gameD, dirc)
                if event.key == K_ESCAPE:
                    return isQuit
                if event.key == K_j:
                    return isSETTING
                if event.key ==K_p:
                    return isPAUSE
                if event.key ==K_r:
                    queue.append(factory.getRandomBlock(allcolors,colorsOp[3][1]))
                    gameD.gameData[0][3] = 1
                    queue.pop(0)
            elif event.type == KEYUP:
                if event.key == K_DOWN or event.key == K_s:
                    fps = 100
        iniTdraw(screen, colorsOp, grade)

        #-------
        #方块提示1
        if gameD.gameData[0][3]>120:
            queue[1].drawBlock(screen, allcolors)
        else:
            gameD.gameData[0][3]+=1
        #方块降落
            #从队列中取出方块,
        #在预告区预告第三个图形
        queue[2].drawInForeshow( screen, allcolors)
        queue[0].drawBlock(screen, allcolors)
        live=queue[0].blockMove(speed, gameD, dirc)
        if not live:#如果方块消亡,向queue中添加方块,并为方块重新赋值
            #写入方块数据,同时获取新方块
            queue[0]. writeData(gameD)
            queue.append(factory.getRandomBlock(allcolors,colorsOp[3][1]))
            gameD.gameData[0][3]=1
            queue.pop(0)
        dirc=0

        #触底,方块生命周期结束将方块数据写入gameD上
                #3,绘制写入后的图像,图像返回值代表游戏结束与否
        gameD.Paint(screen, allcolors)
        pygame.display.update()
        #写完数据:第三行有方块就直接退出游戏
        if gameD.gameData[3][0]:
            GameOver_2(screen, colorsOp, gameD)
            return isOver
        if gameD.isWin():
            #5,如果得分了重绘游戏区域
            iniTdraw(screen, colorsOp,gameD.gameData[0][1])
            gameD.Paint(screen, allcolors)
        #得分重绘后如果第4行有数据直接退出游戏
        if gameD.gameData[4][0]:
            GameOver_2(screen,colorsOp,gameD)
            return isOver
        #-----------
        pygame.display.update()
        fpsClock.tick(fps)

def game_2(initColors, gameD,isPuse):#传入一个界面颜色,游戏操作界面颜色,所有颜色,游戏数据
    # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
    # game_1(initColors, gameData)
    screen = pygame.display.set_mode((700, 760))
    screen.fill(initColors[0])
    colorsOp = [1, 1, 1, initColors]#前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
    ispuse = isPuse
    while True:
        # initColors = [(3, 168, 158), (135, 206, 235), allcolors]  # 背景颜色,操作界面颜色,所有颜色表
        # colorsOp = [1, 1, 1, initColors]  # 前三个操控按钮颜色,后一个是一个列表[界面颜色,操作界面颜色]
        Op=playing_2(screen, colorsOp, gameD,ispuse)
        if Op==isPAUSE:
            Op2=pause(screen, colorsOp, gameD)
            if Op2==isQuit:
                gameD.ReSetGameData()
                return
            elif Op2 == continueGame:
                ispuse = False
        elif Op==isQuit:
            gameD.ReSetGameData()
            return
        elif Op==isSETTING:
            setting(screen, colorsOp, gameD)
        elif Op==isOver:
            return
        elif Op==continueGame:
            ispuse=False
