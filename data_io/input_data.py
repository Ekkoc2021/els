'''
读取数据到游戏
'''
import pickle

'''
读取排名
'''
def input_rank():
    try:
        f2=open("resource/gamedata.properties", "rb")
        l=pickle.load(f2)
        f2.close()
        return l
    except:
        f2.close()
        return None

'''
读取游戏数据
'''
def input_gamedata():
    try:
        f2=open("resource/gamedata.properties", "rb")
        l=pickle.load(f2)
        f2.close()
        return l
    except:
        f2.close()
        return None
# l=input_()
# print(l)
print(input_gamedata())