import pygame

from game_core.core.abstract.abstractBlock import AbstractBlock


# None, None
# None, None
class Block_1(AbstractBlock):
    def __init__(self, color=3):
        self.shape = 0
        self.block1 = [200, 80]
        self.block2 = [240, 80]
        self.block3 = [200, 120]
        self.block4 = [240, 120]
        self.co = color
        self.block = [
            [[self.co, self.block1], [self.co, self.block2]],
            [[self.co, self.block3], [self.co, self.block4]]
        ]
        # 右边:self.block[0][1][1][0],self.block[0][1][1][1]+40
        # 右边:self.block[1][1][1][0],self.block[1][1][1][1]+40
        # 左边:self.block[0][0][1][0],self.block[0][0][1][1]+40
        # 左边:self.block[1][0][1][0],self.block[1][0][1][1]+40

        self.left = -1
        self.right = 1

    def changeShape(self, gameD):
        self.shape=0

    def drawBlock(self, screen, allcolors):
        for i in range(0, 2):
            for j in range(0, 2):
                pygame.draw.rect(screen, allcolors[self.block[i][j][0]],
                                 (self.block[i][j][1][0], self.block[i][j][1][1], 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (self.block[i][j][1][0], self.block[i][j][1][1], 41, 41), 1,border_radius=5)

    def horiMove(self, gameD, dirc):
        # 第i行 = y / 40, 第j列 = (x - 40) / 40
        b1 = self.block1
        b2 = self.block2
        b3 = self.block3
        b4 = self.block4
        g = gameD.gameData
        if dirc > 0 and (int((self.block2[0] - 40) / 40) + 1 < 9):
            a = g[int(b4[1] / 40)][int((b4[0] - 40) / 40) + 1][0] == -1
            b = g[int(b2[1] / 40)][int((b2[0] - 40) / 40) + 1][0] == -1
            if a and b:
                self.block1[0] = self.block1[0] + dirc * 40
                self.block2[0] = self.block2[0] + dirc * 40
                self.block3[0] = self.block3[0] + dirc * 40
                self.block4[0] = self.block4[0] + dirc * 40
        if (dirc < 0) and (int((self.block1[0] - 40) / 40) - 1 > 0 or self.block1[1] < 40):
            if g[int(b1[1] / 40)][int((b1[0] - 40) / 40) - 1][0] == -1 and \
                    g[int(b3[1] / 40)][int((b3[0] - 40) / 40) - 1][0] == -1:
                self.block1[0] = self.block1[0] + dirc * 40
                self.block2[0] = self.block2[0] + dirc * 40
                self.block3[0] = self.block3[0] + dirc * 40
                self.block4[0] = self.block4[0] + dirc * 40

    def downward(self, gameD, speed):
        # 第i行 = y / 40, 第j列 = (x - 40) / 40
        b1 = self.block1
        b2 = self.block2
        b3 = self.block3
        b4 = self.block4
        g = gameD.gameData
        if b3[1] + speed * 40 + 40 < 720:
            x = g[int((b3[1] + speed * 40) / 40 + 1)][int((b3[0] - 40) / 40)]
            if (g[int((b3[1] + speed * 40) / 40 + 1)][int((b3[0] - 40) / 40)][0] == -1) and (
                    g[int((b4[1] + speed * 40) / 40 + 1)][int((b4[0] - 40) / 40)][0] == -1):
                # 可以向下移动
                b1[1] = b1[1] + speed * 40
                b2[1] = b2[1] + speed * 40
                b3[1] = b3[1] + speed * 40
                b4[1] = b4[1] + speed * 40
                return True  # 代表方块依然存活
            else:
                b1[1] = x[1][1] - 80
                b2[1] = x[1][1] - 80
                b3[1] = x[1][1] - 40
                b4[1] = x[1][1] - 40
                return False


        else:
            b1[1] = 640
            b2[1] = 640
            b3[1] = 680
            b4[1] = 680
            return False

    def blockMove(self, speed, gameD, dirc):
        self.horiMove(gameD, dirc)
        return self.downward(gameD, speed)  # 返回的T表示方块依然存活,F表示方块已经消亡

    def writeData(self, gameD):
        b1 = self.block1
        b2 = self.block2
        b3 = self.block3
        b4 = self.block4
        g = gameD.gameData
        g[int(b1[1] / 40)][0] = True
        g[int(b3[1] / 40)][0] = True
        g[int(b1[1] / 40)][int((b1[0] - 40) / 40)][0] = self.co
        g[int(b2[1] / 40)][int((b2[0] - 40) / 40)][0] = self.co
        g[int(b3[1] / 40)][int((b3[0] - 40) / 40)][0] = self.co
        g[int(b4[1] / 40)][int((b4[0] - 40) / 40)][0] = self.co

    def drawInForeshow(self, screen, allcolors):
        pygame.draw.rect(screen, allcolors[self.co], (510, 160, 40, 40),border_radius=5)
        pygame.draw.rect(screen, allcolors[self.co], (550, 160, 40, 40),border_radius=5)
        pygame.draw.rect(screen, allcolors[self.co], (510, 200, 40, 40),border_radius=5)
        pygame.draw.rect(screen, allcolors[self.co], (550, 200, 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (550, 200, 41, 41), 1,border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (510, 200, 41, 41), 1,border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (550, 160, 41, 41), 1,border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (510, 160, 41, 41), 1,border_radius=5)


# i
# i
# i(定位点)
# i
class Block_2(AbstractBlock):
    def __init__(self, color=1):
        self.shape = 0
        self.co = color
        self.block = [200, 80]

    def drawInForeshow(self, screen, allcolors):
        for i in range(4):
            pygame.draw.rect(screen, allcolors[self.co], (550, 120 + i * 40, 40, 40),border_radius=5)
        for i in range(4):
            pygame.draw.rect(screen, (0, 0, 0), (550, 120 + i * 40, 41, 41), 1,border_radius=5)

    def changeShape(self, gameD):
        # 把当前位置对应在gameD中的映射找到,判断是否能变换
        # 第i行 = y / 40, 第j列 = (x - 40) / 40
        i = int(self.block[1] / 40)
        x=self.block[0]
        y=self.block[1]
        j = int((self.block[0] - 40) / 40)
        g = gameD.gameData
        if self.shape == 0:
            # 竖着变躺着
            # if y>=160:
                if x - 80 >= 80 and y - 80 >= 0 and x + 40 <= 420 and y + 40 < 680:
                    # 判断区域内是否存在
                    i1 = i - 2
                    j1 = j - 2
                    # print("j1",j1)
                    # print("i1",i1)
                    if g[i][j + 1][0] != -1:
                        return
                    if g[i + 1][j + 1][0] != -1:
                        return
                    for p in range(3):
                        if g[i1 + p][j1][0] != -1 :
                            return
                        if g[i1 + p][j1 + 1][0] != -1:
                            return
                    self.shape = 1
        # else:
        #     if x-80>=80:
        #         self.shape = 1
        else:
            if i - 2 > 0 and j - 2 > 0 and i + 1 < 18 and j + 1 < 9:
                # 判断区域内是否存在
                i1 = i - 2
                j1 = j - 2
                if g[i + 1][j][0] != -1 :
                    return
                if g[i + 1][j + 1][0] != -1:
                    return
                for p in range(3):
                    if g[i1 + 1][j1 + p][0] != -1 :
                        return
                    if g[i1][j1 + p][0] != -1:
                        return
                self.shape = 0
                # 22/10/6偶然测试发现bug:需要修正方块位置一下:左右移动每次移动一个格子,
                # 往下移动时,定位格子所处的位置,并不一定正好在网格线上,不在网格线上时,但是却可以旋转,
                # 旋转后,会跳过下一格的碰撞检测
                #检测旋转后的下一格是否是方块,或者是边界,修正定位方块位置
                y = self.block[1] + 40 + 40
                i = int(y / 40)
                j = int((self.block[0] - 40) / 40)
                if i<18:
                    if g[i][j][0]!=-1:#如果这个位置是方块
                        self.block[1]=g[i][j][1][1]-40-40
                else:
                    #是边界调整为
                    self.block[1] = 640

    def horiMove(self, gameD, dirc):
        # 第i行 = y / 40, 第j列 = (x - 40) / 40
        i = int(self.block[1]/ 40)
        j = int((self.block[0] - 40) / 40)
        g=gameD.gameData
        #状态0,竖着的时候的左移动:
        if self.shape==0:
            # 第i行 = y / 40, 第j列 = (x - 40) / 40
            #左移动
            if dirc<0:
                i1=i-2
                j1=j-1
                #保证不会超过边界:直接忽略行,行会下移动,但是一开始的时候:位置是数据的第二行:i1=2
                #需要支持在i1=2的时候也能移动
                if (j1>0):
                    if i1>2:#i等于2就别判断了,直接移动
                        for i in range(4):
                            if g[i1+i][j1][0]!=-1:
                                return
                    self.block[0] = self.block[0] + dirc * 40
            else:#右移动
                i1 = i - 2
                j1 = j + 1
                if j1 < 9:
                    if (i1 > 2):
                        for i in range(4):
                            if g[i1 + i][j1][0] != -1:
                                return
                        # 可以移动
                    self.block[0]=self.block[0] + dirc * 40

        else:#状态为1时的移动,横着的时候
            #左移动
            if dirc<0:
                j1=j-3
                if j1>0:
                    if g[i][j1][0] != -1:
                        return
                    #可以移动
                    self.block[0]=self.block[0] + dirc * 40
            #右移动
            else:
                j1=j+2
                if j1<9 :
                    if g[i][j1][0] != -1:
                        return
                    # 可以移动
                    self.block[0]=self.block[0] + dirc * 40
    def downward(self, gameD, speed):
        i = int((self.block[0] - 40) / 40)
        g = gameD.gameData

        if self.shape == 0:
            # 第j行 = y / 40, 第i列 = (x - 40) / 40
            y = self.block[1] + 40 + 40 + speed * 40
            j = int(y / 40)
            if j<18:
                if g[j][i][0] == -1:
                    self.block[1] = self.block[1] + speed * 40
                    return True
                else:
                    self.block[1] = g[j][i][1][1]-40-40
                    return False
            else:
                self.block[1] = 640
        else:
            # 第j行 = y / 40, 第i列 = (x - 40) / 40
            y = self.block[1] + 40 + speed * 40
            j = int(y / 40)
            i = i - 2
            if j<18:
                if i > 0:
                    for q in range(4):
                        if g[j][i + q][0] != -1:
                            self.block[1] = g[j][i][1][1]-40
                            return False
                    self.block[1] = self.block[1] + speed * 40
                    return True

            else:
                self.block[1] = 680


    def blockMove(self, speed, gameD, dirc):
        self.horiMove(gameD,dirc)
        return self.downward(gameD, speed)


    def drawBlock(self, screen, allcolors):
        if self.shape == 0:
            y = self.block[1] - 80
            for i in range(4):
                pygame.draw.rect(screen, allcolors[self.co],
                                 (self.block[0], y + i * 40, 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (self.block[0], y + i * 40, 41, 41), 1,border_radius=5)
        else:
            x = self.block[0] - 80
            for i in range(4):
                pygame.draw.rect(screen, allcolors[self.co],
                                 (x + i * 40, self.block[1], 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (x + i * 40, self.block[1], 41, 41), 1,border_radius=5)

    def writeData(self, gameD):
        #todo:写入数据有bug
        #需要根据不同状态进行写入数据
        # 第i行 = y / 40, 第j列 = (x - 40) / 40
        x = self.block[0]
        y = self.block[1]
        if self.shape==0:#竖着
            # i
            # i
            # i(定位点)
            # i
            for i in range(4):
                gameD.writeDate(x,y-40-40+i*40,self.co)
        else:#横着
            for i in range(4):
                gameD.writeDate(x-40-40+i*40,y,self.co)



#        None
#        None
#   None None(点位点)
class Block_3(AbstractBlock):
    def __init__(self,color=3):
        self.shape=0
        self.co=color
        self.block=[240,120]

    #   i
    #   i
    # i i(定位)
    #
    # i
    # i(定位)i  i

    #    i(定位)i
    #    i
    #    i

    #  i i(定位)i
    #          i

    def drawBlock(self, screen, allcolors):
        x = self.block[0]
        y = self.block[1]
        if self.shape==0:
            #   i
            #   i
            # i i(定位)
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co], (x, y-i*40, 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0,0,0), (x, y-i*40, 41, 41),1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co], (x-40, y, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0,0,0), (x-40, y, 41, 41),1,border_radius=5)
        elif self.shape==1:
            #shepe=1
            # i
            # i(定位)i  i
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co], (x + i * 40, y, 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0), (x+ i * 40, y , 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co], (x , y-40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0), (x, y-40, 41, 41), 1,border_radius=5)
        elif self.shape==2:
            #    i(定位)i
            #    i
            #    i
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co], (x, y + i * 40, 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0), (x, y + i * 40, 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co], (x+40, y, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0), (x+40, y, 41, 41), 1,border_radius=5)
        else:
            #  3
            #  i i(定位)i
            #          i
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co], (x- i * 40, y , 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0), (x- i * 40, y , 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co], (x , y+ 40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0), (x , y+ 40, 41, 41), 1,border_radius=5)

    def horiMove(self, gameD, dire):
        # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
        x = self.block[0]
        y = self.block[1]
        g = gameD.gameData
        if self.shape==0:
            #  3  i
            #  2  i
            # 1 i i(定位)
            # 4
            # 左移动
            if dire<0:
                #同时保证方块底部边界所在位置的左边没有方块
                x4=x-40-40
                y4=y+40
                i4=int(y4 / 40)
                j4=int((x4 - 40) / 40)

                x1 = x - 40 - 40
                i1 = int(y / 40)
                j1 = int((x1 - 40) / 40)

                x2 = x - 40
                y2 = y - 40
                i2 = int(y2 / 40)
                j2 = int((x2 - 40) / 40)


                if i4<18 and j1>0:
                    # g[i1][j1][0] == -1
                    # g[i2][j2][0] == -1
                    # g[i4][j4][0] == -1
                    # g[i2 - 1][j4][0] == -1
                    if g[i1][j1][0]==-1 and g[i4][j4][0]==-1 and g[i2][j2][0]==-1 and g[i2-1][j4][0]==-1:
                        self.block[0] = self.block[0] + 40 * dire
                elif j1>0 :#如果处于底部,这个时候不用考虑i4这个位置的情况,根本不会出现超过底部的情况
                    #当方块方块与方块粘连在一起时,无法移动了,^v^
                    if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i2 - 1][j2][0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
            else:
                #     i 3
                #     i 2
                #   i i(定位)1
                #         4
                # 同时保证方块底部边界所在位置的左边没有方块
                x4 = x+ 40
                y4 = y + 40
                i4 = int(y4 / 40)
                j4 = int((x4 - 40) / 40)

                x1 = x +40
                i1 = int(y / 40)
                j1 = int((x1 - 40) / 40)

                x2 = x + 40
                y2 = y - 40
                i2 = int(y2 / 40)
                j2 = int((x2 - 40) / 40)

                if i4 < 18 and j2<9:
                    if g[i1][j1][0] == -1 and g[i4][j4][0] == -1 and g[i2][j2][0] == -1 and g[i2 - 1][j4][0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
                elif j2<9 :  # 如果处于底部,这个时候不用考虑i4这个位置的情况,根本不会出现超过底部的情况
                    if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i2 - 1][j4][0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
        elif self.shape==1:
            if dire<0:
                #左移动
                # shepe=1
                # 2 i
                # 1 i(定位)i  i
                # 3
                x1=x-40
                i1 = int(y / 40)
                j1 = int((x1 - 40) / 40)

                x3=x-40
                y3=y+40
                i3 = int(y3 / 40)
                j3 = int((x3 - 40) / 40)

                if j1>0 and i3<18:
                    if g[i1][j1][0]==-1 and g[i1-1][j1][0]==-1 and g[i3][j3][0]==-1:
                        self.block[0] = self.block[0] + 40 * dire
                elif j1>0:
                    if g[i1][j1][0]==-1 and g[i1-1][j1][0]==-1:
                        self.block[0] = self.block[0] + 40 * dire
            else:
                # 右移动
                # shepe=1
                #   i 2
                #   i(定位)i  i 1
                #            3
                x1 = x+40+40+40
                i1 = int(y / 40)
                j1 = int((x1 - 40) / 40)

                x2=x+40
                y2=y-40
                i2 = int(y2 / 40)
                j2 = int((x2 - 40) / 40)

                x3 = x + 40+40+40
                y3 = y + 40
                i3 = int(y3 / 40)
                j3 = int((x3 - 40) / 40)

                if j3 <9 and i3 < 18:
                    if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
                elif j3 < 9:
                    if g[i1][j1][0] == -1 and g[i2][j2][0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
        elif self.shape==2:
            #    l1 i(定位)i
            #    l2 i
            #    l3 i
            #    l4
            # getMapping( x, y)
            # getLoation( i, j)
            # getColor(i, j):
            if dire<0:#左移动
                #10/8,把由坐标到gameData索引的映射做了个封装
                l1=gameD.getMapping(x-40,y)
                l2=gameD.getMapping(x-40,y+40)
                l3=gameD.getMapping(x-40,y+40+40)
                l4=gameD.getMapping(x-40,y+40+40+40)#l4为空只有一种可能就是到达边界了
                if l1!=None and l2!=None and l3!=None and l4!=None:
                    if l1[0]==-1 and l2[0]==-1 and l3[0]==-1 and l4[0]==-1 :
                        self.block[0] = self.block[0] + 40 * dire
                elif l1!=None and l2!=None and l3!=None:
                    if l1[0]==-1 and l2[0]==-1 and l3[0]==-1 :
                        self.block[0] = self.block[0] + 40 * dire
            elif dire>0:
                l1 = gameD.getMapping(x + 40+40, y)
                l2 = gameD.getMapping(x + 40, y + 40)
                l3 = gameD.getMapping(x + 40, y + 40 + 40)
                l4 = gameD.getMapping(x+40 , y + 40 + 40+40)  # l4为空只有一种可能就是到达边界了
                l5 = gameD.getMapping(x + 40 + 40, y+40) #下边缘碰撞检测
                if l1 != None and l2 != None and l3 != None and l4 != None and l5!=None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1 and l5[0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
                elif l1 != None and l2 != None and l3 != None and l5!=None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l5[0] == -1:
                        self.block[0] = self.block[0] + 40 * dire
        elif self.shape==3:
                #  3
                # 1 i i(定位)i
                # 2       3 i
                #         4
                if dire<0:#左
                    l1 = gameD.getMapping(x - 40-40-40, y)
                    l2 = gameD.getMapping(x - 40-40-40, y + 40)#下边缘
                    l3 = gameD.getMapping(x - 40, y + 40)
                    l4 = gameD.getMapping(x-40 , y + 40 + 40)  # l4为空只有一种可能就是到达边界了
                    if l1!=None and l2!=None and l3!=None and l4!=None:
                        if l1[0]==-1 and l2[0]==-1 and l3[0]==-1 and l4[0]==-1 :
                            self.block[0] = self.block[0] + 40 * dire
                    elif l1!=None and l2!=None and l3!=None:
                        if l1[0]==-1 and l2[0]==-1 and l3[0]==-1 :
                            self.block[0] = self.block[0] + 40 * dire
                else:
                    l1 = gameD.getMapping(x +40, y)
                    l2 = gameD.getMapping(x+ 40, y + 40)  # 下边缘
                    l4 = gameD.getMapping(x+40, y + 40 + 40)  # l4为空只有一种可能就是到达边界了
                    if l1 != None and l2 != None and  l4 != None:
                        if l1[0] == -1 and l2[0] == -1 and l4[0] == -1:
                            self.block[0] = self.block[0] + 40 * dire
                    elif l1 != None and l2 != None :
                        if l1[0] == -1 and l2[0] == -1 :
                            self.block[0] = self.block[0] + 40 * dire



        # shepe=1
        # i
        # i(定位)i  i
        #    i(定位)i
        #    i
        #    i
        #  3
        #  i i(定位)i
        #          i

    def downward(self, gameD, speed):
        x=self.block[0]
        y=self.block[1]
        g=gameD.gameData
        if self.shape==0:
            #第5种方块的形状0的代码c过来删除几行后完美运行,泪目
            # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
            #   i
            #   i
            # i i(定位)
            # 底部坐标移动后在对应列表的映射位置
            y1 = y + 40 + 40 * speed
            i1 = int(y1 / 40)
            j1 = int((x - 40) / 40)

            if i1 < 18:
                if g[i1][j1][0] == -1 and g[i1][j1 - 1][0] == -1 :
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = g[i1][j1][1][1]-40
                    return False

            else:
                self.block[1] = 680
                return False
        elif self.shape==1:

            # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
            #定位块的下一块
            y1 = y + 40 + 40 * speed
            i1 = int(y1 / 40)
            j1 = int((x - 40) / 40)

            if i1 < 18:
                if g[i1][j1][0] == -1 and g[i1][j1 + 1][0] == -1 and g[i1][j1 + 2][0] == -1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = g[i1][j1][1][1]-40
                    return False

            else:
                self.block[1] = 680
                return False
        elif self.shape==2:
            # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
            #    i(定位)i
            #    i     1
            #    i
            #    2
            y1 = y + 40 + 40 * speed
            x1=x+40
            i1 = int(y1 / 40)
            j1 = int((x1- 40) / 40)

            y2 = y + 40 +40+40+ 40 * speed
            i2 = int(y2 / 40)
            j2 = int((x - 40) / 40)
            if i2 < 18:
                if g[i1][j1][0] == -1 and g[i2][j2][0] == -1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = g[i1][j1][1][1]-40
                    return False

            else:
                self.block[1] = 680-40-40
                return False
        else:
            #  3
            #  i i(定位)i
            #          i
            # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
            # 定位块的下一块
            y1 = y + 40 + 40 * speed
            i1 = int(y1 / 40)
            j1 = int((x - 40) / 40)

            y2=y+40+40+40*speed
            i2 = int(y2 / 40)
            j2 = int((x - 40) / 40)

            if i2 < 18:
                #todo:有bug2022/10/13
                if  g[i1][j1 - 1][0] == -1 and g[i1][j1 - 2][0] == -1 and g[i2][j2][0]==-1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = g[i1][j1][1][1] - 40
                    return False

            else:
                self.block[1] = 640
                return False

    def blockMove(self, speed, gameD, dire):
        self.horiMove(gameD, dire)
        return self.downward( gameD, speed)

    def writeData(self, gameD):
        if self.shape==0:
            #   i
            #   i
            # i i(定位)
            for i in range(3):
                gameD.writeDate(self.block[0], self.block[1]-i*40, self.co)
            gameD.writeDate(self.block[0]-40, self.block[1], self.co)
        elif self.shape==1:
            # shepe=1
            # i
            # i(定位)i  i
            for i in range(3):
                gameD.writeDate(self.block[0]+i*40, self.block[1], self.co)
            gameD.writeDate(self.block[0], self.block[1]-40, self.co)
        elif self.shape==2:
            #    i(定位)i
            #    i
            #    i
            for i in range(3):
                gameD.writeDate(self.block[0], self.block[1]+i*40, self.co)
            gameD.writeDate(self.block[0]+40, self.block[1], self.co)
        elif self.shape==3:
            #  3
            #  i i(定位)i
            #          i
            for i in range(3):
                gameD.writeDate(self.block[0]- i * 40 , self.block[1], self.co)
            gameD.writeDate(self.block[0] , self.block[1]+ 40, self.co)

    def drawInForeshow(self, screen, allcolors):
        #   i
        #   i
        # i i(定位)
        for i in range(3):
            pygame.draw.rect(screen, allcolors[self.co], (550, 200 - i * 40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0), (550, 200 - i * 40, 41, 41), 1,border_radius=5)
        pygame.draw.rect(screen, allcolors[self.co], (550 - 40, 200, 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (550 - 40, 200, 41, 41), 1,border_radius=5)

    def changeShape(self, gameD):
        x=self.block[0]
        y=self.block[1]
        if self.shape==0:
            #   i 1 2
            # 5 i 3 4
            # i i(定位)6 7
            l1=gameD.getMapping(x+40,y-40-40)
            l2=gameD.getMapping(x+40+40,y-40-40)
            l3=gameD.getMapping(x+40,y-40)
            l4=gameD.getMapping(x+40+40,y-40)
            l5=gameD.getMapping(x-40,y-40)
            l6=gameD.getMapping(x+40+40,y)
            l7=gameD.getMapping(x+40+40,y)
            if l1!=None and l2!=None and l3!=None and l4!=None and l5!=None and l6!=None and l7!=None:
                if l1[0]==-1 and l2[0]==-1 and l3[0]==-1 and l4[0]==-1 and l5[0]==-1 and l6[0]==-1 and l7[0]==-1:
                    self.shape=1
        elif self.shape==1:
            # shepe=1
            # i 7
            # i(定位)i  i
            # 1   2   3
            # 4   5   6
            l1 = gameD.getMapping(x , y+40)
            l2 = gameD.getMapping(x +40, y+40)
            l3 = gameD.getMapping(x + 40+40, y + 40)
            l4 = gameD.getMapping(x , y + 40+40)
            l5 = gameD.getMapping(x + 40, y + 40+40)
            l6 = gameD.getMapping(x + 40+ 40, y + 40 + 40)
            l7 = gameD.getMapping(x - 40, y + 40 )
            if l1 != None and l2 != None and l3 != None and l4 != None and l5 != None and l6 != None and l7 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1 and l5[0] == -1 and l6[0] == -1 and l7[
                    0] == -1:
                    self.shape = 2
        elif self.shape==2:
            #   2 1 i(定位)i
            #   3 4 i    7
            #   5 6 i
            l1 = gameD.getMapping(x, y - 40)
            l2 = gameD.getMapping(x , y -40-40)
            l3 = gameD.getMapping(x + 40, y - 40-40)
            l4 = gameD.getMapping(x+40, y-40)
            l5 = gameD.getMapping(x + 40+40, y - 40 - 40)
            l6 = gameD.getMapping(x + 40 + 40, y -40)
            l7 = gameD.getMapping(x + 40, y + 40)
            if l1 != None and l2 != None and l3 != None and l4 != None and l5 != None and l6 != None and l7 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1 and l5[0] == -1 and l6[0] == -1 and l7[0] == -1:
                    self.shape = 3
        elif self.shape==3:
            #     4   5
            #  1  2   3
            #  i i(定位)i
            #        6 i
            l1 = gameD.getMapping(x-40, y - 40-40)
            l2 = gameD.getMapping(x-40, y - 40 )
            l3 = gameD.getMapping(x - 40, y )
            l4 = gameD.getMapping(x - 40-40, y - 40)
            l5 = gameD.getMapping(x - 40 - 40, y )
            l6 = gameD.getMapping(x  + 40, y - 40)
            # l7 = gameD.getMapping(x + 40, y + 40)
            if l1 != None and l2 != None and l3 != None and l4 != None and l5 != None and l6 != None :
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1 and l5[0] == -1 and l6[0] == -1 :
                    self.shape = 0


#    None
#    None
#    None(定位点) None
class Block_4():
    def __init__(self):
        pass


#   None None
#  (定位点)None None
class Block_5(AbstractBlock):
    def __init__(self,color=5):
        self.shape=1#只有两种状态
        self.co=color
        self.block=[200,80]

    def drawBlock(self, screen, allcolors):
        if self.shape==0:
            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0],self.block[1], 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0], self.block[1], 41, 41), 1,border_radius=5)

            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0], self.block[1]-40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0], self.block[1]-40, 41, 41), 1,border_radius=5)

            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0]+40, self.block[1], 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0]+40, self.block[1], 41, 41), 1,border_radius=5)

            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0]-40, self.block[1]-40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0]-40, self.block[1]-40, 41, 41), 1,border_radius=5)
        else:
            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0], self.block[1], 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0], self.block[1], 41, 41), 1,border_radius=5)

            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0], self.block[1] +40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0], self.block[1] +40, 41, 41), 1,border_radius=5)

            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0]+40 , self.block[1], 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0]+40 , self.block[1], 41, 41), 1,border_radius=5)

            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0] + 40, self.block[1] - 40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0] + 40, self.block[1] - 40, 41, 41), 1,border_radius=5)
    def horiMove(self, gameD, dirc):
        x=self.block[0]
        y=self.block[1]
        g=gameD.gameData
        # 0
        #   None None
        #  (定位点)None None
        if self.shape == 0:
            if dirc>0:
                # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
                x1=x+40+40
                i1=int(y / 40)
                j1=int( (x1 - 40) / 40)

                y2=y-40
                x2=x+40
                i2=int(y2 / 40)
                j2=int((x2 - 40) / 40)

                y3 = y +40
                x3 = x + 40+40
                i3 = int(y3 / 40)
                j3 = int((x3 - 40) / 40)
                #   None None
                #  (定位点)None None
                if y3<720:
                    if  0<j1<9 and  0<j2<9 and  0<j3<9 and  0<i1<18 and 0<i2<18 and 0<i3<18 :
                        if g[i1][j1][0]==-1 and g[i2][j2][0]==-1and g[i3][j3][0]==-1:
                            self.block[0] = self.block[0]+40*dirc
                else:
                    if  0<j1<9 and  0<j2<9 and  0<j3<9 and  0<i1<18 and 0<i2<18 :
                        if g[i1][j1][0]==-1 and g[i2][j2][0]==-1:
                            self.block[0] = self.block[0]+40*dirc

            else:
                # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
                x1=x-40
                i1=int(y / 40)
                j1=int( (x1 - 40) / 40)

                x2=x-40-40
                y2=y-40
                i2=int(y2 / 40)
                j2=int( (x2 - 40) / 40)

                #不应该只判断一个点
                x3 = x - 40 - 40
                y3 = y
                i3 = int(y3 / 40)
                j3 = int((x3 - 40) / 40)

                if  0<j1<9 and  0<j2<9 and  0<j3<9 and 0<i1<18 and 0<i2<18 and 0<i3<18 :
                    if g[i1][j1][0] == -1 and g[i2][j2][0] == -1and g[i3][j3][0] == -1:
                        self.block[0] = self.block[0]+40*dirc
        else:
            #第二种情况
            #              None
            #  (定位点)None None
            #         None
            if dirc > 0:
                # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
                #              None
                #  (定位点)None None
                #         None
                x1 = x + 40 + 40
                i1 = int(y / 40)
                j1 = int((x1 - 40) / 40)

                y2 = y - 40
                x2 = x + 40+40
                i2 = int(y2 / 40)
                j2 = int((x2 - 40) / 40)

                y3=y+40
                x3=x+40
                i3 = int(y3 / 40)
                j3 = int((x3 - 40) / 40)

                x4 = x + 40+40
                y4=y+40
                i4 = int(y4 / 40)
                j4 = int((x4 - 40) / 40)

                if  0<j1<9 and  0<j2<9 and  0<j3<9 and  0<j4<9 and 0<i1<18 and 0<i2<18 and 0<i3<18 and 0<i4<18:
                    if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1  and g[i4][j4][0] == -1 :
                        self.block[0] = self.block[0]+40*dirc

            else:
                # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
                #              None
                #  (定位点)None None
                #         None
                x1 = x -40
                i1 = int(y / 40)
                j1 = int((x1 - 40) / 40)

                x2 = x - 40
                y2 = y +40
                i2 = int(y2 / 40)
                j2 = int((x2 - 40) / 40)

                y3=y-40
                i3 = int(y3 / 40)
                j3 = int((x - 40) / 40)

                x4 = x + 40 + 40
                i4 = int(y / 40)
                j4 = int((x4 - 40) / 40)

                y5 = y + 40 + 40
                x5 = x - 40
                i5 = int(y5 / 40)
                j5 = int((x5 - 40) / 40)
                if y5<720:
                    if j2 > 0:
                        if j4<9:
                            if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1 and g[i4][j4][0] == -1and g[i5][j5][0] == -1:
                                self.block[0] = self.block[0]+40*dirc
                        else:
                            if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1 and g[i5][j5][0] == -1:
                                self.block[0] = self.block[0]+40*dirc
                else:
                    if j2 > 0:
                        if j4 < 9:
                            if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1 and g[i4][j4][0] == -1:
                                self.block[0] = self.block[0] + 40 * dirc
                        else:
                            if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1:
                                self.block[0] = self.block[0] + 40 * dirc


    def downward(self, gameD, speed):
        # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
        x=self.block[0]
        y=self.block[1]
        g=gameD.gameData
        # 0
        #   None None
        #  (定位点)None None
        if self.shape==0:
            #底部坐标移动后在对应列表的映射位置
            y1=y+40+40*speed
            i1=int(y1 / 40)
            j1=int( (x - 40) / 40)

            #顶部坐标移动后列表的投影位置
            y2=y+40*speed
            x2=x-40
            i2=int(y2 / 40)
            j2=int( (x2 - 40) / 40)
            if i1<18:
                if g[i1][j1][0]==-1 and g[i1][j1+1][0]==-1 and g[i2][j2][0]==-1:
                    self.block[1]=self.block[1]+40*speed
                    return True
                else:
                    self.block[1] = g[i2][j2][1][1]
                    return False

            else:
                self.block[1]=680
                return False
        else:

            #              None
            #  (定位点)None None
            #         None
            # x = self.block[0]
            # y = self.block[1]
            # g = gameD.gameData
            # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
            y1=y+40+40+40*speed
            i1=int(y1 / 40)
            j1=int( (x - 40) / 40)
            y2=y+40+40*speed
            i2=int(y2 / 40)
            j2=int( (x - 40) / 40)+1
            if i1<18:
                if g[i1][j1][0]==-1 and g[i2][j2][0]==-1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = g[i2][j2][1][1]-40
                    return False
            else:
                self.block[1]=640
                return False

    def blockMove(self, speed, gameD, dirc):
        self.horiMove( gameD, dirc)
        return self.downward(gameD, speed)

    def writeData(self, gameD):
        x = self.block[0]
        y = self.block[1]
        g = gameD.gameData
        i = int(y / 40)
        j=int( (x - 40) / 40)
        # 0
        #   None None
        #  (定位点)None None
        if self.shape == 0:
            g[i][j][0]=self.co
            g[i][0]=True
            g[i][j+1][0]=self.co
            g[i-1][j][0] = self.co
            g[i-1][0]=True
            g[i-1][j-1][0] = self.co
        else:
            g[i][j][0] = self.co
            g[i][0]=True
            g[i][j+1][0] = self.co
            g[i-1][j+1][0] = self.co
            g[i-1][0]=True
            g[i+1][j][0] = self.co
            g[i+1][0]=True



    def drawInForeshow(self, screen, allcolors):
        pygame.draw.rect(screen, allcolors[self.co], (550, 200 , 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), (550, 200, 41, 41), 1,border_radius=5)

        pygame.draw.rect(screen, allcolors[self.co],
                         (550, 200 - 40, 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0),
                         (550, 200 - 40, 41, 41), 1,border_radius=5)

        pygame.draw.rect(screen, allcolors[self.co],
                         (550 + 40, 200, 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0),
                         (550 + 40, 200, 41, 41), 1,border_radius=5)

        pygame.draw.rect(screen, allcolors[self.co],
                         (550 - 40, 200 - 40, 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0),
                         (550 - 40, 200 - 40, 41, 41), 1,border_radius=5)

    def changeShape(self, gameD):
        x = self.block[0]
        y = self.block[1]
        g = gameD.gameData
        # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
        # 0
        #     1   2
        #   None None
        #  (定位点)None None
        #          3   4
        # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
        if self.shape==0:
            x1=x-40
            y1=y-40-40
            i1=int(y1 / 40)
            j1=int( (x1 - 40) / 40)

            y2=y-40-40
            i2=int(y2 / 40)
            j2=int( (x - 40) / 40)

            y3=y+40
            i3=int(y3 / 40)
            j3=int( (x - 40) / 40)

            x4=x+40
            y4=y+40
            i4=int(y4 / 40)
            j4=int( (x4 - 40) / 40)
            #懒得思考了
            if 0<j1<9 and  0<j2<9 and  0<j3<9 and  0<j4<9 and 0<i1<18 and 0<i2<18 and 0<i3<18 and 0<i4<18:
                if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1 and g[i4][j4][0] == -1 :
                    self.shape=1
                    #位置修正
                    y5 = y + 40+40
                    i5 = int(y5 / 40)
                    j5 = int((x - 40) / 40)
                    if i5<18:
                        if g[i1][j1][0] != -1:
                            self.block[1]=g[i1][j1][1][1]-40-40
                    else:
                        self.block[1]=640


        else:
            #     1    2  None
            #  (定位点)None None
            #         None  3
            # 第i行 = int(y / 40), 第j列 =int( (x - 40) / 40)
            x1 = x - 40
            y1 = y - 40
            i1 = int(y1 / 40)
            j1 = int((x1 - 40) / 40)

            y2 = y - 40
            i2 = int(y2 / 40)
            j2 = int((x - 40) / 40)

            y3 = y + 40
            x3=x+40
            i3 = int(y3 / 40)
            j3 = int((x3 - 40) / 40)

            if 0 < j1 < 9 and 0 < j2 < 9 and 0 < j3 < 9 and  0 < i1 < 18 and 0 < i2 < 18 and 0 < i3 < 18 :
                if g[i1][j1][0] == -1 and g[i2][j2][0] == -1 and g[i3][j3][0] == -1:
                    self.shape = 0
                x4=x-40
                i4 = int(y / 40)
                j4 = int((x4 - 40) / 40)
                if g[i4][j4][0] != -1:
                    self.block[1] = g[i4][j4][1][1]


