from abc import ABC,abstractmethod
class abstractGameData:
    '''
    判断得分与否,得分重置gamedata的数据
    '''

    @abstractmethod
    def isWin(self):
        pass

    '''
      绘制出gameData的数据
    '''
    @abstractmethod
    def Paint(self,screen):
        pass

    '''
    返回gamedata[i][j][0]的坐标,j>0
    '''
    @abstractmethod
    def getColor(self,i,j):
        pass

    '''
    返回gamedata[i][j][1],j>0,也就是返回坐标
    '''
    @abstractmethod
    def getLoation(self, i, j):
        pass
    '''
    返回这组坐标在gamedata的映射
    '''
    @abstractmethod
    def getMapping(self,x,y):
        pass
    '''
    返回这组坐标在gamedata写入对应颜色数据
    '''
    @abstractmethod
    def writeDate(self,x,y,co):
        pass