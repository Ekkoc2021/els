from abc import ABC,abstractmethod
class AbstractBlock():

    #在画板上绘制出该方块
    @abstractmethod
    def drawBlock(self,screen,allcolors):
        pass
    #方块水平移动
    @abstractmethod
    def horiMove(self, gameD, dire):
        pass
    #方块向下移动,无法移动时返回False
    @abstractmethod
    def downward(self, gameD, speed):
        pass
    #组装方块移动: # 返回的T表示方块依然存活,F表示方块已经消亡
    @abstractmethod
    def blockMove(self, speed, gameD, dire):
        pass

    #用于对象消亡时写入数据的方法
    @abstractmethod
    def writeData(self,gameD):
        pass

    #在预告栏里面展示出第三个图像
    @abstractmethod
    def drawInForeshow(self, screen, allcolors):
        pass

    #改变图像形状
    @abstractmethod
    def changeShape(self,gameD):
        pass