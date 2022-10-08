
'''
:param 传入窗口对象
'''
import pygame

from data_io.input_data import *
# from game_core.game1 import *

'''
colors是一个列表:前三个数据用于按钮的颜色,第4个是一个列表,包含界面颜色,操作界面颜色
'''
linecolor = (0, 0, 0)
def iniTdraw(screen, colors, grade):
    #绘制图形提示框x=20+470,210-40=170
    screen.fill(colors[3][0])
    pygame.draw.rect(screen, (205,205,180),(470, 80, 200, 280))
    #绘制游戏操作界面
    pygame.draw.rect(screen, colors[3][1], (40, 0, 402, 762))
    # 说明栏 470 472
    introductionFont = pygame.freetype.Font("C:\Windows\Fonts\msyhl.ttc" ,20)
    introductionFont.render_to(screen, (460, 472), "按 键 说 明：", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 502), " 1，← / A：左移动", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 532), " 2，→ / D：右移动", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 562), " 3，↑ / W：顺时针旋转", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 592), " 4，↓ / S： 向下加速移动", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 622), " 5，P：暂停", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 652), " 6，Esc：结束游戏", (0, 0, 0), 0)
    introductionFont.render_to(screen, (470, 682), " 7，J：设置", (0, 0, 0), 0)
    #绘制线条
    pygame.draw.line(screen, linecolor, (80,0), (80,760), 1)
    pygame.draw.line(screen,linecolor, (400,0), (400,760), 1)
    pygame.draw.line(screen, linecolor, (40,720), (440,720), 1)

    for i in range(0,18):
        pygame.draw.line(screen, linecolor, (40,0+i*40), (80,0+i*40), 1)
        pygame.draw.line(screen, linecolor, (400,0+i*40), (442,0+i*40), 1)
        if i<5:
            pygame.draw.line(screen, linecolor, (80, 0 + 40 * i), (440, 0 + 40 * i), 1)
        if i<8:
            pygame.draw.line(screen, linecolor, (120 + i * 40, 0), (120 + i * 40, 160), 1)
        if i<7:
            pygame.draw.line(screen, linecolor, (120+i*40,720), (120+i*40,760), 1)
        if i<4:
            pygame.draw.line(screen, linecolor, (510+i*40,80), (510+i*40,360), 1)
        if i<6:
            pygame.draw.line(screen, linecolor, (470,120+i*40), (670,120+i*40), 1)
    #绘制按钮
    bFont = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 20)
    drawButton(screen, "暂停", colors[0], (470, 15, 55, 25), bFont)
    drawButton(screen,"退出", colors[1], (545, 15, 55, 25), bFont)
    drawButton(screen, "设置", colors[2], (615, 15, 55, 25), bFont)
    gradeFont = pygame.freetype.Font("C:\Windows\Fonts\STXINWEI.TTF", 36)
    gradeFont.render_to(screen, (460, 405), "分数:" + str(grade), (0, 0, 0), 0)

    #游戏界面边框
    pygame.draw.rect(screen, (0, 0, 0), (38, -3, 406, 766), 3)
    pygame.draw.rect(screen, (0,0,0), (468, 78, 203, 283),3)
    # pygame.font.get_fonts()
    # font = pygame.font.SysFont("SimHei", 150)
    # text = font.render("竞技模式", True, (128, 128, 128))
    # text.set_alpha(100)
    # text = pygame.transform.rotate(text, 90)  # 显示文字
    #
    # screen.blit(text, (390, 90))
'''
:param 窗口对象,RGB元组,位置+尺寸的元组,字体对象
'''

def drawButton(screen,lable,color,Loc_Dim,bfont):
    #loc_Dim=(x,y,w,h)
    if color==1:
        pygame.draw.rect(screen, (255,255,255), Loc_Dim,border_radius=5)
    else:
        pygame.draw.rect(screen, (128, 128, 128), Loc_Dim,border_radius=5)
    pygame.draw.rect(screen, (0, 0, 0), Loc_Dim, 1, border_radius=5)
    bfont.render_to(screen, (Loc_Dim[0]+6, Loc_Dim[1]+2), lable, (0, 0, 0), 0)





