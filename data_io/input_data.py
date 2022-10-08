'''
读取数据到游戏
'''
import pickle
def input_data(filepath):
    try:
        f2=open(filepath, "rb")
        l=pickle.load(f2)
        f2.close()
        return l
    except:
        f2.close()
        return None
'''
读取排名
'''
def input_rank():
    return input_data("resource/rank.properties")
'''
读取游戏数据
'''
def input_gamedata():
    return input_data("resource/gamedata.properties")

'''
从配置文件中读取所有颜色
'''
def input_ALLCOLORS():
    return input_data("resource/ALLCOLORS.properties")
