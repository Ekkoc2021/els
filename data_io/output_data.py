import datetime
import pickle


def output_rank(l):
    try:
        f=open("resource/rank.properties", "wb")
        pickle.dump(l,f)
        f.close()
        return True
    except:
        return False


def output_gamedata(gamedata):
    try:
        f=open("resource/gamedata.properties", "wb")
        pickle.dump(gamedata,f)
        f.close()
        return True
    except:
        return False
output_gamedata([1,2,3])
# output_rank([["2022.9.29.19.54",1000],["2022.9.29.19.54",900],["2022.9.29.19.54",900],["2022.9.29.19.54",700],["2022.9.29.19.54",600]])
# x=datetime.datetime.now()
# d=str(x.year)+"."+str(x.month)+"."+str(x.day)+"."+str(x.hour)+"."+str(x.minute)
# print(d)