import random

from game_core.core.allclass.blockClass import Block_1, Block_2, Block_5, Block_3, Block_7


class blockFactory:

    def __init__(self) -> None:
        pass

    def getRandomBlock(self,allcolors,playingcolor):
        i = random.randint(0, 4)
        colorIndex=random.randint(0, 137)
        ##  不能和操作界面背景一样! 需要多colorindex进行效验
        while 0==0:
            if allcolors[colorIndex][0]!=playingcolor[0] and allcolors[colorIndex][1]!=playingcolor[1] and allcolors[colorIndex][2]!=playingcolor[2]:
                break
            colorIndex = random.randint(0, 137)

        if i == 0:
            return Block_1(colorIndex)
        if i == 1:
            return Block_2(colorIndex)
        if i == 2:
            return Block_5(colorIndex)
        if i == 3:
            return Block_3(colorIndex)
        if i == 4:
            return Block_7(colorIndex)
    '''
    指定颜色的任意方块
    '''
    def getRandomBlock_2(self,co):
        i = random.randint(0, 4)
        if i == 0:
            return Block_1(co)
        if i == 1:
            return Block_2(co)
        if i == 2:
            return Block_5(co)
        if i == 3:
            return Block_3(co)
        if i == 4:
            return Block_7(co)
