from chooseWindows.choose import *
from game_core.core.allclass.coreData import GameData
from game_core.game import game_1
from loadGame.loadData import loadGameW, loadRankW
from data_io.input_data import *
pygame.init()

#-----读游戏默认配置数据---
allcolors=input_ALLCOLORS()#读取颜色表
initColors=input_setting()
if initColors is  None:
    initColors=[(3,168,158), (135, 206, 235),allcolors]#背景颜色,操作界面颜色,所有颜色表

gameD=GameData()

while True:#跳出该循环等于退出游戏
    pygame.display.set_caption("俄罗斯方块")
    #跳出该循环等于完成模式选择:返回1表示选择了竞技模式,返回2表示选择了创造模式,返回3表示退出游戏
    c=choose1(initColors[0])
    if c==1:
        #竞技模式
        pygame.display.set_caption("竞技模式")
        while True:
            c2=choose2(initColors[0])
            if c2==1:
                game_1(initColors,gameD,False)
            elif c2==2:
                #继续游戏
                loaddata=loadGameW(initColors)
                if loaddata!=None:
                    gameD.gameData=loaddata
                    game_1(initColors,gameD,True)
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
        break


