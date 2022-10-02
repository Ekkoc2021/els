'''
游戏入口
'''
import pygame,sys, time, random
from pygame.locals import *
from chooseWindows.choose import *
from game_core.game import game_1
from loadGame.loadData import loadGameW, loadRankW
from data_io.input_data import input_ALLCOLORS

pygame.init()

allcolors=input_ALLCOLORS()#颜色表
#读取配置:界面设置,游戏数据,最高分最低分

initColors=[(3,168,158), (135, 206, 235),allcolors]#背景颜色,操作界面颜色,所有颜色表
gameData=[]
# game(initColors)
loop=True

while loop:#跳出该循环等于退出游戏
    pygame.display.set_caption("俄罗斯方块")
    #跳出该循环等于完成模式选择:返回1表示选择了竞技模式,返回2表示选择了创造模式,返回3表示退出游戏
    c=choose1(initColors[0])
    if c==1:
        #竞技模式
        pygame.display.set_caption("竞技模式")
        while True:
            c2=choose2(initColors[0])
            if c2==1:
                #todo:新游戏开始
                print("新游戏?还没做!")
                game_1(initColors,gameData)
            elif c2==2:
                # todo:读取旧游戏数据,然后开始
                print("继续游戏?还没做!")
                loaddata=loadGameW(initColors)
                if loaddata!=None:
                    game_1(initColors,loaddata)
            elif c2==4:
                loadRankW(initColors)
            elif c2==5:
                break
    elif c==2:
        pygame.display.set_caption("创造模式")
        print("创造模式?还没做!")
        #调用game2
        # game_1(initColors,gameData)
    else:
        loop=False
        print("退出游戏")


