
import datetime
from chooseWindows.choose import *
from game_core.core.allclass.coreData import GameData
from game_core.game import game_1
from loadGame.loadData import loadGameW, loadRankW
from data_io.input_data import input_ALLCOLORS
def initGameData():
    gameData = []
    DataC = [0] * 4
    gameData.append(DataC)
    # 第一行数据 (80,40),(120,40)
    # 第二行:   (80,80)
    for i in range(1, 18):
        DataC = [False]
        for j in range(0, 8):
            DataC.append([-1, [80 + j * 40, 40 + (i - 1) * 40]])
        gameData.append(DataC)
    t = datetime.datetime.now()
    s = t.strftime('%Y-%m-%d %H:%M:%S')
    gameData[0][0] = s
    gameData[0][1] = 0
    gameData[0][2] = [None] * 3
    return gameData
pygame.init()

allcolors=input_ALLCOLORS()#颜色表
#读取配置:界面设置,游戏数据,最高分最低分

initColors=[(3,168,158), (135, 206, 235),allcolors]#背景颜色,操作界面颜色,所有颜色表
gamed=initGameData()
gameD=GameData(gamed)
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
                game_1(initColors,gameD)
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


