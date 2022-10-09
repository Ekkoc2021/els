import random

from game_core.core.allclass.blockClass import Block_1, Block_2, Block_5, Block_3, Block_7


class blockFactory:

    def __init__(self) -> None:
        pass

    def getRandomBlock(self):
        i = random.randint(0, 4)
        if i == 0:
            return Block_1(random.randint(0, 137))
        if i == 1:
            return Block_2(random.randint(0, 137))
        if i == 2:
            return Block_5(random.randint(0, 137))
        if i == 3:
            return Block_3(random.randint(0, 137))
        if i == 4:
            return Block_7(random.randint(0, 100))
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