#        None None
#   None None(定位点)
class Block_6():
    def __init__(self):
        pass


#        None
#   None None(定位点) None
class Block_7(AbstractBlock):
    def __init__(self,color=7):
        self.co=color
        self.shape=0
        self.block = [240, 120]


    #        None
    #   None None(定位点) None

    #        None
    #(定位点) None None
    #        None

    #       (定位点)
    #   None None None
    #        None

    #        None
    #   None None  (定位点)
    #        None

    def drawInForeshow(self, screen, allcolors):
        for i in range(3):
            pygame.draw.rect(screen, allcolors[self.co],
                             (550 - 40 + i * 40, 200, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (550 - 40 + i * 40, 200, 41, 41), 1,border_radius=5)
        pygame.draw.rect(screen, allcolors[self.co],
                         (550, 200 - 40, 40, 40),border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0),
                         (550, 200 - 40, 41, 41), 1,border_radius=5)
    def drawBlock(self, screen, allcolors):
        if self.shape==0:
            #        None
            #   None None(定位点) None
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co],
                                 (self.block[0] - 40 + i * 40, self.block[1], 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (self.block[0]-40+i*40, self.block[1], 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0], self.block[1]-40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0], self.block[1]-40, 41, 41), 1,border_radius=5)
        elif self.shape==1:
            #        None
            #(定位点) None None
            #        None
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co],
                                 (self.block[0] , self.block[1]- 40 + i * 40, 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (self.block[0] , self.block[1]- 40 + i * 40, 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0]+ 40, self.block[1] , 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0]+ 40, self.block[1] , 41, 41), 1,border_radius=5)
        elif self.shape==2:
            #       (定位点)
            #   None None None
            #        None

            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co],
                                 (self.block[0] - 40 + i * 40, self.block[1], 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (self.block[0] - 40 + i * 40, self.block[1], 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0], self.block[1]+40, 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0], self.block[1] + 40, 41, 41), 1,border_radius=5)
        elif self.shape==3:
            #        None
            #   None None  (定位点)
            #        None
            for i in range(3):
                pygame.draw.rect(screen, allcolors[self.co],
                                 (self.block[0], self.block[1] - 40 + i * 40, 40, 40),border_radius=5)
                pygame.draw.rect(screen, (0, 0, 0),
                                 (self.block[0], self.block[1] - 40 + i * 40, 41, 41), 1,border_radius=5)
            pygame.draw.rect(screen, allcolors[self.co],
                             (self.block[0] - 40, self.block[1], 40, 40),border_radius=5)
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.block[0] - 40, self.block[1], 41, 41), 1,border_radius=5)

    def horiMove(self, gameD, dire):
        x = self.block[0]
        y = self.block[1]
        if self.shape == 0:
            #        None 1
            #   None None(定位点) None 2
            #                         3
            if dire>0:#右移动
                l1=gameD.getMapping(x+40,y-40)
                l2=gameD.getMapping(x+40+40,y)
                l3=gameD.getMapping(x+40+40,y+40)
                if l1 !=None and l2 != None and l3 !=None:
                    if l1[0]==-1 and l2[0]==-1 and l3[0]==-1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 !=None and l2!=None:
                    #当l3=None时,说明底部边缘已经到最底了,此时方块已经消亡
                    #todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
            else :
                #       1  None
                #   2 None None(定位点) None
                #   3
                l1 = gameD.getMapping(x - 40, y - 40)
                l2 = gameD.getMapping(x -40 - 40, y)
                l3 = gameD.getMapping(x - 40 - 40, y + 40)
                if l1 != None and l2 != None and l3 != None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None:
                    # 当l3=None时,说明底部边缘已经到最底了,此时方块已经消亡,移动失去意义
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1 :
                        self.block[0] = self.block[0] + dire * 40
        elif self.shape == 1:
            #        None  1
            # (定位点) None None  2
            #        None  3
            #              4
            if dire > 0:
                l1 = gameD.getMapping(x + 40, y - 40)
                l2 = gameD.getMapping(x + 40 + 40, y)
                l3 = gameD.getMapping(x + 40 , y + 40)
                l4 = gameD.getMapping(x + 40, y + 40+40)
                if l1 != None and l2 != None and l3 != None and l4 != None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None and l3!=None:
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
            else:
                #      1  None
                #      2  None(定位点) None
                #      3  None
                #      4
                l1 = gameD.getMapping(x - 40, y - 40)
                l2 = gameD.getMapping(x - 40, y)
                l3 = gameD.getMapping(x - 40, y + 40)
                l4 = gameD.getMapping(x - 40, y + 40 + 40)
                if l1 != None and l2 != None and l3 != None and l4 != None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None and l3 != None:
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40

        elif self.shape == 2:
            #       (定位点)
            #   None None None
            #        None
            if dire > 0:
                #       (定位点)
                #   None None None 1
                #        None  2
                #              3
                l1 = gameD.getMapping(x + 40+40, y )
                l2 = gameD.getMapping(x + 40, y+40)
                l3 = gameD.getMapping(x+40, y + 40+40)
                if l1 != None and l2 != None and l3 != None :
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None :
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1 :
                        self.block[0] = self.block[0] + dire * 40
            else:
                #       (定位点)
                #  1 None None None
                #  2      None
                #  3
                l1 = gameD.getMapping(x - 40 - 40, y)
                l2 = gameD.getMapping(x - 40, y + 40)
                l3 = gameD.getMapping(x - 40, y + 40 + 40)
                if l1 != None and l2 != None and l3 != None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None:
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
        elif self.shape == 3:
            #        None
            #   None None  (定位点)
            #        None
            if dire > 0:
                #            None  1
                # None (定位点)None 2
                #            None  3
                l1 = gameD.getMapping(x + 40 , y)
                l2 = gameD.getMapping(x + 40, y + 40)
                l3 = gameD.getMapping(x + 40, y + 40 + 40)
                if l1 != None and l2 != None and l3 != None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None:
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
            else:
                #        None
                #   None None  (定位点)
                #        None
                l1 = gameD.getMapping(x - 40, y)
                l2 = gameD.getMapping(x - 40, y + 40)
                l3 = gameD.getMapping(x - 40, y + 40 + 40)
                if l1 != None and l2 != None and l3 != None:
                    if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                        self.block[0] = self.block[0] + dire * 40
                elif l1 != None and l2 != None:
                    # todo:这个elif好像可以删除
                    if l1[0] == -1 and l2[0] == -1:
                        self.block[0] = self.block[0] + dire * 40

    def downward(self, gameD, speed):
        x = self.block[0]
        y = self.block[1]
        if self.shape == 0:
            #        None
            #   None None(定位点) None
            #   1     2           3
            l1 = gameD.getMapping(x - 40, y + 40)
            l2 = gameD.getMapping(x, y + 40)
            l3 = gameD.getMapping(x + 40, y + 40)
            if l1 != None and l2 != None and l3 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1]=l1[1][1]-40
                    return False
            else:
            #实际测试不用这个else也能通过测试:
            #所有方块边缘一定会经过网格线,当到达最后一个网格线,所有l数据都是None,不会进入赋值条件
                self.block[1]=680
                return False
        elif self.shape == 1:
            #        None
            # (定位点) None None
            #        None   2
            #         1
            l1 = gameD.getMapping(x , y + 40+40)
            l2 = gameD.getMapping(x+40, y + 40)
            if l1 != None and l2 != None:
                if l1[0] == -1 and l2[0] == -1 :
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = l1[1][1] - 40-40
                    return False
            else:
                self.block[1] = 640
                return False
        elif self.shape == 2:
            #       (定位点)
            #   None None None
            #        None
            l1 = gameD.getMapping(x - 40, y + 40)
            l2 = gameD.getMapping(x, y + 40+40)
            l3 = gameD.getMapping(x + 40, y + 40)
            if l1 != None and l2 != None and l3 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = l1[1][1] - 40
                    return False
            else:
                self.block[1] = 680-40
                return False
        elif self.shape == 3:
            #        None
            #   None None  (定位点)
            #        None
            l1 = gameD.getMapping(x, y + 40 + 40)
            l2 = gameD.getMapping(x - 40, y + 40)
            if l1 != None and l2 != None:
                if l1[0] == -1 and l2[0] == -1:
                    self.block[1] = self.block[1] + 40 * speed
                    return True
                else:
                    self.block[1] = l1[1][1] - 40 - 40
                    return False
            else:
                self.block[1] = 640
                return False
    def blockMove(self, speed, gameD, dire):
        self.horiMove(gameD,dire)
        return self.downward(gameD,speed)

    def writeData(self, gameD):
        x = self.block[0]
        y = self.block[1]
        if self.shape == 0:
            #        None
            #   None None(定位点) None
            for i in range(3):
                gameD.writeDate(x-40+i*40, y, self.co)
            gameD.writeDate(x , y-40, self.co)
        elif self.shape == 1:
            #        None
            # (定位点) None None
            #        None
            for i in range(3):
                gameD.writeDate(x , y- 40 + i * 40, self.co)
            gameD.writeDate(x+ 40, y , self.co)
        elif self.shape == 2:
            #       (定位点)
            #   None None None
            #        None
            for i in range(3):
                gameD.writeDate(x - 40 + i * 40, y, self.co)
            gameD.writeDate(x, y + 40, self.co)
        elif self.shape == 3:
            #        None
            #   None None  (定位点)
            #        None
            for i in range(3):
                gameD.writeDate(x, y - 40 + i * 40, self.co)
            gameD.writeDate(x - 40, y, self.co)

    def changeShape(self, gameD):
        x = self.block[0]
        y = self.block[1]
        if self.shape == 0:
            #      1 None 2
            #   None None(定位点) None
            #         4    3
            l1 = gameD.getMapping(x - 40, y - 40)
            l2 = gameD.getMapping(x - 40, y+40)
            l3 = gameD.getMapping(x , y + 40)
            l4 = gameD.getMapping(x + 40, y + 40)
            if l1 != None and l2 != None and l3 != None and l4 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1:
                   self.shape=1

        elif self.shape == 1:
            #         None  1
            # (定位点)2 None None
            #       3 None  4
            l1 = gameD.getMapping(x + 40, y - 40)
            l2 = gameD.getMapping(x - 40, y )
            l3 = gameD.getMapping(x-40, y + 40)
            l4 = gameD.getMapping(x + 40, y + 40)
            if l1 != None and l2 != None and l3 != None and l4 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1:
                    self.shape = 2
        elif self.shape == 2:
            #     3   4
            #   None None (定位点)None
            #     1  None  2
            l1 = gameD.getMapping(x - 40, y + 40)
            l2 = gameD.getMapping(x + 40, y+40)
            l3 = gameD.getMapping(x -40, y - 40)
            l4 = gameD.getMapping(x , y - 40)
            if l1 != None and l2 != None and l3 != None and l4 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1:
                    self.shape = 3
        elif self.shape == 3:
            #     4   None  3
            #   None None  (定位点)2
            #    1    None
            l1 = gameD.getMapping(x - 40, y + 40)
            l2 = gameD.getMapping(x + 40, y )
            l3 = gameD.getMapping(x + 40, y - 40)
            l4 = gameD.getMapping(x-40, y - 40)
            if l1 != None and l2 != None and l3 != None and l4 != None:
                if l1[0] == -1 and l2[0] == -1 and l3[0] == -1 and l4[0] == -1:
                    self.shape = 0





