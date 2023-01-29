import game_core.game
from selectionWindow.selection import *
from game_core.core.allclass.coreData import GameData
from game_core.game import game_1, game_2
from loadGame.loadData import loadGameW, loadRankW
from data_io.input_data import *
pygame.init()

#-----读游戏默认配置数据---
allcolors=input_ALLCOLORS()#读取颜色表
# print(len(allcolors))
initColors=input_setting()
if initColors is  None:
    initColors=[(3,168,158), (135, 206, 235),allcolors]#背景颜色,操作界面颜色,所有颜色表

gameD=GameData()

while True:#跳出该循环等于退出游戏
    pygame.display.set_caption("俄罗斯方块")
    #跳出该循环等于完成模式选择:返回1表示选择了竞技模式,返回2表示选择了创造模式,返回3表示退出游戏
    c=schema(initColors[0])#选择是竞技模式,创造模式
    if c==1:
        #竞技模式
        while True:
            pygame.display.set_caption("竞技模式")
            c2=selection(initColors[0])#选择开始,继续,退出,查看排名
            if c2==1:
                speed=speedSelection(initColors[0])#选择速度
                if speed == 0.03:
                    pygame.display.set_caption("竞技-普通模式")
                elif speed == 0.05:
                    pygame.display.set_caption("竞技-中级模式")
                elif speed == 0.08:
                    pygame.display.set_caption("竞技-困难模式")
                elif speed == 0.1:
                    pygame.display.set_caption("竞技-炼狱模式")
                if speed!=100:
                    gameD.gameData[0][4] = speed
                    game_1(initColors,gameD,False)#是否是暂停
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
        speed = speedSelection(initColors[0])
        if speed == 0.03:
            pygame.display.set_caption("创造-普通模式")
        elif speed == 0.05:
            pygame.display.set_caption("创造-中级模式")
        elif speed == 0.08:
            pygame.display.set_caption("创造-困难模式")
        elif speed == 0.1:
            pygame.display.set_caption("创造-炼狱模式")
        if speed != 100:
            gameD.gameData[0][4] = speed
            game_2(initColors, gameD, False)  # 是否是暂停
        #调用game2
        # game_1(initColors,gameData)
    elif c==3:
        colorsOp = [1, 1, 1, initColors]
        screen2 = pygame.display.set_mode((700, 760))
        game_core.game.setting2(screen2,colorsOp)
    else:
        break


