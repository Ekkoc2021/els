import pygame

from game_core.core.abstract.abstractCoreData import abstractGameData


class GameData(abstractGameData):
    def __init__(self, gamedata):
        self.gameData = gamedata

    def Paint(self, screen, allcolors):
        for i in range(1, 18):
            if self.gameData[i][0]:
                for j in range(1, 9):
                    if self.gameData[i][j][0] != -1:
                        pygame.draw.rect(screen, allcolors[self.gameData[i][j][0]],
                                         (self.gameData[i][j][1][0], self.gameData[i][j][1][1], 40, 40))
                        pygame.draw.rect(screen, (0, 0, 0),
                                         (self.gameData[i][j][1][0], self.gameData[i][j][1][1], 41, 41), 1)
    '''
    得分了,重置gameData的数据,消除得分的行,分数+1
    '''

    def reset(self, begain):
        #               j                        j+1
        # begain-1[[False],[-1, [640, 40]], [-1, [640, 80]], [-1, [640, 120]], [-1, [640, 160]], [-1, [640, 200]], [-1, [640, 240]], [-1, [640, 280]], [-1, [640, 320]]],
        # begain[[False],[-1, [680, 40]], [-1, [680, 80]], [-1, [680, 120]], [-1, [680, 160]], [-1, [680, 200]], [-1, [680, 240]], [-1, [680, 280]], [-1, [680, 320]]]]
        p1 = begain - 1
        t = 0  # 用于记录当p1指向某一行没有数据时,移动的次数,t=1时,尽管没有遍历完整个,但应该结束了
        while begain >= 1:
            if begain != 1:
                if t <= 0:
                    for j in range(0, 9):
                        if j == 0:
                            self.gameData[begain][j] = self.gameData[p1][j]
                        else:
                            self.gameData[begain][j][0] = self.gameData[p1][j][0]
                else:
                    for i in range(1, 9):
                        self.gameData[begain][i][0] = -1
                    break
                if self.gameData[p1][0] == False:
                    t += 1
            elif self.gameData[begain][0] == True:
                self.gameData[begain][0] = False
                for i in range(1, 9):
                    self.gameData[begain][i][0] = -1
                    # 指针后移
            begain -= 1
            p1 -= 1

    def isWin(self):
        i = 17
        re = False
        while i > 0 and self.gameData[i][0]:
            if self.gameData[i][0]:
                t=0
                for j in range(1, 9):
                    if self.gameData[i][j][0] != -1:
                        t+=1
                        if t == 8:
                            re = True
                            self.gameData[0][1] += 1
                            self.reset(i)
                            i += 1
            i-=1
        return re

    def getColor(self, i, j):
        if 0<j<9 and 0<i<18:
            return self.gameData[i][j][0]
        else:
            return 1

    def getLoation(self, i, j):
        if 0 < j < 9 and 0 < i < 18:
            return self.gameData[i][j][1]
        else:
            return None

    def getMapping(self, x, y):
        # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
        if 80 <= x < 400 and 40 <= y < 720:
            return self.gameData[int(y/40)][int( (x - 40) / 40)]
        else:
            return None

    def writeDate(self, x, y, co):
            #获取对应的映射
            l=self.getMapping(x,y)
            if l!=None:
                self.gameData[int(y/40)][0]=True
                l[0]=co
